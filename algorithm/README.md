# Algorithm


## 1. Sqrt

### Description

Implement int **sqrt(int x)**.

Compute and return the square root of x.

### Example
sqrt(3) = 1

sqrt(4) = 2

sqrt(5) = 2

sqrt(10) = 3

#### Challenge
O(log(x))

### Solution

- Give a hypothesis in a searching range
- Adjust search range based on the closeness of the hypothesis
- assert x >= 0
- init searching range [0, x/2+1]
- [code](https://github.com/childxr/lintleetcode/blob/master/Sqrt/solution.py)

### TAG

- Binary Search


## 2. Sqrt II

### Description

Implement double sqrt(double x) and x >= 0.

Compute and return the square root of x.

You do not care about the accuracy of the result, we will help you to output results.

### Example

Given n = 2 return 1.41421356

### Solution

- Similar as sqrt, the idea is to suggest a value in a searching range, then keep polishing this value until we find the optimal
- The initial searching range is [0, x/2 + 1]
- stop condition is left & right diff is in accepted precision
- [code](https://github.com/childxr/lintleetcode/blob/master/SqrtII/solution.py)

### TAG

- Binary Search

## 3. Last Position of a Target

### Description

Find the last position of a target number in a sorted array. Return **-1** if target does not exist.

### Example

Given `[1, 2, 2, 4, 5, 5]`.

For target = 2, return 2.

For target = 5, return 5.

For target = 6, return -1.

### Solution

- Using binary search to find the target value
- If a match found, keep going right by adjusting left range to mid
- when left + 1 = right stop, check right value to find match, then check left value to find match
- [code](https://github.com/childxr/lintleetcode/blob/master/LastPositionOfTarget/solution.py)

### TAG

- Binary Search

## 4. First Bad Version

### Description

The code base version is an integer start from 1 to n. One day, someone committed a bad version in the code case, so it caused this version and the following versions are all failed in the unit tests. Find the first bad version.

You can call isBadVersion to help you determine which version is the first bad one. The details interface can be found in the code's annotation part.

Please read the annotation in code area to get the correct way to call isBadVersion in different language. For example, Java is SVNRepo.isBadVersion(v)

### Example
Given n = 5:

isBadVersion(3) -> false

isBadVersion(5) -> true

isBadVersion(4) -> true

Here we are 100% sure that the 4th version is the first bad version.

#### Challenge

You should call isBadVersion as few as possible.

### Solution

- Using binary search to find a match
- Once a match is found, keep search to the left by adjusting right boarder to mid
- When left + 1 = right, check left to see if there is a match. Then check right if left match failed. 
- Return -1 if no match found
- [code](https://github.com/childxr/lintleetcode/blob/master/FirstBadVersion/solution.py)

### TAG

- Binary Search



## 5. Find Peak Element

### Description

There is an integer array which has the following features:

The numbers in adjacent positions are different.

A[0] < A[1] && A[A.length - 2] > A[A.length - 1].

We define a position P is a peak if:

A[P] > A[P-1] && A[P] > A[P+1]

Find a peak element in this array. Return the index of the peak.

It's guaranteed the array has at least one peak.
The array may contain multiple peeks, find any of them.
The array has at least 3 numbers in it.

### Example

Given `[1, 2, 1, 3, 4, 5, 7, 6]`

Return index 1 (which is number 2) or 6 (which is number 7)

#### Challenge

Time complexity O(logN)

### Solution

- Use a binary search idea to make a guess within a range. Range query [1, n-2] based on 0 index
- To judge the guess, check if the guess and the element to the right is greater than the guess. If so, move towards the guess by adjusting left boundary to the guess. Otherwise move the right. Eventually return the bigger one between left and right.
- [code](https://github.com/childxr/lintleetcode/blob/master/FindPeakElement/solution.py)

### TAG

- Binary Search


## 6. Find Peak Element II

### Description

There is an integer matrix which has the following features:

The numbers in adjacent positions are different.

The matrix has n rows and m columns.

For all i < m, A[0][i] < A[1][i] && A[n - 2][i] > A[n - 1][i].

For all j < n, A[j][0] < A[j][1] && A[j][m - 2] > A[j][m - 1].

We define a position P is a peek if:

A[j][i] > A[j+1][i] && A[j][i] > A[j-1][i] && A[j][i] > A[j][i+1] && A[j][i] > A[j][i-1]

Find a peak element in this matrix. Return the index of the peak.

The matrix may contains multiple peeks, find any of them.

### Example

Given a matrix:

[

  `[1 ,2 ,3 ,6 ,5]`,
  
  `[16,41,23,22,6]`,
  
  `[15,17,24,21,7]`,
  
  `[14,18,19,20,10]`,
  
  `[13,14,11,10,9]`
  
]

return index of 41 (which is [1,1]) or index of 24 (which is [2,2])

#### Challenge
Solve it in O(n+m) time.

### Solution

- To make the best guess, the initial search area should be wide enough to perform. 
- Starting from the mid line, and find the colomn where the biggest element in this line sits in
- Perform search in that column
  - A[r-1][col] > a[r][col], right = mid
  - A[r+1][col] > a[r][col], left = mid
  - otherwise, output a guess
- [code](https://github.com/childxr/lintleetcode/blob/master/FindPeakElementII/solution.py)


### TAG

- Binary Search
- Searching range [1, n-2] with 0 based index


## 7. Kth Largest In N Arrays

### Description

Find K-th largest element in N arrays.

You can swap elements in the array

### Example

In n=2 arrays [[9,3,2,4,7],[1,2,3,4,8]], the 3rd largest element is 7.

In n=2 arrays [[9,3,2,4,8],[1,2,3,4,2]], the 1st largest element is 9, 2nd largest element is 8, 3rd largest element is 7 and etc.

### Solution

- Arrays are unordered, do a sorting on each array
- Init a max heap and put the last element into heap
- Remove elem from heap steadily, supply next elem in the array where the removed elem comes from. Repeat this step until the Kth largest is found
- [code](https://github.com/childxr/lintleetcode/blob/master/KthLargestInNArray/solution.py)


### TAG

- Heap/Priority Queue



## 8. Kth Smallest Numbers in Unsorted Array

### Description

Find the kth smallest numbers in an unsorted integer array.

### Example

Given [3, 4, 1, 2, 5], k = 3, the 3rd smallest numbers are [1, 2, 3].

#### Challenge

An O(nlogn) algorithm is acceptable, if you can do it in O(n), that would be great.


### Solution

- Use quick sort idea, select a pivot and split the array into two parts: left and right
- Put all elements that are smaller than the pivot to the left
- Put all elements taht are greater than the pivat to the right
- Put the pivot into place, if pivot's index equal to (k-1) with 0 index, then pivot is the target
- [code](https://github.com/childxr/lintleetcode/tree/master/KthSmallestNumberInUnsortedArray)
- The trick here is
 	- use the full range [0, n] to start
 	- init left iter i, right iter j to 0, n 
 	- choose low as pivot
 	- repeat steps
 		- increase i, decrease j by 1
 		- while loop to check a[i] and a[pivot] invariant when i is inbound (hi)
 		- while loop to check a[pivot] and a[j] invariant when j is inbound (lo)
 		- if i crose over j (inclusive), break
 		- swap elements that i and j pointing to
 		
    - swap pivot with element j pointing to, coz when j cross over i, j is pointing element that is smaller than pivot
- Recursively to find the index of k-1 by adjusting the search area from the result of pivot partition
	- pivot < k, then search area to be pivot + 1, hi
	- pivot > k, then search area to be lo, pivot -1

### TAG

- Quick Sort Partition
- Recurssion

## 9. Kth Largest Element

### Description

Find K-th largest element in an array.

You can swap elements in the array

In array [9,3,2,4,8], the 3rd largest element is 4.

In array [1,2,3,4,5], the 1st largest element is 5, 2nd largest element is 4, 3rd largest element is 3 and etc.

#### Challenge 
O(n) time, O(1) extra memory.

### Solution

- Same idea of quick sort partion can be applied here
- First, we need to transform this problem to find element with index (n-k) in sorted order
- We could leverage solution of **Kth Smallest Numbers in Unsorted Array** to get this problem resolved.
- [code](https://github.com/childxr/lintleetcode/blob/master/KthLargestElement/solution.py)

### TAG

- Quick Sort
- Partition
- Recurssion


## 10.  Kth Smallest Number in Sorted Matrix

### Description

Find the kth smallest number in at row and column sorted matrix.

### Example
Given k = 4 and a matrix:
```
[
  [1 ,5 ,7],
  [3 ,7 ,8],
  [4 ,8 ,9],
]
return 5
```

#### Challenge

Solve it in O(k log n) time where n is the bigger one between row size and column size.

### Solution

- Since the row and columns are sorted, it is natual to think some sort of ordered searching may help here
- Searching space is a 2D array(**Sample space could be any value 0, sys.maxint**), means we may need to make a guess on the value of Kth elements, and adjust the searching sample space based on some metric.
- The search metric, should be, how close this guess is to the Kth element. This requirs some sort of counting to be performed. That is for each row, we need to count number of values that is **smaller or equal to the guess**. The total number will be used to compare with K. 
- If after adding all elements, the total is still less than K, means the guess we have should be adjust a little higher => make searching left = mid. otherwise we need to shrink right = mid
- In the final stage, to make sure if pointer to the left to be returned or right, just do a count on left. If with all elements, it adds up >= k, then left. Otherwise, return right.
- [code](https://github.com/childxr/lintleetcode/blob/master/KthSmallestNumberInSortedMatrix/solution.py)


### TAG

- Double binary search
- Guess in the sample area (like sqrt)
- Fast count by binary search


