import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import entropy
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.metrics import mutual_info_score
from scipy.stats.contingency import crosstab


# 1 - Equal Width slide 59
data = pd.read_csv("AustralianCreditApproval.csv")
data["A13_8_bin"] = pd.cut(data["A13"], bins=8)
data["A13_14_bin"] = pd.cut(data["A13"], bins=14)
data["A13_q_4"] = pd.qcut(data["A13"], q=4, duplicates="drop")
data["A13_q_12"] = pd.qcut(data["A13"], q=12, duplicates="drop")


def calculate_entropy(data, col):
    label_counts = data[col].value_counts()
    probablities = label_counts / label_counts.sum()
    entropy_value = entropy(probablities, base=2)
    print(col, "entropy val: ", entropy_value)

discretization = ["A13_8_bin", "A13_14_bin", "A13_q_4", "A13_q_12"]

for dis in discretization:
    calculate_entropy(data, dis)


# #2 -- Standardize and Normalize
# standard_scaler = StandardScaler()
# minmax_scaler = MinMaxScaler()
# data = pd.read_csv("AustralianCreditApproval.csv")
# standardized = pd.DataFrame(
#     standard_scaler.fit_transform(data), 
#     columns=data.columns
# )
# normalized = pd.DataFrame(
#     minmax_scaler.fit_transform(data), 
#     columns=data.columns
# )
# standardized_and_normalized = pd.DataFrame(
#     minmax_scaler.fit_transform(standard_scaler.fit_transform(data)),
#     columns=data.columns
# )
#
# bins = 8
# fig, axes = plt.subplots(nrows=2, ncols=2, sharey=True, tight_layout=True)
# axes = axes.flatten()
#
# axes[0].hist(data["A2"], bins)
# axes[0].set_title("A2 Values")
#
# axes[1].hist(standardized["A2"], bins)
# axes[1].set_title("A2 Standardized Values")
#
# axes[2].hist(normalized["A2"], bins)
# axes[2].set_title("A2 Normalized Values")
#
# axes[3].hist(standardized_and_normalized["A2"], bins)
# axes[3].set_title("A2 Standardized and Normalized Values")
#
# for ax in axes:
#     ax.set_xlabel('Values')
#     ax.set_ylabel('Frequency')
#
# plt.show()


# 3
# data = pd.read_csv("AustralianCreditApproval.csv")
# print(type(data["A4"]))
# grouped = data.groupby("A4")[["A13", "A14"]].agg([
#     'sum',
#     'min',
#     'max',
#     'mean',
#     'median',
#     ('quantile_0.10', lambda x: x.quantile(0.10)),
#     ('quantile_0.90', lambda x: x.quantile(0.90)),
#     'std'
#     ])
#
# print(grouped)
#
#
# 4 Correlation and Mutial Information
data = pd.read_csv("AustralianCreditApproval.csv")


def calculate_covariance(x , y):
    assert(len(x) == len(y))
    n = len(x)
    xm = x.mean()
    ym = y.mean()
    sum = 0
    for item in zip(x, y):
        xi, yi = item
        sum += (xi - xm)*(yi - ym)
    
    return sum / (n - 1)


def calculate_correlation(x, y):
    assert(len(x) == len(y))
    n = len(x)
    sx = x.std()
    sy = y.std()
    xm = x.mean()
    ym = y.mean()

    sum = 0
    for item in zip(x, y):
        xi, yi = item
        sum += ((xi - xm) / sx) * ((yi - ym) / sy)

    return (1 / (n - 1)) * sum


# print(calculate_covariance(data["A4"], data["A12"]))
# print(calculate_correlation(data["A4"], data["A12"]))


# Numerical data A2, A3, A7, A10, A13, A14
# corr_matrix = data.corr()
# names = ["A2", "A3", "A7", "A10", "A13", "A14"]
# numerical = corr_matrix.loc[names, names]
# print(numerical)


# # Catagorical data A1, A4, A5, A6, A8, A9, A11, A12, A15
# catagorical = ["A1", "A4", "A5", "A6", "A8", "A9", "A11", "A12", "A15"]
# mi = pd.DataFrame(0, index=catagorical, columns=catagorical, dtype=float)
# for c1 in catagorical:
#     for c2 in catagorical:
#         X = data[[c1]]
#         y = data[[c2]]
#         c = crosstab(X, y)
#         mi.loc[c1, c2] = mutual_info_score(labels_true=None, labels_pred=None, contingency = c[1])

# print(mi)
