import numpy as np
import tensorflow as tf
from tensorflow import keras
import tensorflow_datasets as tfds
import shutil
import os

def scale(image, label):
    image = tf.cast(image, tf.float32)
    image /= 255
    return image, label

def evaluate_models():
    best_model_path = ""
    best_accuracy = 0
    
    for i in range(1, 4):
        model_path = "trained_model/saved_model_versions/"
        model = keras.models.load_model(model_path)
        
        datasets, _ = tfds.load(name='fashion_mnist', with_info=True, as_supervised=True)
        ds = datasets['test'].map(scale).cache().shuffle(10000).batch(64)
        
        _, accuracy = model.evaluate(ds)
        
        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_model_path = model_path

    destination = "trained_model/saved_model_versions/4"
    if os.path.exists(destination):
        shutil.rmtree(destination)

    shutil.copytree(best_model_path, destination)
    print(f"Best model with accuracy {best_accuracy} is copied to {destination}")

if __name__ == "__main__":
    evaluate_models()




