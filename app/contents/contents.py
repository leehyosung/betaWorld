from fastapi import APIRouter

router = APIRouter(
    prefix="/contents",
    tags=["contents"]
)


@router.get("/")
async def get_contents():
    return [{"name": "test"}, {"name": "Movie"}]