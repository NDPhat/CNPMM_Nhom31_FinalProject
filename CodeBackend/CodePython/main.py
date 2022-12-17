import face_recognition
import numpy as np
known_image = face_recognition.load_image_file("1.jpg")
unknown_image = face_recognition.load_image_file("2.jpg")

biden_encoding = face_recognition.face_encodings(known_image)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

# biden_encoding = np.load('1.npy')
# unknown_encoding = np.load('2.npy')

results = face_recognition.compare_faces([biden_encoding], unknown_encoding)

print(results)
print(face_recognition.face_distance([biden_encoding], unknown_encoding))

print(known_image)
