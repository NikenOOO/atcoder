N, M, Q = map(int, input().split())

rel = []

# N個の頂点の関係性を配列に格納する
for _ in range(0, N):
  check = []
  for __ in range(0, N):
    check.append(False)
  rel.append(check)

# M個の頂点の情報を格納する
for i in range(0, M):
  u, v = map(int, input().split())
  u -= 1
  v -= 1
  rel[u][v] = True
  rel[v][u] = True

# Cの配列を作成し、格納する
C = list(map(int, input().split()))

# クエリを受け取り処理する
for _ in range(0, Q):
  # Sはクエリを受け取る配列
  S = list(map(int, input().split()))

  # 処理1の時
  if S[0] == 1:
    x = S[1] - 1
    print(C[x])
    for i in range(0, N):
      if rel[x][i]:
        C[i] = C[x]

  # 処理2の時
  if S[0] == 2:
    x = S[1] - 1
    y = S[2]
    print(C[x])
    C[x] = y