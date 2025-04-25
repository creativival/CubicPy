# ボクセラミングのライブラリをインポートします
# pip install voxelamming

# スクリプトを起動する
# python python_sample.py

# voxelammingパッケージからVoxelammingクラスをインポートします
from voxelamming import Voxelamming

# Voxelammingアプリに表示されている部屋名を指定してください
room_name = "1000"
# Voxelammingクラスのインスタンスを生成します
vox = Voxelamming(room_name)

# ボクセルのサイズを設定します
vox.set_box_size(1)

# ボクセルを配置するため、位置と色を設定します
for i in range(100):
    vox.create_box(-1, i, 0, r=0, g=1, b=1, alpha=1)
    vox.create_box(0, i, 0, r=1, g=0, b=0, alpha=1)
    vox.create_box(1, i, 0, r=1, g=1, b=0, alpha=1)
    vox.create_box(2, i, 0, r=0, g=1, b=1, alpha=1)

# ボクセルを削除するため、位置を設定します
for i in range(50):
    vox.remove_box(0, i * 2 + 1, 0)
    vox.remove_box(1, i * 2, 0)

# ボクセルデータをアプリに送信します。
vox.send_data("main")
# vox.close_connection()