import streamlit as st
import random

# --- CONFIG PAGE ---
st.set_page_config(page_title="100 Reasons", page_icon="💖", layout="centered")

# --- CSS STYLING (Tema Pink Rachel) ---
st.markdown("""
    <style>
    /* Gradient Background */
    .stApp {
        background: rgb(255,228,225);
        background: linear-gradient(135deg, #facdd5 0%, #ffc0cb 100%);
        background-attachment: fixed;
    }

    /* Hilangkan Menu Navigasi Bawaan */
    [data-testid="stSidebarNav"] { display: none !important; }
    
    /* Container Kartu Alasan */
    .reason-card {
        background-color: rgba(255, 255, 255, 0.6);
        padding: 50px;
        border-radius: 20px;
        text-align: center;
        border: 2px solid white;
        box-shadow: 0 4px 15px rgba(255, 105, 180, 0.3);
        margin-bottom: 20px;
    }
    
    /* Tombol Style */
    div.stButton > button {
        background-color: #2f4f4f; color: white; border-radius: 25px;
        padding: 10px 20px; border: none; font-weight: bold;
        transition: all 0.2s;
        width: 100%;
    }
    div.stButton > button:hover {
        background-color: #556b2f; transform: scale(1.05);
    }
    div.stButton > button:active {
        background-color: #ff69b4 !important; transform: scale(0.95);
    }
    
    </style>
    """, unsafe_allow_html=True)

# --- DAFTAR 100 ALASAN (Isi sendiri sampai 100 ya!) ---
reasons = [
    "U like me! A lot! Yay!",
    "Kamu cina!",
    "Kamu lebih tinggi drpd aku ^^ Hoooraayy!!",
    "A for mata kuliah effort-in Rachel with 6 sks.",
    "Treat me like a pretty princess.",
    "Respects me.",
    "A smarty pants. Siapapun yg dapet jelek di kelas, pasti kamu dapet bagus. Emang cina kamu.",
    "Buy me sooo maanyyy gifts tiba-tiba.",
    "Hidupmu super terstruktur & well prepared. Keak kamu yg di awal cerita ini itu. Plan mu that semester. Magang, S2. Super hot. Keak, this is the man I am looking for. Aku mau yg kayak gini...",
    "Love bombing dari awal sampe sekarang '3'. Semoga di masa depan lebih love bombing",
    "Love doing so many things that makes him so cool. Jadi warga ITS TV, jadi PO sch, jadi wakahima, jadi pacarku, magang + TA + dating me in one time",
    "BISA LULUS 3,5 TAHUN. Padahal so many crazy things happened.",
    "Protecting me in every way.",
    "Kalo I'm sad, aku nangis, kamu jadi ikut sedih kok aku nangis. Lucuu, makasih udah berusaha biar aku ga nangis. Tapi kadang kamu kayak seneng kalo aku nangis?",
    "U are very strong. Strong in every way. Bukan strong fisik ajah. So hot 🤤",
    "Kalo ngomong sangat runtut, terstruktur. Sukak persuasive, teguh sama pendapatmu. Super sexy",
    "Not like the other man. Put me first in every way. 100 buat mata kuliah mencintai Rachel",
    "Gak main-main sama aku. Kamu pacaran sama aku and u treat me so well. U prepared for the next step after pacaran. Well prepared, terstruktur. Soo...",
    "U treat me reaalllyyy well.",
    "I like it when we selesai jalan jalan, trus kita ke rumahku and then kita pelukan, kissing each other.",
    "I like it when u touch me, ternyata ada ya yg so obsessed with me",
    "The way u talk to ur friends, kayak kamu hate them all tapi kamu love them all juga, cara ngomongmu aja yg suka menghina orang lain.",
    "After that, kamu talk to me softly, hati hello kitty. Listens to me very well, cium, pukpuk kepala ku etc.",
    "Ur clever idea. Yang aku ga pernah kepikiran.",
    "Kamu masih bisa sayang aku dikala diterpa so many things yg stressfull",
    "Memperkenalkan aku ke dunia luar yang amazed me. Pergi makan ini itu, ke places u like, belajar billiard, main board game, belajar mahjong, etc.",
    "Ajarin aku new things. IT things, Billiard, dkk",
    "Suggest me to try new things, rok, dress. Then I start to like it.",
    "Telling me things apa aja yg kamu suka. Jadi I could recreate it and do the things u like. Well sometimes aku gamau si. Keak pake shapewear, stocking. Looks nice si benernya on me",
    "Ur smile when u with me. Aku gapernah liat smile mu yg lucu and happy banget before u with me ataupun pas kamu lagi sama temen temenmu.",
    "Ur plan with me yang super adventurous.",
    "Making me super comfortable",
    "How hard u work",
    "Ur perut",
    "U never give up",
    "Tells me everythinggg and ask my pendapat, I feel loved and trusted",
    "How we can grow our relationship together.",
    "Ur personality. It's perfect for me. Charming, enjoyable, and turn me on.",
    "U make me feel safe when I'm around you.",
    "Because you make me feel safe.",
    "Because you have the cutest smile.",
    "Because you support my coding hobby.",
    "Because you love pizza as much as I do.",
    "Because you always know how to cheer me up.",
    "Because even your silence is comfortable.",
    "Because you are my best player 2.",
    "Because you handle my overthinking with patience.",
    "Because you are hardworking and ambitious.",
    "Because simply... you are YOU.",
]

# --- SESSION STATE (Untuk navigasi Next/Prev) ---
if 'current_reason' not in st.session_state:
    st.session_state.current_reason = 0

# Fungsi Navigasi
def next_reason():
    if st.session_state.current_reason < len(reasons) - 1:
        st.session_state.current_reason += 1
    else:
        st.session_state.current_reason = 0 # Balik ke awal

def prev_reason():
    if st.session_state.current_reason > 0:
        st.session_state.current_reason -= 1

def random_reason():
    st.session_state.current_reason = random.randint(0, len(reasons) - 1)

# --- HEADER ---
st.title("💖 100 Reasons Why I Love You")
st.write("Click 'Next' to see why >~<")
st.markdown("---")

# --- LAYOUT TABS ---
tab1, tab2 = st.tabs(["💌 One by One", "📜 The Full List"])

# === TAB 1: ONE BY ONE (CARD VIEW) ===
with tab1:
    # Spacer
    st.write("")
    
    # Menampilkan Nomor Alasan
    index = st.session_state.current_reason
    st.caption(f"Reason #{index + 1} of {len(reasons)}")
    
    # Tampilan Kartu (HTML Custom biar cantik)
    st.markdown(f"""
    <div class="reason-card">
        <h2 style='color: #2f4f4f; font-family: sans-serif;'>“{reasons[index]}”</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Tombol Navigasi
    col_prev, col_rand, col_next = st.columns([1, 1, 1])
    
    with col_prev:
        if st.button("⬅️ Previous"):
            prev_reason()
            st.rerun()
            
    with col_rand:
        if st.button("🎲 Random"):
            random_reason()
            st.rerun()
            
    with col_next:
        if st.button("Next ➡️"):
            next_reason()
            st.rerun()
            
    # Progress Bar biar tau udah baca berapa persen
    progress = (index + 1) / len(reasons)
    st.progress(progress)

# === TAB 2: FULL LIST (DAFTAR SEMUA) ===
with tab2:
    st.subheader("📜 All 100 Reasons")
    st.write("Here is the complete list, written with all my heart.")
    
    # Tampilkan dalam list yang bisa di-scroll
    with st.container(height=500): # height=500 bikin dia punya scrollbar sendiri
        for i, r in enumerate(reasons):
            st.markdown(f"**{i+1}.** {r}")
            st.markdown("<hr style='margin: 5px 0; opacity: 0.3;'>", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("---")
if st.button("⬅️ Back to Home"):
    st.switch_page("app.py") # Sesuaikan dengan nama file Home kamu