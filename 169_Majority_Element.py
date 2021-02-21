class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        set_list = set(nums)    # set 도 for 문 돌아가네 ? (iterable 맞나?)
                                # list(set(nums)) 해줄 필요 없다.
        for i in set_list:
            if nums.count(i) >= len(nums)/2:
                answer = i
                break
            else:
                pass
        
        return answer