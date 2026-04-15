from fastapi import APIRouter, Depends, HTTPException, status

from src.database import database
from src.models.post import posts
from src.schemas.post import PostIn, PostUpdateIn
from src.security import login_required
from src.services.post import PostService
from src.views.post import PostOut

router = APIRouter(prefix="/posts", tags=["posts"])

service = PostService()


# 🔐 READ POSTS
@router.get("/", response_model=list[PostOut])
async def read_posts(
    published: str,
    limit: int,
    skip: int = 0,
    user: dict = Depends(login_required),
):
    published_map = {"on": True, "off": False}

    if published not in published_map:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Invalid published value",
        )

    query = (
        posts.select()
        .where(posts.c.published == published_map[published])
        .limit(limit)
        .offset(skip)
    )

    return await database.fetch_all(query)


# 🔐 CREATE POST
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostOut)
async def create_post(
    post: PostIn,
    user: dict = Depends(login_required),
):
    command = posts.insert().values(**post.model_dump())
    last_id = await database.execute(command)

    return {"id": last_id, **post.model_dump()}


# 🔐 READ POST BY ID
@router.get("/{id}", response_model=PostOut)
async def read_post(
    id: int,
    user: dict = Depends(login_required),
):
    post = await service.read(id)

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found",
        )

    return post


# 🔐 UPDATE POST
@router.patch("/{id}", response_model=PostOut)
async def update_post(
    id: int,
    post: PostUpdateIn,
    user: dict = Depends(login_required),
):
    updated = await service.update(id=id, post=post)

    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found",
        )

    return updated


# 🔐 DELETE POST (IDEMPOTENTE)
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(
    id: int,
    user: dict = Depends(login_required),
):
    await service.delete(id)
    return None
