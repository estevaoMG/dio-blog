import asyncio

import pytest_asyncio
from httpx import ASGITransport, AsyncClient

from src.config import settings

# =========================
# TEST DATABASE
# =========================
TEST_DATABASE_URL = "sqlite:///./tests.db"
settings.database_url = TEST_DATABASE_URL


# =========================
# EVENT LOOP FIX
# =========================
@pytest_asyncio.fixture(scope="session")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


# =========================
# DATABASE ISOLATION (RESET TOTAL)
# =========================
@pytest_asyncio.fixture(autouse=True)
async def db():
    from src.database import database, engine, metadata
    from src.models.post import posts  # garante tabela registrada

    metadata.drop_all(engine)
    metadata.create_all(engine)

    await database.connect()

    try:
        yield
    finally:
        await database.disconnect()
        metadata.drop_all(engine)


# =========================
# HTTP CLIENT
# =========================
@pytest_asyncio.fixture
async def client():
    from src.main import app

    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
        },
    ) as client:
        yield client


# =========================
# AUTH TOKEN FIXTURE
# =========================
@pytest_asyncio.fixture
async def access_token(client: AsyncClient):
    response = await client.post("/auth/login", json={"user_id": 1})

    assert response.status_code == 200, response.text
    return response.json()["access_token"]


# =========================
# 🔥 FIX PRINCIPAL: POST SEED PARA DELETE/UPDATE/READ
# =========================
@pytest_asyncio.fixture
async def post_factory(client: AsyncClient, access_token: str):
    async def _create(**overrides):
        headers = {"Authorization": f"Bearer {access_token}"}

        payload = {
            "title": "Test Post",
            "content": "Test content",
            "published_at": "2024-04-12T04:33:14.403Z",
            "published": True,
        }

        payload.update(overrides)

        response = await client.post("/posts/", json=payload, headers=headers)

        assert response.status_code == 201, response.text
        return response.json()

    return _create


# =========================
# FIX SIMPLES (CASO ÚNICO)
# =========================
@pytest_asyncio.fixture
async def created_post(post_factory):
    return await post_factory()
