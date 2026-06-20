# Google Antigravity 2.0 來了：AI 開發進入多 Agent 時代？

- **影片連結**: https://youtu.be/bstR13jNtzM?si=0k9SZ5oh-yyUXKkC
- **語音轉譯來源**: Whisper 本地語音辨識 (base model)
- **檔案生成日期**: 2026-06-20

---

## 📌 影片摘要 (Summary)

本期影片由 Yuya Mei 分享 Google 新推出的 **AntiGravity 2.0** 大型更新，深入探討 AI 程式開發工具的未來趨勢。作者認為，本次升級最核心的意義在於：**AI 工具正從「聊天輔助編碼器」蛻變為「管理多個 Agent 的操作系統 (Agent Control Center)」**。

### 核心要點：
1. **定位轉變**：
   - 傳統 IDE 聚焦於檔案編輯、終端機與除錯；而 AntiGravity 2.0 聚焦於**任務編排、多 Agent 並行執行、後台自動化**與**項目狀態管理**。它就像是一個 AI 開發的指揮調度台（Mission Control）。
2. **底層模型 - Gemini 3.5 Flash**：
   - 專為 **Agentic Workflow**（工具調用、多步驟任務、持續執行）設計。
   - 在編碼和 Agent 基準測試上超越了 Gemini 1.0 Pro，且輸出速度是其他前沿模型的四倍，兼顧速度與成本，非常適合長時間運作的 Agent 任務。
3. **IDE 新功能實測**：
   - **客製化 Skill**：支援自動讀取與配置自訂 Skills。
   - **任務排程 (Schedule Task)**：支援在特定時間自動執行特定的 Agent 任務。
   - **工作控制台**：分為 **Mission Center**（長遠宏觀目標）與 **Control Center**（每日任務跟進）。
4. **CLI 工具與多 Agent 協作**：
   - 介紹了如何安裝並使用 AntiGravity CLI，並示範將其與 **Claude (負責宏觀計劃)**、**Codex/GPT-CodeX (負責編碼與除錯)** 聯合使用，以提高開發效率。
5. **開發者的三大反思與學習**：
   - **任務拆解**：將開發流程拆分為 Research、Architecture、UI、Backend、Testing 與 Deployment。
   - **Agent 管理**：明確各個 Agent 的職責並進行有效協調。
   - **審核與程式碼審查 (Code Review)**：AI 生成程式碼速度越快，開發者的審核能力（包含安全性、是否破壞舊有功能、是否符合產品目標）就越關鍵。

---

## 📖 專有名詞解析 (Glossary)

為了方便讀者閱讀，以下整理影片中出現的核心專有名詞與概念解析：

* **IDE (Integrated Development Environment，整合開發環境)**：
    * **解釋**：供工程師編寫、測試、除錯軟體的整合性軟體工具（例如著名的 VS Code、Cursor 或 Xcode）。傳統 IDE 主要提供代碼檔案編輯與終端機環境。
* **CLI (Command Line Interface，命令列介面)**：
    * **解釋**：不使用圖形視窗與滑鼠，而是純粹透過鍵入文字指令（Command）來操作系統或軟體的工具（例如 Windows 的 PowerShell 或 macOS 的 Terminal）。
* **Agent / AI Agent (AI 代理/智能體)**：
    * **解釋**：相較於一般的 AI 問答，Agent 具有自主的行動力。給予它一個長遠目標後，它能自主規劃步驟、讀寫檔案、執行指令、並在出錯時自我修正直至任務完成。
* **SDK (Software Development Kit，軟體開發套件)**：
    * **解釋**：由平台官方提供，包含函式庫、工具及說明文件，用以協助開發者在此平台上建立特定應用程式的懶人工具包。
* **Vibe Coding (氛圍編程/感知開發)**：
    * **解釋**：新興的 AI 開發術語。指開發者不親自動手編寫程式碼，而是充當決策與規劃的角色，給出描述（Vibe），讓 AI Agent 去做底層寫程式的苦工。

---

## 🎙️ 完整逐字稿 (Transcript)

哈囉，歡迎回到網均大。那今天想跟大家分享的是 Google AntiGravity 2.0 的一個更新。想要跟小夥伴們分享，這一次呢，不光是有 AntiGravity 的更新，也有就是 Gemini 3.5 Flash 這個模型的一個更新。

我覺得最重要的一點，這一次不是一個新的界面，也不是模型的速度更快。我覺得真正的重要的是，它是從一個聊天工具，變成了一個管理 Agent 的操作系統。這一次的更新呢，它讓我們——我覺得它更像是 Agent 的 Ctrl Center（控制中心），一個可以管理 Agent 的中心，這可能也是未來的方向。

那今天分享呢，就是要分享幾個內容：一個是這個更新怎麼操作使用、它有哪些特別的功能；然後呢，也跟大家分享你還是可以繼續使用 AntiGravity IDE，但是它也有一些不同；還有一個就是最重要的，它也有了 AntiGravity 的 CLI，我會教大家怎麼安裝，你也可以搭配著 Codex 或 Claude 一起使用在你的 AntiGravity 裡面。如果你對今天內容感興趣，那就不要錯過，讓我們就廢話不多說開始吧！

### 1. 什麼是 Agent-First Developer Platform？
Google 新推出的 Agent-First Developer Platform，Google 官方說它不只是一個 Coding 的 assistant，它是一個可以開發和管理、自動管理 Agent 的平台。它有一個新的獨立的桌面，然後呢，可以作為 Agent Interaction 的一個中心，讓用戶協調多個 Agent 去並行執行任務。

所以傳統的 IDE 是以「代碼文件、終端、編輯器、調試器」為核心；而 2.0 核心變了，是以「任務」還有就是「Agent 的並行執行、後台自動化、項目狀態」為核心。它給你一個可以調度 AI Agent 的工作台，這就是這次升級的重要的變化。

### 2. 底層模型 Gemini 3.5 Flash 為什麼很重要？
這次 AntiGravity 2.0 背後的模型就是 Gemini 3.5 Flash，它的定位很明確：它不是單純的追求最強的推理，而是真實的 Agentic Workflow——也就是長任務、多步驟、需要工具調用和持續執行的工作流。

Google 官方說 Gemini 3.5 Flash 在 Coding 和 Agentic Benchmark 超過了 Gemini 1.0 Pro，並且輸出速度是其他的 frontier model 的四倍。所以對開發者來說，AI Coding 不是寫一段漂亮的回答就結束，而是真正開發一個項目。模型要不斷地去讀取項目的結構、理解上下文、修改文件、進行命令執行、查看錯誤日誌、重新修復等等。這些任務最怕的不是模型不夠聰明，而是太慢或者是太貴，還有上下文斷掉或者是跑一半失控。

所以 3.5 Flash 這次的定位很現實：就是把它作為一個可以大量調用，並且可以並行運行、適合 Agentic 長時間工作的模型。所以它和 AntiGravity 2.0 在一起，就是一個模型的大腦加上一個 Agent 的工作 Runtime。

### 3. AntiGravity 2.0 IDE 界面與功能介紹
這個是新的 AntiGravity IDE，你可以登入到 Google，然後你就可以使用。然後你就根據它的指示，例如你選擇你的 Theme，你也可以選擇例如 Google AntiGravity SDK，你都可以選擇你想要的。例如我真的就選了 SDK，我也選擇了 Chrome DevTools，還有一個就是我選擇了 Web Guidance，然後你就可以進入。

然後你可以看到，這邊就是你的 Folder、你的項目，所有的項目應該都是在這裡。然後你可以去建立，或者是開一個項目在本地都可以。然後你也可以選擇模型，現在我是選擇 Gemini 3.5 Flash。然後你也可以換 Folder。真的，還有就是 Conversation History，你也可以有一個新的 Conversation 介面，非常的簡單。

還有一個它有一個新的工具，就是 Schedule Task 工具，我們可以去——待會兒可以去嘗試 Schedule Task。例如這個地方好像它也有一些 Settings，然後你可以在這裡 Settings，例如 Account、Permission、Appearance。這裡就是你可以定制化你的模型（現在是 3.5 Flash）。然後你也可以 customize，這邊你可以看到它自己就有很多 Skill，它全部是它自己自帶的 Skill 在這裡。然後你也可以讓它上網，它也有一些 App 的設定。

我們來測試一下這個 AntiGravity 的新的功能。這邊就是你的 Project，你如果要開一個新的 Project，你可以在這裡開一個 Quick Start。然後這裡我開一個，你可以加一個 Thread，這裡可以開一個新的 Worktree。例如你寫的，從複製一個都可以用。

那我就是想要問它，然後就告訴它我這個項目裡面，讓它幫我看一下哪些已經做好了，哪些還沒有做。去 IDE 的 OpenIDE，這裡就是你可以去 IDE 的這裡。然後你也可以看它的現在的狀態，這裡就是你的 Super Agent，還有你的 Files Changed、Artifacts、Background Task，都在這裡。然後它每一次例如在執行 Command，它也會跟我們確認 Yes。

可以看到它跟我——看到現在我這個項目其實還是做了一段時間了，然後呢，它告訴我這些都是已經做好了，例如 Phase 1、Phase 2、Phase 3，現在應該是 Phase 5。然後呢，你可以讓它——然後是 Phase 5 的 Plan。你可以讓它繼續幫你製作。

可以看到這裡呢，就是我想要它幫我做 Phase 5，它不是說做了多少步嗎？然後我讓它做一個 Plan。可以看一下這個 Plan，這個和以前的 AntiGravity 也是一樣的，它告訴你需要做這些。然後呢，你如果是覺得同意，那你就可以讓它繼續幫你做，然後它就可以幫你製作。例如這個完了，我們可以待會兒可以去看一下，這就是它剛剛製作的。

然後呢，你也可以去看看這個 Worktrees，它和以前的 AntiGravity 也是一樣的。你可以看這個 Worktrees 就是它做了些什麼事情，然後你也可以 Review code，都會在這邊。

### 4. 實戰演練：Mission Center 與 Control Center
我們讓它幫我們看一下最後的產品是什麼樣子的，它也會給你一個預覽。那你可以看到，這個就是我的 AI-BMS OS 這個 Control Center。它其實分了兩個部分，一個是 Mission Center，一個是 Control Center。

那 Mission Center 呢，就是一個宏觀的，例如長遠的你的目標是什麼。大家可以看一下，例如我這個是做給創作者、小企業者管理工作的。另外一個呢，就是你可以在這裡創建 Mission，然後你可以去你的 Control Center。這個就是說你每天要幹什麼的，這就相當於你可以每天跟進。

預計後面還會做記憶，還有就是——那我這一次做的主要是商業的。它也有了 Schedule 的功能，例如 Schedule Task，真就可以 Create New Task。然後呢，也是這個 Folder，你可以選擇其他的 Folder（例如你的其他項目）。例如我要做這個，下午 5 點鐘，然後寫一個 Prompt，然後呢就可以 Schedule Task。然後每天 9 點鐘的時候，他就會做這個工作。

### 5. 怎麼在本機安裝 AntiGravity CLI 搭配其他 AI
我想跟大家分享怎麼在環境中加所有 AI。首先，你可以例如我這裡是 AntiGravity IDE，我可以這裡開一個 Terminal，然後呢，你就可以在這裡複製這一段指令。如果你是像我一樣，你複製這個，然後呢，你就可以安裝這個 Package。

安裝好了之後呢，你需要選擇一些東西，它和這一個還是挺像的，你就選擇 AGB 它就可以開始了。然後呢，它還是可以做一些設定，以後也會有 Plugin，像 Cloud Code 一起有一些額外的功能。當然我這裡就選擇例如 Theme，我是喜歡這種比較暗黑一點的顏色，所以選擇我選這個。我可以看看其他的，我應該是會選這個。這個之後呢，你就選好了之後，就是按照它的說明，你就選 Yes 就可以了，選擇 Done，然後 OK，那你就安裝好了。

安裝好了之後呢，你就可以讓它 Trust 這個 Folder，然後呢，你就可以讓它幫你做事情。然後你可以搭配著使用：你不光是可以用 CLI，你可以用例如 Claude，然後你可以直接把 Claude 叫出來，然後它也可以幫你做計劃。我覺得我喜歡 Claude 做宏觀的計劃，就比較大型的計劃，我覺得它在計劃方面比較厲害；然後呢，你也可以用 Codex 以 Debug，然後來寫程序。

那我就是一般有時候也會把 Codex 聯合著使用，這就是 Claude 使用，然後這個就是 Codex 使用，它是 3.5 或其他的模型，然後這個就是 AntiGravity 使用，你可以搭配著用，可以提高效率。所以這就是怎麼使用 CLI 的一個方式。

### 6. 開發者從中學會的三件事
那這一次 Google 的更新讓我學會了三件事：
1. **第一，你要學會拆解任務**：你要把如果說你要做一個 app，你要拆成 Research、Architecture、UI、Backend、Testing 還有 Deployment 的六個任務，每個任務會對應一個 Artifacts。
2. **第二，你就要學會管理 Agent**：不是每個 Agent 都清楚自己的職責，那你要學會管理 Agent。
3. **第三，就是要學會 Review（審核）**：AI 生成的程式碼越快，你越不能直接相信。你要更改哪些文件、怎麼改、怎麼測試、它會不會破壞原來的功能，還有安全風險，是不是符合你的 PR 還有產品的目標，這些你都需要能夠有審核的能力。

所以我覺得這一次 AntiGravity 2.0，它不一定能立刻成為你主力的工具，但是它有很大的價值，就是你可以看到未來 AI Coding 的新方向。
