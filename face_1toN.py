#coding=gbk
import face_recognition as face

liyifeng_image = face.load_image_file("liyifeng_1.jpg")
liudehua_image = face.load_image_file("liudehua_2.jpg")
wangluodan_image = face.load_image_file("王珞丹_1.jpg")
unknown_image = face.load_image_file("unknown.jpg")


liyifeng_encoding = face.face_encodings(liyifeng_image)[0]
liudehua_encoding = face.face_encodings(liudehua_image)[0]
wangluodan_encoding = face.face_encodings(wangluodan_image)[0]
unknown_encoding = face.face_encodings(unknown_image)[0]

#print(liudehua_encoding)
results = face.compare_faces([liudehua_encoding,wangluodan_encoding,liyifeng_encoding],unknown_encoding)
labels = ["刘德华","王珞丹","李易峰"]
print(results)
i=0
for rs in results:
    if rs:
        print("未知图片识别出来的是: ",labels[i])
    i +=1