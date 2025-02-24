# import os

# # 함수 선언
# def isQueueFull(): # 대기열이 꽉 찼는지 확인하는 함수
#     global SIZE, queue, front, rear
#     if rear == SIZE-1:
#         return True
#     else:
#         return False
    
# def isQueueEmpty(): # 대기열이 비었는지 확인하는 함수
#     global SIZE, queue, front, rear
#     if front == rear:
#         return True
#     else:
#         return False
    
# def enQueue(data): # 예약할 손님을 대기열에 집어넣는 함수
#     global SIZE, queue, front, rear
#     if isQueueFull(): # 대기열이 꽉 찼는지 확인
#         print('대기할 줄이 없습니다.')
#         return
#     # 예약을 받은 후 대기열에 넣음
#     rear +=1
#     queue[rear] = data

# def deQueue(): # 대기한 손님이 식당에 들어감 + 이후의 상황
#     global SIZE, queue, front, rear
#     if isQueueEmpty(): # 대기열이 비었는지 확인
#         print('대기열이 비었습니다.')
#         return None
#     # 손님을 식당에 넣기
#     front += 1
#     data = queue[front]
#     queue[front] = None

#     for i in range(front+1, rear+1): # 대기하는 손님을 한 칸씩 앞으로 당김
#         queue[i-1] = queue[i]
#         queue[i] = None
#     front = -1
#     rear -= 1

#     return data

# def clearScreen(): # 콘솔창 정리 함수
#     command = 'clear'
#     if os.name in ('nt', 'dos'):
#         command = 'cls'
    
#     os.system(command)

# # 전역변수 선언
# clearScreen() # 콘솔창 정리 함수
# SIZE = int(input('대기 가능한 손님의 줄 > ')) # 대기열 입력
# queue = [None for _ in range(SIZE)] # 대기열 생성
# front = rear = -1  # 현재 대기 인원과 최대 대기 인원 수 표현

# while True:
#     clearScreen()
#     print('1. 손님 받기\n'
#           '2. 예약한 손님 입장시키기\n'
#           '3. 영업 종료!')
    
#     menu = int(input('위 메뉴의 번호를 선택하세요 > '))
#     clearScreen()

#     if menu == 1: # 손님을 받음
#         enQueue(input('예약할 손님명 > '))

#     elif menu == 2: # 손님을 가게로 입장시킴
#         name = deQueue()
#         if name != None: # 대기열에 사람이 있는 경우
#             print(f'{name}님 식당에 들어감')
    
#     elif menu == 3: # 영업 종료
#         print('식당 영업 종료!')
#         break

#     print(f'대기열 상태 : {queue}')
#     input('\nEnter를 눌러주세요.')

################################################

# import random
# import os
# ## 함수 선언
# class TreeNode(): # 트리 생성
#     def __init__(self):
#         self.left = None # 왼쪽 노드
#         self.data = None # 현재 노드
#         self.right = None # 오른쪽 노드

# def preorder(node):  # 전위 순휘 함수(재귀함수)
#     if node == None: # 노드의 값이 없으면 반환
#         return
#     print(node.data, end=' ') # 현재 노드 출력
#     preorder(node.left)       # 일단 왼쪽 노드로 들어감(재귀)
#     preorder(node.right)      # 이후 오른쪽 노드로 들어감(재귀)

# def creatNode(sellAry):  # 이진 탐색 트리 생성 함수
#     global node, root, memory  # 노드, 현재노드, 메모리변수 글로벌 선언
#     node.data = sellAry[0]  # 0번째 판매된 물건 현재 노드에 넣기
#     root = node
#     memory.append(node) # 메모리에 현재노드 입력
    
#     for name in sellAry[1:]: # 1번째 판매 물건 부터 끝까지 반복
#         node = TreeNode()  # 노드 다시 생성
#         node.data = name   # 현재 노드에 1번째 판매 물건 부터 등록

#         current = root  # 현재 노드
#         while True:
#             if name == current.data: break  # 현재노드가 선택된 판매 물건과 같으면 종료
            
#             if name < current.data:  # 선택된 판매 물건보다 현재 노드 데이터보다 작으면
#                 if current.left == None:  # 왼쪽 노드가 None일 경우
#                     current.left = node  # 왼쪽 노드에 노드 다시 생성
#                     memory.append(node)  # 메모리에 현재 노드 넣기
#                     break
#                 current = current.left  # 현재노드에서 왼쪽노드로 이동
#             else:  # 선택된 판매 물건보다 현재 노드 데이터보다 크거나 같으면
#                 if current.right == None:  # 오른쪽 노드가 None일 경우
#                     current.right = node  # 오른쪽 노드에 노드 다시 생성
#                     memory.append(node)  # 메모리에 현재 노드 넣기
#                     break
#                 current = current.right # 현재노드에서 오른쪽노드로 이동

# def clearScreen():  # 콘솔창 정리 함수
#     command = 'clear'
#     if os.name in ('nt', 'dos'):
#         command = 'cls'
    
#     os.system(command)

# ## 전역 변수 선언
# memory = []
# root = None
# dataAry = ['콘말차', '삿포로 맥주', '아카페라 벤티 헤이즐넛',
#            '레어치즈푸딩', '척오리지널 메가사워', '요아정 요거트컵',
#            '페퍼로니피자주먹밥', '널담 슈톨렌', '딸기마시멜로케이크',
#            '버니공쥬 딸기뚱카롱', '고추잡채호빵', '체다 슈크림붕어스낵']

# lenData = len(dataAry)  # dataAry 개수
# sellDay = 1  # 판매 일차

# ## 메인 코드
# while True:
#     clearScreen() # 콘솔창 정리
#     menu = int(input('1. 오늘 장사시작!\n' # 메뉴 번호 + 번호 입력
#                      '2. 장사 종료!\n'
#                      '메뉴번호입력 > '))
    
#     clearScreen()

#     if menu == 1:
#         NUM = int(input(f'오늘 판매할 물건의 총 개수 ({lenData}개 이상) > '))  # 판매할 물건 개수 입력
#         if NUM < lenData:  # 들어온 재고의 종류보다 판매할 물건 수가 적은 경우 다시 입력
#             input(f'숫자를 {lenData}이상 입력해 주세요.\n'
#                   'Enter를 누르면 메인매뉴로 이동')
#             continue

#         clearScreen()

#         sellAry = [random.choice(dataAry) for _ in range(20)]  # 판매된 물건

#         print(f'{sellDay}일차 판매된 물건(중복O) --> {sellAry}\n')

#         node = TreeNode()  # 노드(트리) 생성
#         creatNode(sellAry)  # 이진 탐색 트리로 중복 제거

#         print(f'{sellDay}일차 판매된 종류(중복X) --> ', end='')
#         preorder(root)  # 전위 순휘로 이진 탐색 트리 출력
#         input()

#     elif menu == 2:
#         if sellDay != 1:
#             print(f'{sellDay - 1}일 부로 장사 종료!')
#         else:
#             print('0일 부로 장사 종료...')
#         break
#     else:
#         clearScreen()
#         input('번호를 다시 입력해 주세요.')
    
#     sellDay += 1  # 판매일차 증가

################################################

import random
## 클래스와 함수 선언 부분
def binSearch(ary, fData):  # 이진 검색 알고리즘 함수
    global cnt  # 검색 횟수 변수 글로벌 선언
    pos = -1  # 인덱스 번호(-1은 없음)
    start = 0  # 배열 시작 지점
    end = len(ary) - 1  # 배열 끝 지점

    while start <= end:  # 배열 시작값이 끝지점보다 작거나 같은 경우 반복문 탈출
        mid = (start + end) // 2  # 배열의 중앙값 지정
        if fData == ary[mid]:  # 찾으려는 데이터가 중앙값에 있는 배열과 같은 경우
            cnt += 1  # 검색 횟수 1 증가 후
            return mid  # 중앙값 리턴
        elif fData > ary[mid]:  # 찾으려는 데이터가 중앙값 배열의 숫자보다 큰 경우
            start = mid + 1  # 시작 값을 (중앙값 + 1)로 지정
        else:  # 찾으려는 데이터가 중앙값 배열의 숫자보다 작거나 같은 경우
            end = mid - 1  # 끝지점의 값을 (중앙값 - 1)로 지정
        
        cnt += 1  # 검색 횟수 1 증가

    return pos  # 찾은 위치 값 리턴(못 찾았으면 -1)

## 전역 변수 선언 부분
dataAry = [random.randint(0, 100000) for _ in range(100000)]  # 랜덤하게 0 ~ 100,000 숫자 100,000개 생성
dataAry.sort()  # 오름차순 정렬
findData = random.choice(dataAry)  # 생성된 배열의 숫자 중 하나를 랜덤하게 선택
cnt = 0  # 검색 횟수

## 메인 코드
print(f'배열 일부 --> {dataAry[:5]} ~~~~ {dataAry[-5:]}')  # 배열의 일부분인 앞 5번째, 뒤 5번째 값 출력
position = binSearch(dataAry, findData)  # 배열에서 찾으려는 숫자의 인덱스 번호

if position == -1:  # 데이터를 못 찾은 경우
    print(f'{findData}(이)가 없네요.')
else:  # 데이터를 찾은 경우
    print(f'{findData}(은)는 {position} 위치에 있음')

print(f'## {cnt}회 검색함')  # 총 검색 횟수