import glob
import numpy as np
import face_recognition


def create_dataset():
    list_people = glob.glob("image/50_people/*")

    for path_folder in list_people:
        path_image = glob.glob(path_folder + "/*.jpg")[0]
        image = face_recognition.load_image_file(path_image)
        encoding = face_recognition.face_encodings(image)
        if len(encoding) > 0:
            encoding = encoding[0]
            path_save = 'dataset' +'/'+ path_image.split('/')[-1].split('.')[0] + '.npy'
            np.save(path_save, encoding)\

def load_dataset():
    list_people = glob.glob("dataset/*")
    list_name = []
    list_encoding = []
    for path in list_people:
        name = path.split('/')[-1].split('.')[0]
        encoding = np.load(path)
        list_name.append(name)
        list_encoding.append(encoding)
    dataset = {'name': list_name, 'encoding': list_encoding}
    return dataset

