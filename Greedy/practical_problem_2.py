N, M = map(int, input().split())
'''
card = []
for i in range(N):  #배열 입력
  card.append([])
  card[i] = list(map(int, input().split()))

card_ = []  #각 행의 최솟값 모음

for i in range(N):
  card[i].sort()
  card_.append(card[i][0])

card_.sort()  #각 행의 최솟값 정렬
print(card_[-1])
'''

#min() 함수 사용
result = 0
for i in range(N):
  card = list(map(int, input().split()))
  card_min = min(card)
  result = max(result, card_min)

print(result)

#이중 for문 사용(생략)