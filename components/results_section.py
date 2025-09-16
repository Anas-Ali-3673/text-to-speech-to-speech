import streamlit as st

def render_results_section():
    """Render the results section with clean, professional design"""
    if not st.session_state.get('cloned_audio'):
        return

    # Professional Results Section
    st.markdown("""
    <div class="results-container">
        <div class="section-header">
            <h2 class="section-title">
                <span class="title-icon">
                    <svg class="lucide-icon lucide-icon-lg" viewBox="0 0 24 24">
                        <path d="M3 14h3a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-7a9 9 0 0 1 18 0v7a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3"/>
                    </svg>
                </span>
                Audio Generation Complete
            </h2>
            <p class="section-description">Your personalized voice transformation is ready for download</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Audio comparison cards
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
        <div class="audio-card">
            <div class="card-header">
                <h3 class="card-title">
                    <span class="card-icon">
                        <svg class="lucide-icon" viewBox="0 0 24 24">
                            <circle cx="12" cy="12" r="10"/>
                            <polygon points="10,8 16,12 10,16"/>
                        </svg>
                    </span>
                    Original TTS Audio
                </h3>
                <p class="card-subtitle">Standard text-to-speech conversion</p>
            </div>
        """, unsafe_allow_html=True)

        st.audio(st.session_state.original_audio, format='audio/mp3')

        st.download_button(
            label="📥 Download Original",
            data=st.session_state.original_audio,
            file_name="original_tts.mp3",
            mime="audio/mp3",
            key="download_original",
            use_container_width=True
        )

        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="audio-card">
            <div class="card-header">
                <h3 class="card-title">
                    <span class="card-icon">
                        <svg class="lucide-icon" viewBox="0 0 24 24">
                            <path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"/>
                            <path d="M19 10v2a7 7 0 0 1-14 0v-2"/>
                            <line x1="12" x2="12" y1="19" y2="22"/>
                            <line x1="8" x2="16" y1="22" y2="22"/>
                        </svg>
                    </span>
                    Voice Cloned Audio
                </h3>
                <p class="card-subtitle">AI-powered voice transformation</p>
            </div>
        """, unsafe_allow_html=True)

        st.audio(st.session_state.cloned_audio, format='audio/mp3')

        st.download_button(
            label="Download Clone",
            data=st.session_state.cloned_audio,
            file_name="voice_cloned.mp3",
            mime="audio/mp3",
            key="download_clone",
            use_container_width=True,
            type="primary"
        )

        st.markdown("</div>", unsafe_allow_html=True)

    # Success message and next steps
    st.success(" Voice cloning completed successfully!")

    st.info("""
    **Next Steps:**
    - Download your audio files using the buttons above
    - Try generating another voice clone with different settings
    - Share your results with others
    """)

def render_footer():
    """Render clean application footer"""
    st.markdown("""
    <div class="app-footer">
        <div class="footer-content">
            <p class="footer-text">
                <strong>PDF to Voice Clone</strong> - Powered by Streamlit and Resemble AI
            </p>
            <p class="footer-subtext">
                Transform your documents into personalized audio experiences
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_footer():
    """Render the application footer"""
    st.markdown("""
    <div class="footer">
        <div class="footer-content">
            <p>Powered by Streamlit and Resemble AI</p>
            <p>Convert your documents into custom voice audio easily</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
