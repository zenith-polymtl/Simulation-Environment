# Simulation Environment

This repository provides a **complete simulation pipeline** for developing, testing, and validating robotic systems in a controlled virtual environment.

It integrates multiple ROS 2 packages, external dependencies (via Git submodules), and simulation tools into a unified workflow.

---

## 🚀 Overview

The goal of this project is to:

* Provide a **modular simulation environment**
* Enable **rapid testing of algorithms and systems**
* Support **multi-package ROS 2 workflows**
* Ensure reproducibility using **version-controlled dependencies**

The repository acts as a **superproject**, orchestrating several submodules and workspaces into a single simulation pipeline.

---

## 🏗️ Architecture

The project is structured around:

```
.
├── packages/          # External ROS 2 packages (git submodules)
├── workspaces/        # Simulation workspaces
├── scripts/           # Utility scripts (setup, linking, etc.)
├── .gitmodules        # Submodule configuration
```

### Key Concepts

* **Submodules**: External repositories tracked at specific commits
* **Workspaces**: ROS 2 environments configured for specific missions
* **Scripts**: Automation tools for setup and maintenance

---

## 📦 Dependencies

This project relies on:

* ROS 2 (Humble or compatible)
* Git (with submodule support)
* Docker (optional, depending on setup)
* Simulation tools (e.g., Gazebo / SITL)

---

## 🔧 Installation

### 1. Clone the repository

```bash
git clone https://github.com/zenith-polymtl/Simulation-Environment.git
cd Simulation-Environment
```

### 2. Initialize submodules

```bash
git submodule update --init --recursive
```

Or use the provided script:

```bash
./scripts/ensure_submodules.sh
```

This ensures all dependencies are properly fetched and aligned.

---

## 🧪 Usage

### Setup a workspace

```bash
./scripts/link_ws.sh workspaces/<workspace_name>
```

### Build the workspace

```bash
cd workspaces/<workspace_name>
colcon build
```

### Run the simulation

Depending on your setup:

```bash
source install/setup.bash
ros2 launch <package> <launch_file>
```

---

## 🔄 Submodule Management

This repository uses Git submodules to manage external packages.

### Update submodules

```bash
git submodule update --remote
```

### Sync submodules

```bash
git submodule sync --recursive
```

### Common issues

* **Empty folders after clone** → run `git submodule update --init --recursive`
* **Detached HEAD state** → expected behavior for submodules

---

## 📁 Workspaces

Each workspace defines a specific simulation configuration.

Example:

```
workspaces/
└── water_ws/
    ├── src/
    └── pkgs.txt
```

The `pkgs.txt` file specifies which packages are included in that workspace.

---

## 🧰 Scripts

* `ensure_submodules.sh` → Initializes and updates submodules
* `link_ws.sh` → Links selected packages into a workspace

---

## 🧠 Development Workflow

1. Update submodules if needed
2. Select or create a workspace
3. Build with `colcon`
4. Run simulations via ROS 2 launch files

---

## ⚠️ Notes

* Submodules are pinned to specific commits for reproducibility
* Some packages may track custom branches
* Simulation configurations may vary depending on the mission

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request

---

## 📜 License

Specify your license here (MIT, Apache 2.0, etc.)

---

## 👥 Authors

* Zenith Polytechnique Montréal Team

---
