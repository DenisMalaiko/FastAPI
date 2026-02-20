from fastapi import FastAPI, HTTPException
from typing import Optional, List, Dict
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    age: int

class Post(BaseModel):
    id: int
    title: str
    content: str
    author: User

class PostCreate(BaseModel):
    title: str
    content: str
    author_id: int

app = FastAPI()


users = [
    {"id": 1, "name": "John Doe", 'age': 30},
    {"id": 2, "name": "Jane Doe", 'age': 29},
    {"id": 3, "name": "Bob Smith", 'age': 31}
]

posts = [
    { 'id': 1, 'title': 'Post 1', 'content': 'First post content', 'author': users[0] },
    { 'id': 2, 'title': 'Post 2', 'content': 'Second post content', 'author': users[1] },
    { 'id': 3, 'title': 'Post 3', 'content': 'Third post content', 'author': users[2] }
]

@app.get("/posts")
async def read_posts() -> List[Post]:
    return [Post(**post) for post in posts]

@app.post("/posts/add")
async def add_post(post: PostCreate) -> Post:
    author = next((user for user in users if user['id'] == post.author_id), None)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")

    new_post_id = len(posts) + 1

    new_post = { 'id': new_post_id, 'title': post.title, 'content': post.content, 'author': author }

    posts.append(new_post)

    return Post(**new_post)

@app.get("/posts/{id}")
async def read_posts(id: int) -> Post:
    for post in posts:
        if post['id'] == id:
            return Post(**post)
    raise HTTPException(status_code=404, detail="Post not found")

@app.get("/search")
async def search(post_id: Optional[int] = None) -> Dict[str, Optional[Post]]:
    if post_id:
        for post in posts:
            if post['id'] == post_id:
                return { "data": Post(**post) }
        raise HTTPException(status_code=404, detail="Post not found")
    else:
        return { "data": None }