N = int(input())
all_zorome = []

for i in range(0, 555556):
  str_i = f"{i}"
  if len(str_i) == str_i.count(str_i[0]):
    all_zorome.append(i)


print(all_zorome[N])