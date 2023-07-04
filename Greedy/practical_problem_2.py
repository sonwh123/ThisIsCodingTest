N, M = map(int, input().split())

card = []
for i in range(N):  #배열 입력
  card.append([])
  card[i] = list(map(int, input().split()))
  # card[i] = []
  # temp = []
  # temp = list(map(int, input().split()))
  # for j in range(M):
  #   card[i][j] = temp[j]

# for i in card:
#   print(i)

card_ = []  #각 행의 최솟값 모음

for i in range(N):
  card[i].sort()
  card_.append(card[i][0])

card_.sort()  #각 행의 최솟값 정렬
print(card_[-1])