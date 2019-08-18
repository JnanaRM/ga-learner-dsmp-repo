# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df = pd.read_csv(path)
s = len(df)
a = df[df['fico'] > 700].shape[0]
p_a = a/s
print('p(A): ',p_a)

b = df[df['purpose'] == 'debt_consolidation'].shape[0]
p_b= b/s
print('p(B): ',p_b)

df1 = df[df['purpose'] == 'debt_consolidation']

ab = df[(df['purpose'] == 'debt_consolidation') & (df['fico'] > 700)].shape[0]
pab = ab/s

p_a_b = pab/p_a
print('p(B|A) : ',p_a_b)
p_b_a = (p_a_b * p_a) / p_b

print('p(A|B) : ',p_b_a)

result = p_b_a == p_a
print(result)




# --------------
# code starts here
df[df['paid.back.loan'] == 'Yes'].shape[0]
prob_lp = (df[df['paid.back.loan'] == 'Yes'].shape[0]) / s
print('p(A) : ',prob_lp)

prob_cs = (df[df['credit.policy'] == 'Yes'].shape[0]) / s
print('p(B) : ',prob_cs)

new_df = df[df['paid.back.loan'] == 'Yes']
prob_pd_cs = df[(df['paid.back.loan'] == 'Yes') & \
(df['credit.policy'] == 'Yes')].shape[0]/(s * prob_lp)
print('p(B|A) : ',prob_pd_cs)

bayes = (prob_pd_cs * prob_lp) / prob_cs
print('p(A|B) : ',bayes)

# code ends here


# --------------
# code starts here
res = df.purpose.value_counts().sort_values(ascending=False)
res.plot(kind='barh')
plt.show()

df1 = df[df['paid.back.loan'] == 'No']
res1 = df1.purpose.value_counts().sort_values(ascending=False)
res1.plot(kind='barh')
plt.show()
# code ends here


# --------------
# code starts here
inst_median = df.installment.median()
inst_mean = df.installment.mean()
print(inst_median)
print(inst_mean)
plt.hist(df.installment,bins=8)
plt.show()
plt.hist(df['log.annual.inc'],bins=8)
plt.show()
# code ends here


