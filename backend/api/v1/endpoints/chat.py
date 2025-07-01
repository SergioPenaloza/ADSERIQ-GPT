from fastapi import APIRouter
from services.chat_service import Chatservice

router = APIRouter()
chatService = Chatservice()

@router.get("/chat")
async def chat():
    return {"response": await chatService.generar_chat() }