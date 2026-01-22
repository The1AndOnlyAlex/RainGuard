# RainGuard - Project Aegis

An autonomous umbrella drone system designed to provide weather protection.

## Hardware BoM

### Flight Controller
- TBD: Flight controller module
- TBD: GPS module
- TBD: Telemetry system

### Sensors
- TBD: Camera sensor
- TBD: Rain sensor
- TBD: IMU sensor

### Actuators
- TBD: Motors and ESCs
- TBD: Servo motors for umbrella mechanism

### Power System
- TBD: Battery pack
- TBD: Power distribution board

### Frame and Umbrella
- TBD: Drone frame
- TBD: Umbrella mechanism

## Wiring Diagram

Wiring diagrams will be added in the `hardware/schematics` directory.

### Connection Overview
- Flight controller connections
- Sensor integration
- Power distribution
- Communication links

## Installation

### Hardware Setup
1. Assemble the drone frame according to the instructions in `hardware/cad`
2. Install the flight controller and connect sensors following the wiring diagram
3. Mount the umbrella mechanism
4. Connect the power system

### Software Setup

#### Prerequisites
- Python 3.8 or higher
- ROS2 (recommended: Humble or later)
- Git LFS (for large file storage)

#### Installing Dependencies

```bash
# Clone the repository
git clone https://github.com/The1AndOnlyAlex/RainGuard.git
cd RainGuard

# Install Git LFS
git lfs install
git lfs pull

# Install Python dependencies
pip install -r requirements.txt

# Install ROS2 dependencies (if using ROS2)
# Follow ROS2 installation guide for your platform
```

#### Building the Project

```bash
# Build ROS2 workspace (if applicable)
colcon build

# Source the workspace
source install/setup.bash
```

## Usage

### Running the Vision System

```bash
python src/vision/main.py
```

### Running the Control System

```bash
python src/control/main.py
```

### Running with ROS2

```bash
# Launch the autonomous drone system
ros2 launch rainguard aegis.launch.py
```

### Testing

```bash
# Run tests
python -m pytest tests/
```

## Project Structure

```
RainGuard/
├── hardware/
│   ├── cad/           # CAD files for 3D printing and mechanical design
│   └── schematics/    # Electrical schematics and wiring diagrams
├── src/
│   ├── vision/        # Computer vision and object detection
│   └── control/       # Flight control and autonomous navigation
├── models/            # Machine learning models (*.pt files)
├── docs/              # Additional documentation
└── requirements.txt   # Python dependencies
```

## Contributing

Contributions are welcome! Please follow the standard fork-and-pull-request workflow.

## License

See LICENSE file for details.