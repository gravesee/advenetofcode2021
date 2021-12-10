const fs = require("fs");

lines = fs
  .readFileSync("data.txt")
  .toString()
  .split("\n")
  .map((l) => l.split(""));

chars = {
  "(": ")",
  "{": "}",
  "[": "]",
  "<": ">",
};

rev = {
  ")": "(",
  "}": "{",
  "]": "[",
  ">": "<",
};

pts = {
  "(": 3,
  "[": 57,
  "{": 1197,
  "<": 25137,
};

autcomplete_pts = {
  ")": 1,
  "]": 2,
  "}": 3,
  ">": 4,
};

soln1 = 0;
scores = [];
lines.forEach((row) => {
  let l = [];
  let corrupt = false;

  row.forEach((char) => {
    if (Array.from("({[<").includes(char)) {
      l.push(char);
    } else {
      tok = l.pop();
      if (rev[char] !== tok) {
        soln1 += pts[rev[char]];
        corrupt = true;
        return;
      }
    }
  });

  if (!corrupt) {
    score = 0;
    l.reverse().forEach((tok) => {
      score = score * 5;
      score += autcomplete_pts[chars[tok]];
    });
    scores.push(score);
  }
});

console.log("Solution 1", soln1);

soln2 = scores[Math.floor(scores.sort().length / 2)];
console.log("Solution 2", soln2);
