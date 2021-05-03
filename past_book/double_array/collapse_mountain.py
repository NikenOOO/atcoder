N = int(input())
sell = []

for _ in range(0, N):
  row = input()
  sell.append(row)

for k in range(0, N-1):
  for j in range(0, 2*N - 1):
    i = N - 2 - k
    if sell[i][j] == "#":
      if j-1 >= 0 and sell[i+1][j-1] == "X":
        sell[i] = list(sell[i])
        sell[i][j] = "X"
        sell[i] = "".join(sell[i])
      if sell[i+1][j] == "X":
        sell[i] = list(sell[i])
        sell[i][j] = "X"
        sell[i] = "".join(sell[i])
      if j+1 <= 2*N -2 and sell[i+1][j+1] == "X":
        sell[i] = list(sell[i])
        sell[i][j] = "X"
        sell[i] = "".join(sell[i])

print("\n".join(sell))