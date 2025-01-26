"""Visualize the point cloud on the image after projection."""

import argparse
import random

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from pandaset import DataSet, geometry

# load dataset
args = argparse.ArgumentParser()
args.add_argument("--data_root", type=str, required=True)
args.add_argument("--seq_id", type=str, default="021")
args.add_argument("--frame_idx", type=int, default=14)
args.add_argument("--camera_name", type=str, default="front_camera")
args = args.parse_args()

dataset = DataSet(args.data_root)

seq021 = dataset[args.seq_id]
seq021.load()

print(f"Abailable camera: {seq021.camera.keys()}")

lidar = seq021.lidar

# get xyz coordinates of the LiDAR points
points3d_lidar_xyz = lidar.data[args.frame_idx].to_numpy()[:, :3]
choosen_camera = seq021.camera[args.camera_name]

points2d_camera, points3d_camera, inliner_indices = geometry.projection(
    lidar_points=points3d_lidar_xyz,
    camera_data=choosen_camera[args.frame_idx],
    camera_pose=choosen_camera.poses[args.frame_idx],
    camera_intrinsics=choosen_camera.intrinsics,
    filter_outliers=True,
)
print("The shape of projected point cloud on image (2D):", points2d_camera.shape)

# image before projection
ori_image = seq021.camera[args.camera_name][args.frame_idx]
plt.imshow(ori_image)
plt.show()


# image after projection with color based on distance
distances = np.sqrt(np.sum(np.square(points3d_camera), axis=-1))
colors = cm.jet(distances / np.max(distances))
plt.imshow(ori_image)
plt.gca().scatter(points2d_camera[:, 0], points2d_camera[:, 1], color=colors, s=1)
plt.show()


# image after projection with color based on semantic segmentation
semseg = seq021.semseg[args.frame_idx].to_numpy()

# get semseg on image by filting outside points
semseg_on_image = semseg[inliner_indices].flatten()

# generate random color for each class
max_seg_id = np.max(semseg_on_image)
color_maps = [
    (random.random(), random.random(), random.random()) for _ in range(max_seg_id + 1)
]
colors = np.array([color_maps[seg_id] for seg_id in semseg_on_image])

plt.imshow(ori_image)
plt.gca().scatter(points2d_camera[:, 0], points2d_camera[:, 1], color=colors, s=1)
plt.show()
