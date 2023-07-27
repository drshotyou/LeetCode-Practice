Problem Description:
The problem is to find all triplets [nums[i], nums[j], nums[k]] in an integer array `nums` such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Solution Explanation:

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1

            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res
```

Explanation of the Solution:

1. The solution is defined as a class `Solution` with a method `threeSum`, which takes in an integer array `nums` and returns a list of lists containing all the triplets that sum to zero.

2. The variable `res` is initialized as an empty list. It will store the result, i.e., all the triplets that satisfy the condition.

3. The `nums` array is sorted in ascending order. Sorting the array allows us to use two pointers approach to efficiently find the triplets.

4. The code then iterates through each element in the `nums` array using `enumerate`. The current element is represented by the variable `a`, and its index is `i`.

5. Inside the loop, the code checks if the current element `a` is a duplicate. If `i > 0` (not the first element), and `a` is equal to the previous element `nums[i-1]`, then `a` is a duplicate, and we can skip it using the `continue` statement.

6. If `a` is not a duplicate, we initialize two pointers `l` and `r`. `l` starts just after `a` (i.e., `i + 1`), and `r` starts at the end of the `nums` array.

7. We use the two pointers approach to find the triplets. While `l` is less than `r`, we calculate the sum of `a`, `nums[l]`, and `nums[r]` (represented by `threeSum`).

8. If `threeSum` is greater than 0, we need to decrease the sum, so we decrement `r` by 1.

9. If `threeSum` is less than 0, we need to increase the sum, so we increment `l` by 1.

10. If `threeSum` is equal to 0, it means we have found a triplet that satisfies the condition, and we append it to the `res` list. We then increment `l` by 1 to continue searching for more triplets, but we also skip any duplicates in `nums[l]` by using a `while` loop with the condition `nums[l] == nums[l - 1]`.

11. The outer loop continues until we have checked all elements in the `nums` array.

12. Finally, the method returns the `res` list, containing all the triplets that sum to zero.

Time Complexity Analysis:

The time complexity of the provided solution is O(n^2), where n is the number of elements in the `nums` array. The dominant operations are sorting the array (O(n log n)) and the two-pointer loop inside the outer loop (O(n^2)). The sorting step is typically the most time-consuming operation for large input arrays. The `while` loop inside the outer loop runs in O(n) time, and it can be executed multiple times for each `i`, resulting in a time complexity of O(n^2). However, the overall time complexity is still O(n^2) due to the sorting operation.