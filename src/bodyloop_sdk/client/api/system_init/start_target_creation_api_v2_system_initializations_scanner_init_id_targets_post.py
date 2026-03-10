from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_start_target_creation_api_v2_system_initializations_scanner_init_id_targets_post import (
    BodyStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPost,
)
from ...models.http_validation_error import HTTPValidationError
from ...models.start_target_creation_api_v2_system_initializations_scanner_init_id_targets_post_response_start_target_creation_api_v2_system_initializations_scanner_init_id_targets_post import (
    StartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPostResponseStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPost,
)
from ...types import Response


def _get_kwargs(
    scanner_init_id: int,
    *,
    body: BodyStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPost,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/system/initializations/{scanner_init_id}/targets".format(
            scanner_init_id=quote(str(scanner_init_id), safe=""),
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
    | StartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPostResponseStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPost
    | None
):
    if response.status_code == 202:
        response_202 = StartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPostResponseStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPost.from_dict(
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
    | StartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPostResponseStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPost
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    scanner_init_id: int,
    *,
    client: AuthenticatedClient,
    body: BodyStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPost,
) -> Response[
    HTTPValidationError
    | StartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPostResponseStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPost
]:
    """Start Target Creation

     Triggers the initialisation process for scanner_init_id

    Supported target_kind is 'init'

       After starting the initialization. The progress of the initialization (targets) should be
    requested and instructions be followed.

    Args:
        scanner_init_id (int):
        body (BodyStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | StartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPostResponseStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPost]
    """

    kwargs = _get_kwargs(
        scanner_init_id=scanner_init_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    scanner_init_id: int,
    *,
    client: AuthenticatedClient,
    body: BodyStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPost,
) -> (
    HTTPValidationError
    | StartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPostResponseStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPost
    | None
):
    """Start Target Creation

     Triggers the initialisation process for scanner_init_id

    Supported target_kind is 'init'

       After starting the initialization. The progress of the initialization (targets) should be
    requested and instructions be followed.

    Args:
        scanner_init_id (int):
        body (BodyStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | StartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPostResponseStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPost
    """

    return sync_detailed(
        scanner_init_id=scanner_init_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    scanner_init_id: int,
    *,
    client: AuthenticatedClient,
    body: BodyStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPost,
) -> Response[
    HTTPValidationError
    | StartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPostResponseStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPost
]:
    """Start Target Creation

     Triggers the initialisation process for scanner_init_id

    Supported target_kind is 'init'

       After starting the initialization. The progress of the initialization (targets) should be
    requested and instructions be followed.

    Args:
        scanner_init_id (int):
        body (BodyStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | StartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPostResponseStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPost]
    """

    kwargs = _get_kwargs(
        scanner_init_id=scanner_init_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    scanner_init_id: int,
    *,
    client: AuthenticatedClient,
    body: BodyStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPost,
) -> (
    HTTPValidationError
    | StartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPostResponseStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPost
    | None
):
    """Start Target Creation

     Triggers the initialisation process for scanner_init_id

    Supported target_kind is 'init'

       After starting the initialization. The progress of the initialization (targets) should be
    requested and instructions be followed.

    Args:
        scanner_init_id (int):
        body (BodyStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | StartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPostResponseStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPost
    """

    return (
        await asyncio_detailed(
            scanner_init_id=scanner_init_id,
            client=client,
            body=body,
        )
    ).parsed
