# Models for Gazebo simulation, SJSU Robotics 2019
## Usage
### Run it
```
roslaunch gazebo_ros empty_world.launch
```
### Add a model
```
rosrun gazebo_ros spawn_model -file models/chimera/model.sdf -sdf -x 0 -y 0 -z 1 -model cerberus
```

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
