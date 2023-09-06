import cv2
from ambil_data import color_histogram_feature_extraction
from ambil_data import knn_classifier
import os
import os.path
import time
cap = cv2.VideoCapture(0)




(ret, frame) = cap.read()
prediction = ''
PATH = './training.data'
if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
    print ('training data is ready, classifier is loading...')
else:
    print ('training data is being created...')
    open('training.data', 'w')
    color_histogram_feature_extraction.training()
    print ('training data is ready, classifier is loading...')

def camera11():
    global prediction
    global ret
    (ret, frame) = cap.read()
    cv2.putText(frame,'Warna:' + prediction,(15,45),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,50)
    cv2.imshow("test", frame)
    color_histogram_feature_extraction.color_histogram_of_test_image(frame)
    prediction = knn_classifier.main('training.data', 'test.data')
    
while True:
    camera11()
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()
