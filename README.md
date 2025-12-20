# 🖱️ AutoClicker by Pedro Heinrich

A simple, efficient, and safe AutoClicker built with **Python**. It features a graphical interface (GUI) and a "Safety Motion" trigger that stops the automation if the mouse is moved.

## 🌟 Features

* **Coordinate Capture:** Select the click target directly on your screen with a single mouse click.
* **Safety Motion Stop:** Automatically stops clicking if the user moves the physical mouse away from the target.
* **Non-Blocking GUI:** Built with Multi-threading to ensure the window remains responsive during execution.
* **Visual Feedback:** Real-time status updates and click counter.
* **Clean Design:** Simple and intuitive buttons with color-coded states.

## 🛠️ Built With

* **[Python](https://www.python.org/)** - Core language.
* **[Tkinter](https://docs.python.org/3/library/tkinter.html)** - Graphical User Interface.
* **[PyAutoGUI](https://pyautogui.readthedocs.io/)** - Mouse control and automation.
* **[Pynput](https://pynput.readthedocs.io/)** - Mouse event listening.
* **[Threading](https://docs.python.org/3/library/threading.html)** - Concurrent execution.

## 📋 Prerequisites (Linux Mint / Ubuntu)

To allow Python to control your hardware on Linux (X11), you must install the following system dependencies:

```bash
sudo apt update
sudo apt install python3-tk python3-dev libpng-dev libjpeg-dev scrot

```

## 🔧 Installation & Setup

1. **Clone the repository:**
```bash
git clone [https://github.com/pedroantonioheinrich/auto-clicker/]
cd auto-clicker

```


2. **Create and activate a Virtual Environment:**
```bash
python3 -m venv .venv
source .venv/bin/activate

```


3. **Install Python dependencies:**
```bash
pip install pyautogui pynput Pillow

```



## 📖 How to Use

1. **Run the script:**
```bash
python auto.py

```


2. Click the **"Select Target"** button.
3. Click anywhere on your screen to define the  and  coordinates.
4. The AutoClicker will start immediately at the selected position.
5. **To Stop:** Simply move your mouse away from the target or click the **"Stop"** button in the app.

## 📦 Building the Executable

To generate a standalone binary for Linux:

1. Install PyInstaller:
```bash
pip install pyinstaller

```


2. Run the build command:
```bash
pyinstaller --onefile --windowed --icon=icone.png auto.py

```


3. Find your executable in the `dist/` folder.

## 📄 License

This project is open-source and available under the **MIT License**.

---
