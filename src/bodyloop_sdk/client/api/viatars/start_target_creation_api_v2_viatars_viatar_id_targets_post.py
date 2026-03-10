from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_start_target_creation_api_v2_viatars_viatar_id_targets_post import (
    BodyStartTargetCreationApiV2ViatarsViatarIdTargetsPost,
)
from ...models.http_validation_error import HTTPValidationError
from ...models.start_target_creation_api_v2_viatars_viatar_id_targets_post_response_start_target_creation_api_v2_viatars_viatar_id_targets_post import (
    StartTargetCreationApiV2ViatarsViatarIdTargetsPostResponseStartTargetCreationApiV2ViatarsViatarIdTargetsPost,
)
from ...types import Response


def _get_kwargs(
    viatar_id: int,
    *,
    body: BodyStartTargetCreationApiV2ViatarsViatarIdTargetsPost,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/viatars/{viatar_id}/targets/".format(
            viatar_id=quote(str(viatar_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    HTTPValidationError
    | StartTargetCreationApiV2ViatarsViatarIdTargetsPostResponseStartTargetCreationApiV2ViatarsViatarIdTargetsPost
    | None
):
    if response.status_code == 202:
        response_202 = StartTargetCreationApiV2ViatarsViatarIdTargetsPostResponseStartTargetCreationApiV2ViatarsViatarIdTargetsPost.from_dict(
            response.json()
        )

        return response_202

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
    | StartTargetCreationApiV2ViatarsViatarIdTargetsPostResponseStartTargetCreationApiV2ViatarsViatarIdTargetsPost
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
    body: BodyStartTargetCreationApiV2ViatarsViatarIdTargetsPost,
) -> Response[
    HTTPValidationError
    | StartTargetCreationApiV2ViatarsViatarIdTargetsPostResponseStartTargetCreationApiV2ViatarsViatarIdTargetsPost
]:
    """Start Target Creation

     Triggers target creation of a specific 'target_kind'

     The targets have a hierarchical dependency to each other. It is not neccessary, but possible to
    trigger each taget seperat.
        To create the target 'analyzed_avatar_3d' it is only neccessary to trigger the target createion
    of this target_kind. All dependant targets will be triggered automaticaly, if not 'Ready'.

    **imageset_2d**           -> A set of images are captured, using a BodyLoop Scan Device.
    *(Results can be accessed under 'images' endpoints)*

    **coarse_pointcloud_3d**  -> A spares pointcloud of the captured scene.
    *(Results can be accessed under 'models' endpoints)*

    **mesh_3d**               -> A 3d reconstruction of the captured scene.
    *(Results can be accessed under 'models' endpoints)*

    **avatar_3d**             -> A 3d modeled avatar of the 3d reconstruction.
    *(Results can be accessed under 'models' endpoints)*

    **analyzed_avatar_3d**    -> Automatic analyzation of the modeled avatar.
    *(Results can be accessed under 'markers_and_measures' and 'series' endpoints)*

    **report**                -> A first report of the analyzation and the modeled avatar.
    *(Results can be accessed under 'reports' endpoints)*

    Args:
        viatar_id (int):
        body (BodyStartTargetCreationApiV2ViatarsViatarIdTargetsPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | StartTargetCreationApiV2ViatarsViatarIdTargetsPostResponseStartTargetCreationApiV2ViatarsViatarIdTargetsPost]
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
    body: BodyStartTargetCreationApiV2ViatarsViatarIdTargetsPost,
) -> (
    HTTPValidationError
    | StartTargetCreationApiV2ViatarsViatarIdTargetsPostResponseStartTargetCreationApiV2ViatarsViatarIdTargetsPost
    | None
):
    """Start Target Creation

     Triggers target creation of a specific 'target_kind'

     The targets have a hierarchical dependency to each other. It is not neccessary, but possible to
    trigger each taget seperat.
        To create the target 'analyzed_avatar_3d' it is only neccessary to trigger the target createion
    of this target_kind. All dependant targets will be triggered automaticaly, if not 'Ready'.

    **imageset_2d**           -> A set of images are captured, using a BodyLoop Scan Device.
    *(Results can be accessed under 'images' endpoints)*

    **coarse_pointcloud_3d**  -> A spares pointcloud of the captured scene.
    *(Results can be accessed under 'models' endpoints)*

    **mesh_3d**               -> A 3d reconstruction of the captured scene.
    *(Results can be accessed under 'models' endpoints)*

    **avatar_3d**             -> A 3d modeled avatar of the 3d reconstruction.
    *(Results can be accessed under 'models' endpoints)*

    **analyzed_avatar_3d**    -> Automatic analyzation of the modeled avatar.
    *(Results can be accessed under 'markers_and_measures' and 'series' endpoints)*

    **report**                -> A first report of the analyzation and the modeled avatar.
    *(Results can be accessed under 'reports' endpoints)*

    Args:
        viatar_id (int):
        body (BodyStartTargetCreationApiV2ViatarsViatarIdTargetsPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | StartTargetCreationApiV2ViatarsViatarIdTargetsPostResponseStartTargetCreationApiV2ViatarsViatarIdTargetsPost
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
    body: BodyStartTargetCreationApiV2ViatarsViatarIdTargetsPost,
) -> Response[
    HTTPValidationError
    | StartTargetCreationApiV2ViatarsViatarIdTargetsPostResponseStartTargetCreationApiV2ViatarsViatarIdTargetsPost
]:
    """Start Target Creation

     Triggers target creation of a specific 'target_kind'

     The targets have a hierarchical dependency to each other. It is not neccessary, but possible to
    trigger each taget seperat.
        To create the target 'analyzed_avatar_3d' it is only neccessary to trigger the target createion
    of this target_kind. All dependant targets will be triggered automaticaly, if not 'Ready'.

    **imageset_2d**           -> A set of images are captured, using a BodyLoop Scan Device.
    *(Results can be accessed under 'images' endpoints)*

    **coarse_pointcloud_3d**  -> A spares pointcloud of the captured scene.
    *(Results can be accessed under 'models' endpoints)*

    **mesh_3d**               -> A 3d reconstruction of the captured scene.
    *(Results can be accessed under 'models' endpoints)*

    **avatar_3d**             -> A 3d modeled avatar of the 3d reconstruction.
    *(Results can be accessed under 'models' endpoints)*

    **analyzed_avatar_3d**    -> Automatic analyzation of the modeled avatar.
    *(Results can be accessed under 'markers_and_measures' and 'series' endpoints)*

    **report**                -> A first report of the analyzation and the modeled avatar.
    *(Results can be accessed under 'reports' endpoints)*

    Args:
        viatar_id (int):
        body (BodyStartTargetCreationApiV2ViatarsViatarIdTargetsPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | StartTargetCreationApiV2ViatarsViatarIdTargetsPostResponseStartTargetCreationApiV2ViatarsViatarIdTargetsPost]
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
    body: BodyStartTargetCreationApiV2ViatarsViatarIdTargetsPost,
) -> (
    HTTPValidationError
    | StartTargetCreationApiV2ViatarsViatarIdTargetsPostResponseStartTargetCreationApiV2ViatarsViatarIdTargetsPost
    | None
):
    """Start Target Creation

     Triggers target creation of a specific 'target_kind'

     The targets have a hierarchical dependency to each other. It is not neccessary, but possible to
    trigger each taget seperat.
        To create the target 'analyzed_avatar_3d' it is only neccessary to trigger the target createion
    of this target_kind. All dependant targets will be triggered automaticaly, if not 'Ready'.

    **imageset_2d**           -> A set of images are captured, using a BodyLoop Scan Device.
    *(Results can be accessed under 'images' endpoints)*

    **coarse_pointcloud_3d**  -> A spares pointcloud of the captured scene.
    *(Results can be accessed under 'models' endpoints)*

    **mesh_3d**               -> A 3d reconstruction of the captured scene.
    *(Results can be accessed under 'models' endpoints)*

    **avatar_3d**             -> A 3d modeled avatar of the 3d reconstruction.
    *(Results can be accessed under 'models' endpoints)*

    **analyzed_avatar_3d**    -> Automatic analyzation of the modeled avatar.
    *(Results can be accessed under 'markers_and_measures' and 'series' endpoints)*

    **report**                -> A first report of the analyzation and the modeled avatar.
    *(Results can be accessed under 'reports' endpoints)*

    Args:
        viatar_id (int):
        body (BodyStartTargetCreationApiV2ViatarsViatarIdTargetsPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | StartTargetCreationApiV2ViatarsViatarIdTargetsPostResponseStartTargetCreationApiV2ViatarsViatarIdTargetsPost
    """

    return (
        await asyncio_detailed(
            viatar_id=viatar_id,
            client=client,
            body=body,
        )
    ).parsed
