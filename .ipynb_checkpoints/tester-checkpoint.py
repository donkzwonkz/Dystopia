import backend
from backend import preprocess_image, extract_faces, add_face, remove_face, identify_face, identify_all, facedetect
import requests

image=preprocess_image("tham caffeine.png")
image=extract_faces(image)
label="Tham"

data={
    'label':label,
    'image':image
}
url="http://127.0.0.1:5000"
def check_requests:
 requests.post(url,data=data,timeout=2.5)
print(check_requests)