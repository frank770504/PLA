## PLA (Perceptron Learning Algorithm) Demo
### example
``` python
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
```
