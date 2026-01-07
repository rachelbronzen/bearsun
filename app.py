import streamlit as st
import time

#judul di tab browser & icon
st.set_page_config(
    page_title="Bearsun's Hidden Room",
    page_icon="🐻",
    layout="centered"
)

st.markdown("""
    <style>
    /* Gradient Background */
    .stApp {
        background: rgb(255,228,225);
        background: linear-gradient(135deg, #facdd5 0%, #ffc0cb 100%);
        background-attachment: fixed;
    }

    /* --- HILANGKAN MENU NAVIGASI BAWAAN --- */
    [data-testid="stSidebarNav"] {
        display: none;
    }
    
    /* Input Box Style */
    .stTextInput > div > div > input {
        background-color: rgba(255, 255, 255, 0.8); 
        color: #2f4f4f;
        border-radius: 15px;
        border: 2px solid #fff;
        padding: 10px;
    }
    
    /* --- LOGIKA TOMBOL (BUTTON STYLES) --- */
    
    /* 1. KONDISI NORMAL (Hijau Brenden) */
    div.stButton > button {
        background-color: #2f4f4f; 
        color: white;              
        border-radius: 25px;
        padding: 10px 25px;
        border: 2px solid #2f4f4f; 
        font-weight: bold;
        transition: all 0.2s ease-in-out;
    }
    
    /* 2. KONDISI HOVER (Saat mouse nempel - Hijau Terang) */
    div.stButton > button:hover {
        background-color: #556b2f; 
        border-color: #556b2f;
        transform: scale(1.05); 
        color: white;
    }

    /* 3. KONDISI DIPENCET/ACTIVE (Jadi Pink Rachel) */
    div.stButton > button:active, 
    div.stButton > button:focus, 
    div.stButton > button:focus-visible {
        background-color: #ffc0cb !important; /* Pink Pastel */
        color: #2f4f4f !important;            /* Teks jadi Hijau Gelap */
        border-color: #ffc0cb !important;     
        transform: scale(0.95);               
        box-shadow: 0 0 15px rgba(255, 192, 203, 0.8); /* Efek GLOW PINK */
        outline: none;
    }
    
    /* Box Info & Success custom */
    div[data-testid="stAlert"] {
        border-radius: 15px;
        opacity: 0.9;
    }
    </style>
    """, unsafe_allow_html=True)

#website harus inget apakah user sudah login atau belum.
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

#KONDISI A: Belum Login
if not st.session_state.authenticated:
    st.markdown("<br><br>", unsafe_allow_html=True) # Spacer
    st.markdown("<h1 style='text-align: center; font-size: 70px;'>🐻</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: #2f4f4f;'>WAIT A MINUTE!</h1>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown("<p style='text-align: center; font-size: 18px;'>What brings u here? This is a restricted area!!!!</p>", unsafe_allow_html=True)
        st.write("")
    #input password
    codename = st.text_input("Hold up! Password check first✋", type="password")
    
    col1, col2, col3 = st.columns([1,1,1])
    with col2: #tombol ditaruh di tengah
        if st.button("Unlock Access"):
            with st.spinner('Scanning identity... 🔍'):
                    time.sleep(1.5)
            if codename.lower() == st.secrets["general"]["main_password"]:
                st.balloons() 
                st.success("Access Granted. Wuaaaaaaaa haaii sayaaang ^^")
                time.sleep(2)
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Access denied. You’re not supposed to be here🚨")

#KONDISI B: Sudah Login
else:
    st.snow()
    st.title("Bearsun's Hidden Place 🐻")
    st.markdown("""
    <div style='background-color: rgba(255,255,255,0.6); padding: 20px; border-radius: 15px; margin-bottom: 20px;'>
        Haaai 🫶 Welcome <b>Mr Indominus Rex🦖</b> glad you made it back here. Enjoy ur time!
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    
    #navigasi ke page lain
    col_rachel, col_brenden= st.columns(2)
    with col_rachel:
        with st.container():
            st.markdown("<h3 style='text-align: center;'>🌸 Rachel</h3>", unsafe_allow_html=True)
            st.info("bread, spaghetti, zoo")
            if st.button("Open Bearsun's Profile", use_container_width=True):
                st.switch_page("pages/1_bearsun.py")
    with col_brenden:
        with st.container():
            st.markdown("<h3 style='text-align: center;'>🎱 Brenden</h3>", unsafe_allow_html=True)
            st.success("billiard, board game, travel")
            if st.button("Open Dino's Profile", use_container_width=True):
                st.switch_page("pages/2_dino.py")
    
    col_100, col_empty= st.columns([2,1])
    with col_100:
        with st.container():
            st.markdown("<h3 style='text-align: center;'>💖 100 Reasons Why </h3>", unsafe_allow_html=True)
            st.error("100 Reasons Why I love You")
            if st.button("Open the 100 Reasons Why", use_container_width=True):
                st.switch_page("pages/3_100.py")

    #logout
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("---")
    col_logout_l, col_logout_m, col_logout_r = st.columns([1,2,1])
    with col_logout_m:
        if st.button("Lock the door🔐", use_container_width=True):
            st.session_state.authenticated = False
            st.rerun()