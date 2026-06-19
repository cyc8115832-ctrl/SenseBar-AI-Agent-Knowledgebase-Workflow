---
name: youtube-knowledgebase-builder
description: YouTube 影音知識庫建構器。下載 YouTube 影片、高音質音訊、並下載與去重 CC 字幕（或使用 Whisper 語音識別無字幕影片），轉存為 Markdown 逐字稿。說「下載 YouTube 字幕」、「抓 YouTube 逐字稿」、「下載 YouTube 影片音檔」時載入。
---

# YouTube 影音知識庫建構器技能 (YouTube Knowledgebase Builder Skill)

此技能供 AI Agent 在需要從 YouTube 下載影片、音訊、提取與清理 CC 字幕、或針對無字幕影片進行 Whisper 本地轉錄時調用。

## ⚙️ 系統依賴要求
- **yt-dlp**：本機需具備 `yt-dlp` 執行檔（若在 Windows 系統，預設路徑為專案根目錄的 `./yt-dlp.exe`）。
- **Node.js**：簽章解密挑戰需要，執行 `yt-dlp` 時請務必帶上 `--js-runtimes node`。
- **FFmpeg**：音訊轉檔與合併所必需，請確保已加到系統 `PATH`。
- **Whisper (Python)**：無字幕影片轉錄需要，安裝指令：`pip install openai-whisper torch`。

## 🛠️ 常見指令與工作流

### 1. 抓取頻道影片清單並過濾關鍵字
呼叫 [fetch_urls.py](file:///C:/Users/user/.gemini/config/skills/youtube-knowledgebase-builder/scripts/fetch_urls.py) 腳本，從目標 YouTube 頻道中獲取所有影片，並過濾出目標關鍵字網址儲存至 `urls_list.txt`。

### 2. 獲取並清理逐字稿 (自動分流處理)
呼叫 [build_knowledge_base.py](file:///C:/Users/user/.gemini/config/skills/youtube-knowledgebase-builder/scripts/build_knowledge_base.py) 腳本，對 `urls_list.txt` 中的網址進行分析：
- **分支 A（有 CC）**：下載 VTT，並使用去重演算法清理重複滾動行。
- **分支 B（無 CC）**：下載 M4A，呼叫 FFmpeg 轉為 MP3，並使用本地 Whisper 轉錄。

---

## 💻 核心技術指令參考

### 下載字幕 (CC) 且不下載影片
```powershell
./yt-dlp.exe --skip-download --write-subs --write-auto-subs --sub-lang "zh-Hant,zh-TW,zh,en" --sub-format vtt -o "temp_sub.%(ext)s" "URL"
```

### 破解 403 Forbidden 限速下載 M4A 音訊
```powershell
./yt-dlp.exe --js-runtimes node -f 140 -o "temp_audio.m4a" "URL"
```

### 使用 FFmpeg 轉檔音訊為最高品質 MP3
```powershell
ffmpeg -y -i "temp_audio.m4a" -acodec libmp3lame -aq 0 "output_audio.mp3"
```
