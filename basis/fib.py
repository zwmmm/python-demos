def fib(number):
  a, b = 0, 1
  for _ in range(number):
    a, b = b, a + b
    yield b

if __name__ == "__main__":
  for key in fib(20):
    print(key)
