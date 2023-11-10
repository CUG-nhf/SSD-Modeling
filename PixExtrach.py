from PIL import Image, ImageTk
import tkinter as tk

class ImageWithCoordinates:
    def __init__(self, image_path):
        self.image = Image.open(image_path)
        self.width, self.height = self.image.size

        self.root = tk.Tk()
        self.root.title("Image with Coordinates")

        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()

        # 将图像转换为ImageTk.PhotoImage对象
        self.photo = ImageTk.PhotoImage(self.image)
        # 在画布上显示图像
        self.canvas.create_image(0, self.height, anchor=tk.SW, image=self.photo)  # 左下角为原点

        # 创建坐标系
        self.canvas.create_line(0, 0, self.width, 0, fill="red", width=2)  # x轴
        self.canvas.create_line(0, 0, 0, self.height, fill="blue", width=2)  # y轴

        # 设置鼠标点击事件
        self.canvas.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        x, y = event.x, self.height - event.y  # 调整y坐标以匹配左下角为原点
        # 输出点击点的坐标
        print(f"点击坐标: x={x}, y={y}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    image_path = "picture/pic1.png"  # 请替换为你的图片路径
    app = ImageWithCoordinates(image_path)
    app.run()
