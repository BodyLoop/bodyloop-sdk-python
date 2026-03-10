from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    viatar_id: int,
    model_name: str,
    *,
    scale: int | None | Unset = 1,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_scale: int | None | Unset
    if isinstance(scale, Unset):
        json_scale = UNSET
    else:
        json_scale = scale
    params["scale"] = json_scale

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/viatars/{viatar_id}/models/{model_name}".format(
            viatar_id=quote(str(viatar_id), safe=""),
            model_name=quote(str(model_name), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    viatar_id: int,
    model_name: str,
    *,
    client: AuthenticatedClient,
    scale: int | None | Unset = 1,
) -> Response[Any | HTTPValidationError]:
    """Get Model

     Returns the model specified model of the matching viatar. **(Do not use this endpoint via
    RTKQuery)**

    Args:
        viatar_id (int):
        model_name (str):
        scale (int | None | Unset):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        viatar_id=viatar_id,
        model_name=model_name,
        scale=scale,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    viatar_id: int,
    model_name: str,
    *,
    client: AuthenticatedClient,
    scale: int | None | Unset = 1,
) -> Any | HTTPValidationError | None:
    """Get Model

     Returns the model specified model of the matching viatar. **(Do not use this endpoint via
    RTKQuery)**

    Args:
        viatar_id (int):
        model_name (str):
        scale (int | None | Unset):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        viatar_id=viatar_id,
        model_name=model_name,
        client=client,
        scale=scale,
    ).parsed


async def asyncio_detailed(
    viatar_id: int,
    model_name: str,
    *,
    client: AuthenticatedClient,
    scale: int | None | Unset = 1,
) -> Response[Any | HTTPValidationError]:
    """Get Model

     Returns the model specified model of the matching viatar. **(Do not use this endpoint via
    RTKQuery)**

    Args:
        viatar_id (int):
        model_name (str):
        scale (int | None | Unset):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        viatar_id=viatar_id,
        model_name=model_name,
        scale=scale,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    viatar_id: int,
    model_name: str,
    *,
    client: AuthenticatedClient,
    scale: int | None | Unset = 1,
) -> Any | HTTPValidationError | None:
    """Get Model

     Returns the model specified model of the matching viatar. **(Do not use this endpoint via
    RTKQuery)**

    Args:
        viatar_id (int):
        model_name (str):
        scale (int | None | Unset):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            viatar_id=viatar_id,
            model_name=model_name,
            client=client,
            scale=scale,
        )
    ).parsed
