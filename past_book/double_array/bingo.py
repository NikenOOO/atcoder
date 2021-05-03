ans = False
# 初期のビンゴカードを受け取る
bingo = []
for _ in range(0,3):
  row = list(map(int, input().split()))
  bingo.append(row)

# 結果のカードを作成する
bingo_result = []
for i in range(0,3):
  bingo_result.append([False, False, False])

# Nの情報を受け取る
N = int(input())

# 結果の反映
for _ in range(0, N):
  b = int(input())
  for i in range(0,3):
    for j in range(0,3):
      if b == bingo[i][j]:
        bingo_result[i][j] = True

# 横の評価
for i in range(0, 3):
  if bingo_result[i][0] and bingo_result[i][1] and bingo_result[i][2]:
    ans = True

# 縦の評価
for i in range(0, 3):
  if bingo_result[0][i] and bingo_result[1][i] and bingo_result[2][i]:
    ans = True

# 右下斜めの評価
if bingo_result[0][0] and bingo_result[1][1] and bingo_result[2][2]:
  ans = True

# 左下斜めの評価
if bingo_result[2][0] and bingo_result[1][1] and bingo_result[0][2]:
  ans = True

if ans:
  print("Yes")
else:
  print("No")