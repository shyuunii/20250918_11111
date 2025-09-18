# Streamlit 예시 앱
import streamlit as st

st.title("Streamlit 요소 데모")

st.header("1. 텍스트와 마크다운")
st.write("이것은 일반 텍스트입니다.")
st.markdown("**마크다운** _스타일링_도 지원합니다!")

st.header("2. 입력 요소")
name = st.text_input("이름을 입력하세요:")
age = st.number_input("나이", min_value=0, max_value=120, value=20)
st.write(f"입력한 이름: {name}, 나이: {age}")

st.header("3. 버튼과 체크박스")
if st.button("버튼을 눌러보세요"):
    st.success("버튼이 눌렸습니다!")

agree = st.checkbox("동의합니다")
if agree:
    st.info("동의해주셔서 감사합니다!")

st.header("4. 슬라이더와 선택박스")
value = st.slider("값을 선택하세요", 0, 100, 50)
st.write(f"선택한 값: {value}")

option = st.selectbox("좋아하는 동물은?", ["강아지", "고양이", "토끼"])
st.write(f"선택한 동물: {option}")

st.header("5. 이미지와 그래프")
st.image("https://static.streamlit.io/examples/cat.jpg", caption="고양이 이미지")

import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)
st.pyplot(fig)
import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
