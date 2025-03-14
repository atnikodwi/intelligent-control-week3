import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
# Direktori dataset
train_dir = "seg_train/seg_train"
val_dir = "seg_test/seg_test"
# Augmentasi data
train_datagen = ImageDataGenerator(rescale=1./255, rotation_range=20, zoom_range=0.2, 
horizontal_flip=True)
val_datagen = ImageDataGenerator(rescale=1./255)
train_generator = train_datagen.flow_from_directory(train_dir, target_size=(150, 150), 
batch_size=32, class_mode='categorical')
val_generator = val_datagen.flow_from_directory(val_dir, target_size=(150, 150), batch_size=32, 
class_mode='categorical')
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
# Definisi model CNN
model = Sequential([
Conv2D(32, (3,3), activation='relu', input_shape=(150, 150, 3)),
MaxPooling2D(2,2),
Conv2D(64, (3,3), activation='relu'),
MaxPooling2D(2,2),
Flatten(),
Dense(128, activation='relu'),
Dropout(0.5),
Dense(6, activation='softmax')
])
# Kompilasi model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
# Training model
model.fit(train_generator, validation_data=val_generator, epochs=10)
# Simpan model
model.save('cnn_model.h5')