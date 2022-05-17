from fastapi import APIRouter, Body

router = APIRouter()


@router.post("/", response_description="Rota para criar novo usuário")
async def rota_criar_usuario(usuario = Body(...)):
    return {
        "mensagem": "Usuário criado com sucesso"
    }
