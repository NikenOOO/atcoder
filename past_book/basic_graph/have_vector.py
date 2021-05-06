N, Q = map(int, input().split())

status = []

# N人のフォローの関係性を配列に格納する
for _ in range(0, N):
  arr = []
  for __ in range(0, N):
    arr.append(False)
  status.append(arr)

# 処理を全て受け取る
for _ in range(0, Q):
  S = list(map(int, input().split()))
  a = S[1] -1

  # フォロー
  if S[0] == 1:
    b = S[2] -1
    status[a][b] = True
  
  # フォロー全返し
  if S[0] == 2:
    for i in range(0, N):
      if status[i][a] == True:
        status[a][i] = True
  
  # フォローフォロー
  if S[0] == 3:
    stash = []
    for i in range(0, N):
      if status[a][i]:
        for j in range(0, N):
          if status[i][j] and j != a:
            stash.append(j)
    for i in stash:
      status[a][i] = True

# ステータスをフォーマットして出力
for i in range(0, N):
  res = []
  for j in range(0, N):
    if status[i][j]:
      res.append("Y")
    else:
      res.append("N")
  res_str = "".join(res)
  print(res_str)