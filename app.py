# import google.generativeai as genai
# import os
# os.environ["API_KEY"] = "..................."
#

#---------------write code in notepad-------------------------

# genai.configure(api_key=os.environ["API_KEY"])
# a=input("enter something: ")
# model = genai.GenerativeModel("gemini-1.5-flash")
# response = model.generate_content(a)
# b=response.text
# with open('output.txt', 'w') as file:
#     file.write(b)
#
# # Step 2: Automatically open the text file using Notepad
# os.system('notepad.exe output.txt')
# print(response.text)

#---------------chatbot----------------------

# b=True
# while b==True:
#     a=input("enter something: ")
#     model= genai.GenerativeModel("gemini-pro")
#     # model = genai.GenerativeModel("gemini-1.5-flash")
#     # response = model.generate_content(a)
#     chat=model.start_chat()
#     response = chat.send_message(a)
#
#     print(response.text)


#-----------------------project LLM Model------------------------
# import streamlit as st
# import google.generativeai as genai
# import os
# os.environ["API_KEY"] = "........................"
# genai.configure(api_key=os.environ["API_KEY"])
# model= genai.GenerativeModel("gemini-pro")

# def get_gemini_response(question):
#     response = model.generate_content(question)
#     return response.text

# st.set_page_config(page_title="Q&A Demo")
# st.header("Gemini LLM Model")
# input=st.text_input("Input: ", key="input")
# submit=st.button("Tell Me")

# if submit:
#     response=get_gemini_response(input)
#     st.subheader("The response is")
#     st.write(response)

#----------------image also LLM model------------------


import streamlit as st
import google.generativeai as genai
import os
from PIL import Image
os.environ["API_KEY"] = "..........................."
genai.configure(api_key=os.environ["API_KEY"])
model= genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(input, image):
    if input != "":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text

st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Model")
input=st.text_input("Input Prompt : ", key="input")
uploaded_file = st.file_uploader("Choose an image...." , type=["jpg","jpeg","png"])
image=""
if uploaded_file is not None:
    image= Image.open(uploaded_file)
    st.image(image, caption="Uploaded image." ,use_column_width=True)


submit=st.button("Tell Me")

if submit:
    response=get_gemini_response(input, image)
    st.subheader("The response is")
    st.write(response)





