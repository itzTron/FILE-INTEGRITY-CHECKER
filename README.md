# FILE INTEGRITY CHECKER (SHA256 Hash Checker)

A simple Python script to verify the SHA-256 hash of a file. This script allows you to:

- Provide the filename and expected hash as command-line arguments.
- Enter the filename and expected hash interactively.
- Get a `true` or `false` match result.

## 📜 Features

- ✅ Command-line usage
- ✅ Interactive mode for input
- ✅ Error handling for incorrect input
- ✅ Works on **Linux** and **macOS** (uses `sha256sum` command)

---

## 📥 Installation

1. Clone this repository:
   ```sh
   https://github.com/itzTron/FILE-INTEGRITY-CHECKER.git
   cd check_hash_1.py
   ```
2. Ensure you have **Python 3** installed:
   ```sh
   python3 --version
   ```
3. Make the script executable (optional, for Linux/macOS):
   ```sh
   chmod +x check_hash_1.py
   ```

---

## 🚀 Usage

### 1️⃣ Command-Line Mode

You can run the script by passing the filename and the expected SHA-256 hash as arguments:

```sh
python3 check_hash_1.py <filename> <expected_hash>
```

**Example:**

```sh
python3 check_hash_1.py myfile.txt 5d41402abc4b2a76b9719d911017c592
```

- If the hash matches, it will output:
  ```sh
  Match: true
  ```
- If the hash does not match, it will output:
  ```sh
  Match: false
  ```

### 2️⃣ Interactive Mode

If you run the script **without arguments**, it will prompt you for the filename and hash:

```sh
python3 check_hash_1.py
```

Then, enter the details when prompted:

```
Enter filename: myfile.txt
Enter expected SHA-256 hash: 5d41402abc4b2a76b9719d911017c592
Match: true
```

---


## 📌 Notes

- This script **only works on Linux/macOS** as it uses `sha256sum`.
- For **Windows compatibility**, replace `sha256sum` with `certutil`.
- Ensure the file exists before running the script.

## 📜 License

This project is **open-source** and licensed under the Apache License.

---

## 📧 Contact

For any issues or contributions, feel free to open an issue or a pull request on GitHub!

Happy Hash Checking! 🔍🎉

