import streamlit as st
st.title('some sort of web')
name = st.text_input('이름 입력 : ')
menu = st.selectbox('과일 선택', [ '사과', '배', '복숭아' ])
if st.button('heeeeeeeeeeeeeeeeeeeeeeeeeeeello'):
	st.write(f"안녕하세요, {name} 님! 당신이 좋아하는 과일은 {menu}군요!")
