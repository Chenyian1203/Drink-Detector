from ultralytics import YOLO

if __name__ == '__main__':
    print("⏳ 开始极速训练...")
    # 加载本地模型
    model = YOLO(r'B:\OpenCV\Drink_Detector_Project\yolov8n.pt')
    
    # 开始训练
    model.train(
        data=r'B:\OpenCV\Drink_Detector_Project\dataset_slim\data.yaml', # 注意路径变了！
        epochs=20,        # 20 轮足够了，瘦身之后跑得飞快
        imgsz=320,        # 图片缩小一半，速度起飞
        batch=16,         # 批次加大，提高效率
        workers=0,        # Windows 下设为 0 防卡死
        name='drink_slim_v1'
    )