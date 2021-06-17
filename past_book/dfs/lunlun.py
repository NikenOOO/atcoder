# ルンルン数を深さ優先探索で一通り配列に格納し、ソート、
# 最後にK番目のルンルン数を出力する
# 問題：https://atcoder.jp/contests/abc161/tasks/abc161_d

K = int(input())

# ルンルン数を格納する配列を定義する
L = []

# Kの最大値の出力が与えられているため、それを最大値と設定する
max = 3234566667

def dfs(n):
  if max < n:
    return

  global L
  L.append(n)
  mod = n % 10

# 末尾の数字をそのまま追加する
  dfs(10*n+mod)

# 末尾の数字に＋１して追加する、ただし９は含まない
  if mod < 9:
    dfs(10*n+mod+1)

# 末尾の数字に-１して追加する、ただし０は含まない
  if mod >= 1:
    dfs(10*n+mod-1)

for i in range(1, 10):
  dfs(i)

L.sort()
print(L[K-1])