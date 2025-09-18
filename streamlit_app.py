import streamlit as st

import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.title("Streamlit 그림판 예시")
st.write("아래 캔버스에서 자유롭게 그림을 그려보세요!")

# 캔버스 설정
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # 채우기 색상
    stroke_width=5,
    stroke_color="#000000",
    background_color="#fff",
    height=300,
    width=400,
    drawing_mode="freedraw",
    key="canvas",
)

if canvas_result.image_data is not None:
    st.image(canvas_result.image_data, caption="그린 그림")
st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
