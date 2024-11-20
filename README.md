# **Simulation of Packet Transmission with and without Attacker**

This repository contains a simulation of IoT packet transmission, focusing on two scenarios: normal packet transmission and an attacker introducing delays into the communication.

---

## **Project Structure**

### **Files**
- **`sensor.py`**: Simulates an IoT sensor generating and sending temperature data packets.
- **`server.py`**: Represents a server that receives and evaluates packets as `SAFE` or `DANGER`.
- **`attacker.py`**: Acts as a malicious node intercepting packets and introducing delays.

---

## **Simulation Scenarios**

### 1. **Simulation Without Attacker**
- The `sensor.py` sends temperature packets directly to the `server.py`.
- The server evaluates packets based on a temperature threshold.
- No delay is introduced in this scenario.

### 2. **Simulation With Attacker**
- The `sensor.py` sends packets to the `attacker.py`.
- The attacker intercepts packets and introduces a delay (5 seconds) for packets above the temperature threshold (60°C).
- Delayed packets are queued and forwarded to the `server.py`.

---

## **Setup Instructions**

### **Prerequisites**
- Python 3.x installed on your system.
- Basic knowledge of Python socket programming.

### **Steps**
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/packet-simulation.git
   cd packet-simulation
