# headers needed for launching other launch files
import os
from ament_index_python.packages import get_package_share_directory
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import IncludeLaunchDescription

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    #this function gets the absolute shared path of the package
    pkg_teleop= get_package_share_directory('teleop_twist_joy')

    #uncomment these to view the output
    #print(pkg_teleop)
    #file_path= os.path.join(pkg_teleop, 'launch', 'teleop-launch.py'),
    #print(file_path)
    #ld=PythonLaunchDescriptionSource(file_path)
    #print(ld)

    #the include launch description function would launch a separate launch file in another package
    launch_teleop= IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_teleop, 'launch', 'teleop-launch.py'),
        )
    )


    return LaunchDescription([

        Node(
            package='turtlesim',
            namespace='turtlesim1',
            executable='turtlesim_node',
            name='sim'
        ),
        Node(
            package='turtlesim',
            namespace='turtlesim2',
            executable='turtlesim_node',
            name='sim'
        ),
        Node(
            package='turtlesim',
            executable='mimic',
            name='mimic',
            remappings=[
                ('/input/pose', '/turtlesim1/turtle1/pose'),
                ('/output/cmd_vel', '/turtlesim2/turtle1/cmd_vel'),
            ]
        ),
        launch_teleop
    ])
