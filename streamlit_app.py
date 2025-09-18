

import streamlit as st
import math

st.title("넓이 계산기")

shape = st.selectbox("도형을 선택하세요", ["사각형", "삼각형", "원"])

if shape == "사각형":
	width = st.number_input("가로 길이", min_value=0.0, value=0.0, step=0.1)
	height = st.number_input("세로 길이", min_value=0.0, value=0.0, step=0.1)
	if st.button("사각형 넓이 계산"):
		area = width * height
		st.success(f"사각형의 넓이: {area}")
elif shape == "삼각형":
	base = st.number_input("밑변 길이", min_value=0.0, value=0.0, step=0.1)
	height = st.number_input("높이", min_value=0.0, value=0.0, step=0.1)
	if st.button("삼각형 넓이 계산"):
		area = 0.5 * base * height
		st.success(f"삼각형의 넓이: {area}")
elif shape == "원":
	radius = st.number_input("반지름", min_value=0.0, value=0.0, step=0.1)
	if st.button("원의 넓이 계산"):
		area_pi = radius * radius
		st.success(f"원의 넓이: {area_pi}π")
st.title("🎈 My new app")

