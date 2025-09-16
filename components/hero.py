import streamlit as st

def render_welcome_section():
    """Render welcome section using Streamlit native components"""
    
    # Create a container with custom background
    st.markdown("""
        <div style="
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 2rem;
            border-radius: 10px;
            margin: 1rem 0;
        ">
            <div style="
                background: white;
                padding: 2rem;
                border-radius: 8px;
                text-align: center;
            ">
                <h1 style="color: #2c3e50; margin-bottom: 1rem;"> Welcome to PDF Voice Clone</h1>
                <p style="color: #7f8c8d; font-size: 18px; margin-bottom: 2rem;">
                    Get started by navigating through the sidebar to upload your PDF, 
                    configure settings, and create your personalized voice clone.
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Create columns for the steps
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
            <div style="
                background: #f8f9fa;
                padding: 1.5rem;
                border-radius: 8px;
                text-align: center;
                border-left: 4px solid #667eea;
            ">
                <div style="
                    width: 40px;
                    height: 40px;
                    background: #667eea;
                    color: white;
                    border-radius: 50%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    margin: 0 auto 1rem auto;
                    font-weight: bold;
                ">1</div>
                <h4 style="color: #2c3e50; margin-bottom: 0.5rem;">Upload PDF</h4>
                <p style="color: #7f8c8d; font-size: 14px;">Choose your PDF document</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div style="
                background: #f8f9fa;
                padding: 1.5rem;
                border-radius: 8px;
                text-align: center;
                border-left: 4px solid #f093fb;
            ">
                <div style="
                    width: 40px;
                    height: 40px;
                    background: #f093fb;
                    color: white;
                    border-radius: 50%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    margin: 0 auto 1rem auto;
                    font-weight: bold;
                ">2</div>
                <h4 style="color: #2c3e50; margin-bottom: 0.5rem;">Configure</h4>
                <p style="color: #7f8c8d; font-size: 14px;">Set up text-to-speech options</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div style="
                background: #f8f9fa;
                padding: 1.5rem;
                border-radius: 8px;
                text-align: center;
                border-left: 4px solid #4facfe;
            ">
                <div style="
                    width: 40px;
                    height: 40px;
                    background: #4facfe;
                    color: white;
                    border-radius: 50%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    margin: 0 auto 1rem auto;
                    font-weight: bold;
                ">3</div>
                <h4 style="color: #2c3e50; margin-bottom: 0.5rem;">Clone Voice</h4>
                <p style="color: #7f8c8d; font-size: 14px;">Generate your personalized audio</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
            <div style="
                background: #f8f9fa;
                padding: 1.5rem;
                border-radius: 8px;
                text-align: center;
                border-left: 4px solid #43e97b;
            ">
                <div style="
                    width: 40px;
                    height: 40px;
                    background: #43e97b;
                    color: white;
                    border-radius: 50%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    margin: 0 auto 1rem auto;
                    font-weight: bold;
                ">4</div>
                <h4 style="color: #2c3e50; margin-bottom: 0.5rem;">Download</h4>
                <p style="color: #7f8c8d; font-size: 14px;">Get your voice-cloned audio</p>
            </div>
        """, unsafe_allow_html=True)