knight = input()
x = ord(knight[0])-96
y = int(knight[1])
result = 0

move = [[1,2],[2,1],[-1,2],[2,-1],[-2,1],[1,-2],[-2,-1],[-1,-2]]

for m in move:
  dx = x + m[0]
  dy = y + m[1]
  if 1<=dx and dx<=8 and 1<=dy and dy<=8:
    result += 1

print(result)