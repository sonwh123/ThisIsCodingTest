N, K = map(int, input().split())
count = 0

while N != 1:
  if N % K == 0:
    # N /= K        #나누기
    N = N // K      #몫
    count += 1
  else:
    N -= 1
    count += 1

print(count)