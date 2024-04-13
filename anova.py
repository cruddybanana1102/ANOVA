""" Assumptions: there re 10 data points for every sample in the group. the independence assumption across the samples is assumed, as is important for anova.
    two normality tests have been tried on for every sample, although with 10 data points we have sample complexity issues???
    tests for homoskesdasticity of data haven't been performed either, but should be done for anova

    all samples within a group are concatenated and the anova test has been performed to check if the groups themselves have been derived from the same populations

    """
import pandas as pd
import os
import sys
import numpy as np
import scipy as sp
import matplotlib

df = pd.read_excel("popvax.xlsx")
df = df.drop("Sr. No.", axis=1).drop("Parameter", axis=1)

#groupA = [col for col in df if col.startswith("Group A")]
data_matrix = df.to_numpy()
#print(data_matrix)

for i,row in enumerate(data_matrix.transpose()):
    pass
    #statistic, pval = sp.stats.shapiro(row)
    #statistic, pval = sp.stats.normal(row)
    #print("column no = ", i, "statistic = ", statistic)
    #print("column no = ", i, "p value = ", pval)

#means = []
#variances = []
#m = 0 #used to compute the grand mean

#for row in data_matrix.transpose():
#    means.append(np.mean(row))
#    variances.append(np.var(row, ddof=1))
#    for scalar in row:
#        m = m + scalar
#
#grand_mean = m/(len(data_matrix)*len(data_matrix[0]))

D = data_matrix.transpose()
F_val, pval = sp.stats.f_oneway(D[0],D[1],D[2])
print("group A: ")
print("F value = ", F_val)
print("p value = ", pval)

F_val, pval = sp.stats.f_oneway(D[3],D[4],D[5])
print("group B: ")
print("F value = ", F_val)
print("p value = ", pval)

F_val, pval = sp.stats.f_oneway(D[6],D[7],D[8],D[9])
print("group C: ")
print("F value = ", F_val)
print("p value = ", pval)

# Do the one way anova across groups
groupA = D[0]+D[1]+D[2] 
groupB = D[3]+D[4]+D[5] 
groupC = D[6]+D[7]+D[8]+D[9]


F_val, pval = sp.stats.f_oneway(groupA, groupB, groupC)
print("Within groups: ")
print("F value = ", F_val)
print("p value = ", pval)



