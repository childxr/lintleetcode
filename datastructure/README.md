# Data Structure

## 1. Number of Islands

### Description

Given a boolean 2D matrix, 0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.

Find the number of islands.

### Example

Given graph:

[
  
  `[1, 1, 0, 0, 0]`,
  
  `[0, 1, 0, 0, 1]`,
  
  `[0, 0, 0, 1, 1]`,
  
  `[0, 0, 0, 0, 0]`,
  
  `[0, 0, 0, 0, 1]`
  
]

return `3`

### Solution

- Travese the island from `left to right`, `top to button`
- Start a `counter, initialize to 0`
- Whenever reaches to an island, increase the counter, and then visit this island throughly by doing BFS, mark all visited places incase of double visit
- return the counter

- [code](https://github.com/childxr/lintleetcode/blob/master/NumberOfIslands/solution.py)


### TAG

- BFS


## 2. Surrounded Regions

### Description

Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O''s into 'X''s in that surrounded region.

### Example

```
X X X X
X O O X
X X O X
X O X X

After capture all regions surrounded by 'X', the board should be:

X X X X
X X X X
X X X X
X O X X
```

### Solution

The problem can be transfered to capture all aeas that are surrounded by wall, which can be further transfered to capture all areas that are open. 

- Visit the region from four edges
- Whenver reaches to an open area, visit that area throughly. Use a mark table to prevent double visit, let's say mark as 'E'
- Visit the whole region again, whenever reaches to an open area, means we reaches to a area surranded by wall, coz those are not surranded by wall is marked as 'E'
. Change open area to wall, and change edge 'E' area to open area 'O'
- [code](https://github.com/childxr/lintleetcode/blob/master/SurroundedRegion/solution.py)

### Tag

- BFS

```
import Queue
queue = Queue.Queue() # FIFO Queue
queue.put(1)
queue.get()
queue.empty()
queue.qsize()

q1 = Queue.LifoQueue() # LIFO Queue
q1 = Queue.PriorityQueue() # priority Queue
```


## 3. Connected Graph

### Description

Given n nodes in a graph labeled from 1 to n. There is no edges in the graph at beginning.

You need to support the following method:

**connect(a, b)**, add an edge to connect node a and node b`.

**query(a, b)**, check if two nodes are connected

### Example

5 // n = 5

`query(1, 2)` return false

`connect(1, 2)`

`query(1, 3)` return false

`connect(2, 4)`

`query(1, 4)` return true

### Solution

- Use **UnionFind** data structure to back up the operation
- In **UnionFind** data structure, it uses 1, 2, .., n as index to each node in the set. There is an array to represent parent of each node, means Id[1] is the parent of node 1. Whenver we have id[i] == [i], we found a root.
- To perform **query** between **a and b**, just need to find if `root(a) and root(b) has the same result`.
- To perform **connect**, just `make one of the node point to the other`. To have better performance, `usually use a size array to keep track of the size for a set rooted at node i`, initialized as 1, and then point the smaller size tree to a bigger size tree.
- To make **root** operation faster, in the path of searching root, do path shorten operation by pointing to grand parent of i whenenver possible.
- [code](https://github.com/childxr/lintleetcode/blob/master/ConnectingGraph/solution.py)

### TAG

- Union Find

Suppose M is the total operation performed, N is the number of nodes, the complexity is

| Algorithm        | Worst Time           |
| ------------- |:-------------:|
| Weighted QU      | N + M log N |
| Path compression      | N + M log N      |
| Weighted + path | (M + N) lg* N    |

For quick-union or quick-find, complexity is M*N

[link](https://www.cs.princeton.edu/~rs/AlgsDS07/01UnionFind.pdf)


## 4. Add and Search Word - Data structure design

### Description

Design a data structure that supports the following two operations: `addWord(word) and search(word)`

search(word) can search a **literal word** or a **regular expression** string containing only letters a-z or `.`.

A `.` means it can represent any one letter.

You may assume that all words are consist of `lowercase letters a-z`.

### Example

addWord("bad")

addWord("dad")

addWord("mad")

search("pad")  // return false

search("bad")  // return true

search(".ad")  // return true

search("b..")  // return true

### Solution

```
TrieNode
 - is_word
 - children[26]

Trie
 - root: TrieNode
 - addWord(w)
 - searchWord(w)


- ord('a') = 97
- chr(97) = 'a'
```

- [code](https://github.com/childxr/lintleetcode/blob/master/AddAndSearchWord/solution.py)
- [Implement a Trie](https://github.com/childxr/lintleetcode/blob/master/ImplementTrie/solution.py)

### TAG

- Trie (prefix tree)

## 5. Word Search

### Description

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

### Example

Given board =
```
[
  "ABCE",
  "SFCS",
  "ADEE"
]

word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
```

### Solution

- Traverse board from left to right, top to bottom. 
- Whenever reaches to a character that is equals to the first char in the word, performce a full DFS via that node
- Could leverage the same board as visited board and rembember to recover the board once a DFS is finished.
- [code](https://github.com/childxr/lintleetcode/blob/master/WordSearch/solution.py)


### TAG

- DFS



## 6. Word Search II

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


### Solution

- Build a trie based on dic
```
- TrieNode
  - word
  - children

- Trie
  - root
  - add_word(w)
```
- Traverse board from left to right, top to bottom, tried to perform word search on each character, prune accordingly
  - current character not in word prefix path

- Output a record if found a word in prefix path, else for 4 direction of current character, continue searching
- Could leverage board itself to mark visited, remember to recover once a depth path search is done
- [code](https://github.com/childxr/lintleetcode/blob/master/WordSearchII/solution.py)


```
set1 = set([])
set2 = set([])
set1.add(1)
set2.add(2)
set3 = set1 | set 2 # union
set4 = set3 & set2 # intersect
set2.isdisjoint(set3) # False
set2.isdisjoint(set1) # True
set1 < set3 # set1 is subset of set3
set1.remove(1)
```

### TAG

- DFS
- Trie
- Set


