from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'uav_vision'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    (os.path.join('share', package_name, 'models'),
        glob('models/*.pt')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='haipy',
    maintainer_email='haithemtebib24@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        	'vision_node = uav_vision.vision_node:main',
        	'rgb_subscriber = uav_vision.rgb_subscriber:main',
        	'rgb_yolo = uav_vision.rgb_yolo:main',
        	'yolo_3D = uav_vision.yolo_3D:main',
        	'haelthcheck = uav_vision.healthcheck:main',
        	'rgb_yolo_pose = uav_vision.rgb_yolo_pose:main',
        	'yolo_PID_approach = uav_vision.yolo_PID_approach:main',
        ],
    },
)
