import streamlit as st

text = st.text_input('write:')


list1 = []
def convert_list():
    list1[:0] = text.split(' ')
    st.write(list1)

st.button('Return list', on_click = convert_list())



def convert_lower():
    list_lower = [listt.lower() for listt in list1]
    st.write(list_lower)

st.button('lower' , on_click = convert_lower())


def count():
    num = 0
    for i in list1:
        num = num + 1
    st.write(num)

st.button('count' , on_click = count())