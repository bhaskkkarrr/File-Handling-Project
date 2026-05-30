# Command-Line File Management System
A lightweight, interactive command-line application built in Python that allows users to perform basic CRUD (Create, Read, Update, Delete) operations on files and folders. The project utilizes Python's modern `pathlib` module and `os` module for clean and efficient file system manipulation.

## 🚀 Features

* **View Directory Structure:** Automatically lists all existing files and folders before every operation to help you keep track of your directory.
* **Create Files:** Create new files and write initial content to them safely (prevents overwriting existing files).
* **Read Files:** Read and display the text content of any existing file directly in the terminal.
* **Update Files:** Offers three flexible update options:
    * Rename the file.
    * Overwrite existing content.
    * Append new text to the end of the file.
* **Delete Files:** Permanently remove specified files from the local directory.
* **Error Handling:** Equipped with `try-except` blocks to handle unexpected exceptions smoothly without crashing the application.

## 📂 Project Structure

```text
├── main.py          # The core script containing the file management logic
└── README.md        # Project documentation
