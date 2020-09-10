import tensorflow as tf 
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
import PIL
import numpy as np

# load and prepare the image
def load_image(filename):
	# load the image from path
	img = load_img(filename, target_size=(224, 224))
	# convert to array
	img = img_to_array(img) / 255
	# reshape into a single sample with 3 channels
	img = img.reshape(1, 224, 224, 3)
	return img

def classifier(image_file):
	# load the image
    img = load_image(image_file)
	# load model
    model = load_model('models/model1.h5')
	# predict the class
    result = model.predict(img)
    proba = (round(np.max(result)*100, 2))
    pred = result[0].argmax()
    # print(pred)
    return pred, proba

# def get_class_details(class_name):
#     with open('makandex.json', 'r') as myfile:
#         data=myfile.read()
#     obj = json.loads(data)
#     name = obj[class_name]['name']
#     class_type = obj[class_name]['type']
#     desc = obj[class_name]['description1']
#     return name, class_type, desc