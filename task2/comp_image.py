import cv2

# read image --> convert to grayscale
image1 = cv2.imread('task2/img1.jpg')
gray_scale1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
# read image --> convert to grayscale
image2 = cv2.imread('task2/img2.jpg')
gray_scale2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
# Threshold the difference image to highlight the differences
thresh_hold = cv2.threshold(cv2.absdiff(gray_scale1, gray_scale2), 50, 255, cv2.THRESH_BINARY)[1]
# Find the contours
contours, _ = cv2.findContours(
    thresh_hold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# Draw circles around the contours
for contour in contours:
    (x, y), radius = cv2.minEnclosingCircle(contour)
    cv2.circle(image2, (int(x), int(y)), int(radius), (0, 255, 0), 2)
    
# Show result
cv2.imshow("Result", image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
