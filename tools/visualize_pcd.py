"""Visualize the lidar data in the PnadaSet."""

import argparse

import open3d as o3d
from pandaset import DataSet, geometry

# color values are represented as from 0 to 1, not from 0 to 255.
COLOR_BLUE = [0, 0, 1]
COLOR_RED = [1, 0, 0]

# load dataset
args = argparse.ArgumentParser()
args.add_argument("--data_root", type=str, required=True)
args.add_argument("--seq_id", type=str, default="021")
args.add_argument("--frame_idx", type=int, default=14)
args = args.parse_args()

dataset = DataSet(args.data_root)

seq021 = dataset[args.seq_id]
seq021.load_lidar().load_semseg()

# get mechanial LiDAR points
seq021.lidar.set_sensor(0)
points360 = seq021.lidar[args.frame_idx].to_numpy()
print("machanical LiDAR has points: ", points360.shape)

# get front-faceing LiDAR points
seq021.lidar.set_sensor(1)
points_front = seq021.lidar[args.frame_idx].to_numpy()
print("Front-faceing LiDAR has points: ", points_front.shape)

axis_pcd = o3d.geometry.TriangleMesh.create_coordinate_frame(size=2.0, origin=[0, 0, 0])

# world coordinate system
pcd360 = o3d.geometry.PointCloud()
pcd360.points = o3d.utility.Vector3dVector(points360[:, :3])
pcd360.paint_uniform_color(COLOR_BLUE)

pcd_front = o3d.geometry.PointCloud()
pcd_front.points = o3d.utility.Vector3dVector(points_front[:, :3])
pcd_front.paint_uniform_color(COLOR_RED)

# o3d.visualization.draw_geometries(
#     [axis_pcd, pcd360, pcd_front],
#     window_name="World Coordinate System",
# )

# ego coordinate system
ego_points360 = geometry.lidar_points_to_ego(
    points360[:, :3],
    seq021.lidar.poses[args.frame_idx],
)
ego_pcd360 = o3d.geometry.PointCloud()
ego_pcd360.points = o3d.utility.Vector3dVector(ego_points360)
ego_pcd360.paint_uniform_color(COLOR_BLUE)

ego_points_front = geometry.lidar_points_to_ego(
    points_front[:, :3],
    seq021.lidar.poses[args.frame_idx],
)
ego_pcd_front = o3d.geometry.PointCloud()
ego_pcd_front.points = o3d.utility.Vector3dVector(ego_points_front)
ego_pcd_front.paint_uniform_color(COLOR_RED)

o3d.visualization.draw_geometries(
    [axis_pcd, ego_pcd360, ego_pcd_front],
    window_name="Ego Coordinate System",
)
