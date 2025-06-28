import whisper
import time
import warnings
import os
#import torch

# Suppress the FP16 warning
warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")

warnings.filterwarnings("ignore", category=FutureWarning)


# Load the model once to save loading time for each file
model = whisper.load_model("small")     #uncomment if using cpu

# Check if GPU is available and set the device
#device = "cuda" if torch.cuda.is_available() else "cpu"
#print(f"Using device: {device}")

# Load the model once on GPU
#model = whisper.load_model("medium").to(device)

# Folder containing audio files
audio_folder = "audios"

# Loop through all files in the folder
for audio_file in os.listdir(audio_folder):
    if audio_file.endswith((".mp3", ".wav", ".opus", ".m4a", ".flac")):  # Adjust the extension if needed
        audio_path = os.path.join(audio_folder, audio_file)
        
        # Start time
        start_time = time.time()
        
        # Translate Urdu/English mix to English
        result = model.transcribe(audio_path, task="translate", language="ur")
        
        # End time
        end_time = time.time()
        
        # Print the translated text and time taken
        print(f"\nAudio File: {audio_file}")
        print("Translated Text:", result["text"])
        
        time_taken = end_time - start_time
        print("Time taken:", time_taken, "seconds")
