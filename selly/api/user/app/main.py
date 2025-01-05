from fastapi import FastAPI, APIRouter, status
from app.routers import user

app = FastAPI()

router = APIRouter()


@router.get("/healthcheck", status_code=status.HTTP_204_NO_CONTENT)
def healthcheck():
    pass


app.include_router(router)
app.include_router(user.router)
