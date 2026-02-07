# robot_base_ros2
 这里用来记录wheeltec机器人的使用和开发

以下是一些基本指=指令
 ssh -Y wheeltec@192.168.0.100

sudo mount 192.168.0.100:/home/wheeltec/wheeltec_ros2 ~/share

pkill -INT -f 'ros2 launch'


wheeltec@wheeltec:~/lifting_platform_ros2$ uname -r

5.15.148-tegra

wheeltec@wheeltec:~/lifting_platform_ros2$ head -n1 /etc/nv_tegra_release       
            
# R36 (release), REVISION: 4.3, GCID: 38968081, BOARD: generic, EABI: aarch64, DATE: Wed Jan  8 01:49:37 UTC 2025

ros2 run lift_driver lift_driver_node

ros2 topic echo /lift/height

ros2 topic pub /lift/cmd std_msgs/String "data: 'up'"

https://forums.developer.nvidia.com/t/enable-config-usb-serial-pl2303-on-kernel/285574/9

工作流：先把机器人的盘mount过来，如果有需要现pull下更新，然后再进行修改，修改完成后push到github
