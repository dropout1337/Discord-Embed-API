from fastapi import APIRouter, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from core.database.mongo import Database

router = APIRouter()
database = Database().database

router.mount("/assets", StaticFiles(directory="./core/templates"), name="static")
templates = Jinja2Templates(directory="./core/templates")
templates.env.autoescape = False

@router.get("/{id}")
async def root(request: Request, id: str):
    query = await database.find_one({"id": id})
    if query == None:
        return {
            "error": "Invalid ID"
        }
        
    query.pop("_id")
    query.pop("id")
    query["thumbnail"] = bool(query["thumbnail"])

    response = templates.TemplateResponse(
        name="embed.html",
        context={
            "request": request,
            
            **query
        }
    )
    
    return response