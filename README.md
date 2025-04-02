# 🗓️ Smart Calendar API with Django 🐍

This is a **Django + Django REST Framework**-based smart calendar system, featuring **user authentication, JWT token verification, and full event CRUD APIs**. It is ideal for personal productivity tools, team scheduling systems, and smart calendar integrations.

![Django](https://img.shields.io/badge/Django-5.1.7-green?logo=django&style=flat-square)
![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![SQLite](https://img.shields.io/badge/SQLite-3-lightgrey?logo=sqlite)
![JWT](https://img.shields.io/badge/JWT-Authorization-yellow)

---

## 📌 Use Case Scenarios

This isn't just a simple calendar—it helps **users manage time and tasks smartly**:

✔ **For productivity enthusiasts**  
- Manage daily events, notes, and to-dos  
- Build a custom scheduling assistant with frontend integration

✔ **For team collaboration**  
- Create events for each team member  
- Connect to a notification system for reminders

✔ **For students & lifestyle planners**  
- Track study goals, assignment deadlines  
- Use the calendar for organizing life and personal projects 💗

---

## 🧩 API Endpoints

📅 Event Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   | `/api/events/` | Create a new event |
| GET    | `/api/events/` | Retrieve all events |
| GET    | `/api/events/{id}/` | Retrieve a specific event |
| PUT    | `/api/events/{id}/` | Update an event |
| DELETE | `/api/events/{id}/` | Delete an event |

🔑 User Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   | `/api/register/` | Register a new user |
| POST   | `/api/token/` | Login and obtain JWT token |
| POST   | `/api/token/refresh/` | Get a new access token using refresh token |

---

## 🌟 Features

✅ User registration & login  
✅ JWT-based authentication  
✅ Full CRUD for calendar events  
✅ Swagger auto-generated documentation  
✅ ReDoc support  
✅ CORS enabled for cross-origin requests  
✅ SQLite as the default database

---

## 📖 API Documentation

Once the server is running, you can view the API docs at:

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🚀 Installation & Startup

### 1️⃣ Create virtual environment and install dependencies
```bash
git clone https://github.com/AshleyHdev/DjangoAPI.git
cd DjangoAPI
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2️⃣ Initialize the database
```bash
python manage.py makemigrations
python manage.py migrate
```

### 3️⃣ Start the development server
```bash
python manage.py runserver
```

---

## 📁 Project Structure
```bash
DjangoAPI/
├── core/               # Project settings & URL configuration
├── events/             # Event management app
├── users/              # User app
├── templates/          # Swagger UI customization
├── manage.py           # Django entry point
├── requirements.txt    # Dependency list
└── .gitignore          # Files to exclude from version control
```

---

## 🧪 Sample API Requests (via curl)

🔐 Login to get token:
```bash
curl -X POST http://127.0.0.1:8000/api/token/ \
     -H "Content-Type: application/json" \
     -d '{"username": "your_username", "password": "your_password"}'
```

📅 Create a new event:
```bash
curl -X POST http://127.0.0.1:8000/api/events/ \
     -H "Authorization: Bearer your_access_token" \
     -H "Content-Type: application/json" \
     -d '{
           "title": "Finish Django project",
           "description": "Upload it to GitHub",
           "start_time": "2025-04-02T09:00:00Z",
           "end_time": "2025-04-02T10:00:00Z",
           "is_all_day": false
         }'
```

🔍 Retrieve an event:
```bash
curl -X GET http://127.0.0.1:8000/api/events/1/ \
     -H "Authorization: Bearer your_access_token"
```

🗑️ Delete an event:
```bash
curl -X DELETE http://127.0.0.1:8000/api/events/1/ \
     -H "Authorization: Bearer your_access_token"
```

---

## 🛠 Troubleshooting

1️⃣ 401 Unauthorized: Make sure `Authorization: Bearer <token>` is included in the headers  
2️⃣ Database errors: Did you forget to run `migrate`?  
3️⃣ 404 Not Found: Check if the event ID exists first

---

## 💙 Author & Contributions

Author: [@AshleyH.dev](https://github.com/AshleyHdev) 💻🎨  
Feel free to star ⭐, fork 🍴, or submit PRs!

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

# 🗓️ Smart Calendar API with Django 🐍

這是一個基於 **Django + Django REST Framework** 打造的智慧行事曆系統，支援使用者註冊、JWT 驗證，並提供完整的 **行程 CRUD 管理 API**。適合用於個人日程工具、團隊排程服務等場景。

![Django](https://img.shields.io/badge/Django-5.1.7-green?logo=django&style=flat-square)
![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![SQLite](https://img.shields.io/badge/SQLite-3-lightgrey?logo=sqlite)
![JWT](https://img.shields.io/badge/JWT-Authorization-yellow)

---

## 📌 行事曆功能應用場景

這個 API 不只是簡單的行程紀錄，它可以幫助各種使用者 **更智慧地管理時間與任務**：

✔ **個人生產力愛好者**  
- 管理每天的重點行程、備忘、待辦任務  
- 搭配前端介面做成專屬時間助理  

✔ **團隊工作協作**  
- 為每個成員建立獨立行程  
- 可串接通知系統提醒即將到期事項  

✔ **學習與生活排程者**  
- 規劃唸書進度、紀錄作業期限  
- 用行事曆記錄生活目標 💗

---

## 🧩 API 端點

📅 行程管理 Event Management

| 方法 | 路徑 | 說明 |
|------|------|------|
| POST | `/api/events/` | 建立一個新的行程 |
| GET | `/api/events/` | 取得所有行程列表 |
| GET | `/api/events/{id}/` | 查詢單一行程詳細內容 |
| PUT | `/api/events/{id}/` | 更新指定行程 |
| DELETE | `/api/events/{id}/` | 刪除指定行程 |

🔑 使用者認證 User Auth

| 方法 | 路徑 | 說明 |
|------|------|------|
| POST | `/api/register/` | 註冊帳號 |
| POST | `/api/token/` | 登入並取得 JWT Token |
| POST | `/api/token/refresh/` | 透過 Refresh Token 取得新的 Access Token |

---

## 🌟 功能亮點

✅ 使用者註冊 / 登入  
✅ JWT Token 身分驗證機制  
✅ 行程 CRUD 操作完整支援  
✅ Swagger 自動產生 API 文件  
✅ ReDoc 文件備用選項  
✅ 跨來源資源請求（CORS）支援  
✅ 使用 SQLite 儲存資料  

---

## 📖 API 文件瀏覽

啟動伺服器後可以直接瀏覽自動產生的 API 文件：

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🚀 安裝與啟動方式

### 1️⃣ 建立虛擬環境並安裝依賴
```bash
git clone https://github.com/AshleyHdev/DjangoAPI.git
cd DjangoAPI
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2️⃣ 資料庫初始化
```bash
python manage.py makemigrations
python manage.py migrate
```

### 3️⃣ 啟動伺服器
```bash
python manage.py runserver
```

---

## 📁 專案結構簡介
```bash
DjangoAPI/
├── core/               # 專案設定與 URL 配置
├── events/             # 行程管理模組
├── users/              # 使用者模組
├── templates/          # Swagger 自定義模板
├── manage.py           # Django 執行入口
├── requirements.txt    # 套件需求清單
└── .gitignore          # 忽略不需上傳的檔案
```

---

## 🧪 測試範例（使用 curl）

🔐 登入並取得 Token：
```bash
curl -X POST http://127.0.0.1:8000/api/token/ \
     -H "Content-Type: application/json" \
     -d '{"username": "your_username", "password": "your_password"}'
```

📅 建立新行程：
```bash
curl -X POST http://127.0.0.1:8000/api/events/ \
     -H "Authorization: Bearer your_access_token" \
     -H "Content-Type: application/json" \
     -d '{
           "title": "完成 Django 專案",
           "description": "開心上傳 GitHub",
           "start_time": "2025-04-02T09:00:00Z",
           "end_time": "2025-04-02T10:00:00Z",
           "is_all_day": false
         }'
```

🔍 查詢行程：
```bash
curl -X GET http://127.0.0.1:8000/api/events/1/ \
     -H "Authorization: Bearer your_access_token"
```

🗑️ 刪除行程：
```bash
curl -X DELETE http://127.0.0.1:8000/api/events/1/ \
     -H "Authorization: Bearer your_access_token"
```

---

## 🛠 Debug 小提醒

1️⃣ 若出現 401 Unauthorized：請確認有帶入 `Authorization: Bearer {token}`  
2️⃣ 若資料庫連線錯誤：請確認 `migrate` 是否已正確執行  
3️⃣ 若 API 文件無法開啟：請確認有加上 `drf-spectacular` 與設定對應 URL  

---

## 💙 作者與貢獻方式

作者：[@AshleyH.dev](https://github.com/AshleyHdev) 💻🎨  
歡迎 star ⭐、fork 🍴 或留言交流！

---

## 📜 License

本專案採用 MIT 授權條款，請自由使用、修改與散佈，詳情請見 [LICENSE](./LICENSE)。
