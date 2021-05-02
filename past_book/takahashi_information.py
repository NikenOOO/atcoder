[c11, c12, c13] = list(map(int, input().split()))
[c21, c22, c23] = list(map(int, input().split()))
[c31, c32, c33] = list(map(int, input().split()))

check = True
# 1行と2行の差を調べる
if c11 - c21 != c12 - c22 or c11 - c21 != c13 - c23:
  check = False

# 2行と3行の差を調べる
if c21 - c31 != c22 - c32 or c21 - c31 != c23 - c33:
  check = False

# 1列と2列の差を調べる
if c11 - c12 != c21 - c22 or c11 - c12 != c31 - c32:
  check = False

# 2列と3列の差を調べる
if c12 - c13 != c22 - c23 or c12 - c13 != c32 - c33:
  check = False

if check:
  ans = "Yes"
else:
  ans = "No"

print(ans)