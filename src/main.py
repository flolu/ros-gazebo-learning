#!/usr/bin/env python3

import rospy
import time
from geometry_msgs.msg import Twist

rospy.init_node('move_box_node', anonymous=False)
pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)

if __name__ == '__main__':
    move = Twist()
    move.linear.x = 2
    while not rospy.is_shutdown():
        move.linear.x *= -1
        print("publish move", move)
        pub.publish(move)
        time.sleep(.5)
