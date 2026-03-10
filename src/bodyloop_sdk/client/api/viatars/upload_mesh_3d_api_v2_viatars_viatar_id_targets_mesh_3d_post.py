from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_upload_mesh_3d_api_v2_viatars_viatar_id_targets_mesh_3d_post import (
    BodyUploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPost,
)
from ...models.http_validation_error import HTTPValidationError
from ...models.upload_mesh_3d_api_v2_viatars_viatar_id_targets_mesh_3d_post_response_upload_mesh_3d_api_v2_viatars_viatar_id_targets_mesh_3d_post import (
    UploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPostResponseUploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPost,
)
from ...types import Response


def _get_kwargs(
    viatar_id: int,
    *,
    body: BodyUploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPost,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/viatars/{viatar_id}/targets/mesh_3d".format(
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
    | UploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPostResponseUploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPost
    | None
):
    if response.status_code == 200:
        response_200 = UploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPostResponseUploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPost.from_dict(
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
    | UploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPostResponseUploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPost
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
    body: BodyUploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPost,
) -> Response[
    HTTPValidationError
    | UploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPostResponseUploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPost
]:
    """Upload Mesh 3D

     Upload the data of target 'mesh_3d'

    Args:
        viatar_id (int):
        body (BodyUploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPostResponseUploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPost]
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
    body: BodyUploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPost,
) -> (
    HTTPValidationError
    | UploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPostResponseUploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPost
    | None
):
    """Upload Mesh 3D

     Upload the data of target 'mesh_3d'

    Args:
        viatar_id (int):
        body (BodyUploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPostResponseUploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPost
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
    body: BodyUploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPost,
) -> Response[
    HTTPValidationError
    | UploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPostResponseUploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPost
]:
    """Upload Mesh 3D

     Upload the data of target 'mesh_3d'

    Args:
        viatar_id (int):
        body (BodyUploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPostResponseUploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPost]
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
    body: BodyUploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPost,
) -> (
    HTTPValidationError
    | UploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPostResponseUploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPost
    | None
):
    """Upload Mesh 3D

     Upload the data of target 'mesh_3d'

    Args:
        viatar_id (int):
        body (BodyUploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPostResponseUploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPost
    """

    return (
        await asyncio_detailed(
            viatar_id=viatar_id,
            client=client,
            body=body,
        )
    ).parsed
