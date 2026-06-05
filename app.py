import streamlit as st #Streamlit
#pip install streamlit

st.title("Merhaba")

if st.button("Tikla"):
    st.write("Merhaba, Streamlit")
else:
    st.write("Butona bas")

#Veri alma
kilo = st.number_input("Kilo (kg)", min_value=0.0)
yas = st.number_input("Boy(cm)", min_value=0.0)

if st.button("Hesapla"):
    if yas > 0:
        vk= kilo / (yas /100)
        st.metric("Sonuc:", f"{vk}")
    else:
        st.error("HATA")