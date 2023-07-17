# import the necessary packages
from scipy.spatial import distance as dist
from imutils.video import FileVideoStream
from imutils.video import VideoStream
from imutils import face_utils
from playsound import playsound
import constants
import numpy as np
import argparse
import imutils
import time
import dlib
import cv2
import logging
import tensorflow.keras
import json
import os

logging.basicConfig(filename='fatigue.log', filemode='w', format='%(asctime)s %(message)s')
logger=logging.getLogger() 
logger.setLevel(logging.DEBUG) 


def eye_aspect_ratio(eye):
	# compute the euclidean distances between the two sets of
	# vertical eye landmarks (x, y)-coordinates
	A = dist.euclidean(eye[1], eye[5])
	B = dist.euclidean(eye[2], eye[4])
	# compute the euclidean distance between the horizontal
	# eye landmark (x, y)-coordinates
	C = dist.euclidean(eye[0], eye[3])
	# compute the eye aspect ratio
	ear = (A + B) / (2.0 * C)
	# return the eye aspect ratio
	return ear

def gen_labels():
    labels = {}
    with open("data/labels.txt", "r") as label:
        text = label.read()
        lines = text.split("\n")
        print(lines)
        for line in lines[0:-1]:
            hold = line.split(" ", 1)
            labels[hold[0]] = hold[1]
    return labels


def start_procedure(user_data, equipment_data, user):
	# ------------------------------------- #
	# ------- Fatigue Process Setup ------- #
	# ------------------------------------- #
	# construct the argument parse and parse the arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("-p", "--shape-predictor", required=True,
		help="path to facial landmark predictor")
	ap.add_argument("-v", "--video", type=str, default="",
		help="path to input video file")
	args = vars(ap.parse_args())

	# define two constants, one for the eye aspect ratio to indicate
	# blink and then a second constant for the number of consecutive
	# frames the eye must be below the threshold
	EYE_AR_THRESH = 0.27
	EYE_AR_CONSEC_FRAMES = 3
	# initialize the frame counters and the total number of blinks
	COUNTER = 0
	STARTING = time.time()


	# initialize dlib's face detector (HOG-based) and then create
	# the facial landmark predictor
	print("[INFO] loading facial landmark predictor...")
	detector = dlib.get_frontal_face_detector()
	predictor = dlib.shape_predictor(args["shape_predictor"])

	# grab the indexes of the facial landmarks for the left and
	# right eye, respectively
	(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
	(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

	# start the video stream thread
	print("[INFO] starting video stream thread...")
	vs = FileVideoStream(args["video"]).start()
	fileStream = True
	vs = VideoStream(src=0).start()
	fileStream = False
	time.sleep(1.0)
	switch = 0
	startTime = 0
	endTime = 0

	# ------------------------------------- #
	# ------ Equipment Process Setup ------ #
	# ------------------------------------- #
	# Disable scientific notation for clarity
	np.set_printoptions(suppress=True)
	image = cv2.VideoCapture(1)
    # Load the model
	model = tensorflow.keras.models.load_model('keras_model.h5')

	"""
    Create the array of the right shape to feed into the keras model
    The 'length' or number of images you can put into the array is
    determined by the first position in the shape tuple, in this case 1."""
	data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    # A dict that stores the labels
	labels = gen_labels()

	# loop over frames from the video stream
	while True:
		# ----------------------------- #
		# ----- Fatigue Detection ----- #
		# ----------------------------- #
		# grab the frame from the threaded video file stream, resize
		# it, and convert it to grayscale
		# channels)
		frame = vs.read()
		frame = imutils.resize(frame, width=900)
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		# detect faces in the grayscale frame
		rects = detector(gray, 0)
		# loop over the face detections
		for rect in rects:
			# determine the facial landmarks for the face region, then
			# convert the facial landmark (x, y)-coordinates to a NumPy
			# array
			shape = predictor(gray, rect)
			shape = face_utils.shape_to_np(shape)
			# extract the left and right eye coordinates, then use the
			# coordinates to compute the eye aspect ratio for both eyes
			leftEye = shape[lStart:lEnd]
			rightEye = shape[rStart:rEnd]
			leftEAR = eye_aspect_ratio(leftEye)
			rightEAR = eye_aspect_ratio(rightEye)
			# average the eye aspect ratio together for both eyes
			ear = (leftEAR + rightEAR) / 2.0
					# compute the convex hull for the left and right eye, then
			# visualize each of the eyes
			leftEyeHull = cv2.convexHull(leftEye)
			rightEyeHull = cv2.convexHull(rightEye)
			cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
			cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)
			if ear < EYE_AR_THRESH:
				if switch == 0:
					startTime = time.time()
					switch = 1
				else:
					endTime = time.time()
			if ear > EYE_AR_THRESH:
				if switch == 1:
					if(endTime - startTime >= 3):
						playsound('data/wakeUp.mp3', False)
						print('playing sound using playsound')
						logger.warning("You showed some signs of fatigue/drowsiness.") 
						COUNTER += 1
					switch = 0
			cv2.putText(frame, "EAR: {:.2f}".format(ear), (10, 30),
				cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
			
		# --------------------------- #	
		# ----- Equipment Check ----- #
		# --------------------------- #

		# Choose a suitable font
		font = cv2.FONT_HERSHEY_SIMPLEX
		ret, frame1 = image.read()
		key = cv2.waitKey(1) & 0xFF
		frame1 = cv2.flip(frame1, 1)
		# In case the image is not read properly
		if not ret:
			continue
		# Draw a rectangle, in the frame
		frame1 = cv2.rectangle(frame1, (100, 80), (1800, 1000), (0, 0, 255), 3)
		# Draw another rectangle in which the image to labelled is to be shown.
		frame2 = frame1[80:360, 220:530]
		# resize the image to a 224x224 with the same strategy as in TM2:
		# resizing the image to be at least 224x224 and then cropping from the center
		frame2 = cv2.resize(frame2, (224, 224))
		# turn the image into a numpy array
		image_array = np.asarray(frame2)
		# Normalize the image
		normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
		# Load the image into the array
		data[0] = normalized_image_array
		pred = model.predict(data)
		result = np.argmax(pred[0])

		# Print the predicted label into the screen.
		cv2.putText(frame1,  "Label : " +
					labels[str(result)], (230, 50), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
		

        # Show the frame   
		cv2.imshow('Frame1', frame1)
		# show the frame
		cv2.imshow("Frame", frame)
		key = cv2.waitKey(1) & 0xFF
	
		# if the `esc` key was pressed, break from the loop
		if key == 27:
			break
	# do a bit of cleanup
	image.release()
	cv2.destroyAllWindows()
	vs.stop()
	ENDING = time.time()
	# Update operation data
	user_data[user][constants.KEY_OPERATIONS][startTime][constants.KEY_END_TIME] = endTime
	user_data[user][constants.KEY_OPERATIONS][startTime][constants.KEY_FATIGUE_ERRORS] = "" # TODO: track fatigue timestamps here
	user_data[user][constants.KEY_OPERATIONS][startTime][constants.KEY_EQUIPMENT_ERRORS] = "" # TODO: track fatigue timestamps here
	# Update user data
	user_data[user][constants.KEY_ERROR_RECORDS][constants.KEY_FATIGUE_ERROR_COUNT] += COUNTER
	user_data[user][constants.KEY_ERROR_RECORDS][constants.KEY_EQUIPMENT_ERROR_COUNT] += 0 # TODO: track equipment errors and up

def read_in_app_data():
    users_data = None
    equipment_data = None
    
    current_path = os.path.dirname(__file__)
    data_path = os.path.join(current_path, "../data")
    
    with open(data_path + "/users.json", "r") as read_users:
        users_data = json.load(read_users)
    with open(data_path + "/equipment.json", "r") as read_equipment:
        equipment_data = json.load(read_equipment)
    
    if users_data is not None and equipment_data is not None:
        return users_data, equipment_data
    else:
        raise IOError("Could not read in app data")

users_data, equipment_data = read_in_app_data()
start_procedure(users_data, equipment_data, "user")
