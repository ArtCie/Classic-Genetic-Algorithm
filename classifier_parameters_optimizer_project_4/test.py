import pandas as pd

from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import SVC
from sklearn import metrics

def SVCParametersFitness(y, df, numberOfAtributtes, individual):
    split = 5
    cv = StratifiedKFold(n_splits=split)
    listColumnsToDrop=[] #lista cech do usuniecia

    for i in range(numberOfAtributtes,len(individual)):
        if individual[i]==0:
            listColumnsToDrop.append(i-numberOfAtributtes)
    dfSelectedFeatures=df.drop(df.columns[listColumnsToDrop], axis=1, inplace=False)
    mms = MinMaxScaler()
    df_norm = mms.fit_transform(dfSelectedFeatures)
    estimator = SVC(kernel=individual[0],C=individual[1],degree=individual[2],
                    gamma=individual[3],coef0=individual[4],random_state=101)

    resultSum = 0
    for train, test in cv.split(df_norm, y):
        estimator.fit(df_norm[train], y[train])
        predicted = estimator.predict(df_norm[test])
        expected = y[test]
        tn, fp, fn, tp = metrics.confusion_matrix(expected,
                                                  predicted).ravel()
        result = (tp + tn) / (tp + fp + tn + fn)  # w oparciu o macierze
        resultSum = resultSum + result  # zbieramy wyniki z poszczególnych etapów walidacji krzyżowej
    return resultSum / split,

# ---- test data
# df = pd.read_csv("data_example.csv")
#
# y = df['Status']
# df.drop('Status', axis=1, inplace=True)
#
# df.drop('ID', axis=1, inplace=True)
# df.drop('Recording', axis=1, inplace=True)


# ---- actual data
df = pd.read_csv("data/data_main.csv")
df['class'] = df['class'].map({"Positive": 1, "Negative": 0})
df['Gender'] = df['Gender'].map({"Male": 1, "Female": 0})
y = df['class']

for column in df.columns[2:-1]:
    df[column] = df[column].map({"Yes": 1, "No": 0})

numberOfAttributes = len(df.columns)

print(numberOfAttributes)

ind = ['rbf', 0.2, 5, 0.1, 1]
print(SVCParametersFitness(y, df, numberOfAttributes, ind))