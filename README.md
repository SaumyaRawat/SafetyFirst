# Project: SafetyFirst
## Project Description: 
An API that uses computer vision to detect if drivers of vehicles are sleepy, and sounds an alarm to wake them up. We use three primary key point detectors to check if a person is sleepy: 
1. Frontal face detection: to detect the tilt and position of the face and check if the driver is looking ahead. 
2. If the driver's pupils are not visible for a certain amount of time, it is implied that their eyes are closed and hence they have dozed off or they are not looking front. 
3. if the mouth is in a circular/elliptical shape for a long time they are mostly yawning, and chances of paying attention to the road are lesser. In any of these cases we raise a loud alarm 