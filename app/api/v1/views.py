from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.core.exceptions import ExistException
from app.core.handlers import EncryptedHandler, DecryptedHandler
from app.api.v1.serializers import TextInput, ResponseSerializer

router = APIRouter()


@router.post(
    "/text/encrypted",
    tags=["EncryptedText"],
    response_model=ResponseSerializer
)
async def post_encrypted_text(text: TextInput) -> dict:
    """Post text to encrypt """
    try:
        result = EncryptedHandler.encrypted_text(text.text)

        return JSONResponse(
            content={
                "status": result["status"],
                "data": result["data"],
                "message": str(result["message"])
            }
        )
    except ExistException as e:
        return JSONResponse(
            content={
                "status": e.status,
                "data": result["data"],
                "message": str(e.message("Text")),
                "errors": str(e)
            },
            status_code=e.status
        )


@router.post(
    "/text/decrypted",
    tags=["DecryptedText"],
    response_model=ResponseSerializer
)
async def post_decrypted_text(
    text_encrypt: TextInput
) -> dict:
    """Post text to decrypted """
    try:

        result = DecryptedHandler.decrypted_text(
            text_encrypt.text
        )

        return JSONResponse(
            content={
                "status": result["status"],
                "data": result["data"],
                "message": str(result["message"])
            }
        )
    except ExistException as e:
        return JSONResponse(
            content={
                "status": e.status,
                "data": result["data"],
                "message": str(e.message("Text")),
                "errors": str(e)
            },
            status_code=e.status
        )
