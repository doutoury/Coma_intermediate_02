# 재귀적 DFS로 푸는 코드

answer = 0

def solution(numbers, target, length, i):
    global answer
    if i == len(numbers):
        if (sum(numbers)) == target:
            answer += 1
            return
    else:
        solution(numbers, target, length, i+1)
        numbers[i] *= -1
        solution(numbers, target, length, i+1)


def recursive_solution(numbers, target):
    global answer
    length = len(numbers)
    solution(numbers, target, length, 0)

    return answer