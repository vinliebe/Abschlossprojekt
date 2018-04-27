import cv2
import numpy as np
from matplotlib import pyplot as plt




pcb1 = cv2.imread('C:/Users/XPS15/Desktop/Abschlossprojekt/mark1.jpg',cv2.IMREAD_GRAYSCALE)

pcb2 = cv2.imread('C:/Users/XPS15/Desktop/Abschlossprojekt/mark2.jpg',cv2.IMREAD_GRAYSCALE)

mark = cv2.imread('C:/Users/XPS15/Desktop/Abschlossprojekt/mark.jpg',cv2.IMREAD_GRAYSCALE)

cl1  = [122.141,13.8226]
cl2  = [7.2080,13.9886]

def match(pcb,mark):
    
    #w=mark点宽度，h=mark点高度
    w, h = mark.shape[::-1]

    pt=[1,1]
    

    #二值化
    ret,pcb2 = cv2.threshold(pcb,127,255,cv2.THRESH_BINARY)
    ret,mark2 = cv2.threshold(mark,127,255,cv2.THRESH_BINARY)
    
    #模板匹配
    res = cv2.matchTemplate(pcb2,mark2,5)
    threshold = 0.61 
    loc = np.where(res >= threshold)

    for pt in zip(*loc[::-1]): 
        cv2.rectangle(pcb, pt, (pt[0] + w, pt[1] + h), (7,249,151), 1)

    cv2.imshow('result',pcb)
    cv2.waitKey(0)  
    cv2.destroyAllWindows()
    

    print(pt)

    return(pt)


def calculate(mark1,mark2):
    
    
#根据三个mark点坐标进行对准点计算

    
    add = [(mark1[0]+mark2[0])/2,(mark1[1]+mark2[1])/2]
    

    return(add)

def transform(capturelocal,add):

    #进行机床坐标转换
    
    k = 7.576e-03
    
    add = [add[0]*k,add[1]*k]

    tadd = capturelocal + add

    return(tadd)
    

 

def main():
    
    
    mark1 = transform(cl1,match(pcb1,mark))
    mark2 = transform(cl2,match(pcb2,mark))
    

    print(calculate(mark1,mark2))


  
#cv2.imshow('result',pcb)
#cv2.waitKey(0)  
#cv2.destroyAllWindows() 

  #  cv2.imshow('pcb2',pcb2)
  #  cv2.imshow('mark2',mark2)
  #  	cv2.waitKey(0)  
  #  cv2.destroyAllWindows() 
