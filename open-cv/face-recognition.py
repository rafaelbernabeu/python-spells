import cv2
import dlib

# Carrega o modelo de detector de faces pré-treinado
detector = dlib.get_frontal_face_detector()

# Carrega o modelo de reconhecimento facial pré-treinado
#http://dlib.net/files/shape_predictor_5_face_landmarks.dat.bz2
shape_predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
#http://dlib.net/files/dlib_face_recognition_resnet_model_v1.dat.bz2
face_recognition = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')

vid_capture = cv2.VideoCapture(1)

while(vid_capture.isOpened()):
    ret, frame = vid_capture.read()
    if ret == True:
        # Converte a imagem em escala de cinza
        img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detecta todas as faces na imagem
        faces = detector(img_gray)
        for face in faces:
            # Encontra os marcos faciais para a face atual
            landmarks = shape_predictor(img_gray, face)

            face_descriptor = face_recognition.compute_face_descriptor(frame, landmarks)
            face_chip = dlib.get_face_chip(frame, landmarks)    
            face_descriptor_from_prealigned_image = face_recognition.compute_face_descriptor(face_chip)
            #print(f"FaceDescriptor: {list(face_descriptor_from_prealigned_image)}")     

            # Desenha um retângulo ao redor da face atual
            x, y, w, h = face.left(), face.top(), face.width(), face.height()
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Percorre todos os marcos faciais e desenha um círculo em cada um
            for n in range(0, 68):
               x = landmarks.part(n).x
               y = landmarks.part(n).y
               cv2.circle(frame, (x, y), 3, (255, 0, 0), -1)

        # Exibe a imagem com as faces detectadas e os marcos faciais desenhados
        cv2.imshow('Facial Landmarks', frame)

        k = cv2.waitKey(20)
        # 113 is ASCII code for q key
        if k == 113:
            break
    else:
        break
 

vid_capture.release()
cv2.destroyAllWindows()