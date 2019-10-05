# USAGE
# python predict_video.py --model model/activity.model --label-bin model/lb.pickle --input example_clips/lifting.mp4 --output output/lifting_128avg.avi --size 128

# import the necessary packages
from keras.models import load_model
from collections import deque
import numpy as np
import argparse
import pickle
import cv2

class classifer():
    def __init(self, model_path, label_bin):
        self.model_path = model_path
        self.label_bin = label_bin
        self.queue_size = 128

        print ("Load label binarizer and model...")
        self.model = load_model(self.model_path)
        self.lb = pickle.loads(open(self.label_bin, "rb").read())

        # initialize the image mean for mean subtraction along with the
        # predictions queue        
        mean = np.array([123.68, 116.779, 103.939][::1], dtype="float32")
        Q = deque(maxlen=args["size"])

    def isAbuseChild(self, frame):
        (H, W) = frame.shape[:2]

	frame = cv2.resize(frame, (224, 224)).astype("float32")
	frame -= mean

	# make predictions on the frame and then update the predictions
	# queue
	preds = model.predict(np.expand_dims(frame, axis=0))[0]
	Q.append(preds)

	# perform prediction averaging over the current history of
	# previous predictions
	results = np.array(Q).mean(axis=0)
	i = np.argmax(results)
	label = lb.classes_[i]

	if max(results) > 0.9:
            return True
        else:
            return False
