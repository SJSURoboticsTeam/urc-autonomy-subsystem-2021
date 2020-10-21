## Dependencies

* SDL Image Library Version 1.2 (Required by `navigation/map_server`)
```
sudo apt-get install libsdl-image1.2-dev libsdl1.2-dev
```
* GeographicLib (Required by `robot_localization`)
```
sudo apt-get install libgeographic-dev
```
* `librealsense` (Required by `realsense-ros`)
    * See these [installation instructions](https://github.com/IntelRealSense/librealsense/blob/master/doc/distribution_linux.md)

## Packages

* [`robot_localization`](https://github.com/cra-ros-pkg/robot_localization.git)
* [`navigation`](git@github.com:ros-planning/navigation.git)
* [`realsense-ros`](https://github.com/IntelRealSense/realsense-ros.git)
* [`depthimage_to_laserscan`](https://github.com/ros-perception/depthimage_to_laserscan.git)
* [`geometry2`](git@github.com:ros/geometry2.git)
* [`husky`](git@github.com:husky/husky.git)
* [`ddynamic_reconfigure`](git@github.com:pal-robotics/ddynamic_reconfigure.git)
    * Required by `realsense-ros`
* [`dynamic_reconfigure`](git@github.com:ros/dynamic_reconfigure.git)
