
from launch.actions import DeclareLaunchArgument, ExecuteProcess, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, PythonExpression

from launch import LaunchDescription
from launch_ros.actions import Node



from launch.conditions import IfCondition
#    Any launch arguments declared within a :py:class:`launch.LaunchDescription`
#    will be exposed as arguments when that launch description is included, e.g.
#    as additional parameters in the
#    :py:class:`launch.actions.IncludeLaunchDescription` action or as
#    command-line arguments when launched with ``ros2 launch ...``.

# the RewrittenYaml is used to edit certain parameters in the yaml file, before exporting
# the yaml file as a temp file, which is passed onto the node

def generate_launch_description():
    ld=LaunchDescription()

    #declare the launch configuration object. the name in the constructor should be unique
    bringupbool = LaunchConfiguration('bringupbool')
    #declare this argument in the LaunchDescription class
    declare_slam_cmd = DeclareLaunchArgument(
        'bringupbool',
        default_value='True',
        description='Whether run a SLAM')

    ld.add_action(declare_slam_cmd)

    return ld
