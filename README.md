# DSA-PROJECT
The system provides basic social media features such as creating posts, liking posts, adding comments, and supporting undo/redo functionality. The posts are displayed in an HTML table for better visualization. This project demonstrates practical applications of data structures like stacks, queues, linked lists, and hashmaps.

# 📱 Social Media Feed System

A console-based social media simulation project built in Python. It allows users to create posts, like posts, add comments, undo/redo actions, and view all posts in a web browser using HTML formatting.

---

## 🚀 Features

- 📝 Create posts
- ❤️ Like posts
- 💬 Add comments to posts
- ↩️ Undo and Redo actions (using stacks)
- 🌐 View all posts in a styled HTML table in the browser
- 🧠 Implements core data structures: Linked List, Stack, Queue, HashMap

---

## 🧩 Data Structures Used

| Structure      | Purpose                                    |
|----------------|--------------------------------------------|
| `LinkedList`   | Manages comments on each post              |
| `Queue`        | Maintains the order of posts (FIFO)        |
| `Stack`        | Handles undo/redo actions                  |
| `HashMap`      | Stores posts user-wise for easy retrieval  |

---

## 💡 How It Works

1. **Create Post**  
   User enters a message that gets added to the post queue and their post list.

2. **Like Post**  
   User selects a post to increment its like count.

3. **Add Comment**  
   User selects a post and adds a comment using linked list operations.

4. **Undo/Redo**  
   Revert or reapply the last action taken using stack-based history.

5. **Show Posts in Browser**  
   Opens an `HTML` file displaying all posts in a styled table using Python's `webbrowser` module.

---

## ▶️ How to Run the Project

### 🔧 Prerequisites:
- Python 3.x installed on your machine

### 📥 Step-by-Step Instructions:

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/social-media-feed.git
   cd social-media-feed
