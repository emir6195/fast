from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.user import router as user_router
from routes.auth import router as auth_router
from routes.book import router as book_router
from routes.author import router as author_router


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router, prefix="/api/user")
app.include_router(auth_router, prefix="/api/auth")
app.include_router(book_router, prefix="/api/book")
app.include_router(author_router, prefix="/api/author")

