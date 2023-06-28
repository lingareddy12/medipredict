
import pandas as pd
import joblib

df=pd.DataFrame(columns=['radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean',
       'perimeter_se', 'area_se', 'radius_worst', 'texture_worst',
       'perimeter_worst', 'area_worst'])


loaded_clf = joblib.load('project1/breast_cancer.pkl')

class breastcancer:
    def predict(self,val):
        df.loc[len(df)] = val
        y_pred = loaded_clf.predict(df[:1])
        return y_pred[0]
        
# val=[17.99,10.38,122.80,1001.0,8.589,153.40,25.38,17.33,184.60,2019.0]
# a=breast_cancer()
# print(a.predict(val))
