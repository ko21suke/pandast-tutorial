"""Warlkaround to access LiDAR data in PandaSet."""

import argparse
import time

from pandaset import DataSet

# Load dataset
args = argparse.ArgumentParser()
args.add_argument("--data_root", type=str, default="/home/kosuke/dataset/pandaset")
args.add_argument("--seq_id", type=str, default="021")
args = args.parse_args()
dataset = DataSet(args.data_root)

# Show all sequences
for sequence in dataset.sequences():
    print(f"Sequence: {sequence}")

seq021 = dataset[args.seq_id]

# load available sensor data metadata
start = time.time()
seq021.load_lidar()
end = time.time()

print(f"Loading time: {end - start} seconds")

if seq021.lidar:
    print("Sequence 021 is available as it has LIDAR data.")

# default is all point cloud (mechanical 360° LiDAR and front-facing LiDAR)
pcd = seq021.lidar[0]
print(f"Default shape of point cloud is {pcd.shape}")

# the point clouds are stored as pandas.DataFrames
print(f"The type of point cloud is {type(pcd)}")

# you can access the point cloud data as a numpy array
print(f"The type of values of point cloud is {type(pcd.values)}")
print(f"The point cloud values are :\n{pcd.values}")

# you can get the pose of the LiDAR sensor in the world coordinate system
print(seq021.lidar.poses[0])

# you can get specific LIDAR data as to set the sensor index
# set mechanical 360° LiDAR data
seq021.lidar.set_sensor(0)
pcd360 = seq021.lidar[0]
print(f"The shape of mechanical 360° LiDAR: {pcd360.shape}")

# set front-facing LiDAR data
seq021.lidar.set_sensor(1)
pcd_front = seq021.lidar[0]
print(f"The shape of front-facing LiDAR: {pcd_front.shape}")
