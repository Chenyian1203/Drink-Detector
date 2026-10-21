from ultralytics import YOLO
import cv2

model_path = r'B:\OpenCV\Drink_Detector_Project\runs\detect\drink_slim_v1\weights\best.pt'
model = YOLO(model_path)

img_path = 'test_sprite.jpg' 

# 🚨 把 0.5 改成 0.01
results = model(img_path, conf=0.5)

print("\n========== 终极测试报告 ==========")
for r in results:
    # 如果 0.01 都没检测出来，说明真瞎了
    if len(r.boxes) == 0:
        print("❌ 依然没有任何目标")
    
    for box in r.boxes:
        class_name = model.names[int(box.cls[0])]
        conf = float(box.conf[0])
        print(f"🎯 发现目标: {class_name} | 置信度: {conf:.2f}")
    
    im_array = r.plot()
    cv2.imwrite("最终测试结果.jpg", im_array)
    print("📸 结果已保存为 '最终测试结果.jpg'")
print("===================================\n")