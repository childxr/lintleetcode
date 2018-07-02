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


