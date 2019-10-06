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
        self.abused_time_dict = dict()
        self.time_list = list()

        # initialize the image mean for mean subtraction
        # along with the predictions queue
        self.mean = np.array([123.68, 116.779, 103.939][::1], dtype="float32")
        self.Q = deque(maxlen=self.queue_size)


    def isAbusedChild(self, video_path):
        video = cv2.VideoCapture(video_path)
        time_order = 0
        time_switch = 0
        threshold = 0

        (W, H) = (None, None)

        # For debug
        #writer = None

        while True:
            (grabbed, frame) = video.read()

            if not grabbed:
                break

            (H, W) = frame.shape[:2]

            # For debug
            #output = frame.copy()

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (224, 224)).astype("float32")
            frame -= self.mean

            preds = self.model.predict(np.expand_dims(frame, axis=0))[0]
            self.Q.append(preds)


	    # perform prediction averaging over the current history of
	    # previous predictions
            results = np.array(self.Q).mean(axis=0)
            i = np.argmax(results)
            label = self.lb.classes_[i]

            if time_switch == 1:
                threshold += 1

                # For debug
                #text = label + " || " + str(max(results))
                #cv2.putText(output, text, (35, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.25, (0, 255, 0), 5)
                # End Debug
                


            if max(results) > 0.9 and time_switch == 0:
                timestamps = video.get(cv2.CAP_PROP_POS_MSEC)
                print ("start || ", label, " || ", timestamps)
                self.time_list.append(timestamps)
                time_order += 1
                time_switch = 1 

            elif max(results) < 0.9 and time_switch == 1:
                if threshold > 20:
                    timestamps = video.get(cv2.CAP_PROP_POS_MSEC)
                    self.time_list.append(timestamps)
                    self.abused_time_dict[time_order] = self.time_list[:]
                    print ("end || ", threshold, " || ", timestamps)

                time_switch = 0
                threshold = 0
                del self.time_list[:]

            # for debug
            #if writer is None:
                #fourcc = cv2.VideoWriter_fourcc(*"MJPG")
                #writer = cv2.VideoWriter('output/test.avi', fourcc, 30, (W,H), True)

            #writer.write(output)

        #writer.release()
        #end debug

        return self.abused_time_dict
