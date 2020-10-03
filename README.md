# `urc-autonomy-subsystem`
## `mpu9250_viz`

The contents of this branch serves to visualize data from the MPU 9250

## Run it live
1. Ensure `roscore` is live, and the `/imu/data` topic is publishing
2. From this directory, 
  1. `python pose\_repub.py`
  2. `rviz -d imu\_vis.rviz`

## Visualize a `rosbag`
1. Ensure `roscore` is live, and
  1. `rosparam set /use_sim_time true`
  2. Ensure `/imu/data` from the bagfile is ready to publish with `rosbag play --clock --pause <your\_bag\_file>.bag
2. From this directory,
  1. `python pose\_repub.py`
  2. `rviz -d imu\_vis.rviz`
3. Unpause and run `rosbag play` (select the `terminal` window and press the <space> key)

