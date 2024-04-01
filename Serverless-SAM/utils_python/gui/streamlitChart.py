
# https://streamlit.io/

# pip install --upgrade streamlit
# streamlit run streamlitChart.py

import streamlit as st
import matplotlib.pyplot as plt

def main():
    st.title("Simple Pie Chart Example")

    # Sample data
    labels = ['A', 'B', 'C', 'D']
    sizes = [15, 30, 45, 10]

    # Plot pie chart
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig)

if __name__ == "__main__":
    main()
