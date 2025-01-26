# PandaSet チュートリアル

本ソースコードは Zenn [PandaSet チュートリアル](https://zenn.dev/articles/e6ef557911f14e)の参照先である.

## Prerequirements

### ライブラリのインストール

uv を使用してpython環境をセットアップする.

本家ソースコード pandaset-devkit は [__.pkl.gz__](https://github.com/scaleapi/pandaset-devkit/blob/master/python/pandaset/sensors.py#L137)をロードするようになっているが, Kaggle にある [PandaSet](https://www.kaggle.com/datasets/usharengaraju/pandaset-dataset/data) の拡張子は __.pkl__ であるため, 本プロジェクトでは本家ソースコードをフォークして該当ソースを修正したものを使用する. 該当のソースは以下のとおり.

* [pandaset-devkit](https://github.com/ko21suke/pandaset-devkit/tree/fix-extention)



## チュートリアル一覧

### Camera データの探索

* [tools/walkaround_camera_data.py](https://github.com/ko21suke/pandast-tutorial/blob/main/tools/walkaround_camera_data.py)

```
python tools/walkaround_camera_data.py --data_root <path/to/pandaset> --seq_id <seq_id>
````

### LiDAR データの探索

* [tools/walkaround_lidar_data.py](https://github.com/ko21suke/pandast-tutorial/blob/main/tools/walkaround_lidar_data.py)

```
python tools/walkaround_lidar_data.py --data_root <path/to/pandaset> --seq_id <seq_id>
```

### 点群の可視化

* [tools/visualize_pcd.py](https://github.com/ko21suke/pandast-tutorial/blob/main/tools/visualize_pcd.py)

```
python tools/visualize_pcd.py --data_root <path/to/pandaset> --seq_id <seq_id> --frame_idx <frame_idx>
```

### 画像と点群のフュージョン

* [tools/visualize_pcd_on_image.py](https://github.com/ko21suke/pandast-tutorial/blob/main/tools/visualize_pcd_on_image.py)

```
python tools/visualize_pcd_on_image.py --data_root <path/to/pandaset> --seq_id <seq_id> --frame_idx <frame_idx> --camera_name <camera_name>
```
