import streamlit as st 
import time 
import random 
st.markdown("""
    <style>
    /* Background Image */
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1462331940025-496dfbfc7564?ixlib=rb-4.0.3&auto=format&fit=crop&w=2048&q=80");
        background-size: cover;
        background-attachment: fixed;
    }

    /* Glassmorphism card effect */
    .main-container {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 40px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        color: white;
    }

    h1 {
        color: #FFFFFF;
        text-shadow: 2px 2px 10px #8a2be2;
        font-family: 'Trebuchet MS', sans-serif;
        text-align: center;
    }

    .subtitle {
        text-align: center;
        color: #E0E0E0;
        font-style: italic;
        margin-bottom: 30px;
    }

    .gift-box {
        background: rgba(138, 43, 226, 0.2);
        padding: 20px;
        border-radius: 15px;
        border: 1px dashed #BD93F9;
        text-align: center;
        font-size: 20px;
        font-weight: bold;
        margin-top: 20px;
    }
    
    /* Make labels white */
    .stSelectbox label, .stButton label {
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)
gifts = {
    "Song": [
        "🎵 You are like the 'Iktara' song to me", 
        "🎵 You are like 'Abhi na jao chod kar' to me"
    ],
    "Quote": [
        "✨ Some connections do not fade. They just orbit.",
        "✨ You handled this better than you think 💫"
    ]
}

st.set_page_config(page_title="emotional_dialysis",page_icon="🎀")

# st.markdown("<h1>Emotion Acknowledgement</h1>", unsafe_allow_html=True)
# st.markdown("<p class='subtitle'>For the friends who like clogging up</p>", unsafe_allow_html=True)
st.markdown("""
    <div style="text-align: center;">
        <h1 style="margin-bottom: 0;">Emotion Acknowledgement</h1>
        <p style="font-style: italic; color: #E0E0E0; margin-top: 5px;">
            For the friends who like clogging up
        </p>
    </div>
    <br>
""", unsafe_allow_html=True)

mood=st.selectbox(
    "Recent emotional atmosphere:",
    ["Choose💗", "Thunder", "cloudy", "Sunshine(gotta talk)"]
)
if mood=="Thunder":
    st.error("Turbulence detected.⚠️")
    st.write("I know I messed up. I am ready to stay low until you are ready🥺.")
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdmx6aTBueWtldDF1eWV0OWxrY3FwZ2tjdHQ4em1iazE1Y3lmZzVpdiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/98MaHVwJOmWMz4cz1K/giphy.gif", caption="Me right now...")
elif mood =="cloudy": 
    st.warning("☁️ Visibility is low.")
    st.write("I value our friendship more than anything. Can we navigate this together?")
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcnpudWR4ZmUxYTBvenN3NHBkNjlmbm5hZHRuYnViZngxazZnaDBiNSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/DEbcjhoX1zBTiXmr3M/giphy.gif",caption="it means i still have chance yee")

elif mood =="Sunshine(gotta talk)":
    st.success("🚀 Ayooo finallyyyyy!!!")
    gift=st.selectbox(
    "What type of gift you would like: ",
    ["choose", "Song","Quote"]
    )
    if gift in gifts:
        if st.button(f"✨ Open your {gift}"):
               # Progress Bar
                progress_text = "Preparing your gift..."
                my_bar = st.progress(0, text=progress_text)
                
                for percent_complete in range(100):
                    time.sleep(0.01)
                    my_bar.progress(percent_complete + 1)
                
                st.balloons()
                picked_gift = random.choice(gifts[gift])
                
                # Styled Gift Output
                st.markdown(f"""<div class='gift-box'>{picked_gift}</div>""", unsafe_allow_html=True)
    else:
        # Optional: Subtle hint to pick something
        st.warning("Please select a gift type above to unlock your surprise!")      

# st.markdown("</div>", unsafe_allow_html=True)
