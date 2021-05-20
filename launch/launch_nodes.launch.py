from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld= LaunchDescription()

    #run t1
    t1=   Node(
            package='turtlesim',
            namespace='turtlesim1',
            executable='turtlesim_node',
            name='sim'
        )

    #run t2
    t2=  Node(
            package='turtlesim',
            namespace='turtlesim2',
            executable='turtlesim_node',
            name='sim'
        )
    #run mimic
    mimic= Node(
            package='turtlesim',
            executable='mimic',
            name='mimic',remappings=[
                ('/input/pose', '/turtlesim1/turtle1/pose'),
                ('/output/cmd_vel', '/turtlesim2/turtle1/cmd_vel'),
            ]
        )
    ld.add_action(t1)
    ld.add_action(t2)
    ld.add_action(mimic)
    return ld
