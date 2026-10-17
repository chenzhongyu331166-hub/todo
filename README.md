# Todo 命令行工具
用法：
    python todo.py add 学Python
    python todo.py list
功能：
    add  添加任务
    list 列出所有任务

文件说明：
    todo.py        命令行入口
    utils.py       存盘/读盘函数
    data.json      自动生成的存档

## 运行环境
Python >= 3.8
本项目只使用Python内置标准库，无需安装第三方依赖。

## 快速上手步骤（给陌生人）
1. 解压压缩包，把todo文件夹放到本地
2. 打开终端，cd进入todo项目根目录
3. 执行命令运行程序：
```bash
python todo.py add 学Python
python todo.py list
