class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        # 3의 배수, 5의 배수 겹치는 공배수 처리 주의
        
        list = []
        num = 0
        
        while num < n:
            num += 1
            
            if num % 3 == 0 and not num % 5 == 0:
                list.append("Fizz")
            elif not num % 3 == 0 and num % 5 == 0:
                list.append("Buzz")
            elif num % 3 == 0 and num % 5 == 0:
                list.append("FizzBuzz")
            else:
                list.append(str(num))
        
        return list