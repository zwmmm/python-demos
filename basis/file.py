"""
获取文件后缀名
"""

def main(filename, is_dot = False):
  pos = filename.rfind('.')
  if 0 < pos < len(filename) - 1:
    index = pos if is_dot else pos + 1
    return filename[index:]
  else:
    return ''

if __name__ == "__main__":
  name = input('请输入文件名：')
  print(main(name))
