#include <stdio.h>
#include <SoftwareSerial.h>

// read distance serial

#define trigPin1 GPIO 0
#define echoPin1 GPIO 2
#define trigPin2 GPIO 3
#define echoPin2 GPIO 4
#define trigPin3 GPIO 5
#define echoPin3 GPIO 6
#define trigPin4 GPIO 12
#define echoPin4 GPIO 13
#define trigPin5 GPIO 14
#define echoPin5 GPIO 27
#define trigPin6 GPIO 28
#define echoPin6 GPIO 29

int duration, distance, Width_Sensor_1, Width_Sensor_2, Depth_Sensor_1, Depth_Sensor_2, Height_Sensor_1, Height_Sensor_2;
void setup()
{
	Serial.begin(9600);
	pinMode(trigPin1, OUTPUT);
	pinMode(echoPin1, INPUT);
	pinMode(trigPin2, OUTPUT);
	pinMode(echoPin2, INPUT);
	pinMode(trigPin3, OUTPUT);
	pinMode(echoPin3, INPUT);
	pinMode(trigPin4, OUTPUT);
	pinMode(echoPin4, INPUT);
	pinMode(trigPin5, OUTPUT);
	pinMode(echoPin5, INPUT);
	pinMode(trigPin6, OUTPUT);
	pinMode(echoPin6, INPUT);
}
void loop()
{
	SonarSensor(trigPin1, echoPin1);
	Width_Sensor_1 = distance;
	SonarSensor(trigPin2, echoPin2);
	Width_Sensor_2 = distance;
	SonarSensor(trigPin3, echoPin3);
	Depth_Sensor_1 = distance;
	SonarSensor(trigPin4, echoPin4);
	Depth_Sensor_2 = distance;
	SonarSensor(trigPin5, echoPin5);
	Height_Sensor_1 = distance;
	SonarSensor(trigPin6, echoPin6);
	Height_Sensor_2 = distance;
	Serial.print("S1:"); Serial.println(Width_Sensor_1); delayMicroseconds(10);  #Width_1
		Serial.print("S2:"); Serial.println(Width_Sensor_2); delayMicroseconds(10);  #Width_2
		Serial.print("S3:"); Serial.println(Depth_Sensor_1); delayMicroseconds(10);  #Depth_1
		Serial.print("S1:"); Serial.println(Depth_Sensor_2); delayMicroseconds(10);  #Depth_2
		Serial.print("S2:"); Serial.println(Height_Sensor_1); delayMicroseconds(10);  #Height_1
		Serial.print("S3:"); Serial.println(Height_Sensor_2); delayMicroseconds(10);  #Height_2

		Position_from_obstacle = [(-($Serial.println(Width_Sensor_1)) + ($Serial.println(Width_Sensor_2)), (-($Serial.println(Depth_Sensor_1)) + ($Serial.println(Depth_Sensor_2)), (-($Serial.println(Height_Sensor_1)) + ($Serial.println(Height_Sensor_2))]
}