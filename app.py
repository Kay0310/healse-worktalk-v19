
import streamlit as st

# Sample form
name = st.text_input("이름")
department = st.text_input("부서")

uploaded_file = st.file_uploader("작업 사진 업로드", type=["jpg", "jpeg", "png"])
if uploaded_file:
    st.image(uploaded_file, caption="업로드된 작업 사진", use_column_width=True)

    if st.button("저장하기"):
        st.success("저장 완료! 다음 사진을 입력해 주세요.")
        st.rerun()  # <-- 최신 버전에서 사용 가능한 rerun 함수
