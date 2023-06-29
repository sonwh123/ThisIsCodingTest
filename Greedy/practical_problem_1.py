N, M, K = map(int, input().split())

array = []
result = 0

array = list(map(int, input().split()))       #배열 입력
  
array.sort()
first_big = array[-1]
second_big = array[-2]

# if M <= K:
#   result = first_big * M
# else:
#   s = int(M / (K+1))
#   f = M - s

#   result = first_big * f + second_big * s

count = int(M/(K+1))*K
count += M%(K+1)          #가장 큰 수의 개수

result = first_big * count + second_big * (M - count)

print(result)