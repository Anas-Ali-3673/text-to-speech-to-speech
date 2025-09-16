import streamlit as st
from gtts import gTTS
from io import BytesIO

def text_to_mp3(text, lang="en"):
    """Convert text to MP3 using gTTS"""
    tts = gTTS(text=text, lang=lang)
    audio_buffer = BytesIO()
    tts.write_to_fp(audio_buffer)
    audio_buffer.seek(0)
    return audio_buffer.getvalue()

def render_configuration_section():
    """Render the text configuration and TTS generation section"""
    if 'pdf_text' not in st.session_state:
        return
    
    st.markdown('<div class="config-section">', unsafe_allow_html=True)
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("""
    ## <svg class="lucide-icon lucide-icon-lg" viewBox="0 0 24 24" style="vertical-align: middle; margin-right: 0.5rem;">
        <path d="M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0-.73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2z"/>
        <circle cx="12" cy="12" r="3"/>
    </svg>Configure Your Audio
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### <svg class="lucide-icon" viewBox="0 0 24 24" style="vertical-align: middle; margin-right: 0.5rem;">
            <path d="M3 3v18h18"/>
            <path d="m19 9-5 5-4-4-3 3"/>
        </svg>Text Length Selection
        """, unsafe_allow_html=True)
        text_options = {
            "First 500 characters": 500,
            "First 1000 characters": 1000,
            "First 2000 characters": 2000,
            "Full document": len(st.session_state.pdf_text)
        }
        
        selected_option = st.selectbox(
            "Choose how much text to convert:",
            list(text_options.keys()),
            help="Select the amount of text you want to convert to speech"
        )
        
        text_limit = text_options[selected_option]
        
        selected_text = st.session_state.pdf_text[:text_limit] if len(st.session_state.pdf_text) > text_limit else st.session_state.pdf_text
        st.markdown(f'<div class="info-message">📊 Will convert {len(selected_text)} characters to speech</div>', unsafe_allow_html=True)

    with col2:
        st.markdown("#### Generate Speech")
        if st.button("🔊 Convert PDF to Speech", type="primary"):
            with st.spinner("🎵 Converting text to speech..."):
                audio_bytes = text_to_mp3(selected_text)
                st.session_state.original_audio = audio_bytes
            st.markdown('<div class="success-message">🎉 Your PDF has been converted to speech!</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
