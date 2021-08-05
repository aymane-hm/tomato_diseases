# tomato_diseases
fine tuning keras's Xception architecture to train a tomato disease detection model
this model detects 9 diseases
dataset link : 

we created a REST API for the model using FLASK, 
dockertized the app, then deployed it on GCP's Cloud run
deployement link : https://tomato-ago324jaqa-ey.a.run.app    please note it only accepts POST requests with an image file (key=image)
