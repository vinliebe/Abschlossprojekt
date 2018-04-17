import cv2
from matplotlib import pyplot as plt
import numpy as np

pcb1 = cv2.imread('.../pcb1.jpg',cv2.IMREAD_GRAYSCALE)
pcb2 = cv2.imread('.../pcb2.jpg',cv2.IMREAD_GRAYSCALE)
pcb3 = cv2.imread('.../pcb3.jpg',cv2.IMREAD_GRAYSCALE)
mark = cv2.imread('.../mark.jpg',cv2.IMREAD_GRAYSCALE)



def match(pcb,mark):
    
    #w=mark点宽度，h=mark点高度
    w, h = mark.shape[::-1]
    
    #二值化
    ret,pcb2 = cv2.threshold(pcb,127,255,cv2.THRESH_BINARY)
    ret,mark2 = cv2.threshold(mark,127,255,cv2.THRESH_BINARY)
    
    #模板匹配
    res = cv2.matchTemplate(pcb2,mark2,5)
    threshold = 0.7 
    loc = np.where(res >= threshold)

    for pt in zip(*loc[::-1]): 
        cv2.rectangle(pcb, pt, (pt[0] + w, pt[1] + h), (7,249,151), 1)

    return(pt)

def calculate(mark1.mark2,mark3):
    
    #根据三个mark点坐标进行对准点计算

    add = [(mark1+mark2)/2,(mark1+mark3)/2]
    
    return(add)

def transform():

    #进行机床坐标转换
    return()
     
def main():
    
    mark1 = transform(match(pcb1,mark))
    mark2 = transform(match(pcb2,mark))
    mark3 = transform(match(pcb3,mark))

    print(calculate(mark1.mark2,mark3))
    
#cv2.imshow('result',pcb)
#cv2.waitKey(0)  
#cv2.destroyAllWindows() 

  #  cv2.imshow('pcb2',pcb2)
  #  cv2.imshow('mark2',mark2)
  #  	cv2.waitKey(0)  
  #  cv2.destroyAllWindows() 
