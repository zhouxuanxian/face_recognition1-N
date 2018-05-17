#coding=gbk
import face_recognition as face

liyifeng_image = face.load_image_file("liyifeng_1.jpg")
liudehua_image = face.load_image_file("liudehua_2.jpg")
wangluodan_image = face.load_image_file("����_1.jpg")
unknown_image = face.load_image_file("unknown.jpg")


liyifeng_encoding = face.face_encodings(liyifeng_image)[0]
liudehua_encoding = face.face_encodings(liudehua_image)[0]
wangluodan_encoding = face.face_encodings(wangluodan_image)[0]
unknown_encoding = face.face_encodings(unknown_image)[0]

#print(liudehua_encoding)
results = face.compare_faces([liudehua_encoding,wangluodan_encoding,liyifeng_encoding],unknown_encoding)
labels = ["���»�","����","���׷�"]
print(results)
i=0
for rs in results:
    if rs:
        print("δ֪ͼƬʶ���������: ",labels[i])
    i +=1