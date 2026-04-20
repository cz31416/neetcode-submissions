class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_dict = {}
        answer = []
        for i in range(len(nums)):
            a = nums[i]
            b = target - a
            if b in new_dict:
                if new_dict[b] < i:
                    answer.append(new_dict[b])
                    answer.append(i)
                else:
                    answer.append(i)
                    answer.append(new_dict[b])
                return answer
            else:
                new_dict[a] = i