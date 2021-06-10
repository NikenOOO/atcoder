from collections import deque

N, X, Y = list(map(int, input().split()))


# 始点からの最小移動回数を管理する2次元配列。-1であれば未訪問。縦と横で400+1
dist = []
for i in range(403):
  dist.append([-1]*403)

# 障害物をdistに記録する
for i in range(N):
  x, y = list(map(int, input().split()))
  dist[x+201][y+201] = -2

# キューを用意して始点を入れる
Q = deque()
Q.append([201, 201])
dist[201][201] = 0

# キューから取り出しながら探索する
while len(Q) > 0:
  i, j = Q.popleft()
  # 6つの移動先を確認する
  for i2, j2 in [[i+1, j+1], [i, j+1], [i-1, j+1], [i+1, j], [i-1, j], [i, j-1]]:
    # もし盤面の範囲内でなければ無視する
    if not (0 <= i2 < 403 and 0 <= j2 < 403):
      continue
    # もし障害マスであれば無視する
    if dist[i2][j2] == -2:
      continue
    # もし未訪問（dist[i2][j2]が-1）であれば、距離を更新してキューに入れる
    if dist[i2][j2] == -1:
      dist[i2][j2] = dist[i][j] + 1
      Q.append([i2, j2])

# 始点から終点までの移動回数を出力
if dist[X+201][Y+201] > 0:
  ans = dist[X+201][Y+201]
else:
  ans = "-1"

print(ans)