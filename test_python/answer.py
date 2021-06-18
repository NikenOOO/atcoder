
N, W = list(map(int, input().split()))

ws = [0]
vs = [0]

for i in range(N):
  w, v = list(map(int, input().split()))
  ws.append(w)
  vs.append(v)

v_range = N*5
weight = []
for i in range(N+1):
  weight.append([10**9+1]*(v_range+1))


weight[0][0] = 0

for i in range(1, N+1):
  for v in range(v_range+1):
    weight[i][v] = min(weight[i][v], weight[i-1][v])
    if v - vs[i] >= 0:
      weight[i][v] = min(weight[i][v], weight[i-1][v-vs[i]]+ws[i])
print(weight)

ans = 0
for i in range(N+1):
  for j in range(v_range+1):
    if weight[i][j] <= W and j >= ans:
      ans = j

print(ans)