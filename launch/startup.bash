#!/bin/bash

SESSION=$USER

# setup
tmux new-session -d -s $SESSION
tmux split-window -v
tmux split-window -v
tmux select-pane -t 1
tmux split-window -h
tmux split-window -h
tmux select-pane -t 4
tmux split-window -h

# roscore
tmux select-pane -t 0
tmux send-keys "roscore" C-m
sleep 3
# main
## t265
tmux select-pane -t 1
tmux send-keys "source devel/setup.bash" C-m
tmux send-keys "roslaunch launch/t265.launch" C-m
## left camera
tmux select-pane -t 2
tmux send-keys "source devel/setup.bash" C-m
tmux send-keys "rosrun usb_cam usb_cam_node _image_width:=1920 _image_height:=1080 _pixel_format:=mjpeg _framerate:=30 _video_device:=/dev/video2 /usb_cam:=/stereo/left" C-m
## right camera
tmux select-pane -t 3
tmux send-keys "source devel/setup.bash" C-m
tmux send-keys "rosrun usb_cam usb_cam_node _image_width:=1920 _image_height:=1080 _pixel_format:=mjpeg _framerate:=30 _video_device:=/dev/video0 /usb_cam:=/stereo/right" C-m
# rviz
tmux select-pane -t 4
tmux send-keys "rviz" C-m
# rosbag
tmux select-pane -t 5
tmux send-keys "cd bags; rosbag record /cam_2/odom/sample /stereo/left/image_raw/compressed /stereo/right/image_raw/compressed /tf /tf_static" C-m

tmux attach-session -t $SESSION

