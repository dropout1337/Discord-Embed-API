from pydantic import BaseModel

class CreateEmbed(BaseModel):
    redirect: str = None
    
    title: str
    url: str = "https://discord.com/"
    color: str = None
    
    image: str = None
    thumbnail: str = None
    description: str