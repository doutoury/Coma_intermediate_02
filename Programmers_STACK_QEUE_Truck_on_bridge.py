def solution(bridge_length, weight, truck_weights):
    answer = 0
    return answer

    # 대기 트럭이 정해진 순서대로 건너야 하므로, 연속된 k개 트럭의 합 =< weight 이어야 함
    # 시작 0초, 종료 answer초를 제외하고, 그 사이에서 각 트럭은 bridge-length 만큼 리스트 차지
    
    # 컴퓨터의 시선 : 다리를 건너는 트럭 리스트에 stack 후 bridge-length 초 만큼 있다가 que
    # 연속된 대기트럭 사이의 합이 weight 안 넘을 경우, 각 트럭간 다리 건너는 시간 겹침

    # 단순한 접근 : 시간을 count 변수 놓고 다리 무너지지 않는 선에서 while 반복문
    # 어려운 접근 : 다리 위에 동시에 있을 경우 시간계산을 수식화 해서 대기트럭렬 전체 for문 돌며 적용
    
    # 들어온 트럭이 언제 나갈지 결정 문제
    # 각 truck_idx 마다 count 2개씩 올리며 [2, 2, 2, 1, 0, 0, ...] 이진 체크 리스트 채워가기
    
    count = 0
    truck_idx = -1
    bridge_trucks = []
    finish_trucks = []
    
    while len(finish_trucks) == len(truck_weights):
        truck_idx += 1
        # 트럭 out 결정
        
        # 트럭 in 결정
        if sum(bridge_trucks) <= weight:
            bridge_trucks.append(0)
        # 트럭별 다리위 시간 업데이트