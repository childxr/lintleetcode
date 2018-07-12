# Dynamic Programing

## Max Square II

### Description

Given a 2D binary matrix filled with 0's and 1's, find the largest square which diagonal is all 1 and others is 0.
Only consider the main diagonal situation.

### Example
For example, given the following matrix:

```
1 0 1 0 0
1 0 0 1 0
1 1 0 0 1
1 0 0 1 0
return 9
```


### Solution

- To be qualified as a square, need to keep track of the number of 1 in diagnose and number of 0 in both up-down and left-right direction
- Consider a matrix point [i,j]
- Suppose u(i,j) is the number of continuous 0s from upper direction to matrix point [i,j] 
- Suppose l(i,j) is the number of continuous 0s from left direction to matrix point [i,j]
- Suppose f(i,j) is the max length of square when matrix point[i,j] is taken
- if matrix point [i,j] is 0
	- u(i,j) = u(i-1,j)+1 if i > 0 else 1
	- l(i,j) = l(i,j-1)+1 if j > 0 else 1
	- f(i,j) = 0
- else
	- f(i,j) = min(f(i-1,j-1), min(u(i-1,j), l(i,j-1)) when i > 0 and j > 0
	- f(i,j) = 1

- Need a global max variable to keep track of max(f(i,j))

### TAG

- DP

## Longest Repeating Subsequence

### Description

Given a string, find length of the longest repeating subsequence such that the two subsequence don’t have same string character at same position, i.e., any ith character in the two subsequences shouldn’t have the same index in the original string.
