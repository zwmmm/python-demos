import os
import time

content = '菜🐔前来报道'

while True:
  os.system('clear')
  print(content)
  time.sleep(.2)
  content = content[1:] + content[0]
