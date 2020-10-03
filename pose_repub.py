#/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseStamped
from sensor_msgs.msg import Imu

pose_pub = None

def callback(imu_msg):
  global pose_pub
  pose_msg = PoseStamped()
  pose_msg.header = imu_msg.header
  pose_msg.pose.orientation = imu_msg.orientation
  pose_pub.publish(pose_msg)

def init():
  global pose_pub
  rospy.init_node('pose_repub')
  pose_pub = rospy.Publisher('pose/data', PoseStamped, queue_size=10)
  rospy.Subscriber('imu/data', Imu, callback)
  rospy.spin()

if __name__ == '__main__':
  init() 
