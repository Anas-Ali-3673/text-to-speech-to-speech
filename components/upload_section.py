import streamlit as st
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_file):
    """Extract text from uploaded PDF file"""
    try:
        pdf_document = fitz.open(stream=pdf_file.read(), filetype="pdf")
        text = ""
        for page_num in range(pdf_document.page_count):
            page = pdf_document[page_num]
            text += page.get_text()
        pdf_document.close()
        return text
    except Exception as e:
        st.error(f"Error extracting text from PDF: {str(e)}")
        return ""

def render_upload_section():
    """Render the PDF upload section"""
    st.markdown("### 📄 Upload Your PDF")
    
    uploaded_pdf = st.file_uploader(
        "Choose a PDF file",
        type="pdf",
        help="Upload a PDF document to convert to speech"
    )
    
    if uploaded_pdf is not None:
        with st.spinner("🔍 Extracting text from PDF..."):
            extracted_text = extract_text_from_pdf(uploaded_pdf)
            st.session_state.pdf_text = extracted_text
        
        st.markdown(f'<div class="success-message">✅ Successfully extracted {len(extracted_text)} characters from your PDF!</div>', unsafe_allow_html=True)

        # Preview text
        if len(extracted_text) > 300:
            preview_text = extracted_text[:300] + "..."
            st.markdown(f'<div class="text-preview"><strong>Preview:</strong><br>{preview_text}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="text-preview"><strong>Extracted Text:</strong><br>{extracted_text}</div>', unsafe_allow_html=True)
    
    return uploaded_pdf
