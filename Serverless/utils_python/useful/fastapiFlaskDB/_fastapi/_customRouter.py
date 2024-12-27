
# https://www.youtube.com/watch?v=0A_GCXBCNUQ

from fastapi import APIRouter, status, HTTPException

router = APIRouter(
    prefix="/api/v1/users",
    tags=["users"],
    responses={ 401: {"description": "Not authorized"},
                404: {"description": "Not found"}
    },
    # dependencies=[Depends(get_current_user)]
)

router.get("/")
def get_users():
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authorized")

