import math, util, rotmat, time
import random
from rotmat import Vector3, Matrix3

class Aircraft(object):
    '''a basic aircraft class'''
    def __init__(self):
        self.home_latitude = 0
        self.home_longitude = 0
        self.home_altitude = 0
        self.ground_level = 0
        self.frame_height = 0.0

        self.latitude  = self.home_latitude
        self.longitude = self.home_longitude
        self.altitude  = self.home_altitude

        self.dcm = Matrix3()

        # rotation rate in body frame
        self.gyro = Vector3[0,0,0] # rad/s
        self.prospected_position = [0, 0, 0]

        self.velocity = Vector3[0, 0, 0] # m/s, North, East, Down
        self.position = Vector3[0, 0, 0] # m North, East, Down
        self.mass = 0.0
        self.update_frequency = 50 # in Hz
        self.gravity = 9.80665 # m/s/s
        self.accelerometer = Vector3(0, 0, -self.gravity)

        self.time_base = time.time()
        self.time_now = self.time_base + 100*1.0e-6
    def controller(self):
        #command from controller
        self.position = [0, 0, 0]
        self.prospected_position = [0, 0, 0]
        command = [0, 0, 0]
        if command == [1, 0, 0]: # to north
            prospected_position = ($Position_from_obstacle)+($command)
            if not (prospected_position[0] == 0 or prospected_position[1] == 0 or prospected_position[2] == 0):
                self.velocity = command
                self.position = self.velocity
            if (prospected_position[0] == 0 or prospected_position[1] == 0 or prospected_position[2] == 0):
                tone(buzzer, 1000)
                delay(1000)
                noTone(buzzer)
                delay(1000)
        if command == [-1, 0, 0]: # to south
            prospected.position = ($Position_from_obstacle) + ($command)
            if not (prospected_position[0] == 0 or prospected_position[1] == 0 or prospected_position[2] == 0):
                self.velocity = command
                self.position = self.velocity
            if (prospected_position[0] == 0 or prospected_position[1] == 0 or prospected_position[2] == 0):
                tone(buzzer, 1000)
                delay(1000)
                noTone(buzzer)
                delay(1000)
        if command == [0, 1, 0]: # to East
            prospected_position = ($Position_from_obstacle) + ($command)
            if not (prospected_position[0] == 0 or prospected_position[1] == 0 or prospected_position[2] == 0):
                self.velocity = command
                self.position = self.velocity
            if (prospected_position[0] == 0 or prospected_position[1] == 0 or prospected_position[2] == 0):
                tone(buzzer, 1000)
                delay(1000)
                noTone(buzzer)
                delay(1000)
        if command == [0, -1, 0]: # to West
            prospected_position = ($Position_from_obstacle) + ($command)
            if not (prospected_position[0] == 0 or prospected_position[1] == 0 or prospected_position[2] == 0):
                self.velocity = command
                self.position = self.velocity
            if (prospected_position[0] == 0 or prospected_position[1] == 0 or prospected_position[2] == 0):
                tone(buzzer, 1000)
                delay(1000)
                noTone(buzzer)
                delay(1000)
        if command == [0, 0, 1]: # to Up
            prospected_position = ($Position_from_obstacle) + ($command)
            if not (prospected_position[0] == 0 or prospected_position[1] == 0 or prospected_position[2] == 0):
                self.velocity = command
                self.position = self.velocity
            if (prospected_position[0] == 0 or prospected_position[1] == 0 or prospected_position[2] == 0):
                tone(buzzer, 1000)
                delay(1000)
                noTone(buzzer)
                delay(1000)
        if command == [0, 0, -1]: # to Down
            prospected_position = ($Position_from_obstacle) + ($command)
            if not (prospected_position[0] == 0 or prospected_position[1] == 0 or prospected_position[2] == 0):
                self.velocity = command
                self.position = self.velocity
            if (prospected_position[0] == 0 or prospected_position[1] == 0 or prospected_position[2] == 0):
                tone(buzzer, 1000)
                delay(1000)
                noTone(buzzer)
                delay(1000)
