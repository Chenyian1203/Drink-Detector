from ultralytics import YOLO
import cv2

# 1. 召唤最强大脑
model_path = r'B:\OpenCV\Drink_Detector_Project\runs\detect\drink_slim_v1\weights\best.pt'
model = YOLO(model_path)

# 2. 读取你刚下载的可乐图
img_path = 'test_cola.jpg' 
print(f"🖼️ 正在测试可乐: {img_path}")

# 3. 推理（用 0.5 的及格线）
results = model(img_path, conf=0.5)

# 4. 打印并保存结果
print("\n========== 可乐测试报告 ==========")
for r in results:
    if len(r.boxes) == 0:
        print("❌ 完蛋，它没认出可乐...")
        
    for box in r.boxes:
        class_name = model.names[int(box.cls[0])]
        conf = float(box.conf[0])
        print(f"🎯 发现目标: {class_name} | 置信度: {conf:.2f}")
    
    # 画框并保存
    im_array = r.plot()
    cv2.imwrite("最终可乐结果.jpg", im_array)
    print("📸 结果已保存为 '最终可乐结果.jpg'，快去打开看看！")
print("===================================\n")