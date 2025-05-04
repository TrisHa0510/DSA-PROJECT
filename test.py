from tabulate import tabulate
import webbrowser
import os

class CommentNode:
    def __init__(self, comment):
        self.comment = comment
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, comment):
        new_comment = CommentNode(comment)
        if not self.head:
            self.head = new_comment
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_comment

    def remove(self, comment):
        current = self.head
        previous = None
        while current:
            if current.comment == comment:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return
            previous = current
            current = current.next

    def __str__(self):
        comments = []
        current = self.head
        while current:
            comments.append(current.comment)
            current = current.next
        return ", ".join(comments)

class Post:
    def __init__(self, user, message):
        self.user = user
        self.message = message
        self.likes = 0
        self.comments = LinkedList()

    def add_like(self):
        self.likes += 1

    def add_comment(self, comment):
        self.comments.append(comment)

    def __str__(self):
        return f"Post by {self.user}: {self.message} | Likes: {self.likes} | Comments: {str(self.comments)}"

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, post):
        self.queue.append(post)

    def dequeue(self):
        return self.queue.pop(0) if self.queue else None

    def is_empty(self):
        return len(self.queue) == 0

class HashMap:
    def __init__(self):
        self.map = {}

    def __contains__(self, key):
        return key in self.map

    def __setitem__(self, key, value):
        self.map[key] = value

    def __getitem__(self, key):
        return self.map[key]

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop() if self.stack else None

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        return self.stack[-1] if self.stack else None

class SocialMediaFeed:
    def __init__(self):
        self.posts = Queue()
        self.user_posts = HashMap()
        self.undo_stack = Stack()
        self.redo_stack = Stack()

    def create_post(self, user, message):
        post = Post(user, message)
        self.posts.enqueue(post)
        if user not in self.user_posts:
            self.user_posts[user] = []
        self.user_posts[user].append(post)
        self.undo_stack.push(('create_post', post))

    def like_post(self, user, post):
        post.add_like()
        self.undo_stack.push(('like_post', post))

    def add_comment(self, user, post, comment):
        post.add_comment(comment)
        self.undo_stack.push(('add_comment', post, comment))

    def undo(self):
        if not self.undo_stack.is_empty():
            action = self.undo_stack.pop()
            if action[0] == 'create_post':
                self.posts.dequeue()
                self.user_posts[action[1].user].remove(action[1])
            elif action[0] == 'like_post':
                post = action[1]
                post.likes -= 1
            elif action[0] == 'add_comment':
                post = action[1]
                post.comments.remove(action[2])

    def redo(self):
        if not self.redo_stack.is_empty():
            action = self.redo_stack.pop()
            if action[0] == 'create_post':
                self.create_post(action[1].user, action[1].message)
            elif action[0] == 'like_post':
                self.like_post(action[1].user, action[1].post)
            elif action[0] == 'add_comment':
                self.add_comment(action[1].user, action[1].post, action[1].comment)

    def show_posts_in_browser(self):
        html_content = """
        <html>
        <head>
            <title>Social Media Feed</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    padding: 20px;
                }
                table {
                    width: 100%;
                    border-collapse: collapse;
                    margin-top: 20px;
                }
                th, td {
                    border: 1px solid #ddd;
                    padding: 12px;
                    text-align: left;
                }
                th {
                    background-color: #4CAF50;
                    color: white;
                }
                tr:nth-child(even) {
                    background-color: #f9f9f9;
                }
            </style>
        </head>
        <body>
            <h1>📱 Social Media Feed</h1>
            <table>
                <tr>
                    <th>User</th>
                    <th>Post Message</th>
                    <th>Likes</th>
                    <th>💬 Comments</th>
                </tr>
        """

        for post in self.posts.queue:
            user = f"👤 {post.user}"
            message = f"📝 {post.message}"
            likes = f"❤️ {post.likes}"
            comments = str(post.comments) if str(post.comments) else "💬 No comments"
            html_content += f"""
                <tr>
                    <td>{user}</td>
                    <td>{message}</td>
                    <td>{likes}</td>
                    <td>{comments}</td>
                </tr>
            """

        html_content += """
            </table>
        </body>
        </html>
        """

        with open("social_feed.html", "w", encoding="utf-8") as file:
            file.write(html_content)

        webbrowser.open('file://' + os.path.realpath("social_feed.html"))

# Function to handle user interaction
def user_interface():
    feed_system = SocialMediaFeed()

    while True:
        print("\n----- Social Media Feed System -----")
        print("1. Create Post")
        print("2. Like Post")
        print("3. Add Comment")
        print("4. Undo")
        print("5. Redo")
        print("6. Show All Posts")
        print("7. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            user = input("Enter your name: ")
            message = input("Enter your post message: ")
            feed_system.create_post(user, message)
            print("Post created successfully!")

        elif choice == '2':
            user = input("Enter your name: ")
            if user not in feed_system.user_posts or len(feed_system.user_posts[user]) == 0:
                print("No posts to like!")
                continue
            print("Select the post to like:")
            for i, post in enumerate(feed_system.user_posts[user]):
                print(f"{i+1}. {post.message}")
            post_index = int(input("Enter post number: ")) - 1
            post = feed_system.user_posts[user][post_index]
            feed_system.like_post(user, post)
            print(f"You liked: {post.message}")

        elif choice == '3':
            user = input("Enter your name: ")
            if user not in feed_system.user_posts or len(feed_system.user_posts[user]) == 0:
                print("No posts to comment on!")
                continue
            print("Select the post to comment on:")
            for i, post in enumerate(feed_system.user_posts[user]):
                print(f"{i+1}. {post.message}")
            post_index = int(input("Enter post number: ")) - 1
            post = feed_system.user_posts[user][post_index]
            comment = input("Enter your comment: ")
            feed_system.add_comment(user, post, comment)
            print(f"Comment added: {comment}")

        elif choice == '4':
            feed_system.undo()
            print("Last action undone!")

        elif choice == '5':
            feed_system.redo()
            print("Last undone action redone!")

        elif choice == '6':
            print("\nOpening posts in browser...")
            feed_system.show_posts_in_browser()

        elif choice == '7':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

# Run the user interface
if __name__ == "__main__":
    user_interface()
