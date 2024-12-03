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
    
def fetch_ai_response(client, text_input, message_history):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]
    # Add message history to provide context
    messages.extend(message_history)
    # Add current user message
    messages.append({"role": "user", "content": text_input})
    
    return client.chat.completions.create(
        model="gpt-4o-mini", 
        messages=messages,
        stream=True
    )

def main():
    st.sidebar.title("Audio Recorder")
    api_key = st.sidebar.text_input("OpenAI API Key", type="password")
    
    st.title('Salibo Incident Report Demo')
    
    # Initialize chat history in session state
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hi there, I am your assistant! How can I help you today?"}
        ]
    
    # Add clear chat button in sidebar
    if st.sidebar.button("Clear Chat History"):
        st.session_state.messages = [
            {"role": "assistant", "content": "Hi there, I am your assistant! How can I help you today?"}
        ]
        st.rerun()

    # Display chat messages from history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
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
            
            # Display user message
            with st.chat_message("user"):
                st.markdown(transcribe_text)
            st.session_state.messages.append({"role": "user", "content": transcribe_text})
            
            # Get and display AI response with streaming
            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                full_response = ""
                
                # Stream the response with chat history context
                for chunk in fetch_ai_response(client, transcribe_text, st.session_state.messages[:-1]):  # Exclude the last message as it's already added
                    if chunk.choices[0].delta.content is not None:
                        full_response += chunk.choices[0].delta.content
                        message_placeholder.markdown(full_response + "▌")
                message_placeholder.markdown(full_response)
            
            # Add the complete response to session state
            st.session_state.messages.append({"role": "assistant", "content": full_response})
    else:
        st.warning("Please enter your OpenAI API key.")
        
    
        

if __name__ == "__main__":
    main()