from openai import OpenAI
from zhipuai import ZhipuAI
import streamlit as st

st.title("小智机器人")

client = ZhipuAI(api_key="fffff14805094b61044d9ed081039afb.qwRg71myXVJpw4Sg")

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        response= client.chat.completions.create(
            model="glm-4",  # 填写需要调用的模型名称
            messages=st.session_state.messages
        )
        context=response.choices[0].message.content
        st.markdown(context)
        end=f"{context}"
    st.session_state.messages.append({"role": "assistant", "content": end})





