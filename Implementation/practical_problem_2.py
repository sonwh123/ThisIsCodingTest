N, M = map(int, input().split())
maps = [[0] * M for _ in range(N)]
count = 1

directions = ((0,-1),(1,0),(0,1),(-1,0))

x, y, direction = map(int, input().split())

start = [x, y]

for i in range(N):
  maps[i] = list(map(int, input().split()))

maps[x][y] = -1

while True:
  if direction == 0:      #1단계 왼쪽 보기
    direction = 3
  else:
    direction -= 1
    
  if maps[x+1][y] * maps[x][y+1] * maps[x-1][y] * maps[x][y-1] == 0:  #주변에 육지가 있을 때
    dx = x + directions[direction][0]
    dy = y + directions[direction][1]
  
    if maps[dx][dy] == 0:  #이동 가능할 때
      count += 1
      x = dx
      y = dy
      maps[x][y] = -1
  else:    #주변에 육지가 없을 때
    dx = x - directions[direction][0]
    dy = y - directions[direction][1]

    if maps[dx][dy] == 1:  #뒤가 바다일 때
      break
    else:    #뒤가 육지일 때
      x = dx
      y = dy

print(count)