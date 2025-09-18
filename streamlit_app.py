import streamlit as st

import streamlit as st

st.title("Hello, Streamlit!")

st.write("이것은 Streamlit의 간단한 예시 앱입니다.")

name = st.text_input("이름을 입력하세요:")
if name:
    st.success(f"안녕하세요, {name}님!")
st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
