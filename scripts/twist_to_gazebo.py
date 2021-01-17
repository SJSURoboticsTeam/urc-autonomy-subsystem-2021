#!/usr/bin/env python

import rospy

from geometry_msgs.msg import Twist
from std_msgs.msg import Float64

def callback(msg):
    x-dir = msg.linear.x
    y-dir = msg.linear.y



def twist_translator():
    rospy.init_node('twist_listener', anonymous=True)
    rospy.Subscriber("orthrus/cmd_vel", Twist, callback)


if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: 
        pass