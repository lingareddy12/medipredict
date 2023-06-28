import numpy as np
from tensorflow import keras 

model = keras.Sequential([
    keras.layers.Dense(units=8, activation='relu', input_shape=(8,)),
    keras.layers.Dense(units=64, activation='relu'),
    keras.layers.Dense(units=128, activation='relu'),
    keras.layers.Dense(units=256, activation='relu'),
    keras.layers.Dense(units=512, activation='relu'),
    keras.layers.Dense(units=1, activation='sigmoid') 
])


model.load_weights('project1/heart_weights1.h5')


class heart:
    def predict(self,val): 
        val=np.array([val])
        y_pred = model.predict(val)
        return y_pred[0][0]
    

