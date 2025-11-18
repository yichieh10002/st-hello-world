import streamlit as st

st.title("我的第一個 Streamlit 應用")
st.header("這是大標題")
st.subheader("這是中標題")
st.write("這是普通文字")
st.write("看出差別了嗎？字的大小不一樣！")
st.divider()

st.title("簡單登入系統")

username = st.text_input("帳號")
password = st.text_input("密碼", type="password")

if st.button("登入"):
    if username == "admin" and password == "1234":
        st.success("登入成功！")
        st.balloons()
    else:
        st.error("帳號或密碼錯誤！")
