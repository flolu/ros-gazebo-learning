**Setup**

```bash
cd ~/catkin_ws
git clone https://github.com/flolu/ros-gazebo-learning
```

```bash
cd ~/catkin_ws && \
source /opt/ros/noetic/setup.bash && \
source /usr/share/gazebo/setup.sh && \
catkin_make && \
source devel/setup.bash && \
export GAZEBO_MODEL_PATH=~/catkin_ws/src/ros-gazebo-learning/models:$GAZEBO_MODEL_PATH
```

**Start Simulation**

```bash
roslaunch ros-gazebo-learning create_world.launch --screen
```
