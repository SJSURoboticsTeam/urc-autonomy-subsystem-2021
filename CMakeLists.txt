cmake_minimum_required(VERSION 2.8.3)
project(pri_sjr_gazebo)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
  tf
  sensor_msgs
  controller_manager
  joint_state_controller
  robot_state_publisher
  gazebo_ros
)

catkin_package(DEPENDS gazebo_ros)

install(DIRECTORY launch worlds config models
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

add_executable(tf_orthrus_publisher scripts/tf_orthrus_publisher.cpp)

 target_link_libraries(tf_orthrus_publisher
   ${catkin_LIBRARIES}
 )

 catkin_install_python(PROGRAMS
  scripts/twist_to_gazebo.py
  scripts/coupler_angle_calculator.py
  scripts/set_couplers_forward.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})