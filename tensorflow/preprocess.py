# TensorFlow and tf.keras
import tensorflow as tf

# Helper libraries
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

fig, ax = plt.subplots()
def update(frame):
    global fig, ax
    fig.clear()
    ax = plt.imshow(train_images[frame])
    return train_images[frame]

ani = animation.FuncAnimation(fig=fig, func=update, frames=len(train_images), interval=1)
plt.show()