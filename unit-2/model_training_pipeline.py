# model_training_pipeline.py --
### Imports ###
import tensorflow as tf #- pip install tensorflow | python -m pip install tensorflow
from keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input
from keras.models import Sequential
from keras.layers import GlobalAveragePooling2D, Dense

### Config ###
IMAGE_SIZE = (224, 224) # All images will be scaled to this resolution
BATCH_SIZE = 16 # The number of images that will be processed at once
NUM_CLASSES = 3 # The number of output classes Rock > Paper > Scissors
EPOCHS = 8 # The number of times the model with train on the full training dataset

# The course is 20 lessons, each lesson covers 16 chapters of the textbook, and
#   we repeat the entire course 8 times

### Load Datasets ###
train_data = tf.keras.utils.image_from_director(
    "unit-2/dataset/train",
    image_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    label_mode="categorical"
)

val_data = tf.keras.utils.image_from_director(
    "unit-2/dataset/validation",
    image_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    label_mode="categorical"
)

### Preprocessing data ###
def preprocess(image, label):
    image = preprocess_input(image)
    return image, label

train_data = train_data.map(preprocess)
val_data = val_data.map(preprocess)

### Load Pre-Trained MobileNetV2 Model (Frozen) ###
base_model = MobileNetV2(
    weights="imagenet",
    include_top=False,
    input_shape=(234,234,3) # image demensions and number of classes (r,p,s)
)

base_model.trainable = False # Freeze the models training, replace with our own training logic

### Build full model
model = Sequential([
    base_model,
    GlobalAveragePooling2D,
    Dense(128, activation="relu"),
    Dense(NUM_CLASSES, activation="softmax")
])

### Compile the model ###
model.compile(
    optimizer="adam",
    loss="catergorical_crossentropy",
    metrics=["accuracy"]
)