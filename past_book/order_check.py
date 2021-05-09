N = int(input())
C = list(map(int, input().split()))
Q = int(input())

ans = 0

min_odd = 10000000000
min_all = 10000000000

for i in range(0, N):
  if i % 2 == 0:
    min_odd = min(min_odd, C[i])
  else:
    min_all = min(min_all, C[i])

dec_o = 0
dec_a = 0

for _ in range(0, Q):
  S = list(map(int, input().split()))
  # 単品販売
  if S[0] == 1:
    x = S[1]
    a = S[2]
    if x % 2 != 0:
      if C[x-1] - dec_a - dec_o >= a:
        C[x-1] = C[x-1] - a
        min_odd = min(min_odd, C[x-1])
        ans += a
    else: 
      if C[x-1] - dec_a >= a:
        C[x-1] = C[x-1] - a
        min_all = min(min_all, C[x-1])
        ans += a
  # セット販売
  elif S[0] == 2:
    a = S[1]
    if min_odd - dec_a - dec_o >= a:
      dec_o += a
  # 全種類販売
  elif S[0] == 3:
    a = S[1]
    if min(min_all - dec_a, min_odd - dec_a -dec_o) >= a:
      dec_a += a

for i in range(0, N):
  if i % 2 == 0:
    ans += dec_o

ans += N*dec_a

print(ans)