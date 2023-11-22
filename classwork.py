import streamlit as st
from PIL import Image

st.title("CURRENCY CONVERTER")
img = Image.open("CCC.png")
st.image(img.resize((200,200)))
curr = ["Naira", "Pounds", "Dollars", "Euros", "Yen", "Cedis"]
conv = [1, 1023, 816, 890, 114, 68]

def convert(num, initial, final):
    ini_id = curr.index(initial)
    fin_id = curr.index(final)

    value1 = conv[ini_id]
    value2 = conv[fin_id]

    result = num * value1 / value2

    return round(result,2)
    
num = st.number_input("How much are you converting?")
initial = st.selectbox("From", curr)
final = st.selectbox("To", curr)

amount = convert( num,initial,final)

if st.button("Convert"):
   st.write(amount)
st.balloons()