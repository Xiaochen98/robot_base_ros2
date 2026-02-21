from launch import LaunchDescription
from launch.substitutions import EnvironmentVariable
import launch
import launch.actions
import launch_ros.actions
from ament_index_python.packages import get_package_share_directory
import os
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    use_sim_time = launch.substitutions.LaunchConfiguration('use_sim_time', default='false')

    bringup_dir = get_package_share_directory('turn_on_wheeltec_robot')
    launch_dir = os.path.join(bringup_dir, 'launch')

    wheeltec_lidar = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(launch_dir, 'wheeltec_lidar.launch.py')),
    )

    wheeltec_robot = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(launch_dir, 'turn_on_wheeltec_robot.launch.py')),
    )

    # ✅ 延迟启动 gmapping：让雷达/TF/EKF 先稳定起来
    delayed_gmapping = TimerAction(
        period=4.0,   # 你可以试 3.0~6.0；先用 4 秒通常就稳了
        actions=[
            launch_ros.actions.Node(
                package='slam_gmapping',
                executable='slam_gmapping',
                output='screen',
                parameters=[{'use_sim_time': use_sim_time}],
            )
        ]
    )

    return LaunchDescription([
        SetEnvironmentVariable('RCUTILS_LOGGING_BUFFERED_STREAM', '1'),
        wheeltec_robot,
        wheeltec_lidar,
        delayed_gmapping,
    ])
