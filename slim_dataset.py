import os
import shutil

# ================= 配置区 =================
# 原来的数据集路径 (注意改成你的真实路径)
src_dir = r'B:\OpenCV\Drink_Detector_Project\dataset'
# 精简后的新数据集路径
dst_dir = r'B:\OpenCV\Drink_Detector_Project\dataset_slim'

# 原数据集中可乐的ID是0，雪碧的ID是2
# 如果我们只留这两个，新的ID会变成 0 和 1
# 下面的映射表会把老ID转换成新ID：0->0, 2->1
id_map = {0: 0, 2: 1}
# ==========================================

print("开始瘦身，只保留可乐和雪碧...")

# 创建新文件夹
for split in ['train', 'val']:
    os.makedirs(os.path.join(dst_dir, 'images', split), exist_ok=True)
    os.makedirs(os.path.join(dst_dir, 'labels', split), exist_ok=True)

count = 0
for split in ['train', 'val']:
    img_dir = os.path.join(src_dir, 'images', split)
    lbl_dir = os.path.join(src_dir, 'labels', split)
    
    if not os.path.exists(img_dir):
        continue
        
    for img_name in os.listdir(img_dir):
        if not img_name.endswith(('.jpg', '.png', '.jpeg')):
            continue
            
        lbl_name = img_name.rsplit('.', 1)[0] + '.txt'
        lbl_path = os.path.join(lbl_dir, lbl_name)
        
        if os.path.exists(lbl_path):
            with open(lbl_path, 'r') as f:
                lines = f.readlines()
            
            new_lines = []
            for line in lines:
                parts = line.strip().split()
                if len(parts) > 0:
                    cls_id = int(parts[0])
                    # 如果这个类别是我们想要的（可乐或雪碧）
                    if cls_id in id_map:
                        # 替换成新的类别ID (0或1)
                        parts[0] = str(id_map[cls_id])
                        new_lines.append(" ".join(parts) + "\n")
            
            # 如果这张图里至少有一个可乐或雪碧，就把它复制过去
            if new_lines:
                shutil.copy(os.path.join(img_dir, img_name), os.path.join(dst_dir, 'images', split, img_name))
                with open(os.path.join(dst_dir, 'labels', split, lbl_name), 'w') as f:
                    f.writelines(new_lines)
                count += 1

print(f"瘦身完成！一共保留了 {count} 张包含可乐或雪碧的图片。")