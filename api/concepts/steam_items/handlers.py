from fastapi import APIRouter

router = APIRouter(
    prefix="steamItems",
)


@router.get("/getAll")
def get_all():
