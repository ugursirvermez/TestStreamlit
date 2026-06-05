import streamlit as st #Streamlit
#pip install streamlit
import pandas as pd

#Sayfa configure ayarı yapılır. Bu sayfanın temel özelliklerini belirtir.
st.set_page_config(page_title="Mini Görev Panosu", 
                   page_icon="pictures/checklist.png", layout="centered")

#STYLE -> CSS KISMI
st.markdown(
"""
<style>
.app-header{
    color: blue;
    padding: 28px, 32px;
}
</style>
""",
unsafe_allow_html=True

)
#DURUM -> Görev durumlarını belirten bir değişken
if "tasks" not in st.session_state:
    st.session_state.tasks = [
        {"text": "Streamlit Hesabı Aç", "done": True},
        {"text": "Uygulamayı Yükle", "done": True}
    ]
#BAŞLIK -> HTML DIV
st.markdown(
    """
    <div class = "app-header"> 
    <h1>GÖREV LİSTESİ</h1>
    <p>TEST PROJEMİZ</p>
    </div>
    """,
    unsafe_allow_html=True
)
#GÖREVLER EKLEME
col_input, col_btn = st.columns([4,1])
with col_input:
    new_task = st.text_input("Yeni Görev", placeholder="Görevi yaz...", 
                             label_visibility="visible")
with col_btn:
    if st.button("Ekle", use_container_width=True):
        if new_task.strip():
            st.session_state.tasks.append({"text": new_task.strip(),
                                           "done":False})
            st.rerun() #Güncelleme yap
st.write("")

#GÖREVLERİN LİSTESİ

#ÖZET