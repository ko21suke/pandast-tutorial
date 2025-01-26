"""Warlkaround to access camera data in PandaSet."""

import argparse
import time

from pandaset import DataSet

# Load dataset
args = argparse.ArgumentParser()
args.add_argument("--data_root", type=str, required=True)
args.add_argument("--seq_id", type=str, default="021")
args = args.parse_args()
dataset = DataSet(args.data_root)

# show all sequences
for sequence in dataset.sequences():
    print(f"Sequence: {sequence}")

# accsess a specifi sequence
seq021 = dataset[args.seq_id]
if not seq021.camera:
    print("Sequence 021 is not available as it doesn't have camera.")

# load available sensor data and metadata
start = time.time()
print("Loading sensor data and metadata")
seq021.load()
end = time.time()
print(f"Loading time: {end - start} seconds")

if seq021.camera:
    print("Sequence 021 is available as it has camera data.")

print(f"Camera keys are {seq021.camera.keys()}")
front_camera = seq021.camera["front_camera"]

# the caemra data are stored as PIL.Image
print(f"The type of front camera data is {type(front_camera[0])}")

front_camera[0].show()

print(f"Camera pose as in world coordinates system: {front_camera.poses[0]}")
print(
    f"Camera intrinsic parameters (fx, fy, cx, cy): \
    {front_camera.intrinsics.fx}, {front_camera.intrinsics.fy}, \
    {front_camera.intrinsics.cx},{front_camera.intrinsics.cy}",
)
print(f"Timestamp of the recording: {front_camera.timestamps[0]}")
