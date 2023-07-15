from flask import Flask
import subprocess
import time
import sqlite3 as sqlite
import json

from common.constants import *

app = Flask(__name__)

@app.route("/", methods = ['POST'])
def hello_world():
    p1 = subprocess.Popen("python3 detect_blinks.py --shape-predictor shape_predictor_68_face_landmarks.dat".split(" "), start_new_session=True)
    p2 = subprocess.Popen("python3 equipment_check.py".split(" "), start_new_session=True)
    p1.wait()
    p2.wait()
    return "Success!"

@app.route("/fatigue", methods = ['GET'])
def get_fatigue_of_operation(users, user, operation_start_time):
    return users[user][operation_start_time][KEY_FATIGUE_LOG]

def read_in_app_data():
    users_data, equipment_data
    with open("users.json", "r") as read_users:
        users_data = json.load(read_users)
    with open("equipment.json", "r") as read_equipment:
        equipment_data = json.load(read_equipment)
    
    if users_data is not None and equipment_data is not None:
        return users_data, equipment_data
    else:
        raise IOError("Could not read in app data")
    
def main():
    users_data, equipment_data = read_in_app_data()
    print(get_fatigue_of_operation(users_data, "user", "1625309473.357246"))