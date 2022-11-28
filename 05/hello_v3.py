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
preset_path = bpy.utils.preset_find('30', bpy.utils.preset_paths("framerate")[0])
bpy.ops.script.execute_preset(filepath=preset_path, menu_idname="RENDER_MT_framerate_presets")
#   上記は以下を実行する
#   bpy.context.scene.render.fps = 30
#   bpy.context.scene.render.fps_base = 1

#  フレームレンジに30秒 (30×30=900)
bpy.context.scene.frame_end = bpy.context.scene.render.fps * 30
#  ファイルフォーマットにFFmpeg
bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
#  エンコーディングにMPEG-4
bpy.context.scene.render.ffmpeg.format = 'MPEG4'

# Rigid Body Worldの設定
#  Rigid Body Worldがなければ作成
if bpy.context.scene.rigidbody_world is None:
    bpy.ops.rigidbody.world_add()
#  Cacheに30秒 (30×30=900)
bpy.context.scene.rigidbody_world.point_cache.frame_end = bpy.context.scene.render.fps * 30
#  Gravityに0
bpy.context.scene.rigidbody_world.effector_weights.gravity = 0
