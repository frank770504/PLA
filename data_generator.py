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
    return (scale * np.random.random_sample( (dim,) )) + shift
  def SetDataLabel(self, label):
    self.label_ = label
    return 0


##########
## test ##
##########


