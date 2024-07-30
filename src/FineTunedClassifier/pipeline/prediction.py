import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os



class PredictionPipeline:
    def __init__(self,filename):
        self.filename =filename


    
    def predict(self):
        ## load model
        
        model = load_model(os.path.join("artifacts","training", "model.h5"))
        # model = load_model(os.path.join("model", "model.h5"))

        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (224,224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        r = model.predict(test_image)
        result = np.where(r[0] == 1.0)[0][0]
        # result = np.argmax(model.predict(test_image), axis=1)
        print('chmolokolondhd    ---------',r, result)

        if result == 0:
            prediction = 'Adenocarcinoma Cancer'
            return [{ "image" : prediction}]
        elif result == 1:
            prediction = 'large cell carcinoma'
            return [{ "image" : prediction}]
        # elif result == 2:
        #     prediction = 'Normal'
        #     return [{ "image" : prediction}]
        # else:
        #     prediction = 'squamous cell carcinoma'
        #     return [{ "image" : prediction}]