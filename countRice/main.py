import cv2
import numpy as np

image = cv2.imread(r'C:\Users\ahmettakci\PycharmProjects\pythonProject3\prınc.jpg')


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


_, thresholded = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)


kernel = np.ones((5, 5), np.uint8)
morphology_result = cv2.morphologyEx(thresholded, cv2.MORPH_CLOSE, kernel)


_, labels, stats, centroids = cv2.connectedComponentsWithStats(morphology_result, connectivity=8)


num_rice = len(stats) - 1  # İlk etiket arka plan olduğu için çıkarılır


print("Pirinç sayısı:", num_rice)


cv2.imshow('Original Image', image)
cv2.imshow('Thresholded Image', thresholded)
cv2.imshow('Morphology Result', morphology_result)
cv2.waitKey(0)
cv2.destroyAllWindows()