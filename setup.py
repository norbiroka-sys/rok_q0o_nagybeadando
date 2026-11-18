import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'rok_q0o_nagybeadando'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'rviz'), glob('rviz/*.rviz')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ajr',
    maintainer_email='norbiroka@gmail.com',
    description='A-Star path planning and visualization package in ROS 2 Humble',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'planner_node = rok_q0o_nagybeadando.planner_node:main',
        ],
    },
)
