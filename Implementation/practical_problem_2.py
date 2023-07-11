#N, M 입력받기
N, M = map(int, input().split())
#맵 만들기
maps = [[0] * M for _ in range(N)]

#방문한 육지 개수 설정
count = 1

#북, 동, 남, 서 방향 정의
directions = ((0,-1),(1,0),(0,1),(-1,0))

#첫 시작 위치 정보 받기
x, y, direction = map(int, input().split())
#맵 정보 입력 받기
for i in range(N):
  maps[i] = list(map(int, input().split()))

#방문한 육지는 '-1' 설정
maps[x][y] = -1

#시뮬레이션 시작
while True:
  #1단계 왼쪽 보기(함수로 재정의 가능)
  if direction == 0: 
    direction = 3
  else:
    direction -= 1

  #주변에 육지가 있을 때
  if maps[x+1][y] * maps[x][y+1] * maps[x-1][y] * maps[x][y-1] == 0:  
    #해당 방향으로 이동 가정
    dx = x + directions[direction][0]
    dy = y + directions[direction][1]
    #이동 가능할 때
    if maps[dx][dy] == 0:  
      #지나간 육지 개수 증가
      count += 1
      #실제로 이동
      x = dx
      y = dy
      maps[x][y] = -1
      
  #주변에 육지가 없을 때
  else:
    #해당 방향 뒤로 이동 가정
    dx = x - directions[direction][0]
    dy = y - directions[direction][1]
    
    #뒤가 바다일 때
    if maps[dx][dy] == 1:  
      break

    #뒤가 육지일 때
    else:    
      x = dx
      y = dy

#결과 출력
print(count)