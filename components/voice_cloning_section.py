import streamlit as st
import requests
import time

# Removed upload_audio_to_temp_host function as we're now using direct text synthesis

def upload_audio_to_temp_host(audio_bytes):
    """Upload audio to temporary hosting service"""
    try:
        files = {'file': ('audio.wav', audio_bytes, 'audio/wav')}
        response = requests.post('https://bashupload.com', files=files)
        response.raise_for_status()

        response_text = response.text
        for line in response_text.splitlines():
            if line.strip().startswith('wget'):
                public_url = line.strip().split()[1]
                return public_url
        return None
    except Exception as e:
        st.error(f"Error uploading audio: {str(e)}")
        return None

def clone_voice_with_resemble(api_key, voice_uuid, project_uuid, audio_url):
    """Clone voice using Resemble AI API - based on working implementation"""
    try:
        # Step 1: Create clip with voice conversion
        api_url = f"https://app.resemble.ai/api/v2/projects/{project_uuid}/clips"
        headers = {
            'Authorization': f'Token {api_key}',
            'Content-Type': 'application/json'
        }
        payload = {
            "voice_uuid": voice_uuid,
            "body": f"<resemble:convert src='{audio_url}'></resemble:convert>"
        }

        response = requests.post(api_url, headers=headers, json=payload)
        response.raise_for_status()

        data = response.json()
        if not data.get('success'):
            st.error(f"❌ API Error: {data.get('message', 'Unknown error')}")
            return None

        clip_uuid = data['item']['uuid']
        st.info(f"✅ Clip created successfully. UUID: {clip_uuid}")

        # Step 2: Poll for completion
        clip_url = f"https://app.resemble.ai/api/v2/projects/{project_uuid}/clips/{clip_uuid}"
        max_retries = 30

        for i in range(max_retries):
            st.info(f"🔄 Checking conversion progress... ({i+1}/{max_retries})")

            poll_response = requests.get(clip_url, headers={'Authorization': f'Token {api_key}'})
            poll_response.raise_for_status()
            poll_data = poll_response.json()

            if poll_data.get('item') and poll_data['item'].get('audio_src'):
                audio_src_url = poll_data['item']['audio_src']
                st.success("✅ Voice conversion completed!")

                # Step 3: Download the result
                audio_response = requests.get(audio_src_url)
                audio_response.raise_for_status()

                return audio_response.content

            time.sleep(2)

        st.error("❌ Conversion timed out after 60 seconds")
        return None

    except requests.exceptions.HTTPError as err:
        st.error(f"❌ HTTP Error: {err}")
        return None
    except Exception as e:
        st.error(f"❌ Unexpected error: {str(e)}")
        return None

def get_voices(api_key):
    """Get available voices from Resemble AI"""
    try:
        headers = {'Authorization': f'Token {api_key}'}
        params = {'page': 1}
        url = 'https://app.resemble.ai/api/v2/voices'

        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()

        data = response.json()
        if 'items' in data and data['items']:
            return data['items']
        else:
            return []

    except Exception:
        return []

def get_project_uuid(api_key):
    """Get project UUID from Resemble AI - based on working implementation"""
    try:
        headers = {'Authorization': f'Token {api_key}'}
        params = {'page': 1}
        url = 'https://app.resemble.ai/api/v2/projects'

        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()

        data = response.json()
        if data['items']:
            project_uuid = data['items'][0]['uuid']
            project_name = data['items'][0].get('name', 'Unnamed Project')
            st.success(f"✅ Found project: {project_name}")
            return project_uuid, None
        else:
            return None, "No projects found"

    except requests.exceptions.HTTPError as err:
        return None, f"HTTP Error: {err}"
    except Exception as e:
        return None, f"Error: {str(e)}"

def get_projects(api_key):
    """Get available projects from Resemble AI"""
    try:
        headers = {'Authorization': f'Token {api_key}'}
        params = {'page': 1}
        url = 'https://app.resemble.ai/api/v2/projects'

        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()

        data = response.json()
        if 'items' in data and data['items']:
            return data['items']
        else:
            return []

    except Exception:
        return []

def render_voice_cloning_section():
    """Render the voice cloning configuration section - based on working implementation"""
    if not st.session_state.get('original_audio'):
        st.info("🔊 Please generate TTS audio first in the Configuration section.")
        return

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("""
    ## <svg class="lucide-icon lucide-icon-lg" viewBox="0 0 24 24" style="vertical-align: middle; margin-right: 0.5rem;">
        <path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"/>
        <path d="M19 10v2a7 7 0 0 1-14 0v-2"/>
        <line x1="12" x2="12" y1="19" y2="22"/>
        <line x1="8" x2="16" y1="22" y2="22"/>
    </svg>Voice Cloning Setup
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### <svg class="lucide-icon" viewBox="0 0 24 24" style="vertical-align: middle; margin-right: 0.5rem;">
            <circle cx="12" cy="12" r="10"/>
            <polygon points="10,8 16,12 10,16"/>
        </svg>Generated Speech Audio
        """, unsafe_allow_html=True)
        st.markdown("Listen to the AI-generated speech from your PDF:")
        st.audio(st.session_state.original_audio, format='audio/mp3')
        
        # Download button for original TTS
        st.download_button(
            label="📥 Download TTS Audio",
            data=st.session_state.original_audio,
            file_name="original_tts.mp3",
            mime="audio/mp3"
        )
    
    with col2:
        st.markdown("""
        #### <svg class="lucide-icon" viewBox="0 0 24 24" style="vertical-align: middle; margin-right: 0.5rem;">
            <path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"/>
            <path d="M19 10v2a7 7 0 0 1-14 0v-2"/>
            <line x1="12" x2="12" y1="19" y2="22"/>
            <line x1="8" x2="16" y1="22" y2="22"/>
        </svg>Upload Your Voice Sample
        """, unsafe_allow_html=True)
        st.markdown("Upload a clear .wav file of your voice:")

        uploaded_voice = st.file_uploader(
            "Choose a WAV file",
            type=['wav'],
            help="Upload a clear voice sample in WAV format for voice cloning"
        )

        if uploaded_voice is not None:
            st.session_state.voice_audio = uploaded_voice.read()
            st.success("✅ Voice sample uploaded successfully!")
            st.audio(st.session_state.voice_audio, format='audio/wav')

    # API Configuration
    st.markdown("""
    #### <svg class="lucide-icon" viewBox="0 0 24 24" style="vertical-align: middle; margin-right: 0.5rem;">
        <rect width="18" height="11" x="3" y="11" rx="2" ry="2"/>
        <circle cx="12" cy="16" r="1"/>
        <path d="m7 11 0-3a5 5 0 0 1 10 0v3"/>
    </svg>API Configuration
    """, unsafe_allow_html=True)

    col3, col4 = st.columns(2)
    with col3:
        api_key = st.text_input(
            "Resemble AI API Token",
            value=st.session_state.get('api_key', ''),
            type="password",
            help="Enter your Resemble AI API token"
        )
        if 'api_key' not in st.session_state:
            st.session_state.api_key = ""
        st.session_state.api_key = api_key

    with col4:
        voice_uuid = st.text_input(
            "Voice UUID",
            value=st.session_state.get('voice_uuid', ''),
            help="Enter the voice UUID from Resemble AI"
        )
        if 'voice_uuid' not in st.session_state:
            st.session_state.voice_uuid = ""
        st.session_state.voice_uuid = voice_uuid

    # Clone voice button - based on working implementation
    if st.button("🚀 Start Voice Cloning Process", type="primary"):
        if not api_key or not voice_uuid:
            st.error("❌ Please enter both API key and Voice UUID")
        elif not st.session_state.get('voice_audio'):
            st.error("❌ Please upload your voice sample first")
        else:
            with st.spinner("🔄 Starting voice cloning process..."):
                # Get project UUID automatically
                project_uuid, error = get_project_uuid(api_key)

                if error:
                    st.error(f"❌ Error getting project UUID: {error}")
                else:
                    st.info(f"📋 Project UUID: {project_uuid}")

                    # Upload the GENERATED TTS AUDIO (not the voice sample)
                    with st.spinner("📤 Uploading TTS audio for conversion..."):
                        public_url = upload_audio_to_temp_host(st.session_state.original_audio)

                    if not public_url:
                        st.error("❌ Failed to upload TTS audio")
                    else:
                        st.success("✅ TTS audio uploaded successfully")

                        # Clone voice using the working implementation
                        with st.spinner("🎭 Converting TTS audio to your cloned voice... This may take a few minutes..."):
                            cloned_audio = clone_voice_with_resemble(
                                api_key, voice_uuid, project_uuid, public_url
                            )

                        if cloned_audio:
                            st.session_state.cloned_audio = cloned_audio
                            st.success("🎉 Voice cloning completed successfully!")
                            st.balloons()
                            # Auto-navigate to results
                            if 'current_section' in st.session_state:
                                st.session_state.current_section = "results"
                                st.rerun()
                        else:
                            st.error("❌ Voice cloning failed. Please check your settings and try again.")
    
    st.markdown('</div>', unsafe_allow_html=True)
