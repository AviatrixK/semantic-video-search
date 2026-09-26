from .transcription.service import transcribe_video
import json
import os


video_path = "data/videos/test_video.mp4"

result = transcribe_video(video_path)

os.makedirs("data/transcripts", exist_ok=True)

output = {
    "video_name": "test_video.mp4",
    "segments": result["segments"]
}

with open("data/transcripts/test_video.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=2, ensure_ascii=False)

print("Transcription completed!")
print("Saved to data/transcripts/test_video.json")