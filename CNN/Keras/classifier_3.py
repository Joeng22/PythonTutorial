#CNN classifer for Fashion mnist

from tensorflow.keras import datasets

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Conv2D,MaxPool2D,Dropout,Flatten
from tensorflow.keras.utils import to_categorical

def main():
    dataset = datasets.fashion_mnist

    (x_train,y_train),(x_test,y_test) = dataset.load_data()

    print("x_train shape:",x_train.shape)
    print("y_train shape:",y_train.shape)
    print("x_test shape:",x_test.shape)
    print("y_test shape:",y_test.shape)
    

    model = Sequential()

    model.add(Conv2D(16,kernel_size=(3,3),strides=(1,1),padding='valid',activation="relu",input_shape=(28,28,1)))
    model.add(MaxPool2D(pool_size=(2,2)))

    model.add(Flatten())

    model.add(Dense(100,activation="relu"))
    model.add(Dense(10,activation="softmax"))

    y_train = to_categorical(y_train,10)
    y_test = to_categorical(y_test,10)

    model.compile(loss="categorical_crossentropy",metrics=["accuracy"],optimizer="adam")
    model.fit(x_train,y_train,batch_size=16,epochs=50,validation_data=(x_test,y_test))

if __name__=="__main__":
    main()