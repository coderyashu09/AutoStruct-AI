# 📁 AutoStruct AI

**AutoStruct AI** is a Python + Streamlit application that **automatically generates folder and file structures** from a simple `.txt` file.
Simply upload your text file, select a drive, and the app will instantly create the exact folder and file hierarchy for you.

---

## ✨ Key Features

* 🔹 **Upload a `.txt` file** describing your folder structure
* 🔹 **Instantly generate nested folders and files**
* 🔹 **Web-based UI** using Streamlit — no coding required
* 🔹 **Cross-platform** (Windows, macOS, Linux)
* 🔹 **Beginner-friendly & lightweight**

---

## 📂 Example

### **Input File (`structure.txt`)**

```
prompt_to_planet
├── app.py
├── generator
│   ├── story_gen.py
│   ├── map_gen.py
│   └── image_gen.py
├── assets
│   ├── maps
│   ├── images
│   └── stories
├── requirements.txt
└── README.md
```

### **Generated Output**

```
E:\prompt_to_planet\
├── app.py
├── generator\
│   ├── story_gen.py
│   ├── map_gen.py
│   └── image_gen.py
├── assets\
│   ├── maps\
│   ├── images\
│   └── stories\
├── requirements.txt
└── README.md
```

---

## 🛠 Installation

1️⃣ **Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/AutoStruct-AI.git
cd AutoStruct-AI
```

2️⃣ **Create a virtual environment (optional but recommended)**

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux/Mac**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3️⃣ **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage (Web Interface)

1. Start the Streamlit app:

```bash
streamlit run streamlit_app.py
```

2. Open the app in your browser:
   👉 [http://localhost:8501](http://localhost:8501)

3. Steps in the Web App:

   1. **Upload** a `.txt` file with your folder structure
   2. **Select drive letter** (C, D, E…)
   3. **Enter root folder name**
   4. **Click Generate Structure**
   5. ✅ Your folders and files are automatically created!

---

## 📦 Project Structure

```
AutoStruct AI/
├── assets/
│   └── sample_structure.txt      # Example input file
├── file_parser.py                # Parse .txt into file paths
├── file_creator.py                # Create folders & files
├── main.py                        # CLI version (optional)
├── streamlit_app.py               # Web-based UI
├── requirements.txt
└── README.md
```

---

## 📸 Screenshots

*(Optional: Add screenshots of your Streamlit interface here)*

---

## 🤝 Contributing

1. **Fork** the project
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add AmazingFeature'`)
4. **Push to branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request** 🎉

---

## 📜 License

MIT License © 2025 \coderyashu09

---
Feel free to use and modify this project for your needs.

