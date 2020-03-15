# Models for Gazebo simulation, SJSU Robotics 2020
## Usage
### First step: 
```
roslaunch pri_sjr_gazebo orthrus_control.launch
```
This command will launch Gazebo, spawn the Orthrus model and start up nodes that interface the model's joints with ROS. From there Float64 messages can be sent that will actuate each joint. 
### Additional scripts for use with Gazebo
```
rosrun pri_sjr_gazebo set_couplers_forward.py
```
Turns the couplers that connect the robot's wheels with the body so that all the wheels are pointed in the same 'forward' direction.
```
rosrun pri_sjr_gazebo coupler_angle_calculator.py
```
Translates twist messages sent on topic /cmd_vel to steering angles for the wheel couplers and wheel speeds. 



### Visualizing with rviz
Use a launch file. Example (from here[https://answers.ros.org/question/61479/adding-robot_description-to-parameter-server/]):
``` 
<launch>
  <node name="robot_state_publisher" pkg="robot_state_publisher" type="state_publisher" />
  <param name="robot_description" textfile="path/to/model.urdf" />
</launch>
```

Alternatively, instead of `roslaunch`, we can use `rosparam`:
```
rosparam load path/to/model.urdf robot_description
```

**Note: While `.sdf` files are essential in Gazebo in order to provide sensor simulation, `.sdf` files are not compatible ROS-side for visualization.**

## Development
### Conversion from SDF to URDF
When necessary to convert to URDF (such as when visualizing with `rviz`), use:
```
rosrun pysdf sdf2urdf.py path/to/src/file.sdf path/to/dest/file.urdf
```
