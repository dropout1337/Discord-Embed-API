import os
from fastapi import APIRouter

from core.database.mongo import Database
from core.models import CreateEmbed

router = APIRouter(prefix="/api")
database = Database().database

@router.post("/create")
async def create(payload: CreateEmbed):
    id = os.urandom(5).hex()
    
    await database.insert_one({
        "id": id,
        **dict(payload)
    })
    
    return {
        "id": id
    }