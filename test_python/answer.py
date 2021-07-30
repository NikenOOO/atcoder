H, Q = map(int, input().split())

ans = []

for _ in range(H):
  C = input()
  ans.append(C)
  ans.append(C)

for i in range(len(ans)):
  print(ans[i])