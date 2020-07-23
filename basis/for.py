# 寻找花仙树

range_number = range(100, 300)
for num in range_number:
  low = num % 10
  mid = num // 10 % 10
  hig = num // 100
  if num == low ** 3 + mid ** 3 + hig ** 3:
    print(num)
