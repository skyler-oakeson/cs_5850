import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import zscore
data = {"value": [78, 85, 92, 88, 91, 73, 95, 89, 77, 14, 79, 90, 83, 87, 0, 0, 81, 86, 93, 80, 82, 88, 85, 89, 92, 75, 84, 90, 88, 83, 79, 77, 148, 250, 87, 85, 82, 88, 90, 84, 10, 78, 85, 89, 87, 92, 80, 83, 85, 100, 81]}

df = pd.DataFrame(data)


zscore = df.apply(zscore)
print(zscore)
