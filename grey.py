import cv2
from sketchpy import canvas


image_path = "F:\EL_PROFESSO.JPG.png"

image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)


edges = cv2.Canny(image, 200, 200)


processed_image_path = "F:/edges.png"


cv2.imwrite(processed_image_path, edges)

obj = canvas.sketch_from_image(processed_image_path)
obj.draw()
