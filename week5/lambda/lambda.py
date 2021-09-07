def doubleMulti(n):
  return lambda a : a * n

doubleNum = doubleMulti(9)

print(doubleNum(81))