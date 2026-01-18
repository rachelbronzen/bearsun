import streamlit as st
import random
import time

# --- CONFIG PAGE ---
st.set_page_config(page_title="100 Reasons", page_icon="💖", layout="centered")

# --- CSS STYLING (THEMA: PATRICK HAND & QUICKSAND) ---
st.markdown("""
    <style>
    /* 1. IMPORT FONT */
    @import url('https://fonts.googleapis.com/css2?family=Patrick+Hand&family=Quicksand:wght@400;600;700&display=swap');

    /* 2. BACKGROUND & FONT UTAMA (Quicksand biar bersih) */
    .stApp {
        background: linear-gradient(135deg, #fff0f5 0%, #ffc0cb 100%);
        background-attachment: fixed;
        font-family: 'Quicksand', sans-serif;
    }

    /* Hilangkan Menu Navigasi Bawaan */
    [data-testid="stSidebarNav"] { display: none !important; }
    
    /* 3. JUDUL (H1, H2, H3) -> Pakai Patrick Hand biar lucu */
    h1, h2, h3 {
        font-family: 'Patrick Hand', cursive !important;
        color: #d63384;
    }

    /* 4. CONTAINER KARTU ALASAN (ANIMASI FLOAT) */
    .reason-card {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 40px;
        border-radius: 20px;
        text-align: center;
        border: 4px solid #fff;
        box-shadow: 0 10px 25px rgba(255, 105, 180, 0.2);
        margin-bottom: 20px;
        animation: float 3s ease-in-out infinite;
    }

    /* 5. FONT KHUSUS QUOTE DI KARTU -> Patrick Hand */
    .quote-text {
        color: #d63384; 
        font-family: 'Patrick Hand', cursive !important;
        font-size: 32px; /* Ukuran besar biar jelas */
        line-height: 1.4;
    }

    /* Animasi Melayang */
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }
    
    /* 6. TOMBOL STYLE (Quicksand Bold) */
    div.stButton > button {
        background-color: #2f4f4f; color: white; border-radius: 25px;
        padding: 10px 20px; border: none; font-weight: bold;
        transition: all 0.2s;
        width: 100%;
        font-family: 'Quicksand', sans-serif;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    div.stButton > button:hover {
        background-color: #556b2f; transform: scale(1.05);
    }
    div.stButton > button:active {
        background-color: #ff69b4 !important; transform: scale(0.95);
    }
    
    /* Custom Progress Bar Color */
    .stProgress > div > div > div > div {
        background-color: #d63384;
    }
    
    </style>
    """, unsafe_allow_html=True)

# --- DATA LIST (Data Lengkap Kamu) ---
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
    "When our minds sync. Pas liat kelinci langsung bilang, sate. At the same time and same second.",
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
    "How hard u work and u never give up",
    "Ur perut",
    "Tells me everythinggg and ask my pendapat, I feel loved and trusted",
    "How we can grow our relationship together.",
    "Ur personality. It's perfect for me. Charming, enjoyable, and turn me on.",
    "U make me feel safe when I'm around you.",
    "Kamu mau belajar maaf. I know pas dulu di awal kamu susah banget maaf atau merasa bersalah atau kamu juga malah marah balik kalo aku lagi bad mood",
    "You do so many things for me without me asking.",
    "Kamu remember small things about me.",
    "You always try to make me happy.",
    "Gives the best hug. Maybe soalnya aku cuman hug u.",
    "Always there and support me when I'm sad or stressed.",
    "Can read my mind.",
    "When u said, trs aku inget kalo, gapapa deh yg penting pacarku rachel. ga semua orang bisa dapet pacar sewaw kamu",
    "Our freak vibes setara lah.",
    "Shares his tought and feelings with me.",
    "Likes Challenges",
    "Super confident.",
    "A great problem solver.",
    "My biggest cheerleader.",
    "Kamu perhatian juga ke my family and friends.",
    "The way u kiss me every where.",
    "Your hands when we held hands.",
    "Your eyes when you look at me.",
    "Always has my back.",
    "How clingy and loving you are to me. But not the others",
    "You know it when something is wrong with me.",
    "U let me come to your zone. Misal tanya ini itu, buka hapemu. And u doesn't mad at all.",
    "Rambutmu after keramas",
    "U always trust me, support me, babying me.",
    "Ur smell",
    "Dewasa",
    "U make me feel special",
    "Spoils me every time",
    "U do computer science just like me",
    "The way u compliment me",
    "ur attention",
    "ur voice that calms me down",
    "ur silliness",
    "ur height. a nice view for me",
    "ur sassiness",
    "our bond",
    "the way u protect me",
    "gentle, just when u're with me",
    "ur face when u tired",
    "how we stroll around surabaya and find something to eat",
    "how we dress up darling for each other",
    "us being goofy together",
    "how u light up my world",
    "ur FUNNY jokes",
    "ur snoring",
    "ur talent",
    "ur skills",
    "i love the way u obbsess over me",
    "the way u focus when u'r driving and I snuggle next to u",
    "when u drive me from anywhere to my home. I feel so princessy",
    "how much u taught me about life",
    "when u imitate me",
    "when u kilikitik aku",
    "when u secretly touch me in public",
    "when we are in ur room and u hold me tight",
    "when u buy me so many things padahal kamu juga harus nabung ke taiwan dkk",
    "u heal my pain",
    "u help me with many things apalagi kalo bingung matkul ini itu",
    "how we can go everywhere together pas kita masih di Surabaya",
    "ur existence",
    "I can see a long future with you.",
    "Because simply... you are YOU.",
]

# --- SESSION STATE ---
if 'current_reason' not in st.session_state:
    st.session_state.current_reason = 0

# --- FUNGSI LOGIKA ---
def next_reason():
    if st.session_state.current_reason < len(reasons) - 1:
        st.session_state.current_reason += 1
        pesan = ["Next reason!", "There's more...", "Wait for it...", "Love this one!"]
        st.toast(random.choice(pesan), icon="💖")
    else:
        st.session_state.current_reason = 0 
        st.toast("Back to start!", icon="🔄")

def prev_reason():
    if st.session_state.current_reason > 0:
        st.session_state.current_reason -= 1

def random_reason():
    st.session_state.current_reason = random.randint(0, len(reasons) - 1)
    st.toast("Spinning the wheel of love...", icon="🎲")

# --- MAIN PAGE ---
# Judul Pakai Patrick Hand
st.markdown("<h1 style='text-align: center;'>💖 100 Reasons Why 💖</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #555;'>Hi cutie >~< </p>", unsafe_allow_html=True)
st.write("") 

tab1, tab2 = st.tabs(["💌 The Flashcards", "📜 Full List"])

# === TAB 1: INTERACTIVE CARD ===
with tab1:
    index = st.session_state.current_reason
    total = len(reasons)
    
    # Milestone Effects
    if index == 0: st.balloons()
    elif index == 49: st.snow()
    elif index == total - 1: st.balloons()

    # Tampilan Kartu (Isi Quote pakai Patrick Hand)
    st.markdown(f"""
    <div class="reason-card">
        <div style="font-size: 14px; color: #888; margin-bottom: 10px; font-family: 'Quicksand', sans-serif;">
            REASON #{index + 1}
        </div>
        <div class="quote-text">
            “{reasons[index]}”
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns([1, 1, 1])
    with c1:
        if st.button("⬅️ Previous"):
            prev_reason()
            st.rerun()
    with c2:
        if st.button("🎲 Random"):
            random_reason()
            st.rerun()
    with c3:
        if st.button("Next ➡️"):
            next_reason()
            st.rerun()
            
    st.write("")
    progress = (index + 1) / total
    st.progress(progress)
    st.caption(f"Love Loading... {int(progress * 100)}%")

# === TAB 2: FULL LIST (ZEBRA STRIPING) ===
with tab2:
    st.subheader("📜 All The Reasons")
    st.write("Written with all my heart.")
    
    # Container Scroll
    with st.container(height=500):
        for i, r in enumerate(reasons):
            
            # WARNA SELANG-SELING (Zebra)
            # Genap: Putih Transparan | Ganjil: Pink Tipis
            bg_color = "rgba(255,255,255,0.7)" if i % 2 == 0 else "rgba(255, 192, 203, 0.3)"
            
            st.markdown(f"""
            <div style='
                background-color: {bg_color};
                padding: 15px;
                border-radius: 10px;
                margin-bottom: 8px;
                display: flex;
                align-items: center;
                border: 1px solid rgba(255,255,255,0.5);
                font-family: 'Quicksand', sans-serif; /* Pakai Quicksand biar kebaca jelas */
            '>
                <div style='
                    background-color: #d63384; 
                    color: white; 
                    width: 30px; 
                    height: 30px; 
                    border-radius: 50%; 
                    display: flex; 
                    justify-content: center; 
                    align-items: center;
                    font-weight: bold;
                    margin-right: 15px;
                    flex-shrink: 0;
                    font-family: 'Patrick Hand', cursive; /* Nomornya pakai Patrick Hand biar lucu */
                '>
                    {i+1}
                </div>
                <div style='color: #444; font-size: 16px; line-height: 1.5;'>
                    {r}
                </div>
            </div>
            """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<br><br>", unsafe_allow_html=True)
if st.button("⬅️ Back to Home"):
    st.switch_page("app.py")