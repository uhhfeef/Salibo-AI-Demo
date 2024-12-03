import streamlit as st
from audio_recorder_streamlit import audio_recorder
import openai
import base64
from prompts import SYSTEM_PROMPT

def setup_openai_api_key(api_key):
    return openai.OpenAI(api_key=api_key)

def transcribe_audio(client, audio_path):
    with open(audio_path, "rb") as f:
        transcription = client.audio.transcriptions.create(
            model="whisper-1", 
            file=f
        )
        return transcription.text
    
def fetch_ai_response(client, text_input):
    response = client.chat.completions.create(
        model="gpt-4o-mini", 
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": text_input},
        ]
    )
    return response.choices[0].message.content


def main():
    st.sidebar.title("Audio Recorder")
    api_key = st.sidebar.text_input("OpenAI API Key", type="password")
    
    st.title('Salibo Incident Report Demo')
    st.write('Hi there, I am your assistant! How can I help you today?')
    
    if api_key:
        client = setup_openai_api_key(api_key)
        recorded_audio = audio_recorder()
        if recorded_audio:
            status_placeholder = st.empty()
            status_placeholder.text("Transcribing audio...")
            audio_path = "audio.mp3"
            with open(audio_path, "wb") as f:
                f.write(recorded_audio)
            
            transcribe_text = transcribe_audio(client, audio_path)
            status_placeholder.empty()
            st.write("Transcription:", transcribe_text)
            ai_response = fetch_ai_response(client, transcribe_text)
            st.write("AI Response:", ai_response)
    else:
        st.warning("Please enter your OpenAI API key.")
        
    
        

if __name__ == "__main__":
    main()