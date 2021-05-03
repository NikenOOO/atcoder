K = int(input())
[A, B] = list(map(int, input().split()))

multiple_number = []

i = 1
while i*K <= B:
  multiple_number.append(i*K)
  i += 1

ans = "NG"
for j in range(0, len(multiple_number)):
  if A <= multiple_number[j] <= B:
    ans = "OK"
    break

print(ans)