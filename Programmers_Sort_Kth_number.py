def solution(array, commands):
    answer = []
    
    for n in range(len(commands)):
        i = commands[n][0]-1   # i : check리스트 시작값
        j = commands[n][1]     # j : check리스트 끝값
        k = commands[n][2]-1   # k : check리스트 k번째 값

        sorted_block = sorted(array[i:j])
        answer.append(sorted_block[k])

    return answer