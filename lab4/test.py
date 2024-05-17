from collections import namedtuple
import numpy as np


def hard_lim(x):
  return -1 if x < 0 else 1


x = np.array([[8, 9, 9], [4, 4, 6], [9, 8, 8], [5, 6, 4]])
y = np.array([1, -1, 1, -1])
w = np.array([[0, 0, 0]])
b = 0
c = 0
t = 4
i = 0
while t != 0:
  c += 1
  print(f"Lan lap { c }")
  if i >= 4:
    i = 0
  tmp = np.array([x[i]])
  realY = hard_lim(np.dot(w, tmp.T) + b)
  if realY != y[i]:
    w += np.dot(y[i] - realY, x[i])
    b += y[i] - realY
    t = 4
  else:
    t -= 1
  print("w = ", w)
  print("b = ", b)
  i += 1

x_test = np.array([[8, 7, 8]])
y_test = hard_lim(np.dot(w, x_test.T))
print(x_test, " => ", y_test)
