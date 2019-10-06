# USAGE
# python predict_video.py --model model/activity.model --label-bin model/lb.pickle --input example_clips/lifting.mp4 --output output/lifting_128avg.avi --size 128

# import the necessary packages
from keras.models import load_model
from collections import deque
import numpy as np
import argparse
import pickle
import cv2

abused_time_dict = dict()
time_list = list()
time_order = 0
time_switch = 0

class AbuseClassifier():
    def __init__(self, model_path, lb_path):
        print ("Loading model and label binarizer...")
        self.model = load_model(model_path)
        self.lb = pickle.loads(open(lb_path, "rb").read())
        self.queue_size = 128

        # initialize the image mean for mean subtraction
        # along with the predictions queue
        self.mean = np.array([123.68, 116.779, 103.939][::1], dtype="float32")
        self.Q = deque(maxlen=self.queue_size)

        threshold = 0

    def isAbusedChild(self, video_path):
        video = cv2.VideoCapture(video_path)
        (W, H) = (None, None)

        while True:
            (grabbed, frame) = video.read()

            if not grabbed:
                break

            (H, W) = frame.shape[:2]

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (224, 244)).astype("float32")
            frame -= self.mean

            preds = self.model.predict(np.expand_dims(frame, axis=0))[0]
            self.Q.append(preds)


# 여기서부터 Tab 씀
	    # perform prediction averaging over the current history of
	    # previous predictions
            results = np.array(self.Q).mean(axis=0)
            i = np.argmax(results)
            label = lb.classes_[i]

            if max(results) > 0.9 and time_switch == 0:
                timestamps = video.get(cv2.CAP_PROP_POS_MSEC)
                time_list.append(timestamps)
                time_order += 1
                time_switch = 1
                threshold += 1

            elif max(result) < 0.9 and time_switch == 1:
                if threshold > 30:
                    timestamps = video.get(cv2.CAP_PROP_POS_MSEC)
                    time_list.append(timestamps)
                    abused_time_dict[time_order] = time_list
                    del time_list[:]
                    time_switch = 0
                    
                threshold = 0

        return abused_time_dict
