/* VITORIUM in the browser: the trained TF-IDF + logistic regression pipeline,
   re-implemented to match scikit-learn's TfidfVectorizer(ngram_range=(1,2),
   stop_words="english", norm="l2") and multinomial LogisticRegression. */
(function (root) {
  "use strict";
  var TOKEN = /[\p{L}\p{N}_]{2,}/gu;  // sklearn: (?u)\b\w\w+\b

  function VitoriumModel(m) {
    this.classes = m.classes;
    this.coef = m.coef;
    this.intercept = m.intercept;
    this.idf = m.idf;
    this.index = new Map();
    for (var i = 0; i < m.terms.length; i++) this.index.set(m.terms[i], i);
    this.stop = new Set(m.stop_words);
  }

  VitoriumModel.prototype.features = function (text) {
    var tokens = (String(text).toLowerCase().match(TOKEN) || []).filter(function (t) {
      return !this.stop.has(t);
    }, this);
    var counts = new Map(), self = this;
    function add(term) {
      var j = self.index.get(term);
      if (j !== undefined) counts.set(j, (counts.get(j) || 0) + 1);
    }
    for (var k = 0; k < tokens.length; k++) {
      add(tokens[k]);
      if (k + 1 < tokens.length) add(tokens[k] + " " + tokens[k + 1]);
    }
    var norm = 0;
    counts.forEach(function (c, j) { var v = c * self.idf[j]; counts.set(j, v); norm += v * v; });
    norm = Math.sqrt(norm);
    if (norm > 0) counts.forEach(function (v, j) { counts.set(j, v / norm); });
    return counts;  // Map(featureIndex -> tf-idf weight)
  };

  VitoriumModel.prototype.predict = function (text) {
    var x = this.features(text), self = this;
    var logits = this.classes.map(function (_, c) {
      var z = self.intercept[c], w = self.coef[c];
      x.forEach(function (v, j) { z += v * w[j]; });
      return z;
    });
    var max = Math.max.apply(null, logits);
    var exps = logits.map(function (z) { return Math.exp(z - max); });
    var sum = exps.reduce(function (a, b) { return a + b; }, 0);
    var proba = {}, best = 0;
    exps.forEach(function (e, c) { proba[self.classes[c]] = e / sum; if (e > exps[best]) best = c; });
    // Top contributing n-grams toward the predicted class (explainability).
    var contrib = [];
    x.forEach(function (v, j) { contrib.push([j, v * self.coef[best][j]]); });
    contrib.sort(function (a, b) { return b[1] - a[1]; });
    return {
      urgencia: this.classes[best],
      probabilidades: proba,
      features_ativas: x.size,
      top_termos: contrib.slice(0, 6).filter(function (p) { return p[1] > 0; })
    };
  };

  VitoriumModel.prototype.termOf = function (j) {
    if (!this._terms) { var t = []; this.index.forEach(function (i, s) { t[i] = s; }); this._terms = t; }
    return this._terms[j];
  };

  if (typeof module !== "undefined") module.exports = VitoriumModel;
  else root.VitoriumModel = VitoriumModel;
})(this);
