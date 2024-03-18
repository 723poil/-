''' # 문제 이해 - 요구사항 정리 - 패턴 분석 - 구현 - 예외 케이스
중요 포인트: 1. 문제에서 나오는 전구 리스트의 인덱스와 실제 리스트의 인덱스 차이'''
### solution 1

# import sys
# num_bulb, num_command = map(int, sys.stdin.readline().split()) 
# bulb_list = [0] + list(map(int, sys.stdin.readline().split())) 
# # command_list = list(map(int, sys.stdin.readline().split()))

# command_mat = [list(map(int, sys.stdin.readline().split())) for _ in range(num_command)]

# # print(command_mat)
# # 1번째 명령 실행 함수
# def cmd_1(bulb_list, command_list):
#     if bulb_list[command_list[1]] == 0:
#         bulb_list[command_list[1]] += 1
#     else:
#         bulb_list[command_list[1]] -= 1
    
#     return bulb_list

# # 2번째 명령 실행 함수 # 2,4 일떄
# def cmd_2(bulb_list, command_list):
#     l = command_list[1] # l = 1
#     r = command_list[2] # r = 3
#     for i in range(l, r+1): # i = 1, 2, 3
#         if bulb_list[i] == 0:
#             bulb_list[i] += 1
#         else:
#             bulb_list[i] -= 1

#     return bulb_list

# # 3번째 명령 실행 함수
# def cmd_3(bulb_list, command_list):
#     l = command_list[1]
#     r = command_list[2]

#     #bulb_list[l:r] = 0 -> 이런 문법 없음
#     # 범위 l~r을 0으로 채운 리스트로 교체
#     bulb_list[l:r+1] = [0] * (r+1 - l)

#     return bulb_list

# # 4번째 명령 실행 함수
# def cmd_4(bulb_list, command_list):
#     l = command_list[1]
#     r = command_list[2]
#     bulb_list[l:r+1] = [1] * (r+1 - l)

#     return bulb_list
    

# def main(num_bulb, num_command, bulb_list, command_mat):
#     # for command_list in command_mat:
#     for command_list in command_mat:
#         # print(command_list)
#         # 1번째 명령
#         if command_list[0] == 1:
#             bulb_list = cmd_1(bulb_list, command_list)
#         elif command_list[0] == 2:
#             bulb_list = cmd_2(bulb_list, command_list)
#         elif command_list[0] == 3:
#             bulb_list = cmd_3(bulb_list, command_list)
#         else:
#             bulb_list = cmd_4(bulb_list, command_list)

#     for i in range(1,num_bulb+1):
# 	    print(bulb_list[i], end=' ')


# main(num_bulb, num_command, bulb_list, command_mat)
# #####################################################################

### solution 2
n, m = map(int,input().split())
bulb = [0] + list(map(int,input().split()))
for _ in range(m):
	a,b,c = map(int, input().split())
	if a == 1:
		bulb[b] = c
	
	elif a == 2:  # 전구 상태 변경
		for i in range(b,c+1):
			if bulb[i] == 0:
				bulb[i] = 1
			elif bulb[i] == 1:
				bulb[i] = 0

	elif a == 3:  # 켜진 전구 끄기
		for i in range(b,c+1):
			if bulb[i] == 1:
				bulb[i] = 0
	elif a == 4:  # 꺼진 전구 켜기
		for i in range(b,c+1):
			if bulb[i] == 0:
				bulb[i] = 1

for i in range(1,n+1):
	print(bulb[i], end=' ')
