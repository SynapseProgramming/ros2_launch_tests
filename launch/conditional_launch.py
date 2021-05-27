from launch.actions import DeclareLaunchArgument, ExecuteProcess, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, PythonExpression

from launch import LaunchDescription
from launch_ros.actions import Node

#import conditional functions
from launch.conditions import IfCondition, UnlessCondition

def generate_launch_description():
    ld=LaunchDescription()

    launchturtle = LaunchConfiguration('launchturtle')
    #declare this argument in the LaunchDescription class
    declareturtle = DeclareLaunchArgument(
        'launchturtle',
        default_value='false',
        description='true would launch turtlesim. false would launch the turtle teleop key')

    run_teleop= Node(
        condition=UnlessCondition(launchturtle),
        package='turtlesim',
        executable='turtle_teleop_key',
        name='turtle_teleop_key',
        output='screen')


    run_turtlesim= Node(
        condition=IfCondition(launchturtle),
        package='turtlesim',
        executable='turtlesim_node',
        name='turtlesim_node',
        output='screen')

    ld.add_action(declareturtle)
    ld.add_action(run_teleop)
    ld.add_action(run_turtlesim)

    return ld
