import streamlit as st

def get_lucide_icon_svg(icon_name: str) -> str:
    """Get SVG markup for Lucide icons"""
    icons = {
        "home": '''<svg class="lucide-icon" viewBox="0 0 24 24"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9,22 9,12 15,12 15,22"/></svg>''',
        "file-text": '''<svg class="lucide-icon" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14,2 14,8 20,8"/><line x1="16" x2="8" y1="13" y2="13"/><line x1="16" x2="8" y1="17" y2="17"/><polyline points="10,9 9,9 8,9"/></svg>''',
        "settings": '''<svg class="lucide-icon" viewBox="0 0 24 24"><path d="M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0-.73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2z"/><circle cx="12" cy="12" r="3"/></svg>''',
        "mic": '''<svg class="lucide-icon" viewBox="0 0 24 24"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" x2="12" y1="19" y2="22"/><line x1="8" x2="16" y1="22" y2="22"/></svg>''',
        "headphones": '''<svg class="lucide-icon" viewBox="0 0 24 24"><path d="M3 14h3a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-7a9 9 0 0 1 18 0v7a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3"/></svg>''',
        "clipboard": '''<svg class="lucide-icon" viewBox="0 0 24 24"><rect width="8" height="4" x="8" y="2" rx="1" ry="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/></svg>''',
        "upload": '''<svg class="lucide-icon" viewBox="0 0 24 24"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7,10 12,15 17,10"/><line x1="12" x2="12" y1="15" y2="3"/></svg>''',
        "download": '''<svg class="lucide-icon" viewBox="0 0 24 24"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7,10 12,15 17,10"/><line x1="12" x2="12" y1="15" y2="3"/></svg>''',
        "play": '''<svg class="lucide-icon" viewBox="0 0 24 24"><polygon points="5,3 19,12 5,21"/></svg>''',
        "check": '''<svg class="lucide-icon" viewBox="0 0 24 24"><polyline points="20,6 9,17 4,12"/></svg>''',
        "clock": '''<svg class="lucide-icon" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polyline points="12,6 12,12 16,14"/></svg>''',
        "menu": '''<svg class="lucide-icon" viewBox="0 0 24 24"><line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="18" y2="18"/></svg>''',
        "x": '''<svg class="lucide-icon" viewBox="0 0 24 24"><path d="m18 6-12 12"/><path d="m6 6 12 12"/></svg>''',
    }
    return icons.get(icon_name, icons["home"])

# Constants
APP_CONFIG = {
    "page_title": "PDF to Voice Clone",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

NAVIGATION_ITEMS = [
    {"icon": "home", "label": "Home", "key": "home"},
    {"icon": "file-text", "label": "Upload PDF", "key": "upload"},
    {"icon": "settings", "label": "Configuration", "key": "config"},
    {"icon": "mic", "label": "Voice Clone", "key": "voice"},
    {"icon": "headphones", "label": "Results", "key": "results"},
]

def configure_page() -> None:
    """Configure Streamlit page settings with best practices"""
    st.set_page_config(**APP_CONFIG)

def apply_responsive_styles() -> None:
    """Apply responsive CSS styles for mobile-first design"""
    st.markdown("""
    <style>
    /* Base styles */
    .lucide-icon {
        width: 18px;
        height: 18px;
        stroke: currentColor;
        stroke-width: 2;
        fill: none;
        stroke-linecap: round;
        stroke-linejoin: round;
    }
    
    .lucide-icon-xl {
        width: 32px;
        height: 32px;
    }
    
    /* Mobile Toggle Button - Hidden by default */
    .mobile-nav-toggle {
        display: none;
        position: fixed;
        top: 20px;
        left: 20px;
        z-index: 1001;
        background: #1f2937;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 12px;
        cursor: pointer;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        transition: all 0.3s ease;
    }
    
    .mobile-nav-toggle:hover {
        background: #374151;
        transform: scale(1.05);
    }
    
    /* Mobile overlay - Hidden by default */
    .mobile-overlay {
        display: none;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.5);
        z-index: 999;
    }
    
    /* Navigation styles */
    .nav-button {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 12px 16px;
        margin: 4px 0;
        border-radius: 8px;
        background: transparent;
        color: #374151;
        text-decoration: none;
        font-weight: 500;
        transition: all 0.2s ease;
        cursor: pointer;
        border: 1px solid transparent;
    }
    
    .nav-button:hover {
        background: #f3f4f6;
        color: #1f2937;
    }
    
    .nav-button.active {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-color: #667eea;
        box-shadow: 0 2px 8px rgba(102, 126, 234, 0.3);
    }
    
    .nav-icon {
        flex-shrink: 0;
    }
    
    .nav-label {
        font-size: 14px;
        white-space: nowrap;
    }
    
    /* Header styles */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 24px;
        border-radius: 12px;
        margin-bottom: 24px;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
    }
    
    .header-content {
        display: flex;
        align-items: center;
        justify-content: space-between;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    .header-left {
        flex: 1;
    }
    
    .header-title {
        display: flex;
        align-items: center;
        gap: 16px;
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0;
        margin-bottom: 8px;
    }
    
    .title-icon {
        background: rgba(255, 255, 255, 0.2);
        padding: 12px;
        border-radius: 12px;
    }
    
    .header-description {
        font-size: 1.1rem;
        opacity: 0.9;
        margin: 0;
    }
    
    .header-right {
        flex-shrink: 0;
    }
    
    .status-indicator {
        display: flex;
        align-items: center;
        gap: 8px;
        background: rgba(255, 255, 255, 0.1);
        padding: 8px 16px;
        border-radius: 24px;
        backdrop-filter: blur(10px);
    }
    
    .status-dot {
        width: 8px;
        height: 8px;
        background: #10b981;
        border-radius: 50%;
        animation: pulse 2s infinite;
    }
    
    .status-text {
        font-size: 14px;
        font-weight: 500;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.5; }
    }
    
    /* Progress indicator styles */
    .progress-step {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 12px;
        padding: 8px 0;
        font-size: 14px;
    }
    
    .progress-step .lucide-icon {
        width: 16px;
        height: 16px;
        color: #10b981;
    }
    
    .progress-step.incomplete .lucide-icon {
        color: #6b7280;
    }
    
    /* Sidebar customization */
    section[data-testid="stSidebar"] > div {
        background: #f8fafc;
        border-right: 1px solid #e2e8f0;
    }
    
    /* Desktop styles (1025px and above) - Sidebar always visible, no toggle */
    @media (min-width: 1025px) {
        section[data-testid="stSidebar"] {
            display: block !important;
            visibility: visible !important;
            position: relative !important;
            left: 0 !important;
            transform: none !important;
        }
        
        /* Ensure mobile toggle is completely hidden */
        .mobile-nav-toggle {
            display: none !important;
            visibility: hidden !important;
        }
        
        .mobile-overlay {
            display: none !important;
            visibility: hidden !important;
        }
        
        /* Hide Streamlit's default sidebar toggle */
        section[data-testid="stSidebar"] button[kind="header"] {
            display: none !important;
        }
        
        .main .block-container {
            padding-top: 2rem !important;
        }
    }
    
    /* Tablet styles (769px to 1024px) - Hide sidebar, show toggle */
    @media (min-width: 769px) and (max-width: 1024px) {
        .mobile-nav-toggle {
            display: flex !important;
            align-items: center;
            justify-content: center;
        }
        
        .main .block-container {
            padding-top: 80px !important;
        }
        
        section[data-testid="stSidebar"] {
            position: fixed !important;
            top: 0 !important;
            left: -100% !important;
            height: 100vh !important;
            width: 300px !important;
            z-index: 1000 !important;
            transition: left 0.3s ease !important;
            box-shadow: 2px 0 10px rgba(0, 0, 0, 0.1) !important;
        }
        
        section[data-testid="stSidebar"].mobile-active {
            left: 0 !important;
        }
        
        section[data-testid="stSidebar"] button[kind="header"] {
            display: none !important;
        }
        
        .mobile-overlay.active {
            display: block;
        }
    }
    
    /* Mobile styles (768px and below) - Hide sidebar, show toggle */
    @media (max-width: 768px) {
        /* Show mobile toggle button */
        .mobile-nav-toggle {
            display: flex !important;
            align-items: center;
            justify-content: center;
        }
        
        /* Adjust main content for mobile toggle */
        .main .block-container {
            padding-top: 80px !important;
        }
        
        /* Mobile header adjustments */
        .header-title {
            font-size: 1.8rem;
        }
        
        .header-content {
            flex-direction: column;
            gap: 16px;
            text-align: center;
        }
        
        .status-indicator {
            margin: 0 auto;
        }
        
        /* Sidebar mobile behavior - completely hidden by default */
        section[data-testid="stSidebar"] {
            position: fixed !important;
            top: 0 !important;
            left: -100% !important;
            height: 100vh !important;
            width: 280px !important;
            z-index: 1000 !important;
            transition: left 0.3s ease !important;
            box-shadow: 2px 0 10px rgba(0, 0, 0, 0.1) !important;
        }
        
        /* Show sidebar when active */
        section[data-testid="stSidebar"].mobile-active {
            left: 0 !important;
        }
        
        /* Hide Streamlit's default sidebar controls on mobile */
        section[data-testid="stSidebar"] button[kind="header"] {
            display: none !important;
        }
        
        /* Show overlay when sidebar is open */
        .mobile-overlay.active {
            display: block;
        }
        
        /* Adjust navigation for mobile */
        .nav-button {
            padding: 16px;
            font-size: 16px;
        }
    }
    
    /* Very small screens (480px and below) */
    @media (max-width: 480px) {
        .main-header {
            padding: 16px;
            margin-bottom: 16px;
        }
        
        .header-title {
            font-size: 1.5rem;
            flex-direction: column;
            gap: 12px;
        }
        
        .title-icon {
            padding: 8px;
        }
        
        .header-description {
            font-size: 1rem;
        }
        
        .mobile-nav-toggle {
            top: 16px;
            left: 16px;
            padding: 10px;
        }
        
        section[data-testid="stSidebar"] {
            width: 260px !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)

def render_mobile_toggle() -> None:
    """Render mobile navigation toggle button"""
    # Add JavaScript for mobile navigation
    st.markdown("""
    <div class="mobile-overlay" id="mobileOverlay" onclick="closeMobileNav()"></div>
    <button class="mobile-nav-toggle" id="mobileNavToggle" onclick="toggleMobileNav()">
        <svg class="lucide-icon" id="toggleIcon" viewBox="0 0 24 24">
            <line x1="4" x2="20" y1="6" y2="6"/>
            <line x1="4" x2="20" y1="12" y2="12"/>
            <line x1="4" x2="20" y1="18" y2="18"/>
        </svg>
    </button>
    
    <script>
    function forceSidebarState() {
        const sidebar = document.querySelector('section[data-testid="stSidebar"]');
        if (sidebar && window.innerWidth <= 1024) {
            // Force remove any Streamlit classes that might show the sidebar
            sidebar.classList.remove('st-emotion-cache-1cypcdb');
            sidebar.classList.remove('st-emotion-cache-1d391kg');
            // Ensure our mobile class is not active by default
            sidebar.classList.remove('mobile-active');
        }
    }
    
    function toggleMobileNav() {
        const sidebar = document.querySelector('section[data-testid="stSidebar"]');
        const overlay = document.getElementById('mobileOverlay');
        const toggleIcon = document.getElementById('toggleIcon');
        
        if (sidebar && overlay) {
            const isActive = sidebar.classList.contains('mobile-active');
            
            if (isActive) {
                sidebar.classList.remove('mobile-active');
                overlay.classList.remove('active');
                toggleIcon.innerHTML = '<line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="18" y2="18"/>';
            } else {
                sidebar.classList.add('mobile-active');
                overlay.classList.add('active');
                toggleIcon.innerHTML = '<path d="m18 6-12 12"/><path d="m6 6 12 12"/>';
            }
        }
    }
    
    function closeMobileNav() {
        const sidebar = document.querySelector('section[data-testid="stSidebar"]');
        const overlay = document.getElementById('mobileOverlay');
        const toggleIcon = document.getElementById('toggleIcon');
        
        if (sidebar && overlay && toggleIcon) {
            sidebar.classList.remove('mobile-active');
            overlay.classList.remove('active');
            toggleIcon.innerHTML = '<line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="18" y2="18"/>';
        }
    }
    
    // Close mobile nav when clicking on navigation items
    document.addEventListener('click', function(e) {
        if (e.target.closest('.nav-button') || e.target.closest('button[kind="primary"]')) {
            setTimeout(closeMobileNav, 100);
        }
    });
    
    // Close mobile nav on window resize to desktop
    window.addEventListener('resize', function() {
        forceSidebarState();
        if (window.innerWidth > 1024) {
            closeMobileNav();
        }
    });
    
    // Initialize sidebar state based on screen size
    window.addEventListener('load', function() {
        forceSidebarState();
        if (window.innerWidth <= 1024) {
            closeMobileNav();
        }
    });
    
    // Use MutationObserver to watch for Streamlit changes
    const observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
            if (mutation.type === 'childList' || mutation.type === 'attributes') {
                forceSidebarState();
            }
        });
    });
    
    // Start observing when DOM is ready
    document.addEventListener('DOMContentLoaded', function() {
        const sidebar = document.querySelector('section[data-testid="stSidebar"]');
        if (sidebar) {
            observer.observe(sidebar, {
                attributes: true,
                childList: true,
                subtree: true
            });
        }
        forceSidebarState();
    });
    </script>
    """, unsafe_allow_html=True)

def render_sidebar() -> str:
    """Render responsive sidebar navigation"""
    with st.sidebar:
        # Navigation menu
        st.markdown('<h3 style="margin-bottom: 1rem; color: #374151;">Navigation</h3>', unsafe_allow_html=True)

        # Initialize current section if not set
        if 'current_section' not in st.session_state:
            st.session_state.current_section = "home"

        # Create navigation buttons with active state
        for item in NAVIGATION_ITEMS:
            is_active = st.session_state.current_section == item['key']
            icon_svg = get_lucide_icon_svg(item['icon'])

            if is_active:
                st.markdown(f"""
                <div class="nav-button active">
                    <span class="nav-icon">{icon_svg}</span>
                    <span class="nav-label">{item['label']}</span>
                </div>
                """, unsafe_allow_html=True)
            else:
                if st.button(f"{item['label']}", key=f"nav_{item['key']}", use_container_width=True):
                    st.session_state.current_section = item['key']
                    st.rerun()

        st.markdown("---")
        render_progress_indicator()
        st.markdown("---")
        render_quick_stats()

        return st.session_state.current_section

def render_progress_indicator() -> None:
    """Render responsive progress indicator"""
    st.markdown('<h3 style="margin-bottom: 1rem; color: #374151;">Progress</h3>', unsafe_allow_html=True)

    steps = [
        ("Upload PDF", st.session_state.get('pdf_text', '') != ''),
        ("Generate TTS", st.session_state.get('original_audio') is not None),
        ("Clone Voice", st.session_state.get('cloned_audio') is not None)
    ]

    for i, (step_name, completed) in enumerate(steps, 1):
        status_class = "progress-step" if completed else "progress-step incomplete"
        status_icon = get_lucide_icon_svg("check") if completed else get_lucide_icon_svg("clock")
        
        st.markdown(f"""
        <div class="{status_class}">
            <span>{status_icon}</span>
            <span><strong>Step {i}:</strong> {step_name}</span>
        </div>
        """, unsafe_allow_html=True)

def render_quick_stats() -> None:
    """Render responsive quick statistics"""
    st.markdown('<h3 style="margin-bottom: 1rem; color: #374151;">Quick Stats</h3>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label="PDF Pages",
            value=st.session_state.get('pdf_pages', 0)
        )

    with col2:
        st.metric(
            label="Text Length",
            value=f"{len(st.session_state.get('pdf_text', ''))}"
        )

def hide_streamlit_elements() -> None:
    """Hide default Streamlit UI elements for clean interface"""
    st.markdown("""
    <style>
    /* Hide Streamlit branding and menu */
    #MainMenu, footer, header, .stDeployButton, .stDecoration {
        visibility: hidden !important;
        display: none !important;
    }

    /* Adjust main content area */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Main application function
def main():
    """Main application entry point"""
    configure_page()
    apply_responsive_styles()
    hide_streamlit_elements()
    render_mobile_toggle()
    
    # Render navigation
    current_section = render_sidebar()
    
    # Your page content based on current_section
    if current_section == "home":
        st.write("Welcome to the home page!")
    elif current_section == "upload":
        st.write("Upload your PDF here")
    # Add other sections as needed

if __name__ == "__main__":
    main()