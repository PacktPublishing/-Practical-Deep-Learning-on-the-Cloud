import tensorflow as tf

mnist = tf.keras.datasets.mnist

(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(512, activation=tf.nn.relu),
  tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=2)
print('Evaluation:')
print(model.evaluate(x_test, y_test))
model.save('MNISTmodel.h5')
modelImported = tf.keras.models.load_model('MNISTmodel.h5')
print('Evaluation by imported model:')
print(modelImported.evaluate(x_test, y_test))