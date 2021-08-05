from flask import Flask, request, jsonify
import os
import numpy as np
from tensorflow.keras.models import Model
from tensorflow.keras.applications.xception import Xception
from tensorflow.keras.applications.xception import preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model
#from keras.preprocessing import img_to_array

model=None

app = Flask(__name__)


UPLOAD_FOLDER='static'




def load_model1():
	global model
	model=load_model('model_Xception.h5')


def prepare_image(image, target):

    image = image.resize(target)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = preprocess_input(image)


    return image





@app.route("/",methods=["POST"])
def upload_predict():
	if request.method=="POST":
		image_file=request.files["image"]
		if image_file:
			image_location=os.path.join(
				UPLOAD_FOLDER,
				image_file.filename)
			image_file.save(image_location)
			image=prepare_image(load_img(image_location), target=(224, 224))
			#model=load_model('model_Xception.h5')
			model.predict(image)
			a=np.argmax(model.predict(image), axis=1)
			if a[0]==0:
					predict= 'Tomato___Bacterial_spot'
			elif a[0]==1:
					predict= "Tomato___Early_blight"
			elif a[0]==2:
					predict= 'Tomato___Late_blight'
			elif a[0]==3:
					predict= "Tomato___Leaf_Mold"
			elif a[0]==4:
					predict='Tomato___Septoria_leaf_spot'
			elif a[0]==5:
					predict= "Tomato___Spider_mites Two-spotted_spider_mite"
			elif a[0]==6:
					predict= 'Tomato___Target_Spot'
			elif a[0]==7:
					predict= "Tomato___Tomato_Yellow_Leaf_Curl_Virus"
			elif a[0]==8:
					predict= 'Tomato___Tomato_mosaic_virus'
			elif a[0]==9:
    				predict= "Tomato___healthy"
			else:
    				predict='0'
			return jsonify({'ETAT': predict}),200
	return jsonify({'ETAT': 'bad request'}),400

if __name__ == "__main__":
    print(("* Loading Keras model and Flask starting server..."
       "please wait until server has fully started"))

    load_model1()
    app.run(host="0.0.0.0",port=8080, debug=True)


