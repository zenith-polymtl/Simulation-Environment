# 🚁 Vision-Based Drone Simulation Environment

This repository provides a **complete simulation environment for vision-based drone control**, integrating autonomous flight stacks, physics-based simulation, and real-time computer vision.

The goal is to test and develop **end-to-end perception → decision → control pipelines** for autonomous UAV systems.

---

## 🧠 Overview

The full system forms a closed-loop autonomous pipeline enabling a simulated drone to:

1. **Simulate**: Spawn inside a Gazebo environment with ArduPilot SITL.
2. **Perceive**: Process real-time RGB camera data via YOLO-based object detection.
3. **Estimate**: Infer object position (2D and optional 3D depth).
4. **Control**: Execute visual servoing using a PID controller.
5. **Actuate**: Send MAVLink commands to ArduPilot for physical motion.
<img src="sim_env/Screenshot from 2025-11-30 15-02-26.png" alt="Alt Text" width="500">
<img src="sim_env/Screenshot from 2026-03-01 16-54-19.png" alt="Alt Text" width="500">
---

## 🚀 Features

### 🛸 Simulation Stack
* **ArduPilot SITL** integration for flight logic.
* **Gazebo** physics-based environment.
* **Iris-based UAV** model with custom sensor configurations.
* Custom world definitions (`iris_rubicon.sdf`).

### 👁️ Vision System
* **YOLO-based** real-time object detection.
* Support for multiple pretrained and custom `.pt` models.
* Real-time RGB stream processing via OpenCV/ROS 2.

### 🎯 Control System
* **Visual Servoing** loop (image-plane to 3D motion).
* **PID Controller** for precise trajectory and centering correction.
* Closed-loop tracking for dynamic targets.

---

## ⚙️ Requirements

### System Dependencies
* **ROS 2** (Humble recommended)
* **ArduPilot SITL**
* **Gazebo** (Classic or Ignition)
* **Python** ≥ 3.8

### Python Dependencies
```bash
pip install numpy opencv-python torch ultralytics rclpy
```

---

## 🔧 Setup & Execution

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd <repo-name>
```

### 2. Launch Simulation Environment
```bash
ros2 launch sim_env iris_rubicon.launch.py
```
**This command will:**
* Launch the Gazebo world.
* Spawn the drone model.
* Initialize the ArduPilot SITL interface.

### 3. Run Vision Pipeline
Execute the detection node:
```bash
python3 vision_node.py
# OR
python3 rgb_yolo.py
```

### 4. Run Visual Servoing Controller
In a new terminal, launch the PID control logic:
```bash
python3 yolo_PID_approach.py
```

---

## 🧪 Core Pipeline Logic
The data flow follows this sequence:
**Camera Stream** → **YOLO Detection** → **Position Estimation** → **PID Controller** → **ArduPilot** → **Drone Motion**

---

## 🧠 Models
The `models/` directory contains pretrained neural networks optimized for different use cases:

| Model File | Description |
| :--- | :--- |
| `best.pt` | Main detection model. |
| `best-medium.pt` | Balanced speed/accuracy (YOLOv8m). |
| `yolo_m_100_epoch.pt`| Custom trained model (100 epochs). |
| `yolov8n-seg.pt` | Segmentation-specific model. |

---

## 📡 Directory Structure
* **`sim_env/`**: Contains simulation assets.
    * `iris_rubicon.sdf`: Drone and world definitions.
    * `iris_rubicon.launch.py`: Primary ROS 2 launch file.
* **`screenshots/`**: Visual documentation of the simulation.

---

## ⚠️ Critical Notes
* **SITL Sync**: Ensure ArduPilot SITL is fully initialized and in a "GUIDED" or "LOITER" state before running control scripts.
* **ROS 2 Topics**: Verify that the camera topic (e.g., `/camera/image_raw`) is active using `ros2 topic list`.
* **Pathing**: Update model paths in the Python scripts if running from a different directory.

---

## 📌 Future Improvements
* [ ] Multi-drone swarm simulation support.
* [ ] SLAM integration for GPS-denied navigation.
* [ ] Reinforcement Learning (RL) based control policies.
* [ ] Direct MAVROS/MAVLink integration refinements.

---

## 👥 Authors
**Zenith Simulation Team** - *Polytechnique Montréal*

## 📜 License
Distributed under the MIT License. See `LICENSE` for more information.

## 🤝 Acknowledgements
* The **ArduPilot** Dev Team
* **Open Robotics** (Gazebo/ROS 2)
* **Ultralytics** (YOLOv8)
