BeeRef 中文版 — 简单的参考图像查看器
======================================

.. raw:: html

   <img align="left" width="100" height="100" src="https://raw.githubusercontent.com/rbreu/beeref/main/beeref/assets/logo.png">

`BeeRef <https://beeref.org>`_ 让您可以快速排列参考图像并在创作时查看它们。其极简界面设计不会干扰您的创作过程。

|python-version| |github-ci-flake8| |github-ci-pytest| |codecov| |downloads-total| |downloads-latest|

.. image:: https://github.com/rbreu/beeref/blob/main/images/screenshot.png

.. |python-version| image:: https://github.com/rbreu/beeref/blob/main/images/python_version_badge.svg
   :target: https://www.python.org/

.. |github-ci-flake8| image:: https://github.com/rbreu/beeref/actions/workflows/flake8.yml/badge.svg
   :target: https://github.com/rbreu/beeref/actions/workflows/flake8.yml

.. |github-ci-pytest| image:: https://github.com/rbreu/beeref/actions/workflows/pytest.yml/badge.svg
   :target: https://github.com/rbreu/beeref/actions/workflows/pytest.yml

.. |codecov| image:: https://codecov.io/gh/rbreu/beeref/branch/main/graph/badge.svg?token=QA8HR1VVAL
   :target: https://codecov.io/gh/rbreu/beeref

.. |downloads-total| image:: https://img.shields.io/github/downloads/rbreu/beeref/total.svg
   :target: https://github.com/rbreu/beeref/releases

.. |downloads-latest| image:: https://img.shields.io/github/downloads/rbreu/beeref/latest/total.svg
   :target: https://github.com/rbreu/beeref/releases


安装
----

稳定版本
~~~~~~~~~

从 `最新发布 <https://github.com/biuobiu/beeref-chinese/releases>`_ 页面获取适合您操作系统（Windows、Linux、macOS）的文件。不同的 Linux 版本基于不同版本的 Ubuntu 构建，应该也能在其他发行版上运行，但您可能需要尝试哪个版本适用。

**Linux 用户**需要在运行前给予文件可执行权限。可选：如果您希望 BeeRef 出现在应用菜单中，请将 `发布部分 <https://github.com/biuobiu/beeref-chinese/releases>`_ 中的桌面文件保存到 ``~/.local/share/applications``，保存 `logo <https://raw.githubusercontent.com/rbreu/beeref/main/beeref/assets/logo.png>`_，并调整桌面文件中的路径以匹配您的 BeeRef 安装位置。

**MacOS X 用户**，如果运行 BeeRef 时遇到问题，请查看 `详细说明 <https://beeref.org/macosx-run.html>`_。

通过 `atom feed <https://github.com/biuobiu/beeref-chinese/releases.atom>`_ 关注后续发布。


开发版本
~~~~~~~~~

要获取当前开发版本，您需要有一个工作的 Python 3 环境。运行以下命令安装开发版本::

  pip install git+https://github.com/biuobiu/beeref-chinese.git

然后运行 ``beeref`` 或 ``beeref filename.bee``。


功能特性
--------

* 移动、缩放、旋转、裁剪和翻转图像
* 批量缩放图像到相同的宽度、高度或大小
* 批量垂直、水平或优化空间排列图像
* 添加文本注释
* 启用始终置顶模式并禁用标题栏，让 BeeRef 窗口不引人注目地浮动在您的艺术程序上方
* 支持中文语言界面

.. image:: https://github.com/rbreu/beeref/blob/main/images/screenshot.png


关于 bee 文件格式
~~~~~~~~~~~~~~~~~~

所有图像都以 PNG 或 JPG 格式嵌入到 bee 文件中。bee 文件格式是一个 sqlite 数据库，图像存储在 sqlar 表中——这意味着它们可以使用 `sqlite 命令行程序 <https://www.sqlite.org/cli.html>`_ 提取::

  sqlite3 myfile.bee -Axv

计划在 BeeRef 内部添加导出选项，但上述方法始终独立于 BeeRef 工作。


故障排除
--------

您可以通过 *帮助 -> 显示调试日志* 访问日志输出。如果 BeeRef 根本无法启动，您可以在此处找到日志文件：

Windows：

  C:\Documents and Settings\用户名\Application Data\BeeRef\BeeRef.log

Linux 和 MacOS：

  /home/用户名/.config/BeeRef/BeeRef.log


开发者说明
----------

BeeRef 用 Python 和 PyQt6 编写。更多信息，请参阅 `CONTRIBUTING.rst <https://github.com/biuobiu/beeref-chinese/blob/main/CONTRIBUTING.rst>`_。
