import numpy as np

p = np.array([[8, 9, 9], [4, 4, 6], [9, 8, 8], [5, 6, 4]])
test = np.array([[8, 7, 8]])
t = [1, -1, 1, -1]
w = np.array([[0, 0, 0]])
b = 0
a = 0
k = 0
while True:
  d = True
  k += 1
  print("lan lap thu ", k)

  for i in range(4):
    x = np.array([p[i]])
    n = w.dot(x.T)+b
    a = -1 if n < 0 else 1

    if not np.array_equal(t[i], a):
      e = t[i]-a
      w = w+np.dot(e, x)
      b = b+e
      d = False
  print("w=", w)
  print("b=", b)
  if d == True:
    break


n = w.dot(test.T)+b
wr = -1 if n < 0 else 1

print("Voi x1 = 8, x2 = 7, x3 = 8 thuoc lop "+"\""+str(wr)+"\"")
print("n", n)
