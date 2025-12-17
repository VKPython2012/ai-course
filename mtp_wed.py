# model_training_pipeline.py
### Imports ###
import tensorflow as tf
from keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input
from keras.models import Sequential
from keras.layers import GlobalAveragePooling2D, Dense

### Config ###
IMAGE_SIZE = (224, 224) # All images will be scaled to this
BATCH_SIZE = 16 # number of images will be processed at once
NUM_CLASSES = 3 # The number of output classes R > P > S
EPOCHS = 8 # Amount of times the model with train on the full training dataset
