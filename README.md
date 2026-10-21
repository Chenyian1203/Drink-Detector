# 🥤 Drink Detector: 具身智能视觉感知基础 Demo

基于 YOLOv8 实现的饮料（可口可乐 / 雪碧）目标检测项目。本项目作为具身智能（Embodied AI）的视觉感知模块基础演示，实现了从数据清洗、模型训练到图片推理的完整闭环。

## 📁 项目结构
* train.py: 模型训练脚本
* predict_slim.py: 图像推理与可视化测试脚本
* slim_dataset.py: 数据集瘦身脚本（从多类数据集中自动过滤提取特定类别）
* dataset_download.txt: 数据集获取与使用说明
* test_cola.py: 针对可乐的专项测试脚本

## 🚀 快速开始

### 1. 环境安装
直接运行以下命令安装依赖：
`pip install ultralytics opencv-python`

### 2. 数据集准备
本项目使用的是开源的 Drink_284 数据集。由于数据集体积较大，未直接上传至本仓库。请参考 dataset_download.txt 中的链接下载数据，并使用 slim_dataset.py 脚本提取仅包含可乐和雪碧的黄金数据集。

### 3. 模型训练
运行训练脚本：
`python train.py`
(注：为在 CPU 上实现极速验证，训练参数设置了较小的图片尺寸 320 和较少轮数。)

### 4. 模型推理
将测试图片放至根目录并重命名，运行：
`python predict_slim.py`

## 🏆 训练成果展示
* 雪碧 (Sprite) 测试识别置信度: 0.96
* <img width="883" height="377" alt="image" src="https://github.com/user-attachments/assets/585d1774-d50b-40ce-a29f-ab0cba7b7171" />

* 可乐 (Cola) 测试识别置信度: 0.93
* <img width="1098" height="553" alt="image" src="https://github.com/user-attachments/assets/0c41502d-c5a7-4f47-8243-c07b3c8632b3" />


## 🧠 踩坑与心得 (具身智能视角)
1. 数据决定上限：精简后的 158 张图片配合极速训练，即可达到 mAP50 0.98 的极高精度。
2. 泛化能力的挑战：模型对训练集内的标准易拉罐识别极准，但面对未见过的特殊包装（如大塑料瓶）或纯白底商品图时，会失效。这证明了在真实物理世界中，域偏移（Domain Shift） 是视觉感知落地的巨大挑战。
