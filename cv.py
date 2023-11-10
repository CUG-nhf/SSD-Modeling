import cv2
import numpy as np

def detect_lines(image_path):
    # 读取图像
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 使用Canny边缘检测
    edges = cv2.Canny(gray, 50, 150)

    # 使用霍夫直线变换检测直线
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=50, minLineLength=30, maxLineGap=10)

    return lines

def detect_points(image_path, lines):
    # 读取图像
    image = cv2.imread(image_path)
    
    # 在图像上标记检测到的直线
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # 显示标记直线的图像
    cv2.imshow('Detected Lines', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = "your_image_path.jpg"  # 请替换为你的图片路径
    lines = detect_lines(image_path)
    detect_points(image_path, lines)
