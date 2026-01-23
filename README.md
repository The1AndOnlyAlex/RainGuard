# Mark 1 Hardware Stack

## Frame & Powertrain
[WIP]

## Vision Systems
Raspberry Pi 5 (8GB)
Arducam OV9281 USB
MicroSD Card (64GB)
USB-C Data Cable






# RainGuard

## Hardware BoM [TBD]

### Compute & Control
- **AI Computer:** NVIDIA Jetson Orin Nano (8GB)
- **Flight Controller:** Pixhawk 6C (or Cube Orange) running ArduPilot
- **GPS:** Holybro Micro M10 GPS (or equivalent GNSS)
- **Telemetry:** Internal MAVLink stream to Jetson via UART

### Vision & Connectivity
- **Primary Camera:** Intel RealSense D435i (Depth + RGB) OR High-Quality CSI Camera (IMX477)
- **Wi-Fi Module:** Intel AX210 M.2 or Alfa AWUS036ACM (for Smartphone Hotspot)
- **RC Transmitter:** RadioMaster Pocket (ELRS) - *Required for Emergency Kill Switch*

### Propulsion & Frame
- **Frame:** Custom X-Class Carbon Fiber (1000mm+ wheelbase to clear umbrella)
- **Motors:** Low KV / High Torque (400KV - 600KV)
- **Propellers:** 15-18 inch Carbon Fiber
- **ESC:** 4-in-1 60A+ ESC (BLHeli_32)
- **Power:** 6S LiPo Battery (10,000mAh+) with **AS150 Anti-Spark Connectors**

### Umbrella Mechanism
- **Canopy:** Lightweight wind-vented umbrella (stripped of handle)
- **Mount:** 2-Axis Gimbal (Gravity stabilized) to keep umbrella upright during flight pitch

## Wiring Diagram

Wiring diagrams and pinout maps are located in the `hardware/schematics` directory.

### Connection Overview
- **Jetson <-> Pixhawk:** UART (TELEM2) for MAVLink communication
- **Camera <-> Jetson:** USB 3.0 or CSI Ribbon Cable
- **Power:** PDB to ESCs and Voltage Regulator (5V/12V) for Jetson

## Installation

### Hardware Setup
1. **Frame Assembly:** Assemble the drone frame using files in `hardware/cad`. Ensure arms are long enough so propellers do not overlap with the umbrella diameter. ALEX!: Get an "X-Class" or "Cinelifter" style geometry, not a standard DJI shape!
2. **Mounting:** Secure the Jetson and Pixhawk to the center plate with vibration damping.
3. **Umbrella:** Attach the gimbal mechanism to the top plate.
4. **Power:** Solder AS150 connectors to the PDB to prevent sparking.

### Software Setup

#### Prerequisites
- Python 3.8 or higher
- ROS 2 (Humble recommended)
- MAVSDK or DroneKit
- Git LFS (Required for AI models)

#### Installing Dependencies

```bash
# Clone the repository
git clone https://github.com/The1AndOnlyAlex/RainGuard.git
cd RainGuard

# Initialize Git LFS (Crucial for .pt models)
git lfs install
git lfs pull

# Install Python dependencies
pip install -r requirements.txt
```

## Web App Setup (Smartphone Control)

This project uses a Flask-based web interface hosted on the Jetson to control the drone.

1. **Network:** The Jetson creates a Hotspot named `Aegis-Link`.
2. **Connect:** Connect your smartphone to `Aegis-Link`.
3. **Launch:** Open browser to `http://192.168.50.1:5000` (default IP).

## Usage

### 1. Power On
Connect battery. Wait for ESC initiation beeps. Wait 60s for Jetson to boot and start the `Aegis-Link` hotspot.

### 2. Emergency Override
**ALWAYS** have the RadioMaster Pocket in hand.

- **Switch SA:** Arm/Disarm
- **Switch SD:** **EMERGENCY KILL** (Motor Interlock)

### 3. Running the System (Dev Mode)

```bash
# Launch the full stack (Vision + Control + Web Server)
python src/main_system.py
```
### 4. Running with ROS2
```bash
# Launch the autonomous drone system
ros2 launch rainguard aegis.launch.py
```

## Project Structure

```text
RainGuard/
├── hardware/
│   ├── cad/             # STL/STEP files for mounts & frame
│   └── schematics/      # Wiring diagrams
├── src/
│   ├── vision/          # YOLOv8 & DeepSORT tracking logic
│   ├── control/         # MAVLink flight control scripts
│   └── web_interface/   # Flask app for smartphone control
├── models/              # AI Model weights (*.pt files)
├── docs/                # Setup guides & calibration
└── requirements.txt     # Python dependencies
```

## License
See LICENSE file for details.
