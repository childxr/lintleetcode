class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        if not numbers or len(numbers) < 3:
            return []
        numbers.sort()
        i = 0
        ans = []
        while i < len(numbers) - 2:
            if i > 0 and numbers[i] == numbers[i-1]:
                i += 1
                continue
            j = i + 1
            while j < len(numbers) - 1:
                if j > i + 1 and numbers[j] == numbers[j-1]:
                    j += 1
                    continue
                k = len(numbers) - 1
                while k > j:
                    if k < len(numbers) - 1 and numbers[k] == numbers[k+1]:
                        k -= 1
                        continue
                    tmp = numbers[i] + numbers[j] + numbers[k]
                    if tmp == 0:
                        ans.append([numbers[i], numbers[j], numbers[k]])
                        j += 1
                        k -= 1
                    elif tmp < 0:
                        j += 1
                    else:
                        k -= 1
                j += 1
            i += 1
        return ans
            
                

