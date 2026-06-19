import os
import subprocess
import json
import re
import glob

workspace_dir = "."
yt_dlp_path = "./yt-dlp.exe"  # or "yt-dlp"
urls_file = "urls_list.txt"

# Ensure Whisper is imported for non-CC transcription
try:
    import whisper
    whisper_model = whisper.load_model("base")  # Use 'base' or 'small' for speed/accuracy balance
except ImportError:
    print("Whisper is not installed. Videos without CC will be skipped. Run 'pip install openai-whisper' to enable.")
    whisper_model = None

def clean_filename(filename):
    filename = re.sub(r'[\\/*?:"<>|]', "_", filename)
    filename = re.sub(r'_+', '_', filename)
    return filename.strip()

def parse_vtt(vtt_path):
    if not os.path.exists(vtt_path):
        return ""
    with open(vtt_path, "r", encoding="utf-8") as f:
        content = f.read()
    lines = content.split("\n")
    clean_lines = []
    for line in lines:
        line = line.strip()
        if not line or line.startswith("WEBVTT") or line.startswith("Kind:") or line.startswith("Language:") or "-->" in line:
            continue
        line = re.sub(r'<[^>]+>', '', line).strip()
        if not line:
            continue
        if not clean_lines:
            clean_lines.append(line)
        else:
            last = clean_lines[-1]
            if line.startswith(last):
                clean_lines[-1] = line
            elif last.startswith(line):
                continue
            else:
                clean_lines.append(line)
    return "\n\n".join(clean_lines)

# Read URLs
if not os.path.exists(urls_file):
    print("urls_list.txt not found. Run fetch_urls.py first.")
    exit(1)
    
with open(urls_file, "r", encoding="utf-8") as f:
    urls = [line.strip() for line in f if line.strip()]

env = os.environ.copy()
env["PYTHONIOENCODING"] = "utf-8"

for idx, url in enumerate(urls, 1):
    print(f"\n[{idx}/{len(urls)}] Processing {url}...")
    
    # 1. Fetch JSON Info
    info_cmd = [yt_dlp_path, "--skip-download", "--dump-json", url]
    res = subprocess.run(info_cmd, capture_output=True, env=env)
    if res.returncode != 0:
        continue
    try:
        info_json = json.loads(res.stdout.decode('utf-8'))
        title = info_json.get("title")
        video_id = info_json.get("id")
        subtitles = info_json.get("subtitles", {})
        auto_subtitles = info_json.get("automatic_captions", {})
    except Exception as e:
        print(f"Error parsing metadata: {e}")
        continue

    print(f"Title: {title}")
    safe_title = clean_filename(title)
    md_path = f"{safe_title}.md"
    
    # Check if CC (Closed Caption) or Auto-subtitles are available
    has_cc = len(subtitles) > 0 or len(auto_subtitles) > 0
    
    if has_cc:
        print("-> Found Closed Captions (CC). Downloading subtitles...")
        temp_prefix = f"temp_sub_{video_id}"
        dl_cmd = [
            yt_dlp_path,
            "--skip-download",
            "--write-subs",
            "--write-auto-subs",
            "--sub-lang", "zh-Hant,zh-TW,zh,en",
            "--sub-format", "vtt",
            "-o", f"{temp_prefix}.%(ext)s",
            url
        ]
        subprocess.run(dl_cmd, capture_output=True)
        sub_files = glob.glob(f"{temp_prefix}.*")
        
        if sub_files:
            vtt_file = sub_files[0]
            clean_text = parse_vtt(vtt_file)
            
            # Save Transcript Markdown
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(f"# {title}\n\n- **YouTube Link**: {url}\n- **Source**: YouTube Closed Captions (CC)\n\n## Transcript\n\n{clean_text}\n")
            print(f"Saved: {md_path}")
            
            # Clean temp VTT
            for sf in sub_files:
                os.remove(sf)
        else:
            print("Failed to download VTT subtitle file. Falling back to audio download...")
            has_cc = False
            
    if not has_cc:
        if not whisper_model:
            print("-> No CC available and Whisper is not loaded. Skipping transcription.")
            continue
            
        print("-> No CC found. Downloading audio for Whisper transcription...")
        temp_audio = f"temp_audio_{video_id}.m4a"
        temp_mp3 = f"temp_audio_{video_id}.mp3"
        
        # Download audio using Node.js to solve challenges
        dl_cmd = [
            yt_dlp_path,
            "--js-runtimes", "node",
            "-f", "140",
            "-o", temp_audio,
            url
        ]
        dl_res = subprocess.run(dl_cmd, capture_output=True)
        
        if dl_res.returncode == 0 and os.path.exists(temp_audio):
            # Convert to MP3
            ffmpeg_cmd = ["ffmpeg", "-y", "-i", temp_audio, "-acodec", "libmp3lame", "-aq", "2", temp_mp3]
            subprocess.run(ffmpeg_cmd, capture_output=True)
            os.remove(temp_audio)
            
            if os.path.exists(temp_mp3):
                print(f"Transcribing {temp_mp3} with Whisper...")
                result = whisper_model.transcribe(temp_mp3, language="zh")
                transcribed_text = result.get("text", "")
                
                # Format text slightly into paragraphs
                formatted_text = "\n\n".join(re.split(r'(?<=[。！？])\s*', transcribed_text))
                
                with open(md_path, "w", encoding="utf-8") as f:
                    f.write(f"# {title}\n\n- **YouTube Link**: {url}\n- **Source**: Whisper Local Transcription\n\n## Transcript\n\n{formatted_text}\n")
                print(f"Transcribed & Saved: {md_path}")
                os.remove(temp_mp3)
            else:
                print("Failed to convert audio to MP3.")
        else:
            print("Failed to download audio.")
            
print("Workflow completed!")
