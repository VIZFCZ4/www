from random import random, randbytes, choice

try:
  random()
except RuntimeError:
  pass
else:
  assert False

try:
  randbytes(5)
except RuntimeError:
  pass
else:
  print("randbytes() no")
  assert False

try:
  choice([1, 2, 3])
except RuntimeError:
  pass
else:
  assert False


def t1():
  from random import random, randbytes
  random()
  randbytes(5)
  choice([1,2,3])

def t2():
  random()
  randbytes(5)
  choice([1,2,3])

  t1()

def test():
    t1()
    t2()
