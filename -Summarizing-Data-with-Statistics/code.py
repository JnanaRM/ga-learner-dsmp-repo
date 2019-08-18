# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(path)

#path of the data file- path
data['Gender'].replace('-', 'Agender',inplace=True)
gender_count = data['Gender'].value_counts()
gender_count.plot(kind='bar')
plt.show()
#Code starts here 




# --------------
#Code starts here
alignment = data['Alignment'].value_counts()
plt.pie(alignment,labels=alignment.index,autopct='%1.1f%%')
plt.title('Character Alignment')
plt.show()


# --------------
#Code starts here
sc_df = data[['Strength','Combat']] 
mean_Strength = sc_df.Strength.mean()
mean_Combat = sc_df.Combat.mean()
diff_Strength = sc_df.Strength - mean_Strength
diff_Combat = sc_df.Combat - mean_Combat
summation = (diff_Strength * diff_Combat).sum()
#sc_covariance= summation/(sc_df.shape[0])
sc_covariance= summation/593
print(sc_covariance)

sc_strength = sc_df.Strength.std()
sc_combat = sc_df.Combat.std()
sc_pearson = sc_covariance/(sc_strength * sc_combat)
print(sc_pearson)

ic_df = data[['Intelligence','Combat']] 
mean_Intelligence = ic_df.Intelligence.mean()
mean_Combat = ic_df.Combat.mean()
diff_Intelligence = ic_df.Intelligence - mean_Intelligence
diff_Combat = ic_df.Combat - mean_Combat
summation = (diff_Intelligence * diff_Combat).sum()
#ic_covariance= summation/ic_df.shape[0]
ic_covariance= summation/593
print(ic_covariance)

ic_intelligence = ic_df.Intelligence.std()
ic_combat = ic_df.Combat.std()
ic_pearson = ic_covariance/(ic_intelligence * ic_combat)
print(ic_pearson)


# --------------
#Code starts here
total_high = data.Total.quantile(0.99)
super_best = data[data['Total'] > total_high]
super_best_names = [super_best['Name']]
print(super_best_names)


# --------------
#Code starts here
fig, (ax_1, ax_2, ax_3) = plt.subplots(1,3,figsize=(20,10))
data.boxplot(column = 'Intelligence',ax=ax_1)
data.boxplot(column = 'Speed',ax=ax_2)
data.boxplot(column = 'Power',ax=ax_3)
ax_1.set_title('Intelligence')
ax_2.set_title('Speed')
ax_3.set_title('Power')
plt.show()


