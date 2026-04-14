# 🚁 Vision-Based Drone Simulation Environment

This repository provides a **complete simulation environment for vision-based drone control**, integrating:

- 🛸 ArduPilot SITL (autonomous flight stack)
- 🌍 Gazebo simulation world
- 👁️ Computer vision models (YOLO-based detection)
- 🎯 Visual servoing with PID control

The goal is to test and develop **end-to-end perception → decision → control pipelines** for autonomous UAV systems in a realistic simulation environment.

---

## 🧠 Overview

This project enables a simulated drone to:

1. Spawn inside a Gazebo environment
2. Receive real-time RGB camera data
3. Run YOLO-based object detection
4. Estimate object position (2D and optional 3D inference)
5. Perform visual servoing using PID control
6. Send commands to ArduPilot for flight control

The full system forms a closed-loop autonomous perception and control pipeline.

---
🚀 Features
🛸 Simulation
ArduPilot SITL integration
Gazebo physics-based drone simulation
Iris-based UAV model
Custom world configuration (iris_rubicon.sdf)
👁️ Vision System
YOLO-based object detection
Multiple pretrained models supported
Real-time RGB image processing
Optional pose estimation pipeline
🎯 Control System
Visual servoing loop (image → motion)
PID controller for trajectory correction
Closed-loop tracking of detected targets
⚙️ Requirements
System dependencies
ROS 2 (Humble recommended)
ArduPilot SITL
Gazebo
Python ≥ 3.8
Python dependencies

Install required packages:

pip install numpy opencv-python torch ultralytics

If using ROS 2 Python nodes:

pip install rclpy
🔧 Setup
1. Clone repository
git clone <your-repo-url>
cd <repo-name>
2. Launch simulation environment

Start Gazebo + drone simulation:

ros2 launch sim_env iris_rubicon.launch.py

This will:

Launch Gazebo world
Spawn the drone model
Initialize ArduPilot interface
3. Run vision pipeline

Run the main vision system:

python3 vision_node.py

Or run YOLO directly:

python3 rgb_yolo.py
4. Run visual servoing controller

Start closed-loop control:

python3 yolo_PID_approach.py

This script:

Detects target using YOLO
Computes image error
Estimates position (optional 3D step)
Sends control commands to ArduPilot
🧪 Core Pipeline
Camera Stream → YOLO Detection → Pose / Position Estimation → PID Controller → ArduPilot → Drone Motion
🧠 Models

The models/ directory contains pretrained neural networks:

best.pt → main detection model
best-medium.pt → balanced speed/accuracy model
yolo_m_100_epoch.pt → custom trained model
yolov8n-seg.pt → segmentation model

These models are used for real-time inference on simulated camera feeds.

📡 Simulation Environment

Located in sim_env/:

iris_rubicon.sdf → defines drone + Gazebo world
iris_rubicon.launch.py → ROS 2 launch file
screenshots/ → visual outputs of simulation setup
🎮 Visual Servoing Concept

The control loop is based on:

Capturing image from drone camera
Running YOLO detection on frame
Computing error between target and image center
Estimating depth / 3D position (optional step)
Applying PID controller
Sending velocity/position commands to ArduPilot

This enables autonomous target tracking in simulation.

⚠️ Notes
Ensure ArduPilot SITL is running before launching control scripts
Verify ROS 2 topics for camera streams
Model paths must be correct relative to working directory
Gazebo and ArduPilot must be properly synchronized
📌 Future Improvements
Multi-drone simulation support
Improved 3D depth estimation (SLAM / stereo vision)
Reinforcement learning-based control
Better integration with MAVROS / MAVLink
Hardware deployment (real drone transfer)
👥 Authors
Zenith Simulation Team
📜 License

Specify your license here (e.g., MIT, Apache 2.0)

🤝 Acknowledgements
ArduPilot project
Gazebo simulation environment
Ultralytics YOLO models
ROS 2 ecosystem
