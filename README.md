**Autonomous Rover Powered by Raspberry Pi**

Overview: 
This project is an autonomous rover designed using a Raspberry Pi, equipped with a proximity sensor and a camera module. The rover is capable of navigating and avoiding obstacles using real-time data from the proximity sensor, while also offering the ability to capture images or video feeds through the camera module. It can be controlled remotely, and it operates autonomously with the help of pre-programmed logic to detect objects, follow paths, or avoid obstacles.

Features:

1. Autonomous Navigation: The rover utilizes a proximity sensor to detect obstacles and make decisions on path adjustments for smooth, obstacle-free movement.
2. Camera Integration: The camera module allows the rover to capture images or stream video, providing real-time feedback of its surroundings.
3. Raspberry Pi Powered: The rover is powered by a Raspberry Pi, making it easy to program and modify, while offering flexibility and scalability.
4. Proximity Sensing: Equipped with a distance sensor, the rover can sense objects in its path and perform automated maneuvers to avoid collisions.
5. Remote Control: In addition to autonomous functions, the rover can be controlled manually for specific tasks via a web interface or a mobile app.
6. Expandability: The system allows for future additions of more sensors or modules, such as GPS, for enhanced autonomous features.

Hardware Components:

1. Raspberry Pi (Model 3/4 recommended)
2. Proximity Sensor (Ultrasonic or Infrared)
3. Camera Module (Raspberry Pi Camera Module V2 or compatible)
4. Motor Driver (for controlling rover movement)
5. DC Motors & Wheels (for mobility)
6. Battery Pack (to power the rover and components)
7. Chassis (frame for assembling all components)

Software:

1. Raspberry Pi OS: The operating system installed on the Raspberry Pi for ease of setup and flexibility.
2. Python: The main programming language used to control the rover’s sensors, motors, and camera.
3. OpenCV: For processing the video feed from the camera for object detection or pathfinding (optional).
4. GPIO Library: For interacting with hardware components like motors and sensors.

Setup Instructions:

1. Assemble the Rover: Mount the Raspberry Pi on the chassis. Attach the motors to the wheels, ensuring proper wiring to the motor driver.
2. Connect the Sensors: Wire the proximity sensor and camera module to the Raspberry Pi GPIO pins.
3. Install Software: Download and install Raspberry Pi OS on your Pi. Set up Python and required libraries like RPi.GPIO, opencv-python (if using OpenCV), and any additional dependencies.
4. Upload Code: Clone or download the provided code repository, upload it to your Raspberry Pi, and configure the settings (camera resolution, motor directions, etc.).
5. Test the Rover: Power up the rover, and run the scripts to test the sensor data, camera feed, and motor movement.

This project is an autonomous rover designed using a Raspberry Pi, equipped with a proximity sensor and a camera module. The rover is capable of navigating and avoiding obstacles using real-time data from the proximity sensor, while also offering the ability to capture images or video feeds through the camera module.

![Front View](https://github.com/nmnmdgl/Autonomous_Rover/blob/main/images/Rover_Front.jpeg)
