import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Flatten, MaxPooling2D
from tensorflow.keras import Input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.metrics import Precision,Recall

import logging

logger = logging.getLogger(__name__)

dataset_dir = r'/polyaxon-data/aiap6/workspace/ce_zheng_neo/assignment5/data/tensorfood'

class CNN_Model():
    
    def __init__(self, dataset_dir, base_learning_rate = 0.0001, epochs = 10):
        # init your model here
        img_height = 224
        img_width = 224
        batch_size = 100
        
        # just to try out the parameters
        train_datagen = image.ImageDataGenerator(rescale=1./255,
                                           shear_range=0.2, 
                                           zoom_range=0.2, 
                                           horizontal_flip=True,
                                           validation_split=0.2)
        
        self.train_generator = train_datagen.flow_from_directory(dataset_dir, 
                                                            target_size=(img_height, img_width),
                                                            batch_size=batch_size,
                                                            class_mode='categorical',
                                                            subset='training') # set as training data
        
        self.validation_generator = train_datagen.flow_from_directory(dataset_dir,
                                                                 target_size=(img_height, img_width),
                                                                 batch_size=batch_size,
                                                                 class_mode='categorical',
                                                                 subset='validation') # set as validation data
    
        base_model = MobileNetV2(input_shape= (224, 224, 3),
                         include_top=False,
                         weights='imagenet')
        base_model.trainable = False
        
        # model architecture
        inputs = Input(shape=(224, 224, 3))
        base = base_model(inputs, training=False)
        pool1 = MaxPooling2D(pool_size=(2, 2))(base)
        flat = Flatten()(pool1)
        hidden_1 = Dense(500, activation = 'relu')(flat)
        hidden_2 = Dense(30, activation='relu')(hidden_1)
        out_layer = Dense(12, activation='softmax')(hidden_2)
        self.model = Model(inputs=inputs, outputs=out_layer)
        
        # compile model
        self.model.compile(optimizer=tf.keras.optimizers.Adam(lr=base_learning_rate),
                           loss='categorical_crossentropy',
                           metrics=['accuracy', Precision(), Recall()])
        self.epochs = int(epochs)
        
    def train(self):
                
        self.model.fit_generator(generator=self.train_generator,
                                 validation_data=self.validation_generator, 
                                 epochs = self.epochs)
        
    def test(self):
        metrics = self.model.evaluate(self.validation_generator)
        loss = metrics[0]
        acc = metrics[1]
        prec = metrics[2]
        recall = metrics[3]
        
        return loss, acc, prec, recall


