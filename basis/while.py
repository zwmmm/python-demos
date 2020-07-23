import random
answer = random.randint(1, 10)
counter = 0

while True:
  counter += 1
  number = int(input('请输入：'))
  if number < answer:
    print('小了')
  elif number > answer:
    print('大了')
  else:
    print('正确')
    break

print('你总共猜了%d' % counter)
