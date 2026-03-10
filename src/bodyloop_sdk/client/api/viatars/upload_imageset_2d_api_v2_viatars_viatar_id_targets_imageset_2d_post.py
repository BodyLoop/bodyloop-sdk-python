from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_upload_imageset_2d_api_v2_viatars_viatar_id_targets_imageset_2d_post import (
    BodyUploadImageset2DApiV2ViatarsViatarIdTargetsImageset2DPost,
)
from ...models.http_validation_error import HTTPValidationError
from ...models.upload_imageset_2d_api_v2_viatars_viatar_id_targets_imageset_2d_post_response_upload_imageset_2d_api_v2_viatars_viatar_id_targets_imageset_2d_post import (
    UploadImageset2DApiV2ViatarsViatarIdTargetsImageset2DPostResponseUploadImageset2DApiV2ViatarsViatarIdTargetsImageset2DPost,
)
from ...types import Response


def _get_kwargs(
    viatar_id: int,
    *,
    body: BodyUploadImageset2DApiV2ViatarsViatarIdTargetsImageset2DPost,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/viatars/{viatar_id}/targets/imageset_2d".format(
            viatar_id=quote(str(viatar_id), safe=""),
        ),
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    HTTPValidationError
    | UploadImageset2DApiV2ViatarsViatarIdTargetsImageset2DPostResponseUploadImageset2DApiV2ViatarsViatarIdTargetsImageset2DPost
    | None
):
    if response.status_code == 200:
        response_200 = UploadImageset2DApiV2ViatarsViatarIdTargetsImageset2DPostResponseUploadImageset2DApiV2ViatarsViatarIdTargetsImageset2DPost.from_dict(
            response.json()
        )

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
) -> Response[
    HTTPValidationError
    | UploadImageset2DApiV2ViatarsViatarIdTargetsImageset2DPostResponseUploadImageset2DApiV2ViatarsViatarIdTargetsImageset2DPost
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    viatar_id: int,
    *,
    client: AuthenticatedClient,
    body: BodyUploadImageset2DApiV2ViatarsViatarIdTargetsImageset2DPost,
) -> Response[
    HTTPValidationError
    | UploadImageset2DApiV2ViatarsViatarIdTargetsImageset2DPostResponseUploadImageset2DApiV2ViatarsViatarIdTargetsImageset2DPost
]:
    """Upload Imageset 2D

     Upload the data of target 'imageset_2d'

    Args:
        viatar_id (int):
        body (BodyUploadImageset2DApiV2ViatarsViatarIdTargetsImageset2DPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UploadImageset2DApiV2ViatarsViatarIdTargetsImageset2DPostResponseUploadImageset2DApiV2ViatarsViatarIdTargetsImageset2DPost]
    """

    kwargs = _get_kwargs(
        viatar_id=viatar_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    viatar_id: int,
    *,
    client: AuthenticatedClient,
    body: BodyUploadImageset2DApiV2ViatarsViatarIdTargetsImageset2DPost,
) -> (
    HTTPValidationError
    | UploadImageset2DApiV2ViatarsViatarIdTargetsImageset2DPostResponseUploadImageset2DApiV2ViatarsViatarIdTargetsImageset2DPost
    | None
):
    """Upload Imageset 2D

     Upload the data of target 'imageset_2d'

    Args:
        viatar_id (int):
        body (BodyUploadImageset2DApiV2ViatarsViatarIdTargetsImageset2DPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UploadImageset2DApiV2ViatarsViatarIdTargetsImageset2DPostResponseUploadImageset2DApiV2ViatarsViatarIdTargetsImageset2DPost
    """

    return sync_detailed(
        viatar_id=viatar_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    viatar_id: int,
    *,
    client: AuthenticatedClient,
    body: BodyUploadImageset2DApiV2ViatarsViatarIdTargetsImageset2DPost,
) -> Response[
    HTTPValidationError
    | UploadImageset2DApiV2ViatarsViatarIdTargetsImageset2DPostResponseUploadImageset2DApiV2ViatarsViatarIdTargetsImageset2DPost
]:
    """Upload Imageset 2D

     Upload the data of target 'imageset_2d'

    Args:
        viatar_id (int):
        body (BodyUploadImageset2DApiV2ViatarsViatarIdTargetsImageset2DPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UploadImageset2DApiV2ViatarsViatarIdTargetsImageset2DPostResponseUploadImageset2DApiV2ViatarsViatarIdTargetsImageset2DPost]
    """

    kwargs = _get_kwargs(
        viatar_id=viatar_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    viatar_id: int,
    *,
    client: AuthenticatedClient,
    body: BodyUploadImageset2DApiV2ViatarsViatarIdTargetsImageset2DPost,
) -> (
    HTTPValidationError
    | UploadImageset2DApiV2ViatarsViatarIdTargetsImageset2DPostResponseUploadImageset2DApiV2ViatarsViatarIdTargetsImageset2DPost
    | None
):
    """Upload Imageset 2D

     Upload the data of target 'imageset_2d'

    Args:
        viatar_id (int):
        body (BodyUploadImageset2DApiV2ViatarsViatarIdTargetsImageset2DPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UploadImageset2DApiV2ViatarsViatarIdTargetsImageset2DPostResponseUploadImageset2DApiV2ViatarsViatarIdTargetsImageset2DPost
    """

    return (
        await asyncio_detailed(
            viatar_id=viatar_id,
            client=client,
            body=body,
        )
    ).parsed
