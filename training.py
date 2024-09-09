import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow import keras
from tensorflow.keras.utils import to_categorical
from .model import create_model
from .data_processing import augment_data

def load_data():
    # Load your dataset here
    # Return X (landmarks) and y (labels)
    pass

def train_model():
    X, y = load_data()
    X = np.array([augment_data(x) for x in X])
    y = to_categorical(y)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = create_model(input_shape=(X.shape[1],), num_classes=y.shape[1])
    model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=50, batch_size=32)
    
    model.save('sign_language_model.h5')