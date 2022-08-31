import tensorflow as tf

def get_data():
    mnist=tf.keras.datasets.mnist
    (X_train_full,y_train_full),(X_test,y_test)=mnist.load_data()
    X_valid, X_train = X_train_full[:5000]/255., X_train_full[:5000]/255.
    y_valid,y_train = y_train_full[:5000],y_train_full[5000:]



    return (X_train,y_train)