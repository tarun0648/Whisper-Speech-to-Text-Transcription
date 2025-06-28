# Whisper Speech-to-Text Transcription

This project uses OpenAI's Whisper model for speech-to-text transcription. It supports both GPU and CPU execution and allows the use of different model sizes (small and medium) depending on the accuracy and speed requirements.  

---

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

Before executing code install ffmpeg. Go to link https://www.gyan.dev/ffmpeg/builds/
Under release build section download ffmpeg-release-essentials.zip . Extract in c folder and add bin folder to system path.

Now run code 
```sh
python whisper_test.py
```
### GPU Instructions
I have Nvidia GPU. So, if you have gpu then install suitable cuda (12.1) in my case.
Now install pytorch in virtual environment. See official website to use compatible command.

I have used 2 models small and medium.

**1. Small Model (small)**
Size: ~480 MB
Parameters: **244 M**
Speed: **Faster** compared to the medium model. Suitable for real-time applications or when lower latency is needed.
Accuracy: Good accuracy, especially for clear audio and common languages. Might struggle with complex sentences or noisy backgrounds.
Use Case: When you need faster transcription and are okay with slightly lower accuracy. Ideal for quick experiments or real-time transcription.

**2. Medium Model (medium)**
Size: ~1.5 GB
Parameters: **769 M**
Speed: Slower than the small model, but still manageable.
Accuracy: **Higher accuracy** than the small model, especially for complex language structures, noisy environments, or multilingual audio.
Use Case: When you prioritize accuracy over speed. Suitable for professional transcription tasks where precision is important.

### Why first audio is taking longer time to process?
Model Initialization Overhead: When the model is first loaded and used, there is an initialization cost. This includes loading weights into memory, warming up the GPU (if using one), and setting up internal states. This overhead is only incurred once, which is why the first audio takes longer regardless of its content or length.
