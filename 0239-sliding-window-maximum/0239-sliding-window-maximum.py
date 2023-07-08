class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        left_pointer = 0
        right_pointer = 0
        queue = collections.deque()

        while right_pointer < len(nums):
            # pop smaller values from queue
            while queue and nums[queue[-1]] < nums[right_pointer]:
                queue.pop()
            queue.append(right_pointer)

            # remove left val from window
            if left_pointer > queue[0]:
                queue.popleft()

            # edge case
            if (right_pointer + 1) >= k:
                output.append(nums[queue[0]])
                left_pointer += 1

            right_pointer += 1

        return output