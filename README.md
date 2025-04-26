📂 Project Structure

BLOG_POST/
│
├── app.py               # Main CLI application
├── service/
│   └── blog.py          # Blog services (create, view, search)
├── db/
│   └── database.py      # Database connection
├── requirements.txt     # Required Python libraries
└── README.md            # Project documentation
⚙️ Features
➕ Create a new blog post with tags.

📋 View all blog posts.

🔎 View a specific post by title.

🏷️ Search posts by tag (case-insensitive).

🎨 Colorful and user-friendly command-line interface.

🚀 How to Run
Clone the repository or download the files.

Install dependencies:


pip install -r requirements.txt
Set up a MySQL database with the following tables:

posts (id, title, content)

tags (id, name)

post_tags (id, post_id, tag_id)

Update your database connection in db/database.py file (set host, user, password, database).

Run the application:


python app.py
🛠️ Requirements
Python 3.10+

MySQL Server

Required libraries:

mysql-connector-python

colorama



🛢️ Database Schema 
posts: Stores each blog post's title and content.

tags: Stores name of each tag.

post_tags: Connects posts and tags (for many-to-many relationship).

💡 Bonus Features
Searching by tag works even if you type uppercase/lowercase — it is case-insensitive.

Interface uses colors (colorama) to make the CLI look attractive.

👨‍💻 Author
Made with ❤️ by [Anant Deep]

📌 Example Commands
# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
