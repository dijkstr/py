#!/usr/bin/env python
#coding:utf-8

import numpy as np
from Tkinter import *
import matplotlib
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin

def drawPic():    
    #获取GUI界面上的参数
    try:
        sampleCount=int(inputEntry.get())
        sampleCount2=int(inputEntry2.get())
    except:
        sampleCount=0
        sampleCount2=100
        print '请输入整数'
        inputEntry.delete(0,END)
        inputEntry.insert(0,'0')
        inputEntry.delete(0,END)
        inputEntry.insert(0,'100')
    
    #清空图像，以使得前后两次绘制的图像不会重叠
    drawPic.f.clf()
    drawPic.a=drawPic.f.add_subplot(111, projection='3d')
    n=sampleCount2-sampleCount  
    #绘制这些随机点的散点图，颜色随机选取
    for c, m in [('gray', 'o')]:
        xs = randrange(n, 0, 100)
        ys = randrange(n, 0, 100)
        zs = randrange(n, 0, 100)
        drawPic.a.scatter(xs, ys, zs, s=ys, c=c, marker=m)
    drawPic.a.set_xlabel('X Label')
    drawPic.a.set_ylabel('Y Label')
    drawPic.a.set_zlabel('Z Label')
    drawPic.a.set_title('Demo: Draw Some Dot')
    drawPic.canvas.show()
    
    
if __name__ == '__main__':
    
    matplotlib.use('TkAgg')
    root=Tk()
    
    #在Tk的GUI上放置一个画布，并用.grid()来调整布局
    drawPic.f = Figure(figsize=(5,4), dpi=100) 
    drawPic.canvas = FigureCanvasTkAgg(drawPic.f, master=root)
    drawPic.canvas.show()
    drawPic.canvas.get_tk_widget().grid(row=0, columnspan=4)    
 
    #放置标签、文本框和按钮等部件，并设置文本框的默认值和按钮的事件函数
    Label(root,text='筛选范围：').grid(row=1,column=0)
    inputEntry=Entry(root)
    inputEntry.grid(row=1,column=1)
    inputEntry.insert(0,'50')
    inputEntry2=Entry(root)
    inputEntry2.grid(row=1,column=2)
    inputEntry2.insert(0,'100')
    Button(root,text='画图',command=drawPic).grid(row=1,column=3,columnspan=4)
    
    #启动事件循环
    root.mainloop()
