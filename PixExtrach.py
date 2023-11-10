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
        self.photo = ImageTk.PhotoImage(image=self.image)
        # 在画布上显示图像
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

        # 设置鼠标点击事件
        self.canvas.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        x, y = event.x, self.height - event.y
        # 输出点击点的坐标
        print(f"点击坐标: x={x}, y={y}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    # # 添加以下两行代码以使用aqua渲染引擎
    # from tkinter import TclError
    # tk.Tk().createcommand('tk', lambda: 'tk useNativeDialog 0')
    
    image_path = "picture/pic1.png"  # 请替换为你的图片路径
    app = ImageWithCoordinates(image_path)
    app.run()
