import zipfile
import re
import os

def emu_to_px(emu):
    return int(emu) / 914400 * 96

def analyze_shape(shape):
    nm = re.search(r'<p:cNvPr[^>]*name="([^"]+)"', shape)
    name = nm.group(1) if nm else 'Unknown'

    xfrm = re.search(r'<a:xfrm>(.*?)</a:xfrm>', shape, re.DOTALL)
    pos_info = ''
    if xfrm:
        off = re.search(r'<a:off x="(\d+)" y="(\d+)"', xfrm.group(1))
        ext = re.search(r'<a:ext cx="(\d+)" cy="(\d+)"', xfrm.group(1))
        if off and ext:
            x, y = emu_to_px(off.group(1)), emu_to_px(off.group(2))
            w, h = emu_to_px(ext.group(1)), emu_to_px(ext.group(2))
            pos_info = f'({x:.0f},{y:.0f}) [{w:.0f}x{h:.0f}]'

    fill = re.search(r'<a:solidFill><a:srgbClr val="([0-9A-Fa-f]{6})"', shape)
    fill_s = f' fill=#{fill.group(1)}' if fill else ''

    line = re.search(r'<a:ln>.*?<a:srgbClr val="([0-9A-Fa-f]{6})"', shape, re.DOTALL)
    line_s = f' line=#{line.group(1)}' if line else ''

    texts = re.findall(r'<a:t>([^<]*)</a:t>', shape)
    text = ''.join(texts)[:40] if texts else ''

    info = f'  {name} {pos_info}{fill_s}{line_s}'
    if text:
        info += f' "{text}"'
    return info

def analyze_pic(pic):
    nm = re.search(r'<p:cNvPr[^>]*name="([^"]+)"', pic)
    name = nm.group(1) if nm else 'Unknown'

    xfrm = re.search(r'<a:xfrm>(.*?)</a:xfrm>', pic, re.DOTALL)
    pos_info = ''
    if xfrm:
        off = re.search(r'<a:off x="(\d+)" y="(\d+)"', xfrm.group(1))
        ext = re.search(r'<a:ext cx="(\d+)" cy="(\d+)"', xfrm.group(1))
        if off and ext:
            x, y = emu_to_px(off.group(1)), emu_to_px(off.group(2))
            w, h = emu_to_px(ext.group(1)), emu_to_px(ext.group(2))
            pos_info = f'({x:.0f},{y:.0f}) [{w:.0f}x{h:.0f}]'

    blip = re.search(r'r:embed="([^"]+)"', pic)
    pic_ref = f' embed={blip.group(1)}' if blip else ''
    return f'  [pic] {name} {pos_info}{pic_ref}'

def analyze_layout(z, layout_num, layout_name):
    print(f'\n========== Layout {layout_num}: {layout_name} ==========')
    lf = f'ppt/slideLayouts/slideLayout{layout_num}.xml'
    if lf not in z.namelist():
        print('  Not found')
        return

    content = z.read(lf).decode('utf-8', errors='ignore')

    # Background
    bg = re.search(r'<p:bg>(.*?)</p:bg>', content, re.DOTALL)
    if bg:
        srgb = re.search(r'<a:srgbClr val="([0-9A-Fa-f]{6})"', bg.group(1))
        if srgb:
            print(f'  Background: #{srgb.group(1)}')

    sptree = re.search(r'<p:spTree>(.*?)</p:spTree>', content, re.DOTALL)
    if not sptree:
        print('  No spTree')
        return

    tree = sptree.group(1)

    # Group shapes
    grpsps = re.findall(r'<p:grpSp\b[^>]*>(.*?)</p:grpSp>', tree, re.DOTALL)
    for gi, grpsp in enumerate(grpsps):
        print(f'\n  [Group {gi}]')
        inner_shapes = re.findall(r'<p:sp\b[^>]*>(.*?)</p:sp>', grpsp, re.DOTALL)
        for shape in inner_shapes:
            print(analyze_shape(shape))
        inner_pics = re.findall(r'<p:pic\b[^>]*>(.*?)</p:pic>', grpsp, re.DOTALL)
        for pic in inner_pics:
            print(analyze_pic(pic))

    # Top-level shapes
    shapes = re.findall(r'<p:sp\b[^>]*>(.*?)</p:sp>', tree, re.DOTALL)
    for shape in shapes:
        print(analyze_shape(shape))

    # Top-level pics
    pics = re.findall(r'<p:pic\b[^>]*>(.*?)</p:pic>', tree, re.DOTALL)
    for pic in pics:
        print(analyze_pic(pic))

z = zipfile.ZipFile('C:/Users/jarvan_iv/Desktop/人工智能课件模版.pptx')

layouts = {
    1: '封面',
    2: '目标',
    3: '导入',
    4: '知识储备',
    5: '任务布置',
    6: '课堂实操',
    7: '任务拓展',
    8: '课堂习题',
}

for num, name in layouts.items():
    analyze_layout(z, num, name)

z.close()
