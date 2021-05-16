S = input()
ok = []
hatena = []

for i in range(0, 10):
  if S[i] == "o":
    ok.append(i)
  elif S[i] == "?":
    hatena.append(i)

ans = 0

if len(ok) >= 5:
  ans = 0
elif len(ok) == 4:
  ans = 24
elif len(ok) == 3:
  ans = 36 + 24*len(hatena)
elif len(ok) == 2:
  ans = 14 + 24 * len(hatena) + 12* len(hatena)**2
elif len(ok) == 1:
  ans = 1 + 4 * len(hatena)**3 + 4 * len(hatena) + 6 * len(hatena)**2

if ans == 0 and len(ok) == 0:
  ans = len(hatena)**4

print(ans)