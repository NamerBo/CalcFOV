import tkinter as tk
from tkinter import messagebox
import math

def calculate_fov():
    try:
        focal_length = float(entry_focal_length.get())
        sensor_width = float(entry_sensor_width.get())
        sensor_height = float(entry_sensor_height.get())
            
        hfov = 2 * math.degrees(math.atan(sensor_width / (2 * focal_length)))
        vfov = 2 * math.degrees(math.atan(sensor_height / (2 * focal_length)))
        dfov = 2 * math.degrees(math.atan(math.sqrt(sensor_width**2 + sensor_height**2) / (2 * focal_length)))
        
        label_hfov_result.config(text="HFOV: {:.2f} °".format(hfov))
        label_vfov_result.config(text="VFOV: {:.2f} °".format(vfov))
        label_dfov_result.config(text="DFOV: {:.2f} °".format(dfov))
    except ValueError:
        label_hfov_result.config(text="Invalid input!")
        label_vfov_result.config(text="Invalid input!")
        label_dfov_result.config(text="Invalid input!")

def calculate_dfov():
    try:
        hfov = float(entry_hfov.get())
        vfov = float(entry_vfov.get())
        
        hfov_rad = math.radians(hfov)
        vfov_rad = math.radians(vfov)
        
        tan_hfov = math.tan(0.5 * hfov_rad)
        tan_vfov = math.tan(0.5 * vfov_rad)
        
        dfov = 2 * math.degrees(math.atan(math.sqrt(tan_hfov**2 + tan_vfov**2)))
        
        dfov_result.config(text="DFOV : {:.2f} °".format(dfov))
    except ValueError:
        messagebox.showerror("Invalid input!", "Please input valid numbers!")
# 创建主窗口
root = tk.Tk()
root.geometry("500x500")
root.title("Camera FOV Calculator")

# 创建输入框和标签
calc_fov =tk.LabelFrame(root, text="Calculate Fov",padx=10, pady=10)
calc_fov.pack(padx=10, pady=10)
label_focal_length = tk.Label(calc_fov, text="Focal Length (mm):")
label_focal_length.pack()
entry_focal_length = tk.Entry(calc_fov)
entry_focal_length.pack()

label_sensor_width = tk.Label(calc_fov, text="Sensor Width (mm):")
label_sensor_width.pack()
entry_sensor_width = tk.Entry(calc_fov)
entry_sensor_width.pack()

label_sensor_height = tk.Label(calc_fov, text="Sensor Height (mm):")
label_sensor_height.pack()
entry_sensor_height = tk.Entry(calc_fov)
entry_sensor_height.pack()

# 创建计算按钮
button_calculate = tk.Button(calc_fov, text="Calculate FOV", command=calculate_fov)
button_calculate.pack()

# 创建显示结果的标签
label_hfov_result = tk.Label(calc_fov, text="")
label_hfov_result.pack()

label_vfov_result = tk.Label(calc_fov, text="")
label_vfov_result.pack()

label_dfov_result = tk.Label(calc_fov, text="")
label_dfov_result.pack()

# 计算DFOV
calc_dfov =tk.LabelFrame(root, text="Calculate DFov",padx=10, pady=10)
calc_dfov.pack(padx=10, pady=10)
label_hfov = tk.Label(calc_dfov, text="HFOV (°):")
label_hfov.pack()
entry_hfov = tk.Entry(calc_dfov)
entry_hfov.pack()

label_vfov = tk.Label(calc_dfov, text="VFOV (°):")
label_vfov.pack()
entry_vfov = tk.Entry(calc_dfov)
entry_vfov.pack()

button_calculate = tk.Button(calc_dfov, text="Calculate DFOV", command=calculate_dfov)
button_calculate.pack()

dfov_result = tk.Label(calc_dfov, text="")
dfov_result.pack()

# 运行主循环
root.mainloop()