import assemblyai as aai
import subprocess
import os

input_video = "/path/to/video.mp4"
output_video = f"{input_video.split('.')[0]}_subtitled.mp4"

aai.settings.api_key = "YOUR_API_KEY"
transcriber = aai.Transcriber()

transcript = transcriber.transcribe(input_video)

if transcript.status == aai.TranscriptStatus.error:
    print(transcript.error)
else:
    srt_content = transcript.export_subtitles_srt()
    srt_filename = "my_subtitles.srt"

    with open(srt_filename, "w") as f:
        f.write(srt_content)

        ffmpeg_command = [
        "ffmpeg",
        "-i", input_video,
        "-i", srt_filename,
        "-c", "copy", 
        "-c:s", "mov_text",
        output_video
    ]

    subprocess.run(ffmpeg_command)

   
    os.remove(srt_filename) 

    print("Subtitles embedded in video!") 

