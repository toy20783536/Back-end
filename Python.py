#畫一條貪食蛇
import turtle #繪製圖像的函數庫
def drawSnake (rad,angle,len,neckred):#rad圓形軌跡半徑的位置 angle沿著圓形繪製的弧度值
    for i in range (len) :
        turtle.circle(rad,angle)
        turtle.circle(-rad,angle)
    turtle.circle(rad,angle/2)
    turtle.fd(rad)#爬行的距離
    turtle.circle(neckred+1,180)
    turtle.fd(rad*2/3)
def main():
    turtle.setup(1300,800,0,0) #設定窗口位置(長 寬 座標(X,Y))
    pythonsize=30 #設定繪筆大小
    turtle.pensize(pythonsize)
    turtle.pencolor("blue")#設定顏色
    turtle.seth(-40) #運行角度
    drawSnake(40,80,5,pythonsize/2)
main()