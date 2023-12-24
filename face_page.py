
import streamlit as st
import cv2
from PIL import Image
import numpy as np

# 加载人脸检测模型
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')



def detect_faces(image):
    # 转换为灰度图像
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 检测面部
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # 在检测到的面部周围画矩形
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
    return image

def app():
    # 设置Streamlit页面
    st.title("人脸识别监测")

    # 文件上传器
    uploaded_file = st.file_uploader("选择一个图像或视频文件", type=['jpg', 'png', 'jpeg', 'mp4'])
    if uploaded_file is not None:
        # 读取图像
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        # 人脸检测
        image = detect_faces(image)

        # 显示图像
        st.image(image, channels="BGR")
