import streamlit as st
import time
import random
import datetime
from PIL import Image

st.set_page_config(page_title="Bearsun's World", page_icon="🌸", layout="centered")

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
    
    /* 1. KONDISI NORMAL */
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

    /* 3. KONDISI DIPENCET/ACTIVE  */
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

st.title("🌸 Rach's World")
st.write("Welcome to the softest, calmest, adorably place on the internet. Grab a warm water and enjoy!")
st.markdown("---")

#FITUR INTERAKTIF MENGGUNAKAN TABS
tab1, tab2, tab3, tab4 = st.tabs(["🐻 Profile & Mood", "🧁 The Bakery Game", "💌 Secret Notes", "🎁 Secure ur Blind Box"])

#TAB 1 PROFILE & FEEDING BEARSUN ===
with tab1:
    col_img, col_desc = st.columns([1, 2])
    
    with col_img:
        st.image(
            "image/rachel_cartoon.png", 
            caption="Bearsun Mode", 
            width=150, 
            output_format='PNG' 
        )
            
    with col_desc:
        # --- BAGIAN INI SUDAH DIRAPIKAN ---
        st.subheader("About Bearsun")
        
        # Kita pakai container biar rapi
        with st.container():
            st.write("**Codename:** Rach 🎀")
            st.write("**Love Language:** Acts of Service & Quality Time")
            st.write("**Comfort Food:** Roti, Pizza, Spaghetti")
            
            # Pake expander buat detail biar ga penuh
            with st.expander("See More Details 🧐"):
                st.write("**Fav Activity:** Zoo, Movies, Date w/ Bren")
                st.write("**Fav Movie:** Mean girls, Bratz, Home Alone")
                st.write("**Game:** Hayday only 🌾")
                st.write("**Tired Mode:** Buy so many food then drink (Tizi maybe)")
        
        st.write("") # Spacer
        
        # Kolom khusus Red/Green Flag biar stand out
        c1, c2 = st.columns(2)
        with c1:
            st.error("**Red Flag:**\nOverthinking to an unnecessary things")
            st.warning("**Worst Habit:**\nScared to try new things")
        with c2:
            st.success("**Green Flag:**\nTerlalu baik ke semua orang ^^")
            st.info("**Talent:**\nCaring, Thoughtful, Adorably Pretty")

    st.write("---")
    st.subheader("🧸 Feed the Bear!")
    
    # Session State untuk menghitung Pizza
    if 'pizza_count' not in st.session_state:
        st.session_state.pizza_count = 0
        
    col_feed, col_stats = st.columns(2)
    
    with col_feed:
        if st.button("Give Pizza Slice 🍕"):
            st.session_state.pizza_count += 1
            st.balloons() # Efek balon tiap dikasih makan
            
    with col_stats:
        st.metric("Pizzas Eaten", f"{st.session_state.pizza_count} Slices")
        if st.session_state.pizza_count > 5:
            st.caption("*Burp! I'm full but keep 'em coming!*")


#TAB 2 MINI GAME (BAKERY)
with tab2:
    st.subheader("👩‍🍳 Let's Bake Something!")
    st.write("Choose your ingredients carefully...")
    
    col_ing1, col_ing2 = st.columns(2)
    with col_ing1:
        base = st.selectbox("Choose Base:", ["Flour & Sugar", "Love & Hugs", "Python Code", "Mystery Dough"])
    with col_ing2:
        topping = st.selectbox("Choose Topping:", ["Rainbow Sprinkles", "Spicy Jalapeno", "Extra Chocolate", "Bugs (Error 404)"])
        
    if st.button("Start Oven 🔥"):
        with st.spinner("Mixing ingredients... Baking... Smelling good..."):
            time.sleep(2) # Simulasi loading
            
        st.markdown("### The Result:")
        
        # Logika Hasil Masakan Lucu-lucuan
        if base == "Love & Hugs" and topping == "Rainbow Sprinkles":
            st.success("✨ You baked a **Perfect Pink Cupcake!** (Rach's Favorite)")
            st.image("https://placebear.com/300/200") # Gambar random bear
        elif "Python Code" in base or "Bugs" in topping:
            st.error("💥 Oh no! You baked a **Syntax Error Pie!** It tastes like stress.")
        elif topping == "Spicy Jalapeno":
            st.warning("🔥 Whoa! **Spicy Lava Cake.** Bren might like this one.")
        else:
            st.info(f"🍪 You baked a unique **{base} Cookie** with **{topping}**!")

#TAB 3: SECRET NOTES
with tab3:
    st.subheader("📝 Leave a note for Bearsun")
    note = st.text_area("Makaaaciii notenyaa sayaaanngg!", placeholder="Type here...")
    
    if st.button("Save to Memory"):
        if note:
            # 1. Ambil Waktu Sekarang
            waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # 2. Simpan ke File Text (Append Mode 'a')
            with open("rachel_secret_notes.txt", "a") as f:
                f.write(f"[{waktu}] {note}\n")
            
            st.toast("Message saved! 💾")
            st.success("Note has been sent to the Bearsun's Vault!")
        else:
            st.warning("Cannot save an empty mind!")

    # --- FITUR KHUSUS CODER ---
    with st.expander("🔐 Developer Access (Intip Pesan)"):
        password = st.text_input("Enter Admin Password:", type="password")
        if password == st.secrets["general"]["admin_password"]:
            try:
                with open("rachel_secret_notes.txt", "r") as f:
                    isi_pesan = f.read()
                    st.text_area("Isi File Notes:", isi_pesan, height=200)
            except FileNotFoundError:
                st.info("Belum ada pesan yang masuk.")

#TAB 4: BLIND GACHA
with tab4:
    st.subheader("🎁 Secure ur Blind Box!")
    st.write("Test your luck today. What will you get from Bearsun?")
    
    # --- LOGIKA COOLDOWN ---
    if 'next_roll_time' not in st.session_state:
        # Jika belum ada waktu roll, set ke waktu lampau biar bisa roll
        st.session_state.next_roll_time = datetime.datetime.now()

    current_time = datetime.datetime.now()
    
    # Cek apakah waktu sekarang MASIH KURANG dari waktu boleh roll
    if current_time < st.session_state.next_roll_time:
        # HITUNG SISA WAKTU
        diff = st.session_state.next_roll_time - current_time
        minutes_left = int(diff.total_seconds() / 60)
        seconds_left = int(diff.total_seconds() % 60)
        
        st.error(f"⏳ **COOLDOWN ACTIVE!**")
        st.write(f"Bearsun is restocking boxes... Please wait: **{minutes_left} min {seconds_left} sec**")
        st.button("🎲 ROLL THE FORTUNE (Locked)", disabled=True) # Tombol dimatikan
    
    else:
        # JIKA SUDAH BOLEH ROLL
        if st.button("🎲 ROLL THE FORTUNE", use_container_width=True):
            
            # --- SET WAKTU ROLL BERIKUTNYA (1 JAM DARI SEKARANG) ---
            st.session_state.next_roll_time = datetime.datetime.now() + datetime.timedelta(hours=1)
            
            items = [
                ("Common", "A love from Bearsun 💕"),
                ("Common", "A glass of water 🥤"),
                ("Common", "A virtual warm hug 🫂"),
                ("Common", "A high-five from Bearsun ✋"),
                ("Common", "A 'semangat!' sticker spam 🥺"),
                ("Common", "A quote to brighten your day 🌞"),
                ("Rare", "Slice of Pizza 🍕"),
                ("Rare", "A cute doodle from Bearsun 🎨"),
                ("Rare", "A personalized compliment 😊"),
                ("Rare", "One cute photo of Bearsun now 📸"),
                ("Rare", "A random voice note by request 🎤"),
                ("Legendary", "Big LOVE from Bearsun 💖"),
                ("Legendary", "Nonstop Photo Updates for 1 Day 📸✨"),
                ("Legendary", "Nonstop Life Updates for 1 Day 📝✨"),
                ("Mythical", "Bearsun would do whatever u wanted 🤯")
            ]
            
            progress_text = "Shaking the box..."
            my_bar = st.progress(0, text=progress_text)
            
            for percent_complete in range(100):
                time.sleep(0.015) 
                my_bar.progress(percent_complete + 1)
                if percent_complete == 30: my_bar.progress(percent_complete + 1, text="Hearing something inside...")
                if percent_complete == 60: my_bar.progress(percent_complete + 1, text="Almost open...")
                if percent_complete == 90: my_bar.progress(percent_complete + 1, text="HERE IT COMES!")

            my_bar.empty()
                
            rarity, item = random.choice(items)
            
            st.markdown("---")
            
            if rarity == "Common":
                color = "#a9a9a9" 
                st.snow()
            elif rarity == "Rare":
                color = "#1e90ff" 
                st.snow()
            elif rarity == "Legendary":
                color = "#ffd700" 
                st.balloons() 
            else: # Mythical
                color = "#ff00ff" 
                st.balloons()
                
            st.markdown(f"<h3 style='text-align: center; color: {color};'>✨ {rarity.upper()} DROP! ✨</h3>", unsafe_allow_html=True)
            st.markdown(f"<h1 style='text-align: center; font-size: 50px; color: #2f4f4f;'>{item}</h1>", unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True) 
            
            st.warning("**SCREEN SHOT & KASIH KE BEARSUN YA BUAT DAPETIN HADIAH INI!** 📸", icon="⚠️")
            
            # Info cooldown muncul setelah roll
            st.caption("Next roll available in 1 hour.")

st.markdown("---")
if st.button("⬅️ Back"):
    st.switch_page("app.py")