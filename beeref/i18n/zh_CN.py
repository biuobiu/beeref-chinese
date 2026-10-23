# This file is part of BeeRef.
#
# BeeRef is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# BeeRef is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with BeeRef.  If not, see <https://www.gnu.org/licenses/>.

# 中文翻译字典
#
# 键是代码里的英文原文，未命中的键回退显示英文。
# tests/test_i18n.py 会检查字典与代码是否一致。
zh_CN = {
    # 菜单名称
    '&File': '文件(&F)',
    '&Edit': '编辑(&E)',
    '&View': '视图(&V)',
    '&Insert': '插入(&I)',
    '&Transform': '变换(&T)',
    '&Normalize': '标准化(&N)',
    '&Arrange': '排列(&A)',
    '&Images': '图像(&I)',
    'Open &Recent': '打开最近(&R)',
    # 对话框文本
    '&Settings': '设置(&S)',
    'Cancel': '取消',
    '&Close': '关闭(&C)',
    'Width:': '宽度：',
    'Height:': '高度：',
    'Change Opacity:': '调整透明度：',
    'Restore defaults?': '恢复默认设置？',
    'Do you want to restore all settings to their default values?': (
        '您确定要将所有设置恢复为默认值吗？'),
    'Default Arrange Method:': '默认排列方式：',
    'How images are arranged when inserted in batch': '批量插入时图像的排列方式',
    'Optimal': '最优',
    'Horizontal (by filename)': '水平排列（按文件名）',
    'Vertical (by filename)': '垂直排列（按文件名）',
    'Square (by filename)': '方形排列（按文件名）',
    'Arrange Optimal': '最优排列',
    'Arrange Horizontal (by filename)': '水平排列（按文件名）',
    'Arrange Vertical (by filename)': '垂直排列（按文件名）',
    'Arrannge Square (by filename)': '方形排列（按文件名）',
    'Image Storage Format:': '图像存储格式：',
    'How images are stored inside bee files. Changes will only '
    'take effect on newly saved images.': '图像在 bee 文件中的存储方式。更改仅对新保存的图像生效。',
    'Best Guess': '最佳猜测',
    'Small images and images with alpha channel are stored as '
    'png, everything else as jpg': '小图像和带 alpha 通道的图像存储为 png，其他图像存储为 jpg',
    'Always PNG': '始终使用 PNG',
    'Lossless, but large bee file': '无损，但 bee 文件较大',
    'Always JPG': '始终使用 JPG',
    'Small bee file, but lossy and no transparency support': (
        'bee 文件较小，但有损且不支持透明度'),
    'Arrange Gap:': '排列间距：',
    'The gap between images when using arrange actions.': '使用排列操作时图像之间的间距。',
    'Maximum Image Size:': '最大图像大小：',
    'The maximum image size that can be loaded (in megabytes). '
    'Set to 0 for no limitation.': '可以加载的最大图像大小（以兆字节为单位）。设置为 0 表示无限制。',
    'Confirm when closing an unsaved file:': '关闭未保存文件时确认：',
    'When about to close an unsaved file, should BeeRef ask for '
    'confirmation?': '当要关闭未保存的文件时，BeeRef 是否应该询问确认？',
    'Confirm when closing': '关闭时确认',
    'Settings': '设置',
    '&Miscellaneous': '杂项(&M)',
    '&Images && Items': '图像和项目(&I)',
    '&Restore Defaults': '恢复默认设置(&R)',
    'Debug Log': '调试日志',
    'Help': '帮助',
    'Color Gamut': '色域',
    'Threshold:': '阈值：',
    'Counting pixels...': '正在统计像素...',
    'Paste or drop images here.': '在此粘贴或拖放图像。',
    'Right-click for more options.': '右键点击查看更多选项。',
    'Recent Files': '最近文件',
    # 动作文本
    '&Help': '帮助(&H)',
    '&Open': '打开(&O)',
    '&Save': '保存(&S)',
    'Save &As...': '另存为(&A)...',
    'E&xport Scene...': '导出场景(&X)...',
    'Export &Images...': '导出图像(&I)...',
    '&Quit': '退出(&Q)',
    '&Images...': '图像(&I)...',
    '&Text': '文本(&T)',
    '&Undo': '撤销(&U)',
    '&Redo': '重做(&R)',
    '&Copy': '复制(&C)',
    'Cu&t': '剪切(&T)',
    '&Paste': '粘贴(&P)',
    '&Delete': '删除(&D)',
    '&Raise to Top': '置于顶层(&R)',
    'Lower to Bottom': '置于底层',
    '&Height': '高度(&H)',
    '&Width': '宽度(&W)',
    '&Size': '大小(&S)',
    '&Optimal': '最优(&O)',
    '&Horizontal (by filename)': '水平排列（按文件名）(&H)',
    '&Vertical (by filename)': '垂直排列（按文件名）(&V)',
    '&Square (by filename)': '方形排列（按文件名）(&S)',
    'Change &Opacity...': '调整透明度(&O)...',
    '&Grayscale': '灰度(&G)',
    'Show &Color Gamut': '显示色域(&C)',
    'Sample Color': '采样颜色',
    '&Crop': '裁剪(&C)',
    'Flip &Horizontally': '水平翻转(&H)',
    'Flip &Vertically': '垂直翻转(&V)',
    '&New Scene': '新建场景(&N)',
    '&Fit Scene': '适配场景(&F)',
    'Fit &Selection': '适配选择(&S)',
    'Reset &Scale': '重置缩放(&S)',
    'Reset &Rotation': '重置旋转(&R)',
    'Reset &Flip': '重置翻转(&F)',
    'Reset Cro&p': '重置裁剪(&P)',
    'Reset &All': '重置全部(&A)',
    '&Select All': '全选(&S)',
    'Deselect &All': '取消全选(&A)',
    '&About': '关于(&A)',
    'Show &Debug Log': '显示调试日志(&D)',
    'Show &Scrollbars': '显示滚动条(&S)',
    'Show &Menu Bar': '显示菜单栏(&M)',
    'Show &Title Bar': '显示标题栏(&T)',
    'Move &Window': '移动窗口(&W)',
    '&Fullscreen': '全屏(&F)',
    '&Always On Top': '始终置顶(&A)',
    '&Keyboard && Mouse': '键盘和鼠标(&K)',
    '&Open Settings Folder': '打开设置文件夹(&O)',
    # 对话框和提示信息
    'Discard unsaved changes?': '放弃未保存的更改？',
    'There are unsaved changes. Are you sure you want to open a '
    'new scene?': '有未保存的更改。确定要打开新场景吗？',
    'There are unsaved changes. Are you sure you want to quit?': (
        '有未保存的更改。确定要退出吗？'),
    'Problem loading file': '加载文件失败',
    'Problem saving file': '保存文件失败',
    'Export Scene to Image': '导出场景为图像',
    'Problem writing file': '写入文件失败',
    'Export Images': '导出图像',
    'Select one or more images to open': '选择一个或多个图像打开',
    'No image data or text in clipboard or image too big': (
        '剪贴板中没有图像数据或文本，或图像太大'),
    'About {APPNAME}': '关于 {APPNAME}',
    'Visit the {APPNAME} website': '访问 {APPNAME} 网站',
    'Problem loading images': '加载图像失败',
    'Loading {filename}': '加载 {filename}',
    'Saving {filename}': '保存 {filename}',
    'Exporting {filename}': '导出 {filename}',
    'Exporting to {directory}': '导出到 {directory}',
    # 其他文本
    '[Untitled]': '[未命名]',
    # 命令描述
    'Insert items': '插入项目',
    'Delete items': '删除项目',
    'Move items': '移动项目',
    'Scale items': '缩放项目',
    'Rotate items': '旋转项目',
    'Normalize items': '标准化项目',
    'Flip items': '翻转项目',
    'Reset Scale': '重置缩放',
    'Reset Rotation': '重置旋转',
    'Reset Flip': '重置翻转',
    'Reset Crop': '重置裁剪',
    'Reset All Transformations': '重置所有变换',
    'Arrange items': '排列项目',
    'Crop item': '裁剪项目',
    'Change text': '更改文本',
    'Change Opacity': '调整透明度',
    'Toggle Grayscale': '切换灰度',
    # 新增文案
    '%s image(s) could not be opened.<br/>': '%s 个图像无法打开。<br/>',
    '&Controls': '操作说明(&C)',
    '<p>Problem loading file %s</p><p>Not accessible or not a '
    'proper bee file</p>': '<p>加载文件 %s 失败</p><p>文件不可访问或不是有效的 bee 文件</p>',
    '<p>Problem saving file %s</p><p>File/directory not '
    'accessible</p>': '<p>保存文件 %s 失败</p><p>文件/目录不可访问</p>',
    '<p>Problem writing file %s</p><p>%s</p>': '<p>写入文件 %s 失败</p><p>%s</p>',
    'Co&py To Clipboard': '复制到剪贴板(&P)',
    'File already exists: {filename}': '文件已存在：{filename}',
    'File exists': '文件已存在',
    'Opacity: {value}%': '透明度：{value}%',
    'Open file': '打开文件',
    'Save file': '保存文件',
}
