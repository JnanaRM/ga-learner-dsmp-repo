# --------------
import pandas as pd
from sklearn import preprocessing

#path : File path

# Code starts here
dataset = pd.read_csv(path)

# read the dataset
print(dataset.head())



# look at the first five columns

dataset.drop('Id',axis=1,inplace=True)
# Check if there's any column which is not useful and remove it like the column id

print(dataset.describe())
# check the statistical description



# --------------
# We will visualize all the attributes using Violin Plot - a combination of box and density plots
import seaborn as sns
from matplotlib import pyplot as plt

#names of all the attributes 

cols = dataset.columns
#number of attributes (exclude target)
size = dataset.iloc[:,0:-1].shape[1]

#x-axis has target attribute to distinguish between classes
x = dataset['Cover_Type']


#y-axis shows values of an attribute
y = dataset.drop('Cover_Type',axis=1)

#Plot violin for all attributes
for i in range(size):
    sns.violinplot(x,y.iloc[:,i])
    plt.show()


# --------------
import numpy
upper_threshold = 0.5
lower_threshold = -0.5


# Code Starts Here
subset_train = dataset.iloc[:,0:10]
data_corr = subset_train.corr()
sns.heatmap(data_corr)
correlation = data_corr.unstack().sort_values(kind='quicksort')
corr_var_list = correlation[((correlation > upper_threshold) & (correlation!= 1)) | (correlation < lower_threshold)]
print(corr_var_list)
# Code ends here




# --------------
#Import libraries 
from sklearn import cross_validation
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
# Identify the unnecessary columns and remove it 
dataset.drop(columns=['Soil_Type7', 'Soil_Type15'], inplace=True)


X = dataset.drop('Cover_Type',axis=1)
Y = dataset['Cover_Type']
# Scales are not the same for all variables. Hence, rescaling and standardization may be necessary for some algorithm to be applied on it.

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state=0)

#Standardized
#Apply transform only for continuous data
cont_cols = subset_train.columns
scaler = StandardScaler()
scaler.fit(X_train[cont_cols])
X_train_temp = scaler.transform(X_train[cont_cols])
X_test_temp = scaler.transform(X_test[cont_cols])
X_train[cont_cols] = X_train_temp
X_test[cont_cols] = X_test_temp
scaled_features_train_df = X_train
scaled_features_test_df = X_test
#Concatenate scaled continuous data and categorical






# --------------
from sklearn.feature_selection import SelectPercentile
from sklearn.feature_selection import f_classif
import numpy as np


# Write your solution here:
skb = SelectPercentile(score_func=f_classif,percentile=20)
skb.fit(X_train1,Y_train)
predictors = skb.transform(X_train1)
scores = skb.scores_
Features = X_train1.columns
d = {'Scores':scores,'Features':Features}
dataframe = pd.DataFrame(d,columns =['Scores','Features'])
dataframe = dataframe.sort_values(by='Scores',ascending=False)
support = np.asarray(skb.get_support())
top_k_predictors = list(dataframe['Features'][:predictors.shape[1]])
print(top_k_predictors)


# --------------
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, precision_score

clf = OneVsRestClassifier(LogisticRegression())
clf1 = OneVsRestClassifier(LogisticRegression())

model_fit_all_features = clf1.fit(X_train,Y_train)
predictions_all_features = model_fit_all_features.predict(X_test)
score_all_features = accuracy_score(Y_test,predictions_all_features)
print(score_all_features)

model_fit_top_features = clf.fit(scaled_features_train_df[top_k_predictors],Y_train)
predictions_top_features = model_fit_top_features.predict(scaled_features_test_df[top_k_predictors])
score_top_features = accuracy_score(Y_test,predictions_top_features)
print(score_top_features)


