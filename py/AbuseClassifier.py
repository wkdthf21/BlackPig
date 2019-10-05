# USAGE
# python predict_video.py --model model/activity.model --label-bin model/lb.pickle --input example_clips/lifting.mp4 --output output/lifting_128avg.avi --size 128

# import the necessary packages
from keras.models import load_model
from collections import deque
import numpy as np
import argparse
import pickle
import cv2

class AbuseClassifier():
    def __init__(self, model_path, lb_path):
        print ("Loading model and label binarizer...")
        self.model = load_model(model_path)
        self.lb = pickle.loads(open(lb_path, "rb").read())
        self.queue_size = 128

        # initialize the image mean for mean subtraction
        # along with the predictions queue
        mean = np.array([123.68, 116.779, 103.939][::1], dtype="float32")
        Q = deque(maxlen=self.queue_size)

    def isAbusedChild(self, video):
        (W, H) = (None, None)

        while True:
        #while frame in viedo?:
            (H, W) = frame.shape[:2]

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (224, 244)).astype("float32")
            frame -= mean

            preds = model.predict(np.expand_dims(frame, axis=0))[0]
            Q.append(preds)


# 여기서부터 Tab 씀
	    # perform prediction averaging over the current history of
	    # previous predictions
	    results = np.array(Q).mean(axis=0)
	    i = np.argmax(results)
	    label = lb.classes_[i]

            if max(results) > 0.9:
                return True
            else:
                return False
