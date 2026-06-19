# AntiGravity Project Rules & Metadata - 三師爸Sense Bar的agent

## 專案基本資訊
- **專案名稱**：三師爸Sense Bar的agent
- **主要用途**：利用 `yt-dlp` 進行影音下載與處理的自動化 Agent 工具。
- **核心工具**：
  - `yt-dlp` (位於專案根目錄 [yt-dlp.exe](file:///d:/user/Documents/三師爸Sense%20Bar的agent/yt-dlp.exe))
  - `ffmpeg` (已透過 `winget` 安裝至系統 PATH 中)

## 開發規範與工作流
1. **開工/收工流程**：
   - 開工時載入 `antigravity-workflow` 指引，檢查並回報狀態。
   - 收工時檢查敏感資料，更新專案筆記，僅 stage 與本次變更相關的檔案並 commit。
2. **Git 規範**：
   - 僅在本地進行版本控制，不自動進行 remote push。
   - 保持 Commit 訊息明確具體。
3. **工具調用**：
   - 本地調用 `yt-dlp.exe` 時，應在命令列中使用相對路徑 `./yt-dlp.exe` 或絕對路徑。
   - 轉檔或合併影音時會自動調用系統中的 `ffmpeg`。
