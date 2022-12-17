import face_recognition
import numpy as np

def login_function(image,name):
    unknown_encoding = face_recognition.face_encodings(image)
    if len(unknown_encoding) > 0:
        unknown_encoding = unknown_encoding[0]
        path_save = 'dataset' +'/'+ name + '.npy'
        np.save(path_save, unknown_encoding)
        return True
    return False

def recognize_function(image,dataset):
    unknown_encoding = face_recognition.face_encodings(image)
    if len(unknown_encoding) > 0:
        unknown_encoding = unknown_encoding[0]
        results = face_recognition.face_distance(dataset['encoding'], unknown_encoding)
        # min distance
        min_distance = min(results)
        # index min distance
        index = np.argmin(results)
        # name
        name = dataset['name'][index]
        return name, results[index]
    return None, None
