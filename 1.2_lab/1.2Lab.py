#mathplotlib inline
import numpy as np
import pandas as pd

ph = pd.read_csv('PastHires.csv')

degreecount = ph['Level of Education'].value_counts()
print(degreecount)

