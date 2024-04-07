
# https://streamlit.io/

# pip install --upgrade streamlit
# streamlit run streamlitDemo.py
# http://localhost:8501/

import streamlit as st
import matplotlib.pyplot as plt

from datetime import datetime
import time

def main():

    st.set_page_config(page_title="Simple Pie Chart Example", page_icon=":bar_chart:", layout="centered") #wide
    # st.title("Simple Pie Chart Example")
    # st.markdown("""
    #           ## This is a simple pie chart example
    # """)

    
    st.balloons()

    # st.bar_chart
    # st.bokeh_chart
    # st.altair_chart
    # st.area_chart
    # st.graphviz_chart
    # st.line_chart
#    st.plotly_chart

    # st.map
    # st.form
    # st.form_submit_button
    
    # st.caption("caption")
    # st.color_picker
    # st.audio("https://file-examples.com/wp-content/storage/2017/11/file_example_OOG_1MG.ogg", format='audio/ogg')
    st.code(body="name = input('enter name:')\nprint('code')", language="python", line_numbers=True)
    
    progress_bar = st.progress(0, text="progress:")
    for i in range(100):
        time.sleep(0.01)
        progress_bar.progress(i, text="progress")
    slider_val = st.slider('Select a value')

    with st.sidebar:
        st.chat_input("Chat", key="chat_input", max_chars=20, on_submit=print("chat input"))
        # st.chat_message(name="Chat message", avatar=None)
        st.radio("Radio", ["Option A", "Option B", "Option C"], key="radio", label_visibility="collapsed")

    # # st.header("Simple Pie Chart Example")
    # # st.title("file upload")
    name = st.text_input("Enter your name", key="name", type="default") # "password"
    st.button("Button", key="button", on_click=print("clicked"))
    # # camera = st.camera_input("Camera", key="camera")
    
    with st.container(height=500, border=True):
        col1, col2 = st.columns(2)
        with col1:
            st.header("A cat")
            st.image("https://static.streamlit.io/examples/cat.jpg")               
        with col2:
            st.header("A dog")
            st.image("https://static.streamlit.io/examples/dog.jpg")

        st.date_input("Date", key="date", value=None, on_change=print("date changed"))
        st.checkbox("Check me out", key="checkbox", value=False, on_change=print("checkbox changed"))

    files = st.file_uploader("Upload file", type=["pdf", "csv", "xlsx"], key="file", accept_multiple_files=True)
    with st.spinner("processing..."):
        for file in files:
            # st.write(file.name)
            print(file.name)
            data: bytes = file.read()
            print(len(data))
        st.success("done")

    st.write("done")
    
    # # Sample data
    # labels = ['A', 'B', 'C', 'D']
    # sizes = [15, 30, 45, 10]

    # # Plot pie chart
    # fig, ax = plt.subplots()
    # ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    # ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    # st.pyplot(fig)

if __name__ == "__main__":
    main()
