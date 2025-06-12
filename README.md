# 🗺️ Project Context Mapper

Would you like your favorite AI (ChatGPT, Gemini, Claude, etc.) to understand your project **like a human** before programming, debugging, or adding new features?
This project is the ultimate solution to map the contents of any development project, file by file, and provide AIs with **the real context they need** to truly help you!

---

## 🚀 What is Project Context Mapper?

Project Context Mapper is a tool designed for developers, teams, and communities who want to give AIs the **maximum possible context** about the state, structure, and content of their projects, but with **total control** over what to share and how.
The tool generates a snapshot of your source code into a single text file, with different levels of depth and customization.

---

## 🎯 Project Goals

* **Facilitate collaboration** between humans and AIs in development tasks.
* Enable AIs to better understand the context, dependencies, and real organization of any code.
* Provide fast and controlled snapshots for tasks such as:

  * AI-assisted development.
  * Advanced debugging and troubleshooting.
  * Refactoring with global context.
  * Fast onboarding of new members (humans or bots).
  * Documentation and security analysis.

---

## 🧩 Capture Modes

You can choose among **4 modes** depending on the goal and size of your project:

1. **Capture the ENTIRE project**
   Ideal for small projects or when you want the AI to know absolutely everything (structure + content).

2. **Capture only paths**
   Perfect for large projects or when you only want the AI to understand the **structure** (file and directory tree), without showing the internal content of each file.

3. **Capture only certain files**
   Useful when the AI already knows the structure, but needs to see the contents of **key** files for a specific feature or bug, without overloading the context with unnecessary info.

4. **Combination of paths + some full files**
   The advanced mode!

   * Provides the complete project structure.
   * Adds the content of only **some relevant files** (defined by a whitelist).
   * Utility: Provide specific and efficient context for debugging or incremental development without losing the global view.

---

## 🆕 About `--whitelist` option

The `--whitelist` argument accepts **both file and directory paths** (relative to the project root or absolute).  
If you include a **directory**, the snapshot will include the **full content of all files inside that directory recursively**.

**Examples:**

```bash
# Include a specific file and all files inside a directory
python snapshot_project.py /path/to/project --only-paths --whitelist=app/main.py,app/services

# With spaces (use quotes)
python snapshot_project.py /path/to/project --only-paths "--whitelist=app/main.py, app/services"
```

* Passing a file: includes only that file's content.
* Passing a directory: includes all files within that directory and its subdirectories with full content.

> If any whitelist path does not exist, the script will abort and notify you of the invalid routes.

---

## 🧠 Recommended AI Interaction Strategy

To get the most out of Project Context Mapper and improve collaboration with the AI, we recommend this strategy:

1. First, provide the AI with the complete project structure, either without content or with basic content of key files like application startup, global structure, and navigation. This gives a solid overview without overwhelming it with unnecessary details.

2. Second, allow the AI to identify which specific files it needs to review to address the request or solve the problem.

3. Third, after that identification, ask the AI to give you a list of the required files, separated by commas.

4. Finally, use that list to generate a second snapshot with Project Context Mapper, including only the content of those specific files. This ensures the AI works with relevant, up-to-date information, optimizing time and accuracy.

---

## ✂️ Smart Exclusion of Files and Folders

Project Context Mapper automatically **ignores** files and directories that are not relevant for AI analysis, such as:

* Folders: .git, .cache, node\_modules, dist, build, .venv, **pycache**, etc.
* Files: .DS\_Store, yarn.lock, thumbs.db, etc.
* Extensions: .log, .tmp, .png, .svg, .xlsx, .csv, and other binaries or temporary files.

Need to exclude more? Just edit the EXCLUDE\_DIRS, EXCLUDE\_FILES, and ADDITIONAL\_EXCLUDES lists.

---

## ⚡ How does it work?

You only need Python 3.
Run the script indicating the project path and the desired options.

**Basic usage:**

```bash
python snapshot_project.py <project_path> [--only-paths] [--whitelist=path1,path2,...]
```

**Important note about `--whitelist` usage:**
If your whitelist contains spaces after commas, **you must enclose the entire argument in quotes** to prevent the shell from splitting it into multiple arguments. For example:

```bash
python snapshot_project.py /path/to/project --only-paths "--whitelist=app/main.py, app/database.py, app/core/security.py"
```

Alternatively, you can omit spaces after commas:

```bash
python snapshot_project.py /path/to/project --only-paths --whitelist=app/main.py,app/database.py,app/core/security.py
```

---

**Without extra parameters:**
Captures the complete content of all relevant files.

**With --only-paths:**
Only shows the folder and file structure (no content).

**With --whitelist:**
Shows only the content of specific paths/files (or folders as described above).

**Combined --only-paths + --whitelist:**
Shows the complete project structure and also the content **only** of files included in the whitelist.
Ideal to give the AI a global vision of the project, but only detailed content of certain relevant files.

---

**Usage examples:**

Capture entire project (structure and content):

```bash
python snapshot_project.py /path/to/your/project
```

Only structure (folder and file names):

```bash
python snapshot_project.py /path/to/your/project --only-paths
```

Only some specific files (structure + those full files):

```bash
python snapshot_project.py /path/to/your/project --only-paths --whitelist=src/app.py,README.md,requirements.txt
```

Or with spaces in whitelist (use quotes):

```bash
python snapshot_project.py /path/to/your/project --only-paths "--whitelist=src/app.py, README.md, requirements.txt"
```

---

**What result do you get?**
A TXT file with all structured information, ready to upload to ChatGPT, Gemini, Claude or any AI to work with real and precise context.

---

## 💡 Why is it useful for AI and the community?

* **Avoids noise**: AI works only with relevant and updated information.
* **Maximum context, minimum effort**: share only what is needed, adjust granularity.
* **Audit and traceability**: textual snapshot, portable and ideal to attach to issues, PRs or AI queries.

---

## 🔒 Security and Privacy

* You decide what to share!
* Excludes binaries, passwords, dependencies, large or sensitive files by default.
* Easily customize exclusion lists according to your project needs.

---

## 👨‍💻 Main script (main.py)

The core of the tool is an easy-to-extend Python script (main.py). Here the exclusion filters, whitelist logic and output formatting are defined, so you can adapt it to any workflow.

---

## 🙌 Contribute

Got ideas, need more modes or filters?
Want support for another language or AI integration?
Pull requests, issues, and forks are more than welcome!

---

## ⭐ Give it a star if it helps you, and share your experience using the tool with your favorite AI.

---

Make your AI really understand your project, **not just read loose lines!**
Project Context Mapper – *Taking context to the next level.*

---