# 專案筆記 (Project Notes) - 三師爸Sense Bar的agent

## 🎯 專案里程碑與進度

### 1. 專案初始化 (2026-06-19)
- [x] 盤點專案目錄，確認環境目前僅包含 `yt-dlp.exe`。
- [x] 確認 `FFmpeg` 安裝狀態：發現本地未安裝，並透過 `winget` 成功為系統安裝 `Gyan.FFmpeg` 8.1.1。
- [x] 建立基礎設定文件：`.gitignore`、`ANTIGRAVITY.md`、`README.md`。
- [x] 初始化本地 Git 儲存庫並提交首次 Commit。

### 2. 影片資訊與字幕抓取 (2026-06-19)
- [x] 成功獲取三師爸頻道全部 309 部影片資訊。
- [x] 篩選出與 **Claude / Codex / AntiGravity / OpenCode / AI Agent** 相關的 38 部影片網址，並儲存至 [SenseBar_AI_Agent_URLs.txt](file:///d:/user/Documents/三師爸Sense%20Bar的agent/SenseBar_AI_Agent_URLs.txt)。
- [x] 下載此 38 部影片的字幕檔，過濾 VTT 時間戳記與重複累積字幕，轉存成 37 份乾淨的 `.md` 逐字稿檔案於專案目錄中。

### 3. 最短影片下載與轉檔 (2026-06-19)
- [x] 掃描所有篩選影片的播放長度，找出最短影片為：「使用 AI Agent 來幫忙寫年度課程領域計畫...」（長度僅 104 秒 / 1.73 分鐘）。
- [x] 成功下載其音訊檔，並透過本機安裝的 `FFmpeg` 轉檔為最高品質 MP3：[使用_AI_Agent_來幫忙寫年度課程領域計畫.mp3](file:///d:/user/Documents/三師爸Sense%20Bar的agent/使用_AI_Agent_來幫忙寫年度課程領域計畫.mp3)。

### 4. 公開工作流程說明倉庫 (2026-06-19)
- [x] 建立公開 GitHub Repository：[SenseBar-AI-Agent-Knowledgebase-Workflow](https://github.com/cyc8115832-ctrl/SenseBar-AI-Agent-Knowledgebase-Workflow)。
- [x] 編寫適用於其他 AI Agent 的 `README.md`，並將說明**翻譯成中文對照與解析**，詳細說明如何建構影音知識庫。
- [x] 擴充設計「無字幕影片 (Non-CC)」之處理解決方案，使用 `yt-dlp` 下載音訊並透過 Python Whisper 轉錄字幕。
- [x] 成功在本機安裝 `openai-whisper` 及其相依機器學習庫（含 `torch` 等）。
- [x] 提供 `fetch_urls.py` 與 `build_knowledge_base.py` 完整自動化指令碼。

### 5. 全域與專案 Skill 封裝 (2026-06-19)
- [x] 建立全域 AI Agent Skill [youtube-knowledgebase-builder](file:///C:/Users/user/.gemini/config/skills/youtube-knowledgebase-builder/SKILL.md) 於全域設定路徑，以便於日後任何新專案直接調用。
- [x] 將此技能打包上傳至 GitHub 倉庫的 `skills/` 目錄中完成備份與整合。

### 6. 第二大腦 Obsidian 知識整合 (2026-06-19)
- [x] 將今日整理之「AI Agent 整合分析報告」、「影片篩選清單」、「專案筆記」及「Skill 說明文件」匯出至您的 Obsidian Vault [D:\user\Documents\Obdisian\Obdisian\0619 AI_Agent_整合分析報告\](file:///D:/user/Documents/Obdisian/Obdisian/0619%20AI_Agent_%E6%95%B4%E5%90%88%E5%88%86%E6%9E%90%E5%A0%B1%E5%91%8A/) 目錄中，完成第二大腦的知識庫建構。

### 7. Google AntiGravity 2.0 影片分析與轉譯 (2026-06-20)
- [x] 分析目標影片 `https://youtu.be/bstR13jNtzM`（Google Antigravity 2.0 来了），確認該影片無 CC 字幕。
- [x] 本地下載該影片的音軌，並成功轉換成最高品質 MP3 檔 `Google_Antigravity_2.0.mp3`。
- [x] 撰寫 Python 腳本調用本地 Whisper (base model) 執行語音轉文字，產出完整逐字稿。
- [x] 整合影片內容摘要（包含定位轉變、Gemini 3.5 Flash 優勢、任務排程等核心要點）與三大開發者反思。
- [x] 針對影片中的專業術語（IDE、CLI、Agent、SDK、Vibe Coding）編寫專有名詞解析（Glossary）並寫入檔案中。
- [x] 成功將生成的 `Google_Antigravity_2.0_逐字稿.md` 檔案推播至 GitHub 倉庫中同步。
- [x] 針對 LINE Webhook 與本地 ngrok 串接的可行性進行系統架構、作業規劃與部署準備盤點。

---

## 🚀 下一步計畫 (Next Steps)
1. 檢視與整理所下載的影片逐字稿。
2. 配合 NotebookLM 建立與分析 AI Agent 相關的知識庫。
3. 實作專案的自動化下載與字幕提取指令碼。

---

## 🕳️ 踩坑與解決方案紀錄 (Learnings & Traps)
- **問題 1**：`ffmpeg` 安裝完成後，直接在原環境中執行 `ffmpeg` 出現 `CommandNotFoundException`。
  - **原因**：安裝程式修改了 `PATH` 環境變數，但當前執行緒的環境變數尚未更新。
  - **解決方案**：在命令中手動透過讀取 Registry 的方式更新當前 PowerShell 階段的環境變數：
    ```powershell
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
    ```
- **問題 2**：在 Windows 上透過 Python 的 `subprocess.run` 調用 `yt-dlp` 時，讀取 stdout 會因編碼不符而產生亂碼，且使用系統預設編碼可能導致檔名毀損。
  - **原因**：Windows 命令列編碼與 Python 執行環境輸出編碼預設非 UTF-8，造成 `json.loads` 解析毀損。
  - **解決方案**：
    1. 在執行 `subprocess.run` 時拷貝環境變數，並指定 `PYTHONIOENCODING=utf-8`。
    2. 使用 `res.stdout.decode('utf-8')` 解碼取得正確的 JSON 字串與繁體中文檔名。
- **問題 3**：下載 YouTube 影音串流時遇到 `HTTP Error 403: Forbidden` 錯誤，且提示缺少 JS 執行環境以破解簽章。
  - **原因**：YouTube 為防範機器人設有 signature 挑戰，`yt-dlp` 需要 JavaScript 執行環境（如 Node.js 或 Deno）來執行解密腳本。
  - **解決方案**：確保系統安裝了 Node.js（本機已安裝），並在 `yt-dlp` 執行參數中加上 `--js-runtimes node`，以順利解密並下載音軌，再以 `ffmpeg` 轉為 MP3。

---

## 💡 核心技術與概念備忘 (Key Concepts & Reference Notes)

### 1. Claude Dispatch (遠端遙控 Agent 運作概念)
* **核心定義**：Claude Dispatch（包含在 Cowork 模式中）是讓使用者能透過手機 App 在戶外直接遠端遙控「本機電腦端 Agent」執行自動化對話與任務的技術。
* **運作模式**：
  * **手機與電腦連動**：在手機下載 Claude App 並於 Dispatch 介面輸入對話指令。
  * **非同步/背景化遙控**：例如在戶外下達「幫我出考卷」指令，家中的電腦端 Agent 會自動在背景完成出題並存檔，無須使用者守在電腦旁。
  * **替代傳統方案**：等同內建遠端遙控伺服器（如 LogMeIn/龍蝦軟體）的功能。
* **使用前提要件**：
  1. 需訂閱 **Claude Pro ($20 美金/月)** 方案。
  2. 家中電腦必須保持**開機、不休眠**狀態。
  3. 網頁端/瀏覽器上相關的帳號必須**預先登入完成**，以便 Agent 順利接管並執行網頁操作與自動化任務。

