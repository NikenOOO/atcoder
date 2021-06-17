# Kまでの最小のコストを配列に格納、
# そこから1~Kまでの足場の最小値とコストの最小値を計算していく
# 問題：https://atcoder.jp/contests/dp/tasks/dp_b

N, K = list(map(int, input().split()))
h = list(map(int, input().split()))

# コスト0と1は1通りのみ
cost = [0]*N

# コスト2からはKによって変化する
for i in range(1, K+1):
  if i >= N:
    break
  # cost[i]の候補を格納する配列を定義する
  I = []
  for j in range(0, i):
    I.append(cost[j]+abs(h[j] - h[i]))
  cost[i] = min(I)

for i in range(K, N):
  C = []
  for j in range(1, K+1):
    C.append(cost[i-j]+abs(h[i-j]-h[i]))
  cost[i] = min(C)

print(cost[N-1])