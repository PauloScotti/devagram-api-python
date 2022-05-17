from fastapi import APIRouter, Body

from models.UsuarioModel import UsuarioModel

router = APIRouter()


@router.post("/", response_description="Rota para criar novo usuário")
async def rota_criar_usuario(usuario: UsuarioModel = Body(...)):
    return {
        "mensagem": "Usuário criado com sucesso"
    }
