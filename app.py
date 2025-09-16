import streamlit as st

# Import modular components
from components.header import (
    configure_page,
    render_sidebar,
    hide_streamlit_elements
)
from components.hero import  render_welcome_section
from components.upload_section import render_upload_section
from components.configuration_section import render_configuration_section
from components.voice_cloning_section import render_voice_cloning_section
from components.results_section import render_results_section, render_footer
from components.styles import load_css

def initialize_session_state():
    """Initialize all session state variables"""
    session_defaults = {
        'pdf_text': "",
        'pdf_pages': 0,
        'original_audio': None,
        'voice_audio': None,
        'api_key': "",
        'voice_uuid': "",
        'cloned_audio': None,
        'current_step': 1
    }

    for key, default_value in session_defaults.items():
        if key not in st.session_state:
            st.session_state[key] = default_value

def render_main_content(current_section: str):
    """Render main application content based on navigation section"""
    # Always show hero section

    # Render content based on selected section
    if current_section == "home":
        render_welcome_section()

    elif current_section == "upload":
        st.markdown("## Upload PDF")
        uploaded_pdf = render_upload_section()

    elif current_section == "config":
        st.markdown("## Configuration")
        if st.session_state.get('pdf_text'):
            render_configuration_section()
        else:
            st.info("Please upload a PDF first to access configuration options.")
            if st.button("Go to Upload Section", type="primary"):
                st.session_state.current_section = "upload"
                st.rerun()

    elif current_section == "voice":
        st.markdown("## Voice Cloning")
        if st.session_state.get('original_audio'):
            render_voice_cloning_section()
        else:
            st.info("Please generate TTS audio first to access voice cloning.")
            if st.button("Go to Configuration", type="primary"):
                st.session_state.current_section = "config"
                st.rerun()

    elif current_section == "results":
        st.markdown("## Results")
        if st.session_state.get('cloned_audio'):
            render_results_section()
        else:
            st.info("Please complete voice cloning first to view results.")
            if st.button("Go to Voice Cloning", type="primary"):
                st.session_state.current_section = "voice"
                st.rerun()

def main():
    """Main application function with improved structure"""
    # Configure page settings
    configure_page()

    # Load custom CSS
    load_css()

    # Initialize session state
    initialize_session_state()

    # Hide Streamlit default elements
    hide_streamlit_elements()

    # Render sidebar navigation and get current section
    current_section = render_sidebar()

    
    # Render main content based on navigation
    render_main_content(current_section)

    # Render footer
    render_footer()

if __name__ == "__main__":
    main()







