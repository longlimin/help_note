#!/usr/bin/python
#-*- coding:utf-8 -*-  
import cv2
import numpy
import numpy as np

class OpenCv:
    """ My OpenCv helper """ 
 
    id = ""
    name = ""

    def __init__(self):
        self.id = "test id"
        self.name = "test name"
        
    def set(self, id, name): 
        self.id = id
        self.name = name

        return self
  
    def toString(self):
        res = ""
        res = self.id + " - " + self.name

        return res

    def test(self):
        print("test", self)
        
        #读取文件图片
        img = cv2.imread("bingo1.jpg")
        imgg = img.copy()
        #cv2.nameWindow("Image")
        #cv2.imshow("Image", img) 

        #新建图片
        copyImg = img.copy()    #复制原有的图像来获得一副新图像
        print(img.shape) 
        zerosImg = numpy.zeros(img.shape)  #创建图像，需要使用numpy的函数
        cvtImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #cvtColor获得原图像的副本
        cvtImg[...] = 0  #转成空白的黑色图像


        imgControl = self.controlImage(copyImg.copy());

        # rgbSplit = cv2.split(img)
        # print("rgbSplit", "size", len(rgbSplit), "r", len(rgbSplit[0])) 
        # cv2.imwrite("tsplitb.jpg", rgbSplit[0])
        # cv2.imwrite("tsplitg.jpg", rgbSplit[1])
        # cv2.imwrite("tsplitr.jpg", rgbSplit[2])
        # mergeRB = cv2.merge([rgbSplit[2], cv2.split(cvtImg)[0], rgbSplit[2]]) #前面分离出来的三个通道  
        # cv2.imwrite("tsplitrb.jpg", mergeRB)
        # #直方图 三个通道 
        # cv2.imwrite("thb.jpg", self.drawHist(rgbSplit[2], [0, 0, 255]))
        # cv2.imwrite("thg.jpg", self.drawHist(rgbSplit[1], [0, 255, 0]))
        # cv2.imwrite("thr.jpg", self.drawHist(rgbSplit[1], [255, 0, 0]))
        cv2.imwrite("thrgb.jpg", self.drawHistRGB(img))

        #写入文件 
        #cv2.imwrite("t1img.jpg", img) #第二个是图像矩阵    
        #cv2.imwrite("t2control.jpg", imgControl) #第二个是图像矩阵   
        #cv2.imwrite("t3quality.jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), 5]) 
        #cv2.imwrite("t4copy.jpg", copyImg)
        #cv2.imwrite("t5zeros.jpg", zerosImg)
        cv2.imwrite("t6cvt.jpg", cvtImg)

        #第三个参数 格式：对于JPEG，其表示的是图像的质量，用0-100的整数表示 认为95。 注意，cv2.IMWRITE_JPEG_QUALITY类型为Long，必须转换成int。 
        
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    #转灰度图
        cv2.imwrite("t2gray.jpg", imgGray)
        ret,imgBlack = cv2.threshold(imgGray, 127,255,cv2.THRESH_BINARY) #转二值图
        cv2.imwrite("t2black.jpg", imgBlack)
 
        #二值化5种情况
        self.testThreshold(img)

        #形态学处理
        #结构元素定义 
        element = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))  #5×5的十字形结构元素

        #腐蚀-膨胀
        self.testErodeDilate(imgBlack)
        #开闭运算 
        self.testOpenClose(imgBlack)
        #边缘检测
        self.testFindLine(imgGray.copy())
        #检测拐角
        self.testFindTurn(imgGray.copy())
        #初级滤波 模糊
        self.testBlur(imgGray.copy())

        #sabel算子
        self.testSabel(imgGray.copy())
        #laplacian算子
        self.testLaplacian(imgGray.copy())
        #canny边缘检测
        self.testCanny(imgGray.copy())
        #霍夫变换检测
        self.testHough(img.copy())
        #直方图均衡化处理
        self.testLut(img)
        #轮廓检测绘制
        self.testContours(img.copy())

        return
    #轮廓检测绘制
    def testContours(self, img):
        # cv2.findContours(image, mode, method[, contours[, hierarchy[, offset ]]])  
        # 返回两个值：contours：hierarchy。
        # 参数
        # 第一个参数是寻找轮廓的图像；
        # 第二个参数表示轮廓的检索模式，有四种（本文介绍的都是新的cv2接口）：
        #     cv2.RETR_EXTERNAL表示只检测外轮廓
        #     cv2.RETR_LIST检测的轮廓不建立等级关系
        #     cv2.RETR_CCOMP建立两个等级的轮廓，上面的一层为外边界，里面的一层为内孔的边界信息。如果内孔内还有一个连通物体，这个物体的边界也在顶层。
        #     cv2.RETR_TREE建立一个等级树结构的轮廓。
        # 第三个参数method为轮廓的近似办法
        #     cv2.CHAIN_APPROX_NONE存储所有的轮廓点，相邻的两个点的像素位置差不超过1，即max（abs（x1-x2），abs（y2-y1））==1
        #     cv2.CHAIN_APPROX_SIMPLE压缩水平方向，垂直方向，对角线方向的元素，只保留该方向的终点坐标，例如一个矩形轮廓只需4个点来保存轮廓信息
        #     cv2.CHAIN_APPROX_TC89_L1，CV_CHAIN_APPROX_TC89_KCOS使用teh-Chinl chain 近似算法
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
        ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  
        _, contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  
        # 需要搞一个list给cv2.drawContours()才行！！！！！
        c_max = []
        for i in range(len(contours)):
            cnt = contours[i]
            area = cv2.contourArea(cnt)
            # 处理掉小的轮廓区域，这个区域的大小自己定义。
            if(area < (1000)):
                c_min = []
                c_min.append(cnt)
                # thickness不为-1时，表示画轮廓线，thickness的值表示线的宽度。
                cv2.drawContours(img, c_min, -1, (0,255,0), thickness=-1)
                continue
            c_max.append(cnt)
        cv2.drawContours(img, c_max, -1, (0, 0, 255), thickness=2)
        #cv2.drawContours(img,contours,-1,(0,0,255),6)  
        self.save('tscontrours.jpg', img)

        return img
    #直方图均衡化处理
    def testLut(self, img):
        image = cv2.imread("gili.jpg", 0)  

        lut = np.zeros(256, dtype = image.dtype )#创建空的查找表
        hist= cv2.calcHist([image], #计算图像的直方图
            [0], #使用的通道
            None, #没有使用mask
            [256], #it is a 1D histogram
            [0.0,255.0])
            
        minBinNo, maxBinNo = 0, 255

        #计算从左起第一个不为0的直方图柱的位置
        for binNo, binValue in enumerate(hist):
            if binValue != 0:
                minBinNo = binNo
                break
        #计算从右起第一个不为0的直方图柱的位置
        for binNo, binValue in enumerate(reversed(hist)):
            if binValue != 0:
                maxBinNo = 255-binNo
                break
        #print (minBinNo, maxBinNo)

        #生成查找表，方法来自参考文献1第四章第2节
        for i,v in enumerate(lut):
            if i < minBinNo:
                lut[i] = 0
            elif i > maxBinNo:
                lut[i] = 255
            else:
                lut[i] = int(255.0*(i-minBinNo)/(maxBinNo-minBinNo)+0.5)

        #计算
        result = cv2.LUT(image, lut) 
        self.save("tslut-src.jpg", image)
        self.save("tslut.jpg", result)
        self.save("tslut-src-line.jpg", self.drawHist(image, [0, 0, 255]))
        self.save("tslut-line.jpg", self.drawHist(image, [0, 255, 255]))

        return result    
    #hough直线检测
    def testHough(self, img):  
        img = cv2.GaussianBlur(img,(3,3),0)
        edges = self.testCanny(img)#cv2.Canny(img, 50, 150, apertureSize = 3)
        lines = cv2.HoughLines(edges,1,np.pi/180,118)
        result = img.copy()

        #经验参数
        minLineLength = 200
        maxLineGap = 15
        lines = cv2.HoughLinesP(edges,1,np.pi/180,80,minLineLength,maxLineGap)
        #print(lines)
        for line in lines:
            for x1,y1,x2,y2 in line:
                cv2.line(result,(x1,y1),(x2,y2),(0, 0, 255),3)

        self.save('tshoughline-edges-canny.jpg', edges)
        self.save('tshoughline.jpg', result)

        return result 
    #canny边缘检测
    def testCanny(self, img):
        # edge = cv2.Canny(image, threshold1, threshold2[, edges[, apertureSize[, L2gradient ]]])   
        # 必要参数： •第一个参数是需要处理的原图像，该图像必须为单通道的灰度图；
        # •第二个参数是阈值1；
        # •第三个参数是阈值2。
        # 其中较大的阈值2用于检测图像中明显的边缘，但一般情况下检测的效果不会那么完美，边缘检测出来是断断续续的。所以这时候用较小的第一个阈值用于将这些间断的边缘连接起来。
        # 可选参数中apertureSize就是Sobel算子的大小。而L2gradient参数是一个布尔值，如果为真，则使用更精确的L2范数进行计算（即两个方向的倒数的平方和再开放），否则使用L1范数（直接将两个方向导数的绝对值相加）。
        img = cv2.GaussianBlur(img,(3,3),0)  
        canny = cv2.Canny(img, 50, 150, apertureSize = 3)  
        self.save("tscanny.jpg", canny)

        return canny
    #laplacian算子
    def testLaplacian(self, imgg):
        img = imgg 
        
        gray_lap = cv2.Laplacian(img,cv2.CV_16S,ksize = 3)
        imgLaplacian = cv2.convertScaleAbs(gray_lap)
        self.save("tslaplacian.jpg", imgLaplacian)


        imgGaussian = cv2.GaussianBlur(img,(5,5),1.5)  #去噪

        #dst = cv2.Laplacian(src, ddepth[, dst[, ksize[, scale[, delta[, borderType]]]]])  
        # 如果看了上一篇Sobel算子的介绍，这里的参数应该不难理解。 
        # 前两个是必须的参数：
        # •第一个参数是需要处理的图像；
        # •第二个参数是图像的深度，-1表示采用的是与原图像相同的深度。目标图像的深度必须大于等于原图像的深度；
        # 其后是可选的参数：
        # •dst不用解释了；
        # •ksize是算子的大小，必须为1、3、5、7。默认为1。
        # •scale是缩放导数的比例常数，默认情况下没有伸缩系数；
        # •delta是一个可选的增量，将会加到最终的dst中，同样，默认情况下没有额外的值加到dst中；
        # •borderType是判断图像边界的模式。这个参数默认值为cv2.BORDER_DEFAULT。
        gray_lap = cv2.Laplacian(imgGaussian,cv2.CV_16S,ksize = 3)
        imgLaplacian = cv2.convertScaleAbs(gray_lap)
        self.save("tslaplacian-gaussian-blur.jpg", imgLaplacian)

        return imgLaplacian
    #sabel算子
    def testSabel(self, imgg):
        img = imgg 

        #dst = cv2.Sobel(src, ddepth, dx, dy[, dst[, ksize[, scale[, delta[, borderType]]]]])  
        #•图形，
        #•深度，-1表示采用的是与原图像相同的深度。目标图像的深度必须大于等于原图像的深度 
        #•dx和dy表示的是求导的阶数，0表示这个方向上没有求导，一般为0、1、2
        #•ksize是Sobel算子的大小，必须为1、3、5、7。
        #•scale是缩放导数的比例常数，默认情况下没有伸缩系数；
        #•delta是一个可选的增量，将会加到最终的dst中，同样，默认情况下没有额外的值加到dst中；
        #•borderType是判断图像边界的模式。这个参数默认值为cv2.BORDER_DEFAULT。
        x = cv2.Sobel(img,cv2.CV_16S,1,0)
        y = cv2.Sobel(img,cv2.CV_16S,0,1)
        #Sobel函数求完导数后会有负值，还有会大于255的值。而原图像是uint8，即8位无符号数，所以Sobel建立的图像位数不够，会有截断。因此要使用16位有符号的数据类型，即cv2.CV_16S。
        #在经过处理后，别忘了用convertScaleAbs()函数将其转回原来的uint8形式。否则将无法显示图像，而只是一副灰色的窗口
        absX = cv2.convertScaleAbs(x)   # 转回uint8
        absY = cv2.convertScaleAbs(y)
        #Sobel算子是在两个方向计算的，最后还需要用cv2.addWeighted(...)函数将其组合起来
        imgSabel = cv2.addWeighted(absX,0.5,absY,0.5,0)
        self.save("tssable.jpg", imgSabel)

        return imgSabel
    #初级滤波
    def testBlur(self, imgg):
        img = imgg
        #用低通滤波来平滑图像 将每个像素替换为该像素周围像素的均值
        imgBlur = cv2.blur(img, (5,5)) 
        self.save("tgblur.jpg", imgBlur)
        #高斯模糊
        imgGaussian = cv2.GaussianBlur(img,(5,5),1.5)  
        self.save("tgaussian.jpg", imgGaussian)
        #低通滤波中，滤波器中每个像素的权重是相同的，即滤波器是线性的。而高斯滤波器中像素的权重与其距中心像素的距离成比例

        return imgGaussian
    #形态学处理 
    #检测拐角
    def testFindTurn(self, imgg): 
        image = imgg 
        #image = cv2.cvtColor(imgg, cv2.COLOR_BGR2GRAY)    #转灰度图
        origin = imgg
        #构造5×5的结构元素，分别为十字形、菱形、方形和X型
        cross = cv2.getStructuringElement(cv2.MORPH_CROSS,(5, 5))
        #菱形结构元素的定义稍麻烦一些
        diamond = cv2.getStructuringElement(cv2.MORPH_RECT,(5, 5))
        diamond[0, 0] = 0
        diamond[0, 1] = 0
        diamond[1, 0] = 0
        diamond[4, 4] = 0
        diamond[4, 3] = 0
        diamond[3, 4] = 0
        diamond[4, 0] = 0
        diamond[4, 1] = 0
        diamond[3, 0] = 0
        diamond[0, 3] = 0
        diamond[0, 4] = 0
        diamond[1, 4] = 0
        square = cv2.getStructuringElement(cv2.MORPH_RECT,(5, 5))
        x = cv2.getStructuringElement(cv2.MORPH_CROSS,(5, 5))
        #使用cross膨胀图像
        result1 = cv2.dilate(image,cross)
        #使用菱形腐蚀图像
        result1 = cv2.erode(result1, diamond)

        #使用X膨胀原图像 
        result2 = cv2.dilate(image, x)
        #使用方形腐蚀图像 
        result2 = cv2.erode(result2,square)

        #result = result1.copy()
        #将两幅闭运算的图像相减获得角 
        result = cv2.absdiff(result2, result1)
        #使用阈值获得二值图
        retval, result = cv2.threshold(result, 40, 255, cv2.THRESH_BINARY)

        #在原图上用半径为5的圆圈将点标出。
        for j in range(result.size):
            y = j / result.shape[0] 
            x = j % result.shape[0] 
            if result[x, y] == 255:
                cv2.circle(image, (y, x), 5, (255,0,0))

        cv2.imwrite("tfindturn.jpg", image)
        return image
    #边缘检测
    def testFindLine(self, imgg):
        #构造一个3×3的结构元素 
        element = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))
        dilate = cv2.dilate(imgg, element)
        erode = cv2.erode(imgg, element)

        #将两幅图像相减获得边，第一个参数是膨胀后的图像，第二个参数是腐蚀后的图像
        result = cv2.absdiff(dilate,erode);

        #上面得到的结果是灰度图，将其二值化以便更清楚的观察结果
        retval, result = cv2.threshold(result, 40, 255, cv2.THRESH_BINARY); 
        #反色，即对二值图每个像素取反
        result = cv2.bitwise_not(result); 
        cv2.imwrite("tfindline.jpg", result)

        return result
    #开闭运算 
    def testOpenClose(self, imgg): 
        img = self.toBlackWhite(imgg)

        #定义结构元素
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5, 5))
        #闭运算
        closed = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel) 
        #开运算
        opened = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel) 
        cv2.imwrite("tdopen.jpg", opened); 
        cv2.imwrite("tdclose.jpg", closed); 
        return
    #腐蚀-膨胀
    def testErodeDilate(self, imgg):  
        img = self.toBlackWhite(imgg)
        #img = cv2.cvtColor(imgg, cv2.COLOR_BGR2GRAY)    #转灰度图
        #OpenCV定义的结构元素
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))

        #腐蚀图像
        eroded = cv2.erode(img,kernel)
        cv2.imwrite("tcerode.jpg",eroded);

        #膨胀图像
        dilated = cv2.dilate(img,kernel)
        cv2.imwrite("tcdilate.jpg",dilated); 
        return
    #阈值 二值化灰度图
    def toBlackWhite(self, imgg):
        rgbSize = imgg.ndim 
        if(rgbSize == 2): #灰度图  或者黑白图 [0-1] / [0-255]
            ret,imgBlack = cv2.threshold(imgg,127,255,cv2.THRESH_BINARY) #转二值图 
            img = imgBlack 
        elif(rgbSize == 3): #RGB 彩色图 [0-255, 0-255, 0-255]
            imgGray = cv2.cvtColor(imgg, cv2.COLOR_BGR2GRAY)    #转灰度图
            return self.toBlackWhite(imgGray)

        return img
    #二值化测试
    def testThreshold(self, imgg):
            ret,thresh1 = cv2.threshold(imgg,127,255,cv2.THRESH_BINARY) #转二值图
            ret,thresh2 = cv2.threshold(imgg,127,255,cv2.THRESH_BINARY_INV)
            ret,thresh3 = cv2.threshold(imgg,127,255,cv2.THRESH_TRUNC)
            ret,thresh4 = cv2.threshold(imgg,127,255,cv2.THRESH_TOZERO)
            ret,thresh5 = cv2.threshold(imgg,127,255,cv2.THRESH_TOZERO_INV)   
            cv2.imwrite("THRESH_BINARY.png", thresh1) 
            cv2.imwrite("THRESH_BINARY_INV.png", thresh2) 
            cv2.imwrite("THRESH_TRUNC.png", thresh3) 
            cv2.imwrite("THRESH_TOZERO.png", thresh4) 
            cv2.imwrite("THRESH_TOZERO_INV.png", thresh5) 
            return
    #绘制 三通道 折线图
    def drawHistRGB(self, image):
        h = numpy.zeros((256,256,3)) #创建用于绘制直方图的全0图像    

        bins = numpy.arange(256).reshape(256,1) #直方图中各bin的顶点位置    
        color = [ (255,0,0),(0,255,0),(0,0,255) ] #BGR三种颜色    
        for ch, col in enumerate(color):   
            originHist = cv2.calcHist([image],[ch],None,[256],[0,256])    
            cv2.normalize(originHist, originHist,0,255*0.9,cv2.NORM_MINMAX)    
            hist=numpy.int32(numpy.around(originHist))    
            pts = numpy.column_stack((bins,hist))    
            cv2.polylines(h,[pts],False,col)    

        h=numpy.flipud(h)    
        return h
    #绘制 单通道 直方图
    def drawHist(self, image, color):    
        hist= cv2.calcHist([image], [0], None, [256], [0.0,255.0])    

        # hist = cv2.calcHist([image],  
        #     [0], #使用的通道  
        #     None, #没有使用mask  
        #     [256], #HistSize  
        #     [0.0,255.0]) #直方图柱的范围  

        minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(hist)    
        histImg = numpy.zeros([256,256,3], numpy.uint8)    
        hpt = int(0.9* 256);    

        for h in range(256):    
            intensity = int(hist[h]*hpt/maxVal)    
            cv2.line(histImg,(h,256), (h,256-intensity), color)    

        return histImg;  
    #像素控制
    def controlImage(self, img):
        rgbSize = img.ndim
        rowLen = img.shape[0]
        colLen = img.shape[1]
        print("rgbsize:", rgbSize, " rowLen:", rowLen, " colLen:", colLen)

        for i in range(0, rowLen, 5):
            for j in range(0, colLen, 10):
                if(rgbSize == 1):   #二值图 黑白
                    img[i] = 255
                elif(rgbSize == 2): #灰度图
                    img[i, j] = 255 
                elif(rgbSize == 3): #RGB 彩色图
                    img[i, j, 0] = 255
                    img[i, j, 1] = 255
                    img[i, j, 2] = 250

        # #灰度像素控制
        # img[20, 20] = 255
        # #rgb像素控制 
        # img[20, 20, 0] = 255
        # img[20, 20, 1] = 255
        # img[20, 20, 2] = 255
        
        return img
    #保存图片
    def save(self, name, img):
        cv2.imwrite(name, img)
        return
