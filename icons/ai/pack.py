"""把本目录里的图标打包成 icons.js（内嵌 data URI）。

双击打开 index.html（file://）时，浏览器把每个本地图片都当作跨源资源：
画到画布上会“污染”画布，录制功能就只能录到声音、录不到画面。
内嵌成 data URI 的图片不会污染画布，所以本地打开时游戏只读 icons.js。

增删或替换图标后重新运行一次：  python icons/ai/pack.py
"""
import base64, json, os

here = os.path.dirname(os.path.abspath(__file__))
out = {}
for fn in sorted(os.listdir(here)):
    stem, ext = os.path.splitext(fn)
    if ext.lower() not in ('.svg', '.png'):
        continue
    data = open(os.path.join(here, fn), 'rb').read()
    # 按文件内容判断类型（扩展名可能与实际格式不符）
    if data[:8] == b'\x89PNG\r\n\x1a\n':
        mime = 'image/png'
    elif data[:4] == b'RIFF' and data[8:12] == b'WEBP':
        mime = 'image/webp'
    elif data[:3] == b'\xff\xd8\xff':
        mime = 'image/jpeg'
    else:
        mime = 'image/svg+xml'
    # 同名时 .svg 优先，与游戏里的查找顺序一致
    if stem in out and ext.lower() != '.svg':
        continue
    out[stem] = 'data:%s;base64,%s' % (mime, base64.b64encode(data).decode('ascii'))

with open(os.path.join(here, 'icons.js'), 'w', encoding='utf-8', newline='\n') as f:
    f.write('// 由 pack.py 生成，请勿手改\nwindow.AI_ICONS=' + json.dumps(out, separators=(',', ':')) + ';\n')
print('icons.js: %d 个图标' % len(out), ', '.join(out))
