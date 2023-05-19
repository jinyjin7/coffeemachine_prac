#2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수, 
#solution을 완성해주세요.

#제한 조건
#행렬 arr1, arr2의 행과 열의 길이는 2 이상 100 이하입니다.
#행렬 arr1, arr2의 원소는 -10 이상 20 이하인 자연수입니다.
#곱할 수 있는 배열만 주어집니다.


#내가 시도한 도전 - 미완성임
arr1,arr2 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]],[[5, 4, 3], [2, 4, 1], [3, 1, 1]] #[[22, 22, 11], [36, 28, 18], [29, 20, 14]]
arr2 = [[1, 4], [3, 2], [4, 1]]
answer = [[]]
#저는 일단 변수지정에서 막히고 있습니다...
#arr2의 앞자리만 따서 리스트를 만들어준다
row = len(arr2) # 행 
col = len(arr2[0]) # 열
new_list = [[0 for i in range(row)] for j in range(col)]
# arr2[행][열] > arr2[열][행]
for i in range(row):
    for j in range(col):
        new_list[j][i]=arr2[i][j] #32 -> 23
answer = []
for i in arr1:
    new_row = []
    for j in new_list:
        sum=0
        for k in range(len(arr1[0])):
            sum+=i[k]*j[k]
        new_row.append(sum)
    answer.append(new_row)
    #원래 행열의 갯수대로 인자를 받아와서 리스트로 만들어주기
    #row의 갯수만큼 끊어줘서 리스트를 만들어주기

    for a in arr2:
        
        #새로운 리스트를 만들어서 arry2[i][k]만 모아준다
        new_arry=[]
            #하나씩 분해작업

    

#numpy를 이용한 행렬곱셈
arr1,arr2 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]],[[5, 4, 3], [2, 4, 1], [3, 1, 1]] #[[22, 22, 11], [36, 28, 18], [29, 20, 14]]
arr2 = [[1, 4], [3, 2], [4, 1]]

import numpy as np
#as np = 넘파이를 불러옴
#as np = 앞으로 numpy를 np라고 부를게요 라는 거일 거에요 아마..?
answer2 = np.array(arr1)@np.array(arr2)
print(answer2)










def solution(arr1, arr2):
    row = len(arr2)
    col = len(arr2[0])
    new_list = [[0 for i in range(row)] for j in range(col)]
    for i in range(row):
        for j in range(col):
            new_list[j][i]=arr2[i][j]
    answer = []
    for i in arr1:
        new_row = []
        for j in new_list:
            sum=0
            for k in range(len(arr1[0])):
                sum+=i[k]*j[k]
            new_row.append(sum)
        answer.append(new_row)
    return answer
#[[2, 3, 2], [4, 2, 4], [3, 1, 4]]	[[5, 4, 3], [2, 4, 1], [3, 1, 1]]	[[22, 22, 11], [36, 28, 18], [29, 20, 14]]


#성광님 코드
def solution(arr1, arr2):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*arr2)] for A_row in arr1]



#zip(*) -> 리스트로 거꾸로
# lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# zipped = zip(*lists)
# print(list(zipped))  # 출력: [(1, 4, 7), (2, 5, 8), (3, 6, 9)]