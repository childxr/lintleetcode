## Paint Fence

### Description

There is a fence with n posts, each post can be painted with one of the k colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same color.
Return the total number of ways you can paint the fence.

n and k are non-negative integers.

### Example
Given n=3, k=2 return 6
```
      post 1,   post 2, post 3
way1    0         0       1 
way2    0         1       0
way3    0         1       1
way4    1         0       0
way5    1         0       1
way6    1         1       0
```

### Solution

- If we only have one house and one color, the answer is straight forward: 1
- If we only have one house and k color, the answer is also straight forward: K
- When we have two houses and we know we have K options to pain house 1, the number of ways to pain house 2 is K * C(K, K-1) = K * (K-1) if we do not allow adjacent post has the same color. If we allow adjacent post has the same color, we could do another K. So totally, number of ways to pain house 2 is K * (K-1) + K = K * K
- We could potentially build a transition function as follows:
- **F(i, k)** is the number of ways for painting i houses with k number of colors
- Target is to get **F(N, K)** where **N** is the total number of houses and **K** is total number of colors
- ```F(i+1, k) = F(i, k) * (k-1) + F(i-1,k) * (k-1) where k >= 1```
- Since K is fixed, we could simplified the function as follows:
- ```F(i+1) = F(i) * (k-1) + F(i-1)*(k-1)```
- Use a 1D array could easily solve this problem
- [code](https://github.com/childxr/lintleetcode/blob/master/google/PaintFence/solution.py)
