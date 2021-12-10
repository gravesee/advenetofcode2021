
pts = {
  ')': 3,
 ']': 57,
 '}': 1197,
 '>': 25137,
 '(': 3,
 '[': 57,
 '{': 1197,
 '<': 25137,
}


rev = {
  ')': '(',
  ']': '[',
  '}': '{',
  '>': '<'
}

fwd = {v: k for k, v in rev.items()}

autcomplete_pts = {
  ')': 1,
  ']': 2,
  '}': 3,
  '>': 4
}


with open("data.txt", "r") as fin:
  soln1 = 0
  scores = []
  for row in fin:
    l = []
    corrupt = False
    for char in row.strip():
      if char in "({[<":
        l.append(char)
      else:
        tok = l.pop()
        if (rev.get(char) != tok):
          soln1 += pts[char]
          corrupt = True
          next  
    
    if not corrupt:
      score = 0
      for i, tok in enumerate(map(fwd.get, reversed(l))):
        score = score * 5
        score += autcomplete_pts.get(tok)
      scores.append(score)

  print(soln1)


  soln2 = sorted(scores)[int(len(scores)/2)]
  print(soln2)
    
    



  