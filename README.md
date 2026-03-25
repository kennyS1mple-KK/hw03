# hw03 人脸检测项目 智251 白岳鹏 2025311864

## 项目介绍
基于 Python 与 Streamlit 搭建的简易人脸检测与识别系统，支持上传图片并进行人脸定位与标注。

## 项目结构
- app.py          项目主程序，提供 Web 界面
- src/face_recog.py  人脸处理核心功能
- requirements.txt  运行环境依赖
- README.md       项目说明

## 功能说明
1. 支持上传图片进行人脸检测
2. 自动框选出图片中的人脸区域
3. 提供可视化界面
4. 可扩展为人脸识别功能

## 使用方法
1. 安装环境依赖
2. 运行 Web 程序
3. 上传图片查看结果

## 运行命令
```bash
pip install -r requirements.txt
streamlit run app.py
