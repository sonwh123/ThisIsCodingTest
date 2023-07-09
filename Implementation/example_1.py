#구현 예제 4-1(시뮬레이션 유형)
#O(N)으로 시간 복잡도는 여유로움
N = int(input())
x, y = 1, 1
plan = []

# plan = list(map(str, input().split()))
plan = input().split()  #input은 기본적으로 string

for s in plan:
  if s == 'L':
    if y > 1:
      y -= 1
  elif s == 'R':
    if y < N:
      y += 1
  elif s == 'U':
    if x > 1:
      x -= 1
  elif s == 'D':
    if x < N:
      x += 1

#print(f'{x} {y}')
print(x, y)