## Word Search II

### Description

Given a matrix of lower alphabets and a dictionary. Find all words in the dictionary that can be found in the matrix. A word can start from any position in the matrix and go left/right/up/down to the adjacent position. One character only be used once in one word.

### Example

Given matrix:
```
doaf
agai
dcan

and dictionary:

{"dog", "dad", "dgdg", "can", "again"}

return {"dog", "dad", "can", "again"}
```

**dog**:

`do`af

a`g`ai

dcan

**dad**:

`d`oaf

`a`gai

`d`can

**can**:

doaf

agai

d`can`

**again**:

doaf

`agai`

dca`n`

