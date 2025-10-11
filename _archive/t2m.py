
import requests
from moviepy.editor import ImageClip, AudioFileClip

# ---- ElevenLabs API Setup ----
ELEVENLABS_API_KEY = "sk_4770b8e0f21cd2c49ce946b3f163225b306fe4070d799ecf"  # Replace with your actual API key
VOICE_ID = "vNIPh9nWB7YXKglFnXbX"  # Replace with your voice's ID from ElevenLabs

def generate_audio_with_elevenlabs(text, output_file):
    """
    Generate speech audio using the ElevenLabs API.
    """
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }
    # Adjust the voice_settings as needed (stability, similarity_boost, etc.)
    data = {
        "text": text,
        "voice_settings": {
            "stability": 0.5,         # Adjust for naturalness
            "similarity_boost": 0.75    # Adjust for voice likeness
        }
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code != 200:
        raise Exception(f"Error generating audio: {response.text}")
    with open(output_file, "wb") as f:
        f.write(response.content)
    return output_file

# ---- Your Content ----
notes_text = (
    "Welcome to the course! This isn't just about reading and listening to lectures; it's about actively engaging with Python through coding exercises. By following this approach, you’ll not only learn Python quickly but also retain what you learn for the long term."
)
audio_file = "notes.mp3"  # ElevenLabs returns MP3 by default

# Generate audio using ElevenLabs
generate_audio_with_elevenlabs(notes_text, audio_file)

# ---- Combine Audio and Image into a Video ----
def create_video(image_file, audio_file, output_file, fps=24):
    audio_clip = AudioFileClip(audio_file)
    image_clip = ImageClip(image_file).set_duration(audio_clip.duration)
    video_clip = image_clip.set_audio(audio_clip)
    # Specify codecs to ensure proper audio encoding
    video_clip.write_videofile(output_file, fps=fps, codec="libx264", audio_codec="aac")
    return output_file

# Assuming you have a slide image "slide.png"
slide_image_file = "slide.png"
video_file = "slide_video.mp4"

# Create the final video
create_video(slide_image_file, audio_file, video_file)

print(f"Video created: {video_file}")
