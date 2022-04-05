"""This Python script contains a simple example of two identical robots
    which are connected at their respective endeffecor positions. 
    To stop the simulation simply ctr-c in the python terminal
"""

import os
import pybullet as p
import pybullet_data
import numpy as np


# Configure your robot and relative positions here:
# -------------------------------------------------
urdf_model_name = 'kuka.urdf'

first_robot_position = np.array([0,0,0])
first_robot_orientation = np.array([0,0,0])

second_robot_position = np.array([0,0,0])
second_robot_orientation = np.array([0,0,0])

name_of_connected_links = "kuka_arm_7_link"
#--------------------------------------------------



# Create simulation world
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath()) 
p.setGravity(0,0,-10)
p.setRealTimeSimulation(1)


# Load the two URDF models
#-------------------------
dirname = os.path.dirname(__file__)
urdf_file = os.path.join(
        dirname, 'robot_descriptions', urdf_model_name)

first_robot =  p.loadURDF(urdf_file,
                            first_robot_position,
                            first_robot_orientation,
                            useFixedBase=True)
second_robot =  p.loadURDF(urdf_file,
                            second_robot_position,
                            second_robot_orientation,
                            useFixedBase=True)
#-------------------------

# Creathe the constraint which connects the robots at the Endeffector
# Compare Pybullet Quickstart Guide pp. 26-29 for more info
link_name_to_index = {p.getBodyInfo(
            first_robot)[0].decode('UTF-8'): -1, } #find link index given urdf name

p.createConstraint(first_robot,
                    link_name_to_index[name_of_connected_links],
                    second_robot,
                    link_name_to_index[name_of_connected_links],
                    p.JOINT_POINT2POINT,
                    [0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0])        

                       