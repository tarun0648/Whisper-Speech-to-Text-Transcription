# Whisper Speech-to-Text Transcription

This project uses OpenAI's Whisper model for speech-to-text transcription.  

---

![PHOTO-2025-07-24-18-07-50](https://github.com/user-attachments/assets/e0336b36-b931-4f03-b7c7-f816a68be09a)


## Prerequisites

### Python Version  
Ensure you have Python version **between 3.7 and 3.10**.  

### Virtual Environment Setup  
Create and activate a virtual environment:  
```sh
python -m venv whisper_env
whisper_env\Scripts\activate  # On Windows
source whisper_env/bin/activate  # On MacOS/Linux
```
### Whisper and ffmpeg Setup

Run following commands
```sh
pip install torch torchvision torchaudio
pip install whisper-openai
```

Now run code 
```sh
python whisper_test.py
```

### Why first audio is taking longer time to process?
Model Initialization Overhead: When the model is first loaded and used, there is an initialization cost. This includes loading weights into memory, warming up the GPU (if using one), and setting up internal states. This overhead is only incurred once, which is why the first audio takes longer regardless of its content or length.
