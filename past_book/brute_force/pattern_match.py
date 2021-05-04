S = input()
M = []

# 全ての文字列候補を作成する
C = "abcdefghijklmnopqrstuvwxyz."


def match_check(T, S):
  for i in range(0, len(S) - len(T) +1):
    # デフォルトはTrue
    ok = True

    # Sのi+j番目の文字列とTのj番目が等しくないかつ、.でないときFalse 
    for j in range(0, len(T)):
      if S[i+j] != T[j] and T[j] != ".":
        ok = False

    if ok:
      return True
  return False

# 1文字の確認
for c1 in C:
  if match_check(c1, S):
    M.append(c1)

# 2文字の確認
for c1 in C:
  for c2 in C:
    string = c1 + c2
    if match_check(string, S):
      M.append(string)

# 3文字の確認
for c1 in C:
  for c2 in C:
    for c3 in C:
      string = c1 + c2 + c3
      if match_check(string, S):
        M.append(string)

print(len(M))