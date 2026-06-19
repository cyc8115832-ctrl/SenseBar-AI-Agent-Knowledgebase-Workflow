import subprocess
import json
import os

url = "https://www.youtube.com/@sensebar/videos"
yt_dlp_path = "./yt-dlp.exe"  # or "yt-dlp" if in PATH

# Force UTF-8 encoding for yt-dlp stdout
env = os.environ.copy()
env["PYTHONIOENCODING"] = "utf-8"

cmd = [
    yt_dlp_path,
    "--flat-playlist",
    "--print",
    '{"title": %(title)q, "url": %(url)q}',
    url
]

print("Fetching videos...")
result = subprocess.run(cmd, capture_output=True, env=env)
if result.returncode != 0:
    print("Error:", result.stderr.decode('utf-8', errors='replace'))
    exit(1)

lines = result.stdout.decode('utf-8', errors='replace').strip().split("\n")
videos = []
for line in lines:
    if line.strip():
        try:
            videos.append(json.loads(line))
        except:
            continue

# Filter keywords (case-insensitive)
keywords = ["claude", "codex", "antigravity", "opencode", "agent"]
matched = []
for v in videos:
    title_lower = v['title'].lower()
    if any((kw in title_lower or (kw == "opencode" and "open code" in title_lower)) for kw in keywords):
        matched.append(v)

# Save URLs
with open("urls_list.txt", "w", encoding="utf-8") as f:
    for mv in matched:
        f.write(f"{mv['url']}\n")
        
print(f"Saved {len(matched)} matching URLs to urls_list.txt")
