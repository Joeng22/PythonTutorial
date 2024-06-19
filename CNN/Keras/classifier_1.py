import tensorflow as tf

tf.__version__



if __name__=="__main__":
    mnist_fashion = tf.keras.datasets.fashion_mnist
    (train_images,train_label),(test_images,test_label) = mnist_fashion.load_data()
    print(train_label.shape)


    '''
    Classifier Model
    '''
    model = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=(28,28)),
        tf.keras.layers.Dense(128,activation="relu"),
        tf.keras.layers.Dense(10,activation="sigmoid")
    ]
    )

    model.compile(optimizer="adam",loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),metrics=["accuracy"])
    model.fit(train_images,train_label,epochs=10)