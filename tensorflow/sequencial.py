import tensorflow as tf
import numpy as np
from tensorflow import keras

model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')

xs = np.array([float(i) for i in range(20)], dtype=float)
ys = np.array([float(i * 2) for i in range(20)], dtype=float)

model.fit(xs, ys, epochs=500)

print(model.predict([10.0]))