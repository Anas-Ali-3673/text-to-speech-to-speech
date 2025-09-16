# 🎤 PDF to Voice Clone: AI-Powered Document Narration

![python-shield](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![streamlit-shield](https://img.shields.io/badge/Streamlit-1.28%2B-red)
![resemble-shield](https://img.shields.io/badge/Resemble%20AI-API-purple)
![gtts-shield](https://img.shields.io/badge/gTTS-2.3%2B-green)
![pymupdf-shield](https://img.shields.io/badge/PyMuPDF-1.23%2B-orange)

A **revolutionary Streamlit web application** that transforms PDF documents into personalized audio experiences using advanced AI voice cloning technology. Upload any PDF, extract its content, convert it to speech, and clone it with your own voice using Resemble AI's cutting-edge voice synthesis platform.

> 🚀 **Revolutionary Feature**: Upload a PDF document and hear it narrated in **your own cloned voice** - bridging the gap between written content and personalized audio experiences through state-of-the-art AI technology.

---

## 🌟 Application Features

- 🎯 **PDF Text Extraction**: Advanced text extraction from PDF documents using PyMuPDF
- 🔊 **Text-to-Speech Conversion**: High-quality speech synthesis using Google Text-to-Speech (gTTS)
- 🎭 **AI Voice Cloning**: Professional voice cloning integration with Resemble AI platform
- 📱 **Interactive Web Interface**: Beautiful, responsive Streamlit dashboard with modern UI
- ⚡ **Real-time Processing**: Live progress tracking and instant audio playback
- 💾 **Audio Download**: Download both original TTS and cloned voice audio files
- 🎨 **Custom Styling**: Professional CSS styling with gradient backgrounds and modern design

---

## 🧠 Key Capabilities & Workflow

This application provides a complete pipeline for document-to-voice conversion:

### 📄 Document Processing Pipeline
1. **PDF Upload & Validation** - Secure file upload with format verification
2. **Intelligent Text Extraction** - PyMuPDF-powered text extraction preserving document structure
3. **Content Preview** - Smart text preview with character count and length options
4. **Flexible Text Selection** - Choose from quick (500 chars) to full document conversion

### 🎵 Audio Generation Workflow
1. **Original TTS Creation** - Google Text-to-Speech generates baseline narration
2. **Voice Sample Upload** - User uploads personal voice sample in WAV format
3. **Resemble AI Integration** - Professional voice cloning using advanced AI models
4. **Audio Comparison** - Side-by-side playback of original vs. cloned voice

### 🔧 Technical Architecture
- **Modular Component Design** - Separated UI components for maintainability and reusability
- **Session State Management** - Persistent data handling across user interactions
- **Error Handling** - Comprehensive error management for API failures and file issues
- **Responsive Design** - Mobile-friendly interface with modern CSS variables and component-based styling
- **API Integration** - Seamless Resemble AI integration with progress tracking
- **Component-Based CSS** - Modern CSS architecture with CSS custom properties and utility classes

---

## 📁 Project Structure

```bash
.
├── app.py                     # Main Streamlit application entry point
├── components/                # Modular UI components
│   ├── __init__.py           # Components package initialization
│   ├── header.py             # Navigation header and page configuration
│   ├── hero.py               # Hero section with main title and features
│   ├── upload_section.py     # PDF upload and text extraction
│   ├── configuration_section.py  # Text configuration and TTS generation
│   ├── voice_cloning_section.py  # Voice cloning setup and processing
│   ├── results_section.py    # Results display and audio comparison
│   └── styles.py             # CSS loading and fallback styles
├── style.css                 # Modern component-based CSS styling
├── requirements.txt           # Python dependencies
├── venv/                     # Virtual environment (auto-generated)
└── README.md                  # Project documentation
```

## 🛠️ Tech Stack & Dependencies

| Category                | Tools & Libraries                                        |
|-------------------------|----------------------------------------------------------|
| **Web Framework**       | Streamlit                                               |
| **PDF Processing**      | PyMuPDF (fitz)                                         |
| **Text-to-Speech**      | Google Text-to-Speech (gTTS)                           |
| **Voice Cloning**       | Resemble AI API                                         |
| **File Handling**       | tempfile, BytesIO, base64                              |
| **HTTP Requests**       | requests library for API communication                  |
| **Audio Processing**    | Built-in audio handling and streaming                   |

---

## ⚙️ Installation & Setup

**1. Clone the Repository**
```bash
git clone https://github.com/Anas-Ali-3673/speech-to-speech.git
cd speech-to-speech
```

**2. Create Virtual Environment (Recommended)**
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix/Mac
source venv/bin/activate
```

**3. Install Dependencies**
```bash
pip install -r requirements.txt
```

**4. Resemble AI Setup**
- Create an account at [Resemble AI](https://www.resemble.ai/)
- Generate your API token from the dashboard
- Create a voice model and note the Voice UUID
- Ensure you have a project created (or the app will use the first available project)

---

## 🚀 How to Run the Application

**1. Start the Streamlit Server**
```bash
streamlit run app.py
```

**2. Access the Web Interface**
- Open your browser and navigate to `http://localhost:8501`
- The application will load with the beautiful hero interface

**3. Application Workflow**
1. **Upload PDF**: Choose your PDF document using the file uploader
2. **Configure Settings**: Select text length and conversion options
3. **Generate TTS**: Convert PDF text to speech using gTTS
4. **Upload Voice Sample**: Provide a clear WAV file of your voice
5. **Enter API Credentials**: Input your Resemble AI API token and Voice UUID
6. **Clone Voice**: Start the voice cloning process and wait for completion
7. **Download Results**: Save both original TTS and cloned voice audio files

---

## 🔑 API Configuration Guide

### 🎭 Resemble AI Setup

**1. Create Account**
- Visit [Resemble AI](https://www.resemble.ai/) and create an account
- Navigate to your dashboard

**2. Generate API Token**
- Go to Settings → API Keys
- Generate a new API token and copy it securely

**3. Create Voice Model**
- Upload voice samples to train your voice model
- Note the Voice UUID from your voice model dashboard

**4. Project Management**
- Ensure you have at least one project created
- The application automatically detects your first available project

### 🔊 Voice Sample Requirements
- **Format**: WAV audio files only
- **Quality**: Clear, noise-free recordings
- **Duration**: 10-30 seconds of natural speech
- **Content**: Read any text naturally in your normal speaking voice

---

## 📊 Application Features & Interface

### 🎨 User Interface Components
- **Hero Section**: Engaging landing area with feature highlights and call-to-action
- **PDF Upload Zone**: Drag-and-drop file upload with validation and preview
- **Configuration Panel**: Text length selection and processing options
- **Audio Players**: Built-in audio playback for original and cloned voice comparison
- **Progress Indicators**: Real-time status updates during processing
- **Download Section**: Easy access to generated audio files

### ⚡ Processing Capabilities
- **Text Length Options**: Quick (500 chars), Medium (1000 chars), Long (2000 chars), or Full document
- **Character Preview**: Smart text preview showing extraction results
- **Audio Quality**: High-quality MP3 output using gTTS technology
- **Voice Cloning**: Professional-grade voice synthesis using Resemble AI
- **Error Handling**: Comprehensive error management with user-friendly messages

---

## 🔧 Technical Implementation

### 🧩 Modular Component Architecture

The application follows a modern modular design pattern with separated concerns:

#### **Header Component** (`components/header.py`)
- Navigation bar rendering with consistent branding
- Streamlit page configuration management
- Default UI element hiding for clean interface

#### **Hero Component** (`components/hero.py`)
- Landing section with compelling call-to-action
- Feature highlights and value proposition
- Responsive design with gradient backgrounds

#### **Upload Section** (`components/upload_section.py`)
- PDF file upload handling with validation
- Text extraction using PyMuPDF
- Real-time preview and character counting

#### **Configuration Section** (`components/configuration_section.py`)
- Text length selection with multiple options
- TTS generation using Google Text-to-Speech
- Progress tracking and user feedback

#### **Voice Cloning Section** (`components/voice_cloning_section.py`)
- Resemble AI API integration
- Audio upload and processing management
- Real-time status updates and error handling

#### **Results Section** (`components/results_section.py`)
- Audio comparison interface
- Download functionality for both original and cloned audio
- Professional footer with attribution

#### **Styles Component** (`components/styles.py`)
- CSS loading with fallback support
- Modern component-based styling
- Responsive design utilities

### 📚 Core Functions

#### `extract_text_from_pdf(pdf_file)`
- Extracts text from uploaded PDF documents using PyMuPDF
- Handles multi-page documents with complete text preservation
- Returns clean, formatted text ready for speech conversion

#### `text_to_mp3(text, lang="en")`
- Converts extracted text to MP3 audio using Google Text-to-Speech
- Supports multiple languages with English as default
- Returns audio bytes for immediate playback and download

#### `clone_voice_with_resemble(api_key, voice_uuid, project_uuid, audio_url)`
- Integrates with Resemble AI API for professional voice cloning
- Handles clip creation, processing polling, and audio retrieval
- Includes comprehensive error handling and timeout management

#### `upload_audio_to_temp_host(audio_bytes)`
- Uploads TTS audio to temporary hosting for Resemble AI processing
- Uses bashupload.com for temporary file hosting
- Returns public URL for API consumption

---

## 🎯 Use Cases & Applications

### 📚 Educational Applications
- **Accessibility**: Convert textbooks and research papers to audio for visually impaired students
- **Language Learning**: Practice pronunciation and listening with personalized voice narration
- **Study Materials**: Transform lecture notes and study guides into portable audio content

### 💼 Professional Use Cases
- **Content Creation**: Generate personalized audiobooks and podcasts from written content
- **Business Reports**: Convert lengthy documents into convenient audio summaries
- **Training Materials**: Create voice-narrated training modules with personal touch

### 🎭 Creative Projects
- **Personalized Audiobooks**: Transform favorite books into your own voice narration
- **Voice Memos**: Convert written notes into spoken reminders
- **Custom Content**: Create unique audio content for social media and presentations

---

## 🔍 Advanced Configuration

### 📋 Environment Variables (Optional)
```bash
# Create .env file for default API credentials
RESEMBLE_API_KEY=your_api_key_here
DEFAULT_VOICE_UUID=your_voice_uuid_here
```

### 🎨 Custom Styling & Theming
The application uses a modern component-based CSS architecture:

- **CSS Custom Properties**: Centralized color palette, spacing, and typography variables
- **Component-Based Design**: Modular CSS classes for each UI component
- **Responsive Design**: Mobile-first approach with breakpoints for all device sizes
- **Modern Gradients**: Professional gradient backgrounds and hover effects
- **Utility Classes**: Pre-built classes for common styling patterns

**Customization Options:**
- Modify CSS variables in `style.css` for global theme changes
- Update component-specific styles for targeted modifications
- Add custom utility classes for extended functionality
- Responsive breakpoints ensure compatibility across all devices

### ⚡ Performance Optimization
- Text length limitations for faster processing
- Session state management for efficient memory usage
- Streaming audio playback for immediate feedback
- Asynchronous API calls with progress tracking

---

## 🚨 Troubleshooting Guide

### Common Issues & Solutions

**❌ PDF Upload Failures**
- Ensure PDF is not password-protected or corrupted
- Check file size limitations (typically under 10MB for optimal performance)
- Verify PDF contains extractable text (not scanned images)

**🔑 API Authentication Errors**
- Verify your Resemble AI API token is active and has sufficient credits
- Confirm Voice UUID matches your trained voice model
- Check project permissions and API rate limits

**🎵 Audio Processing Issues**
- Ensure voice sample is in WAV format with clear audio quality
- Check internet connection for API communication
- Verify temporary file hosting service availability

**⚡ Performance Optimization**
- Use shorter text selections for faster processing
- Ensure stable internet connection for API calls
- Close other resource-intensive applications during voice cloning

---

## 🔮 Future Enhancements

- [ ] **Multiple Language Support**: Expand TTS beyond English with language detection
- [ ] **Batch PDF Processing**: Upload and process multiple PDFs simultaneously
- [ ] **Advanced Voice Models**: Integration with additional voice cloning services
- [ ] **Real-time Voice Cloning**: Live voice training and immediate synthesis
- [ ] **Audio Enhancement**: Noise reduction and audio quality improvement
- [ ] **Cloud Storage Integration**: Direct upload to cloud storage services
- [ ] **Mobile App Version**: Native mobile application development
- [ ] **Voice Model Training**: Built-in voice training capabilities

---

## 📚 Dependencies & Requirements

### 🐍 Python Requirements
```
streamlit>=1.28.0
PyMuPDF>=1.23.0
gTTS>=2.3.0
requests>=2.28.0
```

### 🔗 External Services
- **Resemble AI Account**: Professional voice cloning API access
- **Internet Connection**: Required for API communication and audio hosting
- **Modern Web Browser**: Chrome, Firefox, Safari, or Edge for optimal experience





