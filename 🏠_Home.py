from streamlit import session_state as state
import streamlit as st
from PIL import Image
from pathlib import Path
import logging

st.set_page_config(
    page_title="Home | SMD 1.0 App",
    page_icon="🏠",
)

PATH = '.'
# PATH = Path(Path(__file__).resolve()).parent
# logger = logging.getLogger(__name__)

state['login'] = False
state['PATH'] = PATH

image = Image.open(f'{PATH}/data/images/logo_all.png')
st1, st2, st3 = st.columns(3)

with st2:
    st.image(image)

st.markdown('<h3 style=\'text-align:center;\'>Welcome to SMD 1.0! 👋</h3>', unsafe_allow_html=True)

st.markdown(
    """
    ### Want to learn more and purchase it?
    - Check out [SMD 1.0 Website] (https://github.com/erwin-ngitung/smd-1.0)
    - Jump into our [Documentation] (https://github.com/erwin-ngitung/smd-1.0)
    - Ask a question in our [Company] (corporate.secretary@medcoenergi.com)
    """
)
