import bpy

print("hello!!")

# 最初の手順
#  Blenderを起動して、Generalを選択します
#   スプラッシュスクリーンを非表示に
#   https://blender.stackexchange.com/questions/5208/prevent-splash-screen-from-being-shown-when-using-a-script
#   ただし、設定が変更されてしまうため、今後、スプラッシュスクリーンが常に非表示になる
bpy.context.preferences.view.show_splash = False

#   なにもしなくてもGeneralになるので、コメントアウト
# bpy.ops.wm.read_homefile(app_template="")  # Generalを選択

#  立方体は不要なので削除します
cube = bpy.data.objects['Cube']
if cube is not None:
    bpy.data.objects.remove(cube)

# 出力の設定
#  フレームレートに30
#  フレームレンジに30秒 (30×30=900)
#  ファイルフォーマットにFFmpeg
#  エンコーディングにMPEG-4

# Rigid Body Worldの設定
#  Cacheに30秒 (30×30=900)
#  Gravityに0
