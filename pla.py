import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import data_generator as dg

class PLA:
  def __init__(self):
    self.init = 0
    self.figure_ = plt.figure()
  def PlotDataList(self, handle, figure_number=0):
    plt.figure(figure_number)
    for data in handle:
      if data.label_ > 0:
        plt.plot( data.value_[0], data.value_[1], 'b.')
      else:
        plt.plot( data.value_[0], data.value_[1], 'r.')
    plt.title('x vs y')
    plt.xlabel('x')
    plt.ylabel('y')
  def PlotWeightLine(self, weight, figure_number=0, color='k'):
    plt.figure(figure_number)
    # ax + by + c = 0
    a = weight[0]
    b = weight[1]
    c = weight[2]
    x1 = -10
    y1 = ( -a * x1 - c ) / b
    x2 = 10
    y2 = ( -a * x2 - c ) / b
    plt.plot([x1, x2],[y1, y2], color)
  def ShowFigure(self, figure_number=0):
    plt.figure(figure_number)
    plt.show()
  def SaveFigure(self, name="test", figure_number=0):
    plt.savefig('pla_{}.png'.format(name))
  def EvaluateWeight(self, handle, weight):
    n = 0
    a = 0
    for data in handle:
      a = a + 1
      if np.sign(np.dot(data.value_, weight)) != data.label_:
        n = n + 1
    return float(n) / float(a)
  def Learning(self, handle, tolerance=0.01, time_out=1000):
    # init weight
    w = np.array([1 ,1 ,1])
    i = 0
    while True:
      i = i + 1
      # stop the process when the Ein is inder the tolerance or
      # doing over 100 times
      if self.EvaluateWeight(handle.GetDataList(), w) > tolerance or\
          i < 1000:
        # pick random data from list
        data = handle.GetRandomData()
        # update weight when it is not correct
        if np.sign(np.dot(data.value_, w)) != data.label_:
          w = w + data.label_ * data.value_
      else:
        break
    return w

########
# test #
########
pla = PLA()
# the target line is x + 2y + 0.5 = 0
# generate data from this line
ref_weight = np.array([1 ,2 ,0.5])
data = dg.DataGenerator(20, 2, 10, -10, ref_weight)
# learning by using PLA
weight = pla.Learning(data, 0.05)
pla.PlotDataList(data.GetDataList(), pla.figure_.number)
# black line is the calculated line (learning result)
pla.PlotWeightLine(weight, pla.figure_.number, 'k')
# red line is the refernce line
pla.PlotWeightLine(ref_weight, pla.figure_.number, 'm')
pla.ShowFigure(pla.figure_.number)
