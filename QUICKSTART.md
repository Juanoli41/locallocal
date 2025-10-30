# Quick Start Guide - LocalLocal AI Chat

## 🚀 Steps to Run the Application

### Method 1: Easy Windows Launch (Recommended)
1. **Double-click** `start_app.bat`
2. **Wait** for the server to start (you'll see startup messages)
3. **Open your browser** and go to: `http://localhost:8000`
4. **Start chatting!**

### Method 2: Command Line
1. **Open terminal/command prompt**
2. **Navigate to project folder:**
   ```bash
   cd "c:\Users\juano\OneDrive - The University of Texas-Rio Grande Valley\CODE PROJECTS\locallocal"
   ```
3. **Run the application:**
   ```bash
   python app.py
   ```
4. **Open browser** to: `http://localhost:8000`

### Method 3: First Time Setup (if on a new computer)
1. **Install Python 3.8+** (if not already installed)
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the app:**
   ```bash
   python app.py
   ```
4. **Open browser** to: `http://localhost:8000`

---

## 🎯 What You'll See

### Server Output (Normal):
```
INFO:__main__:Mock AI models initialized successfully!
INFO:__main__:Starting LocalLocal AI Chat server...
INFO:     Started server process [XXXXX]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

### Web Interface:
- Beautiful gradient UI
- Text input area
- Three model options:
  - **Gemma 2-2B**: Direct intelligent responses
  - **Arch Router**: Query analysis and routing
  - **Both Models**: Combined pipeline analysis + response

---

## 🧪 Test Questions to Try

### Factual Questions:
- "How many states in the United States?"
- "What's the capital of the USA?"
- "What's the speed of light?"

### Math & Science:
- "What's 2+2?"
- "Explain photosynthesis"
- "What is DNA?"

### Technology:
- "What is Python programming?"
- "Explain JavaScript"
- "What is HTML?"

### Creative:
- "Tell me a joke"
- "Write a short story"

### General:
- "Hello!"
- "What can you help me with?"

---

## ⏹️ How to Stop the Server

### From Terminal:
- Press `Ctrl + C` in the terminal window

### From Batch File:
- Close the command window or press `Ctrl + C`

### Force Stop (if needed):
```bash
pkill -f "python app.py"
```

---

## 🔧 Troubleshooting

### Server Won't Start:
- Check if port 8000 is already in use
- Try: `python --version` to ensure Python is installed
- Reinstall dependencies: `pip install -r requirements.txt`

### Can't Access Web Interface:
- Make sure server shows "Uvicorn running on http://0.0.0.0:8000"
- Try: `http://127.0.0.1:8000` instead of localhost
- Check Windows Firewall settings

### Import Errors:
- Reinstall dependencies: `pip install fastapi uvicorn jinja2 python-multipart`

---

## 📂 File Structure Reminder

```
locallocal/
├── app.py                    # ← Main application (run this!)
├── start_app.bat            # ← Easy Windows launcher
├── requirements.txt         # ← Dependencies list
├── README.md               # ← Full documentation
├── QUICKSTART.md           # ← This file
└── templates/
    └── index.html          # ← Web interface
```

---

## 🌟 Key Features

✅ **No Heavy AI Dependencies** - Runs on any computer  
✅ **Intelligent Responses** - Actually answers your questions  
✅ **Beautiful UI** - Professional web interface  
✅ **Fast Startup** - Ready in seconds  
✅ **Cross-Platform** - Works on Windows, Mac, Linux  

---

**That's it! Your AI chat application is ready to use anytime! 🎉**