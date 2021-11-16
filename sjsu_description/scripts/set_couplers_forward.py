#!/usr/bin/env python
# Purpose: Sets the green and blue couplers to align with the red coupler
import rospy
from std_msgs.msg import Float64

def set_couplers_forward():

    pub_red = rospy.Publisher('/orthrus/red_coupler_position_controller/command', Float64, queue_size = 5)
    pub_green = rospy.Publisher('/orthrus/green_coupler_position_controller/command', Float64, queue_size = 5)

    pub_blue = rospy.Publisher('/orthrus/blue_coupler_position_controller/command', Float64, queue_size = 5)
    rospy.init_node('set_wheels_forward', anonymous = True)
    rate = rospy.Rate(1)
    rospy.loginfo("Check to see that two couplers have moved in Gazebo, then kill this")
    while not rospy.is_shutdown():
        # numbers based off of pi/6 + pi/2

        pub_red.publish(2.094395)
        pub_green.publish(-2.094395) 
        pub_blue.publish(0)
        rate.sleep()

if __name__ == '__main__':
    try:
        set_couplers_forward()
    except rospy.ROSInterruptException:
        pass
