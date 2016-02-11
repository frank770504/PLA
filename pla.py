import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import data_generator as dg

class PLA:
  def __init__(self):
    self.init = 0
  def DataGeneration(self, n, dim, upper, lower, ref):
    i = 0;
    while i < n:
      dum = dg.Data(dg.Dimension(dim, upper, lower))
      dum.SetDataLabel(np.sign(np.dot(dum.value_, ref)))
      yield dum
      i = i + 1
  def PlotDataHandle(self, handle):
    plt.figure()
    for data in handle:
      if data.label_ > 0:
        plt.plot( data.value_[0], data.value_[1], 'b.')
      else:
        plt.plot( data.value_[0], data.value_[1], 'r.')
    plt.title('x vs y')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
    #plt.savefig('sp_vs_sl_{}.png'.format(name))
  def test(self):
    DataHandle = self.DataGeneration(20, 2, 10, -10, np.array([1 ,2 ,0]))
    self.PlotDataHandle(DataHandle)

########
# test #
########
pla = PLA()
pla.test()
