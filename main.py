from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI()

@app.get("/")
async def read_root() -> dict[str, str]:
    return {"Hello": "World"}

@app.get("/contacts")
async def read_contacts() -> int:
    return 34


posts = [
    { 'id': 1, 'title': 'Post 1', 'content': 'First post content' },
    { 'id': 2, 'title': 'Post 2', 'content': 'Second post content' },
    { 'id': 3, 'title': 'Post 3', 'content': 'Third post content' }
]

@app.get("/posts")
async def read_posts() -> list[dict]:
    return posts

@app.get("/posts/{id}")
async def read_posts(id: int) -> dict:
    for post in posts:
        if post['id'] == id:
            return post
    raise HTTPException(status_code=404, detail="Post not found")

@app.get("/search")
async def search(post_id: Optional[int] = None) -> dict:
    if post_id:
        for post in posts:
            if post['id'] == post_id:
                return post
        raise HTTPException(status_code=404, detail="Post not found")
    else:
        return {"data": "No post id provided"}