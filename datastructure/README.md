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

## 7. Number of Islands II

### Description

Given a n,m which means the row and column of the 2D matrix and an array of pair A( size k). Originally, the 2D matrix is all 0 which means there is only sea in the matrix. The list pair has k operator and each operator has two integer A[i].x, A[i].y means that you can change the grid matrix[A[i].x][A[i].y] from sea to island. Return how many island are there in the matrix after each operator.

0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.

### Example

Given n = 3, m = 3, array of pair A = [(0,0),(0,1),(2,2),(2,1)].

return [1,1,2,2].


### Solution

- Convert to UnionFind operation via the following step
  - map 2D coordinate (i, j) to 1D array via i * m + j
  - define UnionFind structure

```
UnionFind
  - id: size = m * n, init as -1
  - sz: size = m * n, init as 0
  - count: init as 0 // keep track of # of connected component
  - root(a): find root of a connected component a
  - connect(a, b) connect a and b, and update count
  - add(i, j): add a connected component, and update count
  - isconnected_component(p): check if node has been added to uf before.
```
  - [code](https://github.com/childxr/lintleetcode/blob/master/NumberOfIsLandsII/solution.py)

### TAG

- UnionFind


## 8. Sliding Window Maximum

### Description

Given an array of n integer with duplicate number, and a moving window(size k), move the window at each iteration from the start of the array, find the maximum number inside the window at each moving.

### Example

For array [1, 2, 7, 7, 8], moving window size k = 3. return [7, 7, 8]

At first the window is at the start of the array like this

[|1, 2, 7| ,7, 8] , return the maximum 7;

then the window move one step forward.

[1, |2, 7 ,7|, 8], return the maximum 7;

then the window move one step forward again.

[1, 2, |7, 7, 8|], return the maximum 8;

### Challenge
o(n) time and O(k) memory

### Solution

- Leverage deque [double ended queue/ Queue + Stack / Deck]
- The problem to solve is a `window high` value and how to `keep track of the validity of window high value`
- invariants to maintain
  - (1) Elements in deck are in non-descendant order
  - (2) Element in deck are present in current window
- Inorder to keep (1), each time for scaning an element in the array, need to compare it to the peek of the deck, remove peek elem if invariant is broken before adding the new high elem into deck
- Inoder to compute the second requirement for the invariant, make the value of deck element to be the index number of the given array
- [code](https://github.com/childxr/lintleetcode/blob/master/SlidingWindowMaximum/solution.py)

```
from collections import deque
dq = deque()
```
Deque Method

**append(x)**
- Add x to the right side of the deque.

**appendleft(x)**
- Add x to the left side of the deque.

**clear()**
- Remove all elements from the deque leaving it with length 0.

**count(x)**
- Count the number of deque elements equal to x.

**extend(iterable)**
- Extend the right side of the deque by appending elements from the iterable argument.

**extendleft(iterable)**
- Extend the left side of the deque by appending elements from iterable. Note, the series of left appends results in reversing the order of elements in the iterable argument.

**pop()**
- Remove and return an element from the right side of the deque. If no elements are present, raises an IndexError.

**popleft()**
- Remove and return an element from the left side of the deque. If no elements are present, raises an IndexError.

**remove(value)**
- Remove the first occurrence of value. If not found, raises a ValueError.

**reverse()**
- Reverse the elements of the deque in-place and then return None.

**rotate(n=1)**
- Rotate the deque n steps to the right. If n is negative, rotate to the left.


## 8. Sliding Window Maximum

### Description

Given an array of n integer with duplicate number, and a moving window(size k), move the window at each iteration from the start of the array, find the maximum number inside the window at each moving.

### Example

For array [1, 2, 7, 7, 8], moving window size k = 3. return [7, 7, 8]

At first the window is at the start of the array like this

[|1, 2, 7| ,7, 8] , return the maximum 7;

then the window move one step forward.

[1, |2, 7 ,7|, 8], return the maximum 7;

then the window move one step forward again.

[1, 2, |7, 7, 8|], return the maximum 8;

### Challenge
o(n) time and O(k) memory

### Solution

- Leverage deque [double ended queue/ Queue + Stack / Deck]
- The problem to solve is a `window high` value and how to `keep track of the validity of window high value`
- invariants to maintain
  - (1) Elements in deck are in non-descendant order
  - (2) Element in deck are present in current window
- Inorder to keep (1), each time for scaning an element in the array, need to compare it to the peek of the deck, remove peek elem if invariant is broken before adding the new high elem into deck
- Inoder to compute the second requirement for the invariant, make the value of deck element to be the index number of the given array
- [code](https://github.com/childxr/lintleetcode/blob/master/SlidingWindowMaximum/solution.py)

```
from collections import deque
dq = deque()
```
Deque Method

**append(x)**
- Add x to the right side of the deque.

**appendleft(x)**
- Add x to the left side of the deque.

**clear()**
- Remove all elements from the deque leaving it with length 0.

**count(x)**
- Count the number of deque elements equal to x.

**extend(iterable)**
- Extend the right side of the deque by appending elements from the iterable argument.

**extendleft(iterable)**
- Extend the left side of the deque by appending elements from iterable. Note, the series of left appends results in reversing the order of elements in the iterable argument.

**pop()**
- Remove and return an element from the right side of the deque. If no elements are present, raises an IndexError.

**popleft()**
- Remove and return an element from the left side of the deque. If no elements are present, raises an IndexError.

**remove(value)**
- Remove the first occurrence of value. If not found, raises a ValueError.

**reverse()**
- Reverse the elements of the deque in-place and then return None.

**rotate(n=1)**
- Rotate the deque n steps to the right. If n is negative, rotate to the left.



## 9. Sliding Windlow Medium

### Description

Given an array of n integer, and a moving window(size k), move the window at each iteration from the start of the array, find the median of the element inside the window at each moving. (If there are even numbers in the array, return the N/2-th number after sorting the element in the window. )

### Example

For array [1,2,7,8,5], moving window size k = 3. return [2,7,7]

At first the window is at the start of the array like this

[ | 1,2,7 | ,8,5] , return the median 2;

then the window move one step forward.

[1, | 2,7,8 | ,5], return the median 7;

then the window move one step forward again.

[1,2, | 7,8,5 | ], return the median 7;

### Challenge

O(nlog(n)) time

### Solution

- Defined a data structure which contains a minHeap and maxHeap
- **minHeap** is to keep the second half of elements
- **maxHeap** is to keep the first half of elements
- **getMedium**: compute current medium 

```
MediumHeap
 - minHeap
 - maxHeap
 - add(a) : add a into medium heap
 - remove(a): remove a from medium heap

```
- invariant for any operation is: `|size(minHeap) - size(maxHeap)| <= 1`
- initialize a medium heap (**mh**)
- for i in [0: k-1), add num[i] to mh
- for i in [k-1, n), output medium, add i, remove i-k+1

```
import heapq
class minHeap:
  def __init__(self):
    self.h = []
  
  def heappush(self, item):
    heapq.heappush(self.h, item)
    
  def heappop(self):
    return heapq.heappop(self.h)
  
  def remove(self, item):
    self.h.remove(item)
    heapq.heapify(self.h)
  
  def empty(self):
    return len(self.h) == 0
  
  def size(self):
    return len(self.h)

class maxObject:
  def __init__(self, item):
    self.item = item
    
  def __eq__(self, other):
    return self.item == other.item
    
  def __lt__(self, other):
    return self.item > other.item
  
  def __str__(self):
    return str(self.item)

class maxHeap:
  def __init__(self):
    self.h = []
  
  def heappush(self, item):
    heapq.heappush(self.h, maxObject(item))
  
  def heappop(self):
    return str(heapq.heappop(self.h))
    
  def remove(self, item):
    self.h.remove(maxObject(item))
    heapq.heapify(self.h)
  
  def empty(self):
    return len(self.h) == 0
    
  def size(self):
    return len(self.h)

```

### TAG

- Heap



## 10. Find Medium form Data Stream

### Description

Numbers keep coming, return the median of numbers at every time a new number added.

#### Clarification
What's the definition of Median?

Median is the number that in the middle of a sorted array. If there are n numbers in a sorted array A, the median is A[(n - 1) / 2]. For example, if A=[1,2,3], median is 2. If A=[1,19], median is 1.

### Example

For numbers coming list: [1, 2, 3, 4, 5], return [1, 1, 2, 2, 3].

For numbers coming list: [4, 5, 1, 3, 2, 6, 0], return [4, 4, 4, 3, 3, 3, 3].

For numbers coming list: [2, 20, 100], return [2, 2, 20].

#### Challenge
Total run time in O(nlogn).

### Solution

- see Sliding Windlow Medium

### TAG

- Heap



## 11. Heapify

### Description

Given an integer array, heapify it into a min-heap array.

For a heap array A, A[0] is the root of heap, and for each A[i], A[i * 2 + 1] is the left child of A[i] and A[i * 2 + 2] is the right child of A[i].

### Clarification
What is heap?

Heap is a data structure, which usually have three methods: push, pop and top. where "push" add a new element the heap, "pop" delete the minimum/maximum element in the heap, "top" return the minimum/maximum element.

What is heapify?

Convert an unordered integer array into a heap array. If it is min-heap, for each element A[i], we will get A[i * 2 + 1] >= A[i] and A[i * 2 + 2] >= A[i].

What if there is a lot of solutions?
Return any of them.

### Example

Given [3,2,1,4,5], return [1,2,3,4,5] or any legal heap array.

#### Challenge
O(n) time complexity

### Solution

- [slide](https://www.cs.princeton.edu/~wayne/kleinberg-tardos/pdf/DemoHeapify.pdf)
- [priority queue](https://algs4.cs.princeton.edu/24pq/)
- Algorithms on heaps. We represent a heap of size n in private array pq[] of length n + 1, with pq[0] unused and the heap in pq[1] through pq[n]. 
- We access keys only through private helper functions less() and exch(). The heap operations that we consider work by first making a simple modification that could violate the heap condition, then traveling through the heap, modifying the heap as required to ensure that the heap condition is satisfied everywhere. We refer to this process as reheapifying, or restoring heap order.

```
private void swim(int k) {
   while (k > 1 && less(k/2, k)) {
      exch(k, k/2);
      k = k/2;
   }
}

private void sink(int k) {
   while (2*k <= N) {
      int j = 2*k;
      if (j < N && less(j, j+1)) j++;
      if (!less(k, j)) break;
      exch(k, j);
      k = j;
   }
}

public static void sort(Comparable[] pq) {
	int n = pq.length;
    for (int k = n/2; k >= 1; k--)
        sink(pq, k, n);
    while (n > 1) {
        exch(pq, 1, n--);
        sink(pq, 1, n);
    }
}

```


## 12. Trap Rain in Water

### Description

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

Trapping Rain Water

### Example

Given `[0,1,0,2,1,0,1,3,2,1,2,1]`, return 6.

#### Challenge

O(n) time and O(1) memory

O(n) time and O(n) memory is also acceptable.

### Solution

- Just think of each bar is a bin
- How much water to trap depends on the left and right edge of the bin
- example is [2, 1, 3], water to be trap in 1 (as bottom), it is (min(2, 3) - 1)
- Just initialize 2 arrays and compute @ each bar, the highest to the left in one array and highest to the right for the other array
- use equation in the example to get the total output


## 13. Trap Rain in Water II


### Description

Given n x m non-negative integers representing an elevation map 2d where the area of each cell is 1 x 1, compute how much water it is able to trap after raining.

### Example

Given 5*4 matrix

`[12,13,0,12]`

`[13,4,13,12]`

`[13,8,10,12]`

`[12,13,12,12]`

`[13,13,13,13]`

return 14.

### Solution

- This is s 3D problem and the problem we need to solve is **how to keep track of the real edge for each bin**
- Considering any bin height could contribute to the edge of other bins, we should start from the smallest bin height from the outter area. Smallest outter bin height could never trap water but it is likely help other bins in inner area to trap water if inner bin has smaller height
- Starting from the smallest outter bin, do scanning through 4 directions. For those unvisited bins, compute if any water could be trapped. If so, add up the amount of water that is trapped. Mark this unvisited bin as visited, and put it into the min Heap.


### TAG

- BFS with a Priority Queue
- Heap

## 14. Merge K Sorted Interval Lists

### Description

Merge K sorted interval lists into one sorted interval list. You need to merge overlapping intervals too.

### Example

Given

[

  `[(1,3),(4,7),(6,8)]`,
  
  `[(1,2),(9,10)]`
  
]

Return

[(1,3),(4,8),(9,10)]


### Solution

- Define a method to check if two intervals are intercepted or not
- Init an output array as []
- Init a MinHeap with item (start, end)
- PUT first element in list into heap
- Repeat the following until all elements are put into heap
	- move top elem from heap, check if a merge needed with last interval. Init last interval if it is None
	- If a merge needed, update last interval
	- get the next elem in list where the top element comes from, put it into heap
- Output list


### TAG

- Merge Sort
- Heap

## 15. Merge K Sorted List

### Description
Merge k sorted linked lists and return it as one sorted list.

Analyze and describe its complexity.

### Example
Given lists:

[ 

2->4->null,

null,

-1->null

],

return -1->2->4->null.

### Solution

- [code](https://github.com/childxr/lintleetcode/tree/master/MergeKSortedList)

### TAG

- Heap

