import cv2

img = cv2.imread("galaxy.jpg",0)
  # In above code,
  # 0 indicates black and white
  # 1 indicates RGB
  # -1 indicates color image

print(type(img))
print('*'*30)
print(img)
print('*'*30)
print(img.shape)
print('*'*30)
print(img.ndim)

resized_image = cv2.resize(img, (1000,500))
cv2.imshow('Galaxy', resized_image) #resized_image
cv2.waitKey(0)
cv2.destroyAllWindows()
# If we change 0 to 1 or to -1 then results will change
