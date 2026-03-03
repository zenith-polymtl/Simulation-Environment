# 🚁 Simulation Environment – ROS 2 Drone Vision Package

## 📌 Overview

This repository contains a **ROS 2 package** for drone simulation and computer vision processing.

It includes:

* 🧠 Custom ROS 2 nodes for computer vision
* 🎥 Image processing pipelines
* 🚁 A drone simulation environment in Gazebo
* 🔍 Integration between simulated sensors and vision algorithms

The goal of this project is to provide a modular simulation framework for developing and testing autonomous drone perception algorithms.

---

## 🌍 Simulation Environment

The project uses **Gazebo** to simulate a drone equipped with camera sensors.

### Features

* Simulated drone model
* RGB camera sensor
* ROS 2 topic integration
* Real-time vision processing

---

## 👁 Computer Vision Nodes

The ROS 2 package includes nodes for:

* Image subscription from simulated camera
* Object detection / feature extraction
* Processed image publishing
* Debug visualization

Example topics:

```
/camera/image_raw
/vision/detections
/vision/debug_image
```

---

## 🖼 Screenshots

### Gazebo Simulation

<p align="center">
  <img src="sim_env/Screenshot from 2025-11-30 15-02-26.png" width="800"/>
</p>


### Vision Processing Output

<p align="center">
  <img src="sim_env/Screenshot from 2026-03-01 16-54-19.png" width="800"/>
</p>

---

## ⚙️ Requirements

* ROS 2 (Humble / Iron)
* Gazebo
* OpenCV
* cv_bridge
* sensor_msgs

---
## 🚀 How to Build

This simulation integrates with the `ardupilot_gz` packages inside your ArduPilot ROS 2 workspace (`ardu_ws`).

### 1️⃣ Move Required Files

Copy the following files into the ArduPilot Gazebo workspace:

* Move the world file:

```
iris_rubicon.sdf
```

to:

```
ardu_ws/src/ardupilot_gz/ardupilot_gz_gazebo/worlds/
```

* Move the launch file:

```
iris_rubicon.launch.py
```

to:

```
ardu_ws/src/ardupilot_gz/ardupilot_gz_bringup/launch/
```

You can use:

```bash
mv iris_rubicon.sdf ~/ardu_ws/src/ardupilot_gz/ardupilot_gz_gazebo/worlds/
mv iris_rubicon.launch.py ~/ardu_ws/src/ardupilot_gz/ardupilot_gz_bringup/launch/
```

---

### 2️⃣ Build the Required Packages

Navigate to your ArduPilot workspace:

```bash
cd ~/ardu_ws
```

Then build the required packages:

```bash
colcon build --packages-select ardupilot_gz_bringup ardupilot_gz_gazebo
```

---

### 3️⃣ Source the Workspace

After building:

```bash
source install/setup.bash
```

---

## ▶️ How to Run

Launch simulation:

```bash
cd ~ardu_ws
ros2 launch iris_rubicon.launch.py
```

Run vision node:

```bash
ros2 run uav_vision rgb_yolo 
```

---

## 📚 Future Improvements

* SLAM integration
* Multi-drone support
* Deep learning-based detection
* Real-world hardware deployment

---

## 👨‍💻 Author

Zenith PolyMTL
