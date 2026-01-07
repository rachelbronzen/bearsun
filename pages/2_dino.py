import streamlit as st
import time
import random
import os

# --- CONFIG PAGE ---
st.set_page_config(page_title="Dino's Lair", page_icon="🎱", layout="centered")

# --- CSS STYLING (FIX WARNA ATAS) ---
st.markdown("""
    <style>
    /* 1. Background Gradient Hijau Sage */
    .stApp {
        background: rgb(240, 255, 240);
        background: linear-gradient(135deg, #e0eee0 0%, #8fbc8f 100%);
        background-attachment: fixed;
    }

    /* 2. FIX PENTING: MENGUBAH WARNA TOP BAR (HEADER) JADI TRANSPARAN */
    /* Ini yang bikin warna Pink di atas hilang */
    header[data-testid="stHeader"] {
        background-color: transparent !important;
        background: none !important;
    }

    /* 3. HILANGKAN SIDEBAR & MENU NAVIGASI */
    [data-testid="stSidebarNav"] { display: none !important; }
    [data-testid="stSidebar"] { display: none !important; }
    
    /* 4. Style Input Box (Nuansa Hijau) */
    .stTextInput > div > div > input {
        background-color: rgba(255, 255, 255, 0.9); 
        color: #2f4f4f;
        border-radius: 10px;
        border: 2px solid #556b2f; 
        padding: 10px;
    }
    
    /* 5. Container Transparan */
    .stContainer, .css-1r6slb0 {
        background-color: rgba(255,255,255,0.5);
        border-radius: 15px;
        padding: 15px;
        border: 1px solid #556b2f;
    }

    /* 6. LOGIKA TOMBOL (BUTTON STYLES) */
    div.stButton > button {
        background-color: #2f4f4f; 
        color: white; 
        border-radius: 5px; 
        padding: 10px 25px; 
        border: 2px solid #2f4f4f; 
        font-family: 'Courier New', monospace; 
        font-weight: bold;
        transition: all 0.2s ease-in-out;
    }
    
    div.stButton > button:hover {
        background-color: #556b2f; 
        border-color: #556b2f;
        transform: scale(1.05); 
        color: white;
    }

    div.stButton > button:active, div.stButton > button:focus {
        background-color: #98fb98 !important; 
        color: #006400 !important;            
        border-color: #006400 !important;     
        box-shadow: 0 0 15px rgba(0, 255, 0, 0.5); 
    }
    </style>
    """, unsafe_allow_html=True)

# --- FUNGSI LOAD & SAVE BUCKET LIST ---
FILE_BUCKET = "bucket_list.txt"

def get_bucket_list():
    if not os.path.exists(FILE_BUCKET):
        return [] # Kalau file belum ada, kembalikan list kosong
    with open(FILE_BUCKET, "r") as f:
        # Baca per baris dan hapus spasi/enter
        items = [line.strip() for line in f.readlines()]
    return [i for i in items if i] # Bersihkan baris kosong

def add_item(item):
    with open(FILE_BUCKET, "a") as f: # Mode 'a' untuk append (nambah)
        f.write(f"{item}\n")

def delete_items(items_to_delete):
    current_list = get_bucket_list()
    # Buat list baru yang TIDAK mengandung item yg mau dihapus
    new_list = [item for item in current_list if item not in items_to_delete]
    
    # Tulis ulang file dengan list baru
    with open(FILE_BUCKET, "w") as f:
        for item in new_list:
            f.write(f"{item}\n")

# --- HEADER ---
st.title("🎱 Dino's Command Center")
st.write("System Online. Welcome back, Agent Brenden.")
st.markdown("---")

# --- FITUR INTERAKTIF (TABS) ---
tab1, tab2, tab3, tab4 = st.tabs(["🦖 Stats", "🎱 Magic 8-Ball", "🔓 The Vault", "✈️ Travel Log"])

# === TAB 1: PLAYER STATS ===
with tab1:
    c1, c2 = st.columns([1, 2])
    with c1:
        # Avatar Dino
        st.image("image/bren_cartoon2.png", caption="Agent Dino", width=150)
        
    with c2:
        st.subheader("Player Profile")
        with st.container():
            st.write("**Codename:** Brenden💚")
            st.write("**Love Language:** Physical Touch")
            st.write("**Comfort Food:** Mie")
            
            # Pake expander buat detail biar ga penuh
            with st.expander("See More Details 🧐"):
                st.write("**Fav Activity:** Billiard and Board Games")
                st.write("**Fav Movie:** Pacific Rim")
                st.write("**Game:** Dota 2")
                st.write("**What Feels like home:** ranjang and rachel")
        
        st.write("") # Spacer

        c3, c4 = st.columns(2)
        with c3:
            st.error("**Red Flag:**\nsulit menjaga badan sendiri")
            st.warning("**Worst Habit:**\nga cuci muka")
        with c4:
            st.success("**Green Flag:**\naddicted to giving gifts")
            st.info("**Talent:**\nNjago nyetir 1 tangan")

    st.subheader("Skill Tree")
    st.write("")
    st.write("🦖 Roaring Ability + Ngomong Kekerasen")
    st.progress(95)
    st.write("💻 IT Knowledge")
    st.progress(85)
    st.write("🎱 Billiard Accuracy")
    st.progress(70)
    st.write("❤️ Love for Rachel")
    st.progress(100)

# === TAB 2: MAGIC 8-BALL ===
with tab2:
    st.subheader("🎱 The Oracle Ball")
    st.write("Got a yes/no question? Ask the 8-Ball.")
    
    question = st.text_input("Ask your question here:", placeholder="Will I win my Billiard Match?")
    
    if st.button("Shake the 8-Ball"):
        if question:
            with st.spinner("Ball is rolling..."):
                time.sleep(1.5)
            
            answers = ["It is certain.", "Without a doubt.", "Yes - definitely.", "Outlook good.", "Ask Rachel first.", "My sources say no.", "Very doubtful.", "The Dino says YES!"]
            result = random.choice(answers)
            
            st.markdown(f"""
            <div style='text-align: center; margin-top: 20px;'>
                <div style='background-color: black; color: white; width: 100px; height: 100px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto; box-shadow: 5px 5px 15px rgba(0,0,0,0.3);'>
                    <span style='font-size: 40px;'>8</span>
                </div>
                <h2 style='color: #2f4f4f; margin-top: 15px;'>{result}</h2>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.warning("You must ask a question first!")

# === TAB 3: THE VAULT ===
with tab3:
    st.subheader("🔓 Decrypt The Message")
    st.write("Rachel left a locked message for you.")
    code_attempt = st.text_input("Enter Passcode:", type="password")
    
    if st.button("Decrypt Data"):
        if code_attempt == "160225": 
            st.balloons()
            st.success("ACCESS GRANTED.")
            time.sleep(1)
            st.markdown("""
            ### 💌 Incoming Transmission:
            *Hai Brenden sayang!* Thank you for being the best person I met in my life.  
            Semangat di Taiwan sayaaang. Jangan lupa jaga kesehatan dan makannya yg teratur hayooo.
            *Love, Bearsun.* 🐻
            """)
        elif code_attempt == "":
            st.warning("Input is empty.")
        else:
            st.error("ACCESS DENIED.")

# === TAB 4: TRAVEL LOG ===
with tab4:
    st.subheader("✈️ Our Bucket List")
    st.write("What's next on ur adventure list? Add your dreams below!")
    
    current_items = get_bucket_list()
    
    if not current_items:
        st.info("Bucket list is empty. Start dreaming! ✨")
    else:
        # Tampilkan dalam kolom biar rapi (mirip code kamu sebelumnya)
        for i, item in enumerate(current_items):
            # Kita pakai checkbox biar ada kesan "Checklist"
            # Tapi checkbox ini cuma visual, tidak menghapus permanen
            st.checkbox(f"{item}", key=f"item_{i}")

    st.write("---")
    
    # 2. TAMBAH ITEM BARU
    col_add1, col_add2 = st.columns([3, 1])
    with col_add1:
        new_dream = st.text_input("Tambah mimpi baru:", placeholder="Contoh: Go to Japan 🇯🇵", label_visibility="collapsed")
    with col_add2:
        if st.button("Add ➕", use_container_width=True):
            if new_dream:
                add_item(new_dream)
                st.success("Added!")
                time.sleep(0.5)
                st.rerun() # Refresh halaman biar muncul langsung
            else:
                st.warning("Isi dulu teksnya!")

    # 3. HAPUS ITEM (DELETE)
    with st.expander("🗑️ Manage / Delete List"):
        st.write("Pilih item yang mau dihapus:")
        # Multiselect memudahkan hapus banyak sekaligus
        selected_to_delete = st.multiselect("Select items:", current_items)
        
        if st.button("Delete This ❌"):
            if selected_to_delete:
                delete_items(selected_to_delete)
                st.success("Deleted!")
                time.sleep(0.5)
                st.rerun()
            else:
                st.warning("Pilih dulu yang mau dihapus.")

# --- TOMBOL KEMBALI ---
st.markdown("---")
if st.button("⬅️ Back"):
    st.switch_page("app.py")