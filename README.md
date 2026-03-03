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

## 🏗 Project Structure

```
Simulation-Environment/
│
├── src/
│   └── <your_ros2_package>/
│
├── assets/
│   └── images used in README
│
└── README.md
```

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

```bash
cd ~/ros2_ws
colcon build
source install/setup.bash
```

---

## ▶️ How to Run

Launch simulation:

```bash
ros2 launch <your_package> simulation.launch.py
```

Run vision node:

```bash
ros2 run <your_package> vision_node
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
