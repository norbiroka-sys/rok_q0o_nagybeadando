import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    pkg_share = get_package_share_directory('rok_q0o_nagybeadando')
    rviz_config_path = os.path.join(pkg_share, 'rviz', 'default.rviz')

    return LaunchDescription([
        Node(
            package='rok_q0o_nagybeadando',
            executable='planner_node',
            name='planner_node',
            output='screen'
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_config_path] if os.path.exists(rviz_config_path) else [],
            output='screen'
        )
    ])
