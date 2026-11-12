<div align="center">

# 🗂️ File Organizer

### Turn a messy folder into a clean one with a single command.

Zero dependencies. 18 built-in categories. Never overwrites your files.

![Python](https://img.shields.io/badge/Python-3.6%2B-3776AB?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Dependencies](https://img.shields.io/badge/Dependencies-None-brightgreen)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)
![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-orange)

</div>

---

## 😩 The Problem

Your **Downloads** folder has 400 files: PDFs next to images next to installers next to random `.zip` files. Finding anything takes longer than the work itself.

## ✨ The Solution

Drop in one script, run it, done.

```
BEFORE                         AFTER
├── cv.pdf                     ├── PDF/
├── photo.jpg                  │   └── cv.pdf
├── setup.exe                  ├── Images/
├── notes.txt                  │   └── photo.jpg
├── song.mp3                   ├── Executables & Installers/
├── project.zip                │   └── setup.exe
└── data.xyz                   ├── Text Files/
                               │   └── notes.txt
                               ├── Audio/
                               │   └── song.mp3
                               ├── ZIP & Archives/
                               │   └── project.zip
                               └── XYZ/
                                   └── data.xyz
```

---

## 🚀 Features

| Feature | Description |
|---|---|
| ⚡ **O(1) lookups** | The category map is flattened into a dictionary, so each file is classified instantly |
| 📦 **18 categories** | PDFs, images, videos, audio, archives, code, fonts, e-books, databases, and more |
| 🧠 **Smart fallback** | Unknown extension like `.xyz`? A folder named `XYZ/` is created automatically |
| 📁 **No-extension handling** | Files without an extension go to `Others/` |
| 🛡️ **Overwrite protection** | Name clash? `report.pdf` becomes `report (1).pdf`, then `(2)`, and so on |
| 🙈 **Safe skipping** | Ignores hidden files, existing folders, and the script itself |
| 🧯 **Error resilient** | One locked file never stops the whole run |
| 🪶 **Zero dependencies** | Pure Python standard library (`pathlib`, `shutil`, `os`, `sys`) |

---

## 📋 Supported Categories

| Folder | Extensions |
|---|---|
| **PDF** | `.pdf` |
| **RAR** | `.rar` |
| **ZIP & Archives** | `.zip` `.7z` `.tar` `.gz` `.bz2` `.xz` `.tgz` `.cab` |
| **Word Documents** | `.doc` `.docx` `.odt` `.rtf` |
| **Excel Spreadsheets** | `.xls` `.xlsx` `.ods` `.csv` |
| **PowerPoint** | `.ppt` `.pptx` `.odp` |
| **Images** | `.jpg` `.jpeg` `.png` `.gif` `.bmp` `.svg` `.webp` `.tiff` `.ico` `.heic` `.raw` `.psd` `.ai` `.eps` |
| **Videos** | `.mp4` `.mkv` `.avi` `.mov` `.wmv` `.flv` `.webm` `.m4v` `.mpg` `.mpeg` `.3gp` |
| **Audio** | `.mp3` `.wav` `.flac` `.aac` `.ogg` `.m4a` `.wma` `.mid` `.midi` |
| **Executables & Installers** | `.exe` `.msi` `.apk` `.app` `.dmg` `.deb` `.rpm` `.bin` |
| **Code & Scripts** | `.py` `.java` `.js` `.html` `.htm` `.css` `.cpp` `.c` `.cs` `.php` `.swift` `.go` `.rb` `.sh` `.bat` `.ps1` `.json` `.xml` `.yaml` `.yml` `.sql` |
| **Text Files** | `.txt` `.md` `.log` |
| **Fonts** | `.ttf` `.otf` `.woff` `.woff2` `.eot` |
| **3D & Design** | `.blend` `.obj` `.fbx` `.stl` `.dwg` `.dxf` `.fig` `.sketch` |
| **Databases** | `.db` `.sqlite` `.sqlite3` `.mdb` `.accdb` |
| **E-Books** | `.epub` `.mobi` `.azw3` |
| **Torrents** | `.torrent` |
| **Disc Images** | `.iso` `.img` `.vcd` |


---

## ⚙️ Setup

File Organizer uses only Python's standard library. There is nothing to install with
`pip`.

### 1. Download the project

Choose either option:

- Download the repository as a ZIP from GitHub and extract it.
- Clone it with Git:

  ```bash
  git clone https://github.com/Ali1180-uni/file-organizer.git
  cd file-organizer
  ```

The main file is named `Organizer.py` (capital `O`).

### 2. Install Python

Python 3.6 or newer is supported. Check whether it is already installed:

```text
Windows:  py --version
Linux:    python3 --version
```

If a command is not recognized, install Python from [python.org](https://www.python.org/downloads/).
On Windows, enable **Add Python to PATH** during installation. On Linux, install
Python using your distribution's package manager if it is not already available.

### 3. Prepare a folder

For the safest first run, create a temporary folder and copy a few test files into
it. The organizer changes the folder immediately; it does not provide an undo
command.

> **Important:** The script organizes the folder where you run the command, not the
> folder containing `Organizer.py`.

---

## ▶️ Usage

### Windows PowerShell

From the project folder, run the organizer on your Downloads folder:

```powershell
Set-Location "$HOME\Downloads"
py "C:\path\to\File Organizer\Organizer.py"
```

If `py` is unavailable but `python` works:

```powershell
Set-Location "$HOME\Downloads"
python "C:\path\to\File Organizer\Organizer.py"
```

### Windows Command Prompt

```bat
cd /d "%USERPROFILE%\Downloads"
py "C:\path\to\File Organizer\Organizer.py"
```

Replace `C:\path\to\File Organizer` with the actual location of the project.
Keep the quotes if any folder name contains spaces.

### Linux

Open a terminal and run:

```bash
cd ~/Downloads
python3 "/path/to/File Organizer/Organizer.py"
```

You can also copy the script into the folder you want to organize:

```bash
cp "/path/to/File Organizer/Organizer.py" ~/Downloads/
cd ~/Downloads
python3 Organizer.py
```

### What happens

The script:

1. Scans files in the current folder only.
2. Creates category folders such as `Images`, `PDF`, and `Text Files`.
3. Moves each file into its matching category.
4. Creates a folder from an unknown extension, such as `XYZ` for `data.xyz`.
5. Renames duplicates as `report (1).pdf`, `report (2).pdf`, and so on.

Example output:

```text
Organizing files in: C:\Users\Ali\Downloads

Moved: cv.pdf -> PDF/
Moved: photo.jpg -> Images/
Moved: data.xyz -> XYZ/

File organization complete!
```

Run the command again whenever you want to organize new files added to the folder.

---

## ⚠️ Safety Notes

Read these before your first run:

- 🚫 **No undo.** Test on a dummy folder first.
- 📍 **Check your location.** Running from your home directory or a project root will rearrange files there.
- 💻 **Don't run it inside a coding project.** `.json`, `.yaml`, `.html`, `.css`, and `.sql` files get moved into `Code & Scripts/` and can break your project.
- 📂 **Not recursive.** Files already inside subfolders are left untouched.

---

## 🔧 Customization

Add or change categories by editing the `FILE_CATEGORIES` dictionary:

```python
FILE_CATEGORIES = {
    'Resumes': ['.pdf'],             # note: the last mapping for an extension wins
    'Design Assets': ['.xd', '.afdesign'],
    # ...
}
```

Each extension maps to exactly one folder. If an extension appears twice, the later entry overrides the earlier one.

---

## 🧠 How It Works

```
┌────────────────────┐
│  FILE_CATEGORIES   │  folder -> [extensions]
└─────────┬──────────┘
          │ flatten
          ▼
┌────────────────────┐
│ extension_mapping  │  extension -> folder   (O(1) lookup)
└─────────┬──────────┘
          │
          ▼
  for each file in cwd:
     skip dirs / hidden files / this script
     pick target folder (mapped, fallback, or "Others")
     create folder if missing
     resolve name collisions -> "name (1).ext"
     shutil.move()
```

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repo
2. Create a branch: `git checkout -b feature/dry-run`
3. Commit: `git commit -m "Add dry-run mode"`
4. Push: `git push origin feature/dry-run`
5. Open a Pull Request

---

## 📄 License

Released under the [MIT License](LICENSE).

---

<div align="center">

### ⭐ If this saved you time, please star the repo. It helps others find it!

Built by [Muhammad Ali](https://github.com/Ali1180-uni)

</div>
