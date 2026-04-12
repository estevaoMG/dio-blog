from fastapi import APIRouter, Response, status

from database import database
from models.post import posts
from schemas.post import PostIn, PostUpdateIn
from services.post import PostService
from views.post import PostOut

router = APIRouter(prefix="/posts")

service = PostService()


@router.get("/", response_model=list[PostOut])
async def read_posts(
    published: bool,
    limit: int,
    skip: int = 0,
):
    query = posts.select()
    return await database.fetch_all(query)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostOut)
async def create_post(post: PostIn):
    command = posts.insert().values(
        title=post.title,
        content=post.content,
        published_at=post.published_at,
        published=post.published,
    )
    last_id = await database.execute(command)
    return {**post.model_dump(), "id": last_id}


@router.get("/{id}", response_model=PostOut)
async def read_post(id: int):
    return await service.read(id)


@router.patch("/{id}", response_model=PostOut)
async def update_post(id: int, post: PostUpdateIn):
    return await service.update(id=id, post=post)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, response_model=None)
async def delete_post(id: int):
    return await service.delete(id)
