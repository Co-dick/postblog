from db.database import get_connection


def create_post(title,content,tags):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO posts (title, content) VALUES (%s, %s)", (title, content))
    post_id = cursor.lastrowid

    tag_list = [tag.strip()for tag in tags.split(",")]
    for tag in tag_list:
        cursor.execute("SELECT id FROM tags WHERE name = %s",(tag,))
        result=cursor.fetchone()
        if result:
            tag_id = result[0]
        else:
            cursor.execute("INSERT INTO tags (name) VALUES (%s)",(tag,))
            tag_id = cursor.lastrowid

        cursor.execute("INSERT INTO post_tags (post_id,tag_id) VALUES (%s,%s)",(post_id,tag_id))

    conn.commit()
    conn.close()
    print('Post created successfully!')

def view_all_posts():
    conn=get_connection()
    cursor=conn.cursor()   
    cursor.execute("SELECT id,title FROM posts")
    posts=cursor.fetchall()
    for post in posts:
        print(f"{post[0]}:{post[1]}")
    cursor.close()
    conn.close()

def view_post_by_title(title):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT title,content FROM posts WHERE title=%s",(title,))
    post = cursor.fetchone()
    if post:
        print(F"TITLE:{post[0]}\n{post[1]}")
    else:
        print("post not found.")
    cursor.close()
    conn.close()

def search_posts_by_tag(tag_name):
    conn = get_connection()
    cursor = conn.cursor()
    query="SELECT posts.title FROM posts JOIN post_tags ON posts.id = post_tags.post_id JOIN tags ON tags.id = post_tags.tag_id  WHERE LOWER(tags.name) = LOWER(%s)"

    cursor.execute(query,(tag_name,))
    posts = cursor.fetchall()
    if posts:
        print("posts with tag",tag_name)
        for post in posts:
            print(f"🏷️{post[0]}")
    else:
        print("No posts found with that tag")
    
    cursor.close()
    conn.close()







