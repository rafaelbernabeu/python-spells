# TensorFlow and tf.keras
import tensorflow as tf

# Helper libraries
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

fig, ax = plt.subplots()
plt.title(class_names[train_labels[0]])
axi = plt.imshow(train_images[0])

def update(frame):
    axi.set_data(train_images[frame])
    plt.title(class_names[train_labels[frame]])
    return fig

ani = animation.FuncAnimation(fig=fig, func=update, frames=range(1, len(train_images)), interval=1000)
plt.show()