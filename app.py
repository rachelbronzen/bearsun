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
    
    /* 1. Target Button Biasa (st.button) */
    div.stButton > button {
        background-color: #2f4f4f !important; 
        color: white !important; 
        border-radius: 15px;
        padding: 10px 20px; 
        border: none; 
        font-weight: bold;
        width: 100%;
        transition: all 0.2s;
    }

    /* 2. Target Link Button (st.link_button) - INI YANG BARU */
    div.stLinkButton > a {
        background-color: #2f4f4f !important; /* Samakan warna */
        color: white !important; 
        border-radius: 15px;
        padding: 10px 20px; 
        border: none; 
        font-weight: bold;
        width: 100%;
        display: flex;             /* Biar teks di tengah */
        justify-content: center;   /* Biar teks di tengah */
        align-items: center;       /* Biar teks di tengah */
        text-decoration: none;     /* Hilangkan garis bawah */
        transition: all 0.2s;
    }

    /* 3. Efek Hover untuk KEDUANYA */
    div.stButton > button:hover, div.stLinkButton > a:hover {
        background-color: #556b2f !important; /* Warna saat disentuh */
        color: white !important;
        transform: scale(1.05);
        border: none;
    }
    
    /* 4. Efek Klik (Active) */
    div.stButton > button:active, div.stLinkButton > a:active {
        background-color: #ff69b4 !important;
        transform: scale(0.95);
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
    col_rach, col_bren= st.columns(2)
    with col_rach:
        with st.container():
            st.markdown("<h3 style='text-align: center;'>🌸 Rach</h3>", unsafe_allow_html=True)
            st.info("bread, spaghetti, zoo")
            if st.button("Open Bearsun's Profile", use_container_width=True):
                st.switch_page("pages/1_bearsun.py")
    with col_bren:
        with st.container():
            st.markdown("<h3 style='text-align: center;'>🎱 Bren</h3>", unsafe_allow_html=True)
            st.success("billiard, board game, travel")
            if st.button("Open Dino's Profile", use_container_width=True):
                st.switch_page("pages/2_dino.py")
    
    col_envelope, col_100= st.columns(2)
    with col_envelope:
        with st.container():
            st.markdown("<h3 style='text-align: center;'>💌One-Year Commit</h3>", unsafe_allow_html=True)
            st.error("Happy 1st Anniversary Sayang!")
            st.link_button(
                label="Open the Secret Message", 
                url="https://bearsundino1st.my.canva.site/", 
                use_container_width=True
            )
    with col_100:
        with st.container():
            st.markdown("<h3 style='text-align: center;'>💖100 Reasons Why </h3>", unsafe_allow_html=True)
            st.warning("100 Reasons Why I love You")
            if st.button("Open the 100 Reasons Why", use_container_width=True):
                st.switch_page("pages/3_100.py")

    col_perjanjian, col_sps = st.columns(2)
    with col_perjanjian:
        with st.container():
            st.markdown("<h3 style='text-align: center;'>📜 Agreement</h3>", unsafe_allow_html=True)
            st.success("LDR Relationship Agreement")
            if st.button("Open the Agreement", use_container_width=True):
                st.switch_page("pages/5_perjanjian.py")
    with col_sps:
        with st.container():
            st.markdown("<h3 style='text-align: center;'>📊 Spreadsheet</h3>", unsafe_allow_html=True)
            st.info("Our Spreadsheet Data")
            st.link_button(
                label="Open the Spreadsheet", 
                url="https://docs.google.com/spreadsheets/d/1dOIdmiLQXz7pptv3EsNo8-t6OO3h6SMLfuHoDGbhEA8/edit?usp=sharing", 
                use_container_width=True
            )
    
    col_spotifylink, emptycol = st.columns([2,1])
    with col_spotifylink:
        with st.container():
            st.markdown("<h3 style='text-align: center;'>🎵 Our Song </h3>", unsafe_allow_html=True)
            st.warning("Songs That Describes How Rachel Feels in This Relationship")
            if st.button("Open the Playlist", use_container_width=True):
                st.switch_page("pages/7_song.py")

    #logout
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("---")
    col_logout_l, col_logout_m, col_logout_r = st.columns([1,2,1])
    with col_logout_m:
        if st.button("Lock the door🔐", use_container_width=True):
            st.session_state.authenticated = False
            st.rerun()