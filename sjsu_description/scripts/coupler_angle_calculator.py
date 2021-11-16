#!/usr/bin/env python
import math
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64

L_side = 0.9236
A_side = 0.26662
B_side = 0.53324

# Angles measured in radians, necessary since the default state of the URDF is 
#   all wheels pointed inwards. Offsets used to point the two 'front' wheels 
#   in the same direction as the 'rear' blue wheel. 
red_offset = 2.094395
green_offset = -2.094395
# Because of Gazebo crap, the model is oriented 90 degrees WRONG so lets FIX that 
general_offset = 1.57079

pub_coupler_red = rospy.Publisher('/orthrus/red_coupler_position_controller/command', Float64, queue_size = 5)
pub_coupler_green = rospy.Publisher('/orthrus/green_coupler_position_controller/command', Float64, queue_size = 5)
pub_coupler_blue = rospy.Publisher('/orthrus/blue_coupler_position_controller/command', Float64, queue_size = 5)

pub_speed_red = rospy.Publisher('/orthrus/red_wheel_velocity_controller/command', Float64, queue_size=5)
pub_speed_green = rospy.Publisher('/orthrus/green_wheel_velocity_controller/command', Float64, queue_size=5)
pub_speed_blue = rospy.Publisher('/orthrus/blue_wheel_velocity_controller/command', Float64, queue_size=5)


def callback(data):
    # allows for the robot spin in place
    if (data.linear.x == 0 and data.angular.z != 0):
        velocity = data.angular.z
        # setting the angle of each coupler to the general offset (90 degrees in radians) has them default to the flat side of the wheel facing the center of the bot
        pub_coupler_green.publish(general_offset)
        pub_coupler_red.publish(general_offset)
        pub_coupler_blue.publish(general_offset)
        pub_speed_red.publish(velocity)
        pub_speed_green.publish(velocity)
        pub_speed_blue.publish(velocity)

    else:
        theta = data.angular.z
        velocity = data.linear.x

        radius = float("inf")

        # calculate turning radius
        if theta != 0.0:
            radius = abs(velocity) / abs(theta)

        theta_inner = math.atan( (radius - L_side) / (2 * A_side) )
        r_inner = math.sqrt( (radius - L_side/2)**2 + A_side**2)

        theta_outer = math.atan( (radius + L_side) / (2 * A_side) )
        r_outer = math.sqrt( (radius + L_side/2)**2 + A_side**2)

        theta_back = math.atan( radius / B_side )
        r_back = math.sqrt( radius**2 + A_side**2 )

        theta_inner -= general_offset
        theta_outer -= general_offset

        # Determine if robot will turn left or right
        if data.angular.z > 0:
            pub_coupler_green.publish(theta_inner + green_offset)
            pub_coupler_red.publish(theta_outer + red_offset)
            pub_coupler_blue.publish(-theta_back - general_offset)
        else:
            pub_coupler_green.publish(theta_outer + green_offset)
            pub_coupler_red.publish(theta_inner + red_offset)   
            pub_coupler_blue.publish(theta_back - general_offset)

        #pub_coupler_blue.publish(theta_back)

        pub_speed_red.publish(velocity)
        pub_speed_green.publish(velocity)
        pub_speed_blue.publish(velocity)

def listener():
    rospy.init_node('coupler_angle_calculator')
    rospy.Subscriber("/cmd_vel", Twist, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass