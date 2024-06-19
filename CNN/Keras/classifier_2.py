import tensorflow as tf

if __name__=="__main__":
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(8,activation="relu",input_shape=(8,)))
    model.add(tf.keras.layers.Dense(8,activation="relu"))
    model.add(tf.keras.layers.Dense(1,activation="sigmoid"))

    #model.compile(optimizer="adam",matrics=["accuracy"],loss="binary")

    print(model.compile.__defaults__)
    print(model.compile.__code__.co_varnames)
    print(model.compile.__code__.co_argcount)