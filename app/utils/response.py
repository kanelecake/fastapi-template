from typing import Union, Any

from fastapi import HTTPException
from starlette.responses import JSONResponse


def json_response(data: dict, status_code: int = 200):
    """  Возвращает JSON ответ сервера """
    return JSONResponse(data, status_code=status_code)


def json_data_response(data: Any, status_code: int = 200):
    """ Ответ сервера в виде Data """
    return json_response({ 'data': data }, status_code)


def json_affect_response(is_affected: bool):
    """ Ответ сервера в виде статуса оказало эффект или нет """
    return json_response({
        "status": "ok",
        "msg": "",
        "data": "affected" if is_affected else "unaffected",
    }, 200)


def json_error_response(status: int, error: str, description: Union[str, None] = None):
    """
    Метод возвращает ошибку в заданном формате.
    """
    return HTTPException(detail={
        "error": error,
        "description": description,
    }, status_code=status)


def build_redirect_url(redirect_uri: str, state: Union[str, None] = None, code: Union[str, None] = None,
                       error: Union[str, None] = None, error_description: Union[str, None] = None) -> str:
    """
    Метод используется для создания redirect url.
    Он учитывает, каким идет параметр по счету.
    """
    is_first_param = True

    if error is not None and code is not None:
        raise json_error_response(500, "server_error", "You can't provide a code and error in one moment!")

    if state is not None:
        redirect_uri += f"{'?' if is_first_param else '&'}state={state}"
        is_first_param = False

    if code is not None:
        redirect_uri += f"{'?' if is_first_param else '&'}code={code}"
        is_first_param = False

    if error is not None:
        redirect_uri += f"{'?' if is_first_param else '&'}error={error}"
        is_first_param = False

    if error_description is not None:
        redirect_uri += f"{'?' if is_first_param else '&'}error_description={error_description}"

    return redirect_uri