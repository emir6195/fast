from fastapi import APIRouter, Depends
from models.author import AuthorModel, AuthorUpdateModel
from lib.author import author_ops
from lib.auth import JWTBearer

router = APIRouter()


@router.get("/", dependencies=[Depends(JWTBearer())],  tags=["author"])
async def getAllAuthors():
    authors = author_ops.get_all_authors()
    return authors

@router.get("/no-join", dependencies=[Depends(JWTBearer())],  tags=["author"])
async def getAllAuthorsNoJoin():
    authors = author_ops.get_all_authors_without_join()
    return authors


@router.get("/{author_id}", dependencies=[Depends(JWTBearer())],  tags=["author"])
async def getAuthorById(author_id):
    author = author_ops.get_author_by_id(author_id)
    return author


@router.post("/", dependencies=[Depends(JWTBearer())],  tags=["author"])
async def createAuthor(author: AuthorModel):
    _author = author_ops.create_author(author)
    return _author


@router.put("/{author_id}", dependencies=[Depends(JWTBearer())],  tags=["author"])
async def updateAuthor(author_id, author: AuthorUpdateModel):
    _author = author_ops.update_author(author_id, author)
    return _author


@router.delete("/{author_id}", dependencies=[Depends(JWTBearer())],  tags=["author"])
async def removeAuthorById(author_id):
    _author = author_ops.remove_author(author_id)
    return _author
