import cv2

# 参考
# https://www.jianshu.com/p/1be8e0880c6c
# https://stackoverflow.com/questions/42073941/convert-image-to-pencil-drawing-not-pencil-sketch-using-imagemagick

imggirl=cv2.imread('./img/girl.jpg')
imggirl1=cv2.imread('./img/girl1.jpg')

sketch_gray, sketch_color = cv2.pencilSketch(imggirl1, sigma_s=60, sigma_r=0.07, shade_factor=0.05)
cv2.imwrite("./img/sketch_gray.jpg",sketch_gray)


stylize = cv2.stylization(imggirl1, sigma_s=60, sigma_r=0.07)
cv2.imwrite("./img/stylization.jpg",stylize)

dst3 = cv2.detailEnhance(imggirl1, sigma_s = 50, sigma_r = 0.15)
cv2.imwrite("./img/detailEnhance.jpg",dst3)

dst4 = cv2.edgePreservingFilter(imggirl1, flags=1, sigma_s = 50, sigma_r = 0.15)
cv2.imwrite("./img/edgePreservingFilter.jpg",dst4)

cv2.namedWindow("girl1")
cv2.imshow("girl1",dst3)
cv2.waitKey(0)
cv2.destroyAllWindows()
