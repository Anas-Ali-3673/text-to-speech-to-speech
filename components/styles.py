import streamlit as st

def load_css():
    """Load and apply custom CSS styles"""
    try:
        with open('style.css') as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        # Fallback inline CSS if style.css doesn't exist
        st.markdown("""
        <style>
        .app-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        .hero-section {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 60px 20px;
            border-radius: 20px;
            margin-bottom: 30px;
        }
        .hero-container {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 40px;
            align-items: center;
        }
        .hero-left h1 {
            font-size: 2.5rem;
            margin-bottom: 20px;
            font-weight: bold;
        }
        .hero-left p {
            font-size: 1.2rem;
            margin-bottom: 30px;
            opacity: 0.9;
        }
        .feature-list {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        .feature-item {
            background: rgba(255,255,255,0.1);
            padding: 10px 15px;
            border-radius: 8px;
            font-weight: 500;
        }
        .section-card {
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            margin: 20px 0;
        }
        .success-message {
            background: #d4edda;
            color: #155724;
            padding: 15px;
            border-radius: 8px;
            margin: 15px 0;
            border: 1px solid #c3e6cb;
        }
        .info-message {
            background: #d1ecf1;
            color: #0c5460;
            padding: 15px;
            border-radius: 8px;
            margin: 15px 0;
            border: 1px solid #bee5eb;
        }
        .text-preview {
            background: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            margin: 15px 0;
            border: 1px solid #dee2e6;
            max-height: 150px;
            overflow-y: auto;
        }
        .footer {
            background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
            color: white;
            text-align: center;
            padding: 40px 20px;
            margin-top: 50px;
            border-radius: 15px;
        }
        .footer-content p {
            margin: 10px 0;
            font-size: 1rem;
        }
        </style>
        """, unsafe_allow_html=True)
