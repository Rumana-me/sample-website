import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")


# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://lottie.host/9e45efb9-b42c-4761-a78b-2ea414be90da/jGBQAmHq8h.json")


# ---- HEADER SECTION ----
with st.container():
    st.subheader("HEY JD, This is Rumans here :wave:")
    st.title("HERE IS THE TASK YOU ASKED FOR!!!")
    st.write("The topic is all about the sky - MY favourite")
    st.write("[Fav view >](https://i.pinimg.com/originals/26/61/61/266161e3d17e989b4cd3a930d75bf171.jpg)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Why its my favourite")
        st.write("##")
        st.write(
            """
           Firstly I choose this one because this relates a lot to us as we mostly stand idle and see the sky in the station. 
           Here I just want to share a few incidents related to it.
           

When I started to come to the office I was like randomly doing something and leaving at 5.30 sharp but even though I went fast, I mostly missed the train. so that time all I do is go and stand near near the spot. I was nearly shocked when I saw you went directly to the spot because even though many people come there, that particular place is always empty. The view from that sky never fails to amuse me the same goes for Central, What a place it is!!! 

The place which view gives peace and the best view everywhere as we'll only get the peace when we're alone and with a favorite person...
            """
        )
        st.write("[another glimpse of view>](https://i.pinimg.com/originals/bb/8b/8b/bb8b8b8bcc02d47dd48668337a85ae35.jpg)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

   