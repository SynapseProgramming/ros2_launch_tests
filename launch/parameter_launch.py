import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():

    current_dir=get_package_share_directory('ros2_launch_tests')
    ld=LaunchDescription()

    my_int_val=66


    run_param=Node(
                package='ros2_launch_tests',
               executable='parameter_node',
                name='parameter_node',
                parameters=[{'my_int': my_int_val}],
                output='screen')
    ld.add_action(run_param)
    return ld;
