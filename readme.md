# Marathi Spell Checker

This project is a Marathi spell checker that utilizes the Aspell library to provide spelling suggestions for Marathi words.

## Installation

Before running the Marathi spell checker, you need to install the Aspell library for Marathi. Follow these steps:

1. Install Aspell for Marathi:

   ```bash
   sudo apt-get install aspell-mr
    ```
    Replace apt-get with your distribution's package manager if you're not using Ubuntu or a Debian-based system.

2. Verify the installation:

    ```bash
    aspell --lang=mr -a
    ```
    If the installation was successful, you should see output similar to:
    ```bash
    @(#) International Ispell Version 3.1.20 (but really Aspell 0.60.8.1)
    ```
    If not check the commands carefully or refer to the documentation on http://aspell.net/

## Usage
To use the Marathi spell checker, follow these steps:

1. Clone the repository:


    ```bash
    git clone https://github.com/Shivranjan17/marathiSpellChecker.git
    ```
    ```bash
    cd marathiSpellChecker
    ```
2. Run the Python script:

    ```bash
    python main.py
    ```
Enter a Marathi word to check its spelling.
