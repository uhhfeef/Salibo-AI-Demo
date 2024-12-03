# Salibo Incident Report Generator

A streamlined web application that converts audio recordings into professional security incident reports using OpenAI's advanced language models.

## Features

- 🎤 Real-time audio recording
- 🔄 Audio to text transcription using OpenAI Whisper
- 📝 Automated incident report generation using GPT-4
- 🌐 User-friendly Streamlit interface
- 🔒 Secure API key management

## Prerequisites

- Python 3.8+
- OpenAI API key
- Internet connection

## Installation

### Local Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Salibo-AI-Demo.git
cd Salibo-AI-Demo
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

### Streamlit Cloud Deployment

1. Fork this repository to your GitHub account
2. Sign up for [Streamlit Cloud](https://streamlit.io/cloud)
3. Create a new app and connect it to your forked repository
4. Add your OpenAI API key in the Streamlit Cloud secrets management

## Usage

### Running Locally

1. Start the application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to `http://localhost:8501`
3. Enter your OpenAI API key in the sidebar
4. Click the microphone button to start recording
5. Speak your incident report details
6. The application will automatically transcribe your audio and generate a professional incident report

### Using Streamlit Cloud

1. Navigate to your deployed Streamlit app URL
2. Follow steps 3-6 from the local usage instructions

## Configuration

The application uses a system prompt template defined in `prompts.py` which can be customized to modify the AI's response format and style.

## Security Notes

- Never commit your OpenAI API key to version control
- The application stores the API key only in session state
- Audio recordings are processed temporarily and not stored permanently

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue in the GitHub repository or contact the maintainers.
