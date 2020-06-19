# `urc-autonomy-subsystem`
## `test-ros-ws-2021`

Lorem ipsum, this is the test ROS workspace to explore the potential of managing individual ROS packages within a single repo via the use of branches and submodules. 

### System Dependencies/Compatibility
* Ubuntu 16.04/ROS Kinetic, or
* Ubuntu 18.04/ROS Melodic

### Init

To set up this workspace on your system, perform the following at the desired parent directory.
```
git clone github.com:SJSURoboticsTeam/urc-autonomy-subsystem-2021.git -b test-ros-ws-2021
cd urc-autonomy-subsystem-2021
git submodule init
git submodule update
catkin init
catkin build
source devel/setup.bash
```
