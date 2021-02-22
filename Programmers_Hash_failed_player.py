def solution(participant, completion):
    
    participant.sort()
    completion.sort()
    
    failure = []
    j = 0
    popnum = 0
    for i in range(len(participant)):

        if participant[i-popnum] == completion[j]:
            try:
                completion[j+1]
                j += 1
            except:
                pass
        else:
            failure.append(participant[i-popnum])
            participant.remove(participant[i-popnum])
            popnum += 1
            
    answer = (failure[0])
    return answer