import json
import keyboard
import asyncio
import time
from audioTranscription import *
from app.constants import *

def find_equipment_errors(equipment_data, equipment_errors):
    while True:
        start_audio_recog(equipment_data)
        
        for equipment in equipment_data:
            if (equipment[KEY_EQUIPMENT_REQUESTED] != equipment[KEY_EQUIPMENT_PRESENT] and
                not equipment[KEY_EQUIPMENT_LOCKED]):
                print(f"Found error with {equipment}")
                equipment_errors += f"{equipment}-{time.time()}"
                equipment[KEY_EQUIPMENT_LOCKED] = True
