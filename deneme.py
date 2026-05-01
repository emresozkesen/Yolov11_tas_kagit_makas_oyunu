import ultralytics
import cv2
import imutils
from ultralytics import YOLO
import numpy as np
img = r"C:\Users\Yunus Emre\Desktop\python\köpek.png"
model_path = "yolo11s-cls.pt"
model = YOLO(model_path)
results = model(img)
class_dict = results[0].names
probs = results[0].probs.data.tolist()
print("sınıflar:", class_dict)
print("olasılıklar:", probs)
predicted_class_idx =np.argmax(probs)
predicted_class = class_dict[predicted_class_idx]
confidence = probs[predicted_class_idx]
print("sonuç:", predicted_class)
img = cv2.imread(img)
font =cv2.FONT_HERSHEY_SIMPLEX
text = f"{predicted_class} ({confidence:.2f})"

cv2.putText(img, text, (15, 40), font, 1, (0, 0, 255), 2)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

