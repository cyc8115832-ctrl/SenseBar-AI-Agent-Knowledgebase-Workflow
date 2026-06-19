# 專案筆記 (Project Notes) - 三師爸Sense Bar的agent

## 🎯 專案里程碑與進度

### 1. 專案初始化 (2026-06-19)
- [x] 盤點專案目錄，確認環境目前僅包含 `yt-dlp.exe`。
- [x] 確認 `FFmpeg` 安裝狀態：發現本地未安裝，並透過 `winget` 成功為系統安裝 `Gyan.FFmpeg` 8.1.1。
- [x] 建立基礎設定文件：`.gitignore`、`ANTIGRAVITY.md`、`README.md`。
- [ ] 初始化本地 Git 儲存庫並提交首次 Commit。

---

## 🚀 下一步計畫 (Next Steps)
1. 完成 Git 儲存庫初始化。
2. 與使用者確認接下來需要實作的引導/自動化指令。
3. 建立常用指令的封裝指令碼 (e.g. `download_mp3.ps1` 或 `download_video.ps1`)。

---

## 🕳️ 踩坑與解決方案紀錄 (Learnings & Traps)
- **問題**：`ffmpeg` 安裝完成後，直接在原環境中執行 `ffmpeg` 出現 `CommandNotFoundException`。
- **原因**：安裝程式修改了 `PATH` 環境變數，但當前執行緒的環境變數尚未更新。
- **解決方案**：在命令中手動透過讀取 Registry 的方式更新當前 PowerShell 階段的環境變數：
  ```powershell
  $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
  ```
