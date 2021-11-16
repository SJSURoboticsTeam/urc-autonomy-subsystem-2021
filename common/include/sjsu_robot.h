/*

Author: Joshua Ramayrat

I legit have no idea if what I'm doing is right and I'm just
imitating from doosan robotics:

https://github.com/doosan-robotics/doosan-robot/blob/master/common/include/dsr_robot.h

*/

#ifndef __SJSU_ROBOT_H__
#define __SJSU_ROBOT_H__

#include <ros/ros.h>
#include <signal.h>
#include <boost/thread/thread.hpp>
#include <cstdlib>
#include <array>
#include <vector>
#include <algorithm>
#include <string>
#include <iostream>

#include <sjsu_msgs/RobotError.h>
#include <sjsu_msgs/RobotState.h>
#include <sjsu_msgs/RobotStop.h>


#include <sjsu_msgs/SetRobotMode.h>
#include <sjsu_msgs/GetRobotMode.h>
#include <sjsu_msgs/SetRobotSystem.h>
#include <sjsu_msgs/GetRobotSystem.h>
