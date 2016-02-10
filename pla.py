import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import data_generator as dg

# 1x + 1y + 0 = 0

def DataGeneration(n, dim, upper, lower, ref):
  i = 0;
  while i < n:
    dum = dg.Data(dg.Dimension(dim, upper, lower))
    dum.SetDataLabel(np.sign(np.dot(dum.value_, ref)))
    yield dum
    i = i + 1

DataHandel = DataGeneration(100, 2, 10, -10, np.array([1 ,1 ,0]))
plt.figure()
for data in DataHandel:
  if data.label_ > 0:
    plt.plot( data.value_[0], data.value_[1], 'b.')
  else:
    plt.plot( data.value_[0], data.value_[1], 'r.')

plt.title('x vs y')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
#plt.savefig('sp_vs_sl_{}.png'.format(name))
