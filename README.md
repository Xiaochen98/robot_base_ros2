# robot_base_ros2
 这里用来记录wheeltec机器人的使用和开发

以下是一些基本指令
ssh登录机器人
ssh -Y wheeltec@192.168.0.100
将机器人文件mount到主机方便修改和管理
sudo mount 192.168.0.100:/home/wheeltec/wheeltec_ros2 ~/share
关闭所有包含ros2 launch的进程，适用于退出出错的程序
pkill -INT -f 'ros2 launch'

机器人内核版本信息
5.15.148-tegra
软件栈版本信息 
R36 (release), REVISION: 4.3, GCID: 38968081, BOARD: generic, EABI: aarch64, DATE: Wed Jan  8 01:49:37 UTC 2025

工作流：先把机器人的盘mount过来，如果有需要现pull下更新，然后再进行修改，修改完成后push到github
