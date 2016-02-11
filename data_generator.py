import numpy as np
import matplotlib
import matplotlib.pyplot as plt

class Dimension:
  def __init__(self, dim, upper=1, lower=-1):
    self.dim_ = dim
    self.upper_ = upper
    self.lower_ = lower
  def GetDimension(self):
    return self.dim_
  def GetDimensionShift(self):
    return self.lower_
  def GetDimensionScale(self):
    return self.upper_ - self.lower_

class Data:
  def __init__(self, value_nplist, label):
    self.label_ = label
    self.value_ = value_nplist
  def __init__(self, dimension, label=0):
    self.label_ = label
    self.value_ = self.DataGenerator(dimension)
  def DataGenerator(self, dimension):
    dim = dimension.GetDimension()
    shift = dimension.GetDimensionShift()
    scale = dimension.GetDimensionScale()
    return np.hstack([(scale * np.random.random_sample( (dim,) )) + shift, 1])
  def SetDataLabel(self, label):
    self.label_ = label
    return 0

class DataGenerator:
  def __init__(self, n = 0, dim = 0, upper = 0, lower = 0, ref = 0):
    self.list_ = self.Generator(n, dim, upper, lower, ref)
    self.number_ = n if n >= 1 else 1
  def SetList(self, data_list):
    self.list_ = data_list
  def SetNumber(self, number):
    self.number_ = number
  def Generator(self, n, dim, upper, lower, ref):
    i = 0;
    dum_list = []
    while i < n:
      dum = Data(Dimension(dim, upper, lower))
      dum.SetDataLabel(np.sign(np.dot(dum.value_, ref)))
      dum_list.append(dum)
      i = i + 1
    return dum_list
  def GetRandomData(self):
    ind = np.floor(np.random.random_sample( (1,) ).item(0) * self.number_)
    return self.list_[int(ind)]
  def GetDataList(self):
    return self.list_
  #~ def GetDataBegin(self):
  #~ def GetDataEnd(self):
##########
## test ##
##########
