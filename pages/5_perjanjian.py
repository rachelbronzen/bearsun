import streamlit as st
import datetime

# --- CONFIG PAGE ---
st.set_page_config(page_title="LDR Agreement", page_icon="⚖️", layout="centered")

# --- CSS STYLING (TEMA SURAT RESMI + TANDA TANGAN) ---
st.markdown("""
    <style>
    /* Import Font: Playfair (Judul), Merriweather (Isi), Great Vibes (Tanda Tangan) */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Merriweather:wght@300;400&family=Great+Vibes&display=swap');

    /* Background Aplikasi: KREM KERTAS BERSIH */
    .stApp {
        background-color: #fdfbf7;
        color: #1a1a1a;
    }

    /* Hilangkan Menu Bawaan */
    [data-testid="stSidebarNav"] { display: none !important; }

    /* Judul Utama */
    h1 {
        font-family: 'Playfair Display', serif !important;
        text-align: center;
        text-transform: uppercase;
        color: #1a1a1a;
        letter-spacing: 2px;
        border-bottom: 2px solid #b8860b; /* Garis Emas */
        padding-bottom: 20px;
        margin-bottom: 30px;
    }

    /* Sub-judul Pasal */
    h3 {
        font-family: 'Playfair Display', serif !important;
        color: #b8860b;
        margin-top: 20px;
        font-size: 18px;
        text-transform: uppercase;
        margin-bottom: 5px;
    }
    
    /* Teks Isi (Pasal) */
    p, li {
        font-family: 'Merriweather', serif !important;
        color: #333 !important;
        line-height: 1.6;
        font-size: 15px;
    }

    /* --- GAYA TANDA TANGAN (TULISAN SAMBUNG) --- */
    .signature-text {
        font-family: 'Great Vibes', cursive;
        font-size: 40px;
        color: #000;
        text-align: center;
        margin-bottom: -10px;
        margin-top: 10px;
    }

    .signature-line {
        border-top: 1px solid #333;
        margin-top: 5px;
        padding-top: 5px;
        text-align: center;
        font-family: 'Playfair Display', serif;
        font-size: 12px;
        font-weight: bold;
        letter-spacing: 1px;
    }

    /* --- TOMBOL BACK (PINK & JELAS) --- */
    div.stButton > button {
        background-color: #ffc0cb !important; /* Pink Pastel */
        color: #2f4f4f !important;            /* Teks Hijau Gelap (Jelas) */
        font-family: 'Playfair Display', serif;
        font-size: 16px;
        font-weight: bold;
        padding: 10px 30px;
        border-radius: 10px;
        border: 2px solid #ffc0cb;
        width: 100%;
        margin-top: 20px;
        transition: all 0.3s;
    }
    div.stButton > button:hover {
        background-color: #ff69b4 !important; /* Pink Lebih Tua pas Hover */
        border-color: #ff69b4 !important;
        color: white !important;
        transform: scale(1.02);
    }
    
    /* Cap Stempel (OFFICIAL) */
    .stamp-box {
        text-align: center;
        margin-top: 40px;
        margin-bottom: 20px;
    }
    .stamp {
        border: 4px double #c0392b; /* Merah Stempel */
        color: #c0392b;
        font-family: 'Courier New', courier, monospace;
        font-size: 24px;
        font-weight: 900;
        text-transform: uppercase;
        padding: 10px 30px;
        display: inline-block;
        transform: rotate(-8deg); /* Miring dikit biar real */
        border-radius: 8px;
        opacity: 0.8;
        letter-spacing: 2px;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER SURAT ---
st.markdown(f"""
    <h1>Relationship Agreement</h1>
    <p style='text-align: center; font-style: italic; color: #555; margin-top: -20px;'>
        Official Protocol for Long Distance Relationship (LDR)
    </p>
    <br>
    <p style="text-align: justify;">
        This agreement is legally binding. Both parties have mutually agreed to the following terms 
        to maintain the integrity, love, and sanity of this relationship forever.
    </p>
""", unsafe_allow_html=True)

# --- ISI PASAL (STATIC LIST) ---
st.write("---")

# Menggunakan Kolom biar rapi (Nomor Pasal di Kiri, Isi di Kanan)
def buat_pasal(nomor, judul, isi):
    c1, c2 = st.columns([0.15, 0.85])
    with c1:
        st.markdown(f"<h3 style='text-align:right; margin-top:0;'>{nomor}</h3>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"**{judul}**")
        st.caption(isi)

buat_pasal("I", "CONSTANT ATTENTION", "Selalu tanya 'lagi ngapain' all the time.")
st.write("")
buat_pasal("II", "VISUAL & AUDIO PROOF", "Wajib lebih sering nge-pap + ada suaranya. Contoh: video note.")
st.write("")
buat_pasal("III", "STATUS UPDATES", "Wajib kabarin kemana dan lagi ngapain.")
st.write("")
buat_pasal("IV", "PLANNING REPORT", "Di malem hari harus kasih tau next day plan ngapain aja.")
st.write("")
buat_pasal("V", "ABSENCE PROTOCOL", "Kalau ga bisa ngechat, ngomong kenapa. Jangan langsung ditinggal.")
st.write("")
buat_pasal("VI", "MANDATORY MEETING", "Setiap Jumat malem Video Call (minimal seminggu 1x)")
st.write("")
buat_pasal("VII", "SPECIAL OCCASION", "Kamu pulang Indo = Kita makan bareng (YES! LET'S GO. MAKAN APA KITA?)")

st.write("---")

# --- BAGIAN TANDA TANGAN & STEMPEL ---
st.markdown("<br>", unsafe_allow_html=True)

# 1. Tanda Tangan
col_a, col_b = st.columns(2)

with col_a:
    st.markdown("""
        <div class="signature-text">Rach</div>
        <div class="signature-line">SIGNED BY RACH<br><span style='font-weight:normal; font-size:10px;'>Party A</span></div>
    """, unsafe_allow_html=True)

with col_b:
    st.markdown("""
        <div class="signature-text">Bren</div>
        <div class="signature-line">SIGNED BY BREN<br><span style='font-weight:normal; font-size:10px;'>Party B</span></div>
    """, unsafe_allow_html=True)

# 2. Cap Stempel
st.markdown("""
    <div class="stamp-box">
        <div class="stamp">OFFICIALLY AGREED ❤️</div>
    </div>
""", unsafe_allow_html=True)

# --- FOOTER ---
st.write("<br>", unsafe_allow_html=True)
if st.button("⬅️ Back to Home"):
    st.switch_page("app.py")