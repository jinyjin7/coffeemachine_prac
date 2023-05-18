"""
피보나치 수는 F(0) = 0, F(1) = 1일 때, 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 수 입니다.

예를들어

F(2) = F(0) + F(1) = 0 + 1 = 1
F(3) = F(1) + F(2) = 1 + 1 = 2
F(4) = F(2) + F(3) = 1 + 2 = 3
F(5) = F(3) + F(4) = 2 + 3 = 5
와 같이 이어집니다.

2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.

제한 사항
n은 2 이상 100,000 이하인 자연수입니다.
"""
# 문제풀이
# while문을 써보자
# 0 1 2 3 4 5 6  7  8  9 ....
# 0 1 1 2 3 5 8 13 21 34 ....
# f_prepre, f_pre , f, count


n=9

count = 1
f_prepre = 0 # F(n-2)
f_pre = 1 # F(n-1)
while True:
    f= f_prepre + f_pre # F(n) = F(n-1) + F(n-2)
    count += 1
    print(count)
    if count == n:
        break
    f_prepre = f_pre
    print("f_prepre",f_prepre)
    f_pre = f
    print("f_pre",f_pre)
answer = f%1234567

# 제출용 함수
def solution(n):
    k = 1
    f_prepre = 0
    f_pre = 1
    while True:
        f = f_prepre + f_pre
        k += 1
        if k == n:
            break
        f_prepre = f_pre
        f_pre = f
    answer = f%1234567
    return answer



"""
준열님 리팩토링

# 재귀함수 사용하기
def fibonacci(n, k=1, f_prepre=0, f_pre=1, f=1):
    if k==n: return f
    return fibonacci(n, k+1, f_pre, f, f_prepre+f_pre)


# F(n-2)
# F(n-1)
# F(n) = F(n-1) + F(n-2)
print(fibonacci(9))


재귀함수 - 팩토리얼

n =5

f = 1
count = 1
while True:
    count+=1
    f*=count
    if count ==n: break

print(f)

# def factorial(n,f=1,count=2):
#     if count > n : return f
#     return factorial(n,f*count,count+1)

def factorial(n):
    if n==1: return 1
    return n*factorial(n-1)

재귀함수 - 합계

def sum_(n):
    if n==1: return 1
    return n+sum_(n-1)

print(sum_(5))

"""