<h1 align="center">
    <br>
    <a href="#"><img src="https://banner2.kisspng.com/20180318/pow/kisspng-eight-ball-magic-8-ball-clip-art-ball-vector-5aae6272c6ee82.9269252915213779068148.jpg" alt="8Bot" width="200"></a>
    <br>
    8Bot
    <br>
</h1>

<h4 align="center">Autonomous Pool Robot using Computer Vision</h4>

<h5 align="center">By: Atif Mahmud and Ethan Guo</h5>

<p align="center">
    <a href="http://python.org/">
        <img src="http://forthebadge.com/images/badges/made-with-python.svg" alt="">
    </a>
    <a href="#">
        <img src="https://forthebadge.com/images/badges/fuck-it-ship-it.svg" alt="">
    </a>
    <a href="#">
        <img src="http://forthebadge.com/images/badges/60-percent-of-the-time-works-every-time.svg" alt="">
    </a>
</p>

<p align="center">
    <a href="#procedures">Background and Motivation</a> •
    <a href="#procedures">Procedures</a> •
    <a href="#related-works">Related Works</a> •
    <a href="#learning-goals">Learning Goals</a> •
    <a href="#engineering-goals">Engineering Goals</a> •
    <a href="#license">License</a>
</p>

# Background and Motivation

# Procedures
## Dependencies
### Python Libraries
The projects primary language is python. Input parsing, computer vision, and
pathfinding are executed by python clients. The
[OpenCV-Python](https://docs.opencv.org/3.4.3/index.html) wrapper is used along
with [Numpy](http://www.numpy.org/) to do the various computer vision and
matrix operations this project employs.

#### Install Python-OpenCV
```shell
sudo apt-get install python-opencv
```

#### Install Pip
```shell
sudo apt-get install python-pip
```

#### Install Numpy
```shell
pip install numpy
```

### MQTT Broker
This project relies on low latency publisher/subscriber based data transfer. To
do this we employ MQTT. MQTT (Message Queuing Telemetry Transport) is an ISO
Standard messaging protocol commonly used in IOT applications. The one caveat
is that its publish/subscriber message pattern requires a persistent broker.
For the purposes of this project we employ the open source MQTT broker [Eclipse
Mosquitto](https://mosquitto.org).

#### Install Broker (Ubuntu)

(Ubuntu 12^)
```shell
sudo apt install mosquitto
```

(Older versions of Ubuntu)
```shell
sudo apt-add-repository ppa:mosquitto-dev/mosquitto-ppa
sudo apt-get update
```

#### Install Python MQTT Client Library
```shell
pip install paho-mqtt
```

# Learning Goals
- [ ] Continuous Integration
- [x] MQTT Protocol

# Engineering Goals
- [ ] Fast robot messaging infrastructure
- [ ] Robust object classification
- [ ] Robust environment description
- [ ] Robust localization

# Related Works

# License

GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007

Refer to LICENSE.txt for full details
