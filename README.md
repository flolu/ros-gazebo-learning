**Setup**

```bash
source /opt/ros/noetic/setup.bash && \
source /usr/share/gazebo/setup.sh && \
catkin_make && \
source devel/setup.bash
```

**Start Simulation**

```bash
roslaunch my_simulations my_world.launch --screen
```
