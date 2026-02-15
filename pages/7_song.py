import streamlit as st
import streamlit.components.v1 as components
import random
import time

# --- CONFIG PAGE ---
st.set_page_config(page_title="Let's Jam In", page_icon="🎧", layout="centered")

# --- CSS STYLING (TEMA ROSE GOLD & DARK ESPRESSO) ---
st.markdown("""
    <style>
    /* Import Font Lucu (Fredoka) */
    @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@400;500;600;700&display=swap');

    /* Background Aplikasi: Dark Espresso */
    .stApp {
        background-color: #120302;
        color: #fcf4f4; 
        font-family: 'Fredoka', sans-serif;
    }

    /* --- MENGHILANGKAN BAR BAWAAN --- */
    [data-testid="stHeader"] {
        background-color: transparent !important;
    }
    header {
        background: transparent !important;
    }

    /* Hilangkan Menu Bawaan */
    [data-testid="stSidebarNav"] { display: none !important; }

    /* --- ANIMASI JUDUL MEMANTUL (BOUNCING) --- */
    h1 {
        font-family: 'Fredoka', sans-serif !important;
        color: #E5A9A9; /* Warna Rose Gold / Dusty Pink */
        text-align: center;
        animation: bounce 2s infinite;
        text-shadow: 0 0 15px rgba(229, 169, 169, 0.4);
        margin-bottom: 5px;
    }

    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% {transform: translateY(0);}
        40% {transform: translateY(-10px);}
        60% {transform: translateY(-5px);}
    }

    /* Subtitle / Teks Biasa */
    p {
        font-family: 'Fredoka', sans-serif !important;
        color: #D9C5C5; 
    }

    /* --- GAYA TABS (ROSE GOLD ELEGAN) --- */
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
        justify-content: center;
    }
    
    /* Gaya Default Tab (Kondisi Belum Dipencet) */
    .stTabs [data-baseweb="tab"] {
        background-color: #2a100f; 
        border-radius: 15px 15px 0 0;
        padding: 10px 30px;
        border: 1px solid transparent;
    }
    
    /* Paksa teks tab yang belum dipencet jadi warna agak gelap */
    .stTabs [data-baseweb="tab"] * {
        color: #8a6c6c !important; 
        font-family: 'Fredoka', sans-serif;
        font-weight: 600;
        transition: all 0.3s;
    }

    /* ✨ TAB 1 (SPOTIFY) - SAAT AKTIF */
    .stTabs [data-baseweb="tab-list"] button:nth-child(1)[aria-selected="true"] {
        background-color: #E5A9A9 !important; /* Rose Gold */
        box-shadow: 0 -5px 20px rgba(229, 169, 169, 0.3);
        border: 1px solid #E5A9A9 !important;
        border-bottom: 3px solid #E5A9A9 !important; /* Hancurkan garis hijau bawaan! */
    }
    
    /* PAKSA TEKS SPOTIFY JADI COKLAT GELAP SAAT AKTIF */
    .stTabs [data-baseweb="tab-list"] button:nth-child(1)[aria-selected="true"] * {
        color: #120302 !important; 
        font-weight: bold !important;
    }

    /* ✨ TAB 2 (YOUTUBE) - SAAT AKTIF */
    .stTabs [data-baseweb="tab-list"] button:nth-child(2)[aria-selected="true"] {
        background-color: #D49393 !important; /* Rose Gold Deep */
        box-shadow: 0 -5px 20px rgba(212, 147, 147, 0.3);
        border: 1px solid #D49393 !important;
        border-bottom: 3px solid #D49393 !important; /* Hancurkan garis merah bawaan! */
    }

    /* PAKSA TEKS YOUTUBE JADI COKLAT GELAP SAAT AKTIF */
    .stTabs [data-baseweb="tab-list"] button:nth-child(2)[aria-selected="true"] * {
        color: #120302 !important; 
        font-weight: bold !important;
    }

    /* --- KARTU MUSIK (EFEK GLOW SOFT ROSE GOLD) --- */
    .music-card {
        background-color: rgba(229, 169, 169, 0.05); /* Transparan Rose Gold */
        border-radius: 20px;
        padding: 20px;
        border: 2px solid #E5A9A9;
        box-shadow: 0 0 20px rgba(229, 169, 169, 0.15);
        text-align: center;
        transition: transform 0.3s ease;
        margin-bottom: 20px;
    }
    .music-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(229, 169, 169, 0.3);
    }

    /* ==========================================
       PERBAIKAN: GAYA TOMBOL INTERAKTIF 
       ========================================== */
    div.stButton > button {
        background-color: #120302 !important; 
        border-radius: 25px;
        border: 2px solid #E5A9A9 !important;
        width: 100%;
        transition: all 0.3s;
        padding: 10px 30px;
    }

    /* PAKSA TEKS TOMBOL MUNCUL & WARNA ROSE GOLD */
    div.stButton > button * {
        color: #E5A9A9 !important;            
        font-family: 'Fredoka', sans-serif !important;
        font-size: 18px !important;
        font-weight: bold !important;
        transition: all 0.3s;
    }

    div.stButton > button:hover {
        background-color: #E5A9A9 !important; 
        transform: scale(1.05);
        box-shadow: 0 0 15px rgba(229, 169, 169, 0.4);
    }

    /* PAKSA TEKS TOMBOL BERUBAH JADI COKLAT SAAT DI-HOVER */
    div.stButton > button:hover * {
        color: #120302 !important;
    }

    /* ==========================================
       PERBAIKAN: GAYA NOTIFIKASI TOAST (POP-UP)
       ========================================== */
    div[data-testid="stToast"] {
        background-color: #E5A9A9 !important; /* Kotaknya jadi Rose Gold */
        border-radius: 12px;
        border: 2px solid #D49393 !important;
        box-shadow: 0 5px 15px rgba(0,0,0,0.5);
    }

    /* PAKSA TEKS NOTIFIKASI JADI COKLAT & TERBACA JELAS */
    div[data-testid="stToast"] * {
        color: #120302 !important;
        font-family: 'Fredoka', sans-serif !important;
        font-size: 16px !important;
        font-weight: 600 !important;
    }
    
    </style>
""", unsafe_allow_html=True)
# =========================================================
# KODE EMBED
# =========================================================

# Kode Embed Spotify 
# (SAYA GANTI DENGAN LINK CONTOH YANG BISA JALAN BIAR GAK ABU-ABU)
# Nanti kamu tinggal ganti ID playlistnya (angka setelah tulisan /playlist/)
SPOTIFY_EMBED = """
<iframe style="border-radius:15px; box-shadow: 0 4px 15px rgba(0,0,0,0.5);" 
src="https://open.spotify.com/embed/playlist/3h7igZlC6ZOaNl5fGP9aFs?utm_source=generator" 
width="100%" height="400" frameBorder="0" allowfullscreen="" 
allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
"""

# Kode Embed YouTube Music
YOUTUBE_EMBED = """
<iframe style="border-radius:15px; box-shadow: 0 4px 15px rgba(0,0,0,0.5);" 
width="100%" height="400" 
src="https://www.youtube.com/embed/videoseries?list=PL1KdPXCFDioXQFx1o9BOF3VXoDRxyk7Nf" 
title="YouTube video player" frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
allowfullscreen></iframe>
"""
# =========================================================

# --- HEADER (JUDUL & SUBTITLE ROMANTIS) ---
st.markdown("<h1>🦖 Let's Jam In, My Dino ❤️</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Welcome to our playlist. Press play and let's listen to the songs that perfectly describe us and connect our hearts, even when we're miles apart. 🎶✨</p>", unsafe_allow_html=True)
st.write("")

# --- TABS INTERAKTIF ---
tab_spotify, tab_youtube = st.tabs(["🎧 Spotify", "🎸 YouTube Music"])

# TAB 1: SPOTIFY 
with tab_spotify:
    st.markdown("""
    <div class='music-card'>
        <h3 style='color: #E5A9A9; font-family: Fredoka; margin-bottom: 5px;'>Our Spotify Mix</h3>
        <p style='font-size: 14px; color: #D9C5C5; margin-top: 0;'>Our feelings translated into melodies.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Menampilkan Spotify
    components.html(SPOTIFY_EMBED, height=420)

# TAB 2: YOUTUBE MUSIC 
with tab_youtube:
    st.markdown("""
    <div class='music-card'>
        <h3 style='color: #E5A9A9; font-family: Fredoka; margin-bottom: 5px;'>Our YouTube Jamz</h3>
        <p style='font-size: 14px; color: #D9C5C5; margin-top: 0;'>Same love, different platform.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Menampilkan YouTube
    components.html(YOUTUBE_EMBED, height=420)

# --- FITUR FUN & INTERAKTIF ---
st.markdown("---")
st.write("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("❤️ FEEL THE RACHEL LOVE!"):
        # Efek romantis saat tombol diklik
        st.balloons()
        pesan_lucu = [
            "Distance means nothing when we jam together! 🎶❤️", 
            "Rawrrrr means I love you in dinosaur! 🦖✨", 
            "Our hearts beating to the same track... 🎧💖", 
            "Sending a big warm hug to you! 🤗❤️"
        ]
        st.toast(random.choice(pesan_lucu), icon="❤️")
        time.sleep(1)

# --- TOMBOL BACK ---
st.write("<br><br>", unsafe_allow_html=True)
if st.button("⬅️ Back to Home"):
    st.switch_page("app.py")