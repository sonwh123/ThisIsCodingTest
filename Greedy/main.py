N, M, K = map(int, input().split())
# print('{} {} {}'.format(N, M, K))
array = []
result = 0

array = list(map(int, input().split()))       #배열 입력
# for i in array:
#   array[i] = int(array[i])
  
array.sort()
first_big = array[-1]
second_big = array[-2]

# first_big = array[0]         #가장 큰 수 추출 
# for i in array:
#   if first_big < array[i]:
#     first_big = array[i]


if M <= K:
  result = first_big * M
else:
  s = int(M / (K+1))
  f = M - s
  # print('{} {}'.format(f, s))
  result = first_big * f + second_big * s

print(result)