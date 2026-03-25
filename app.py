import streamlit as st
from PIL import Image
from src.face_recog import load_known_faces, detect_faces, recognize_faces

# 页面配置
st.set_page_config(page_title="人脸识别系统", page_icon="👤", layout="wide")
st.title("👤 人脸识别Web应用")
st.subheader("上传图片体验人脸检测与识别")

# 加载已知人脸库
with st.spinner("加载人脸库中..."):
    known_encodings, known_names = load_known_faces()

# 功能选择
option = st.radio("选择功能", ["人脸检测", "人脸识别"])
uploaded_file = st.file_uploader("上传图片", type=["jpg", "png", "jpeg"])

# 处理图片
def process_image(image):
    if option == "人脸检测":
        return detect_faces(image)
    else:
        return recognize_faces(image, known_encodings, known_names)

# 展示结果
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="上传图片", use_column_width=True)
    result_img, result_data = process_image(image)
    st.image(result_img, caption="处理结果", use_column_width=True)
    st.write("识别结果：", result_data)