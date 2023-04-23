import cv2
img = cv2.imread("danny-dog.jpg", cv2.IMREAD_GRAYSCALE)

filename = 'danny-dog-copy.png'
v = cv2.imwrite(filename, img)
if v == True:
    print('Image saved successfully')
else:
    print('Image save failed')
