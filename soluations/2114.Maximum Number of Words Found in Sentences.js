/**
 * @param {string[]} sentences
 * @return {number}
 */


var mostWordsFound = function(sentences) {
      return Math.max(...sentences.map((s) => s.split(' ').length));
};

sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
const res = mostWordsFound(sentences);
console.log(res);