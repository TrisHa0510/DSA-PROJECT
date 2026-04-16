<h1 align="center">📱 Social Media Feed System</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&style=for-the-badge" />
  <img src="https://img.shields.io/badge/Data%20Structures-DSA%20Project-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" />
  <img src="https://img.shields.io/github/last-commit/trisha0510/DSA-PROJECT?style=for-the-badge" />
</p>

<p align="center">
  A console-based social media simulation built in Python demonstrating practical applications of 
  core data structures — Linked List, Stack, Queue, and HashMap.
</p>

---

## 📸 Preview

> Posts are rendered and displayed in a styled HTML table directly in the browser.

<!-- Add a screenshot of your HTML output here -->
<!-- ![Preview](assets/preview.png) -->

---

## 🚀 Features

- 📝 **Create Posts** — Add new posts to the feed
- ❤️ **Like Posts** — Increment like count on any post
- 💬 **Add Comments** — Comment on posts using Linked List operations
- ↩️ **Undo / Redo Actions** — Revert or reapply last actions using Stacks
- 🌐 **View in Browser** — All posts rendered in a styled HTML table via Python's `webbrowser` module
- 🧠 **Pure DSA Implementation** — No external libraries; built from scratch

---

## 🧩 Data Structures Used

| Structure | Purpose |
|---|---|
| `LinkedList` | Manages comments on each post |
| `Queue` | Maintains the order of posts (FIFO) |
| `Stack` | Handles undo/redo action history |
| `HashMap` | Stores posts user-wise for fast retrieval |

---

## 💡 How It Works

1. **Create Post** — User enters a message; it gets added to the post queue and their personal post list
2. **Like Post** — User selects a post to increment its like count
3. **Add Comment** — User selects a post and adds a comment using linked list node insertion
4. **Undo/Redo** — Reverts or reapplies the last action using a stack-based history tracker
5. **Show Posts in Browser** — Generates an HTML file and opens it in the default browser using Python's `webbrowser` module

---

## 🗂️ Project Structure
DSA-PROJECT/
│
├── main.py # Entry point — menu-driven interface
├── post.py # Post class definition
├── linked_list.py # LinkedList implementation for comments
├── stack.py # Stack implementation for undo/redo
├── queue.py # Queue implementation for post ordering
├── hashmap.py # HashMap implementation for user-wise storage
├── html_generator.py # Generates and opens HTML table in browser
└── README.md

text

> ⚠️ Adjust filenames above to match your actual file names if different.

---

## ▶️ Getting Started

### 🔧 Prerequisites

- Python 3.x installed — [Download here](https://www.python.org/downloads/)
- No external libraries required

### 📥 Installation & Run

```bash
# Step 1: Clone the repository
git clone https://github.com/trisha0510/DSA-PROJECT.git

# Step 2: Navigate into the project folder
cd DSA-PROJECT

# Step 3: Run the project
python main.py
```

---

## 🖥️ Sample Output
===== Social Media Feed =====

Create Post

Like a Post

Add Comment

Undo Last Action

Redo Last Action

View All Posts in Browser

Exit
Enter your choice: 1
Enter your message: Hello World!
✅ Post created successfully!!

text

---

## 🔮 Future Improvements

- 🔍 Search posts by keyword
- 👤 Multi-user login system
- 💾 Persistent storage using file I/O or SQLite
- 🎨 Enhanced HTML UI with CSS styling

---

## 🧠 Concepts Demonstrated

- Abstract Data Types (ADT) implemented from scratch in Python
- FIFO ordering using Queue
- LIFO-based undo/redo using Stack
- Dynamic node insertion via Linked List
- Key-value storage and retrieval using HashMap
- HTML generation and browser automation in Python

---

## 👩‍💻 Author

**Trisha Patil**  
B.Tech Information Technology | Uka Tarsadia University, Bardoli, Gujarat (Batch 2027)  

[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?logo=linkedin&style=flat-square)](https://www.linkedin.com/in/trisha-patil-629ab3300)
[![GitHub](https://img.shields.io/badge/GitHub-black?logo=github&style=flat-square)](https://github.com/trisha0510)
[![Gmail](https://img.shields.io/badge/Gmail-red?logo=gmail&style=flat-square)](mailto:trishapatil05@gmail.com)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
