from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_capture_camera_image_api_v2_system_cameras_camera_capture_post import (
    BodyCaptureCameraImageApiV2SystemCamerasCameraCapturePost,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    camera: str,
    *,
    body: BodyCaptureCameraImageApiV2SystemCamerasCameraCapturePost | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/system/cameras/{camera}/capture".format(
            camera=quote(str(camera), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    camera: str,
    *,
    client: AuthenticatedClient,
    body: BodyCaptureCameraImageApiV2SystemCamerasCameraCapturePost | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Capture Camera Image

     Capture a single ad-hoc image from one camera, for testing purposes.

    **camera** Camera identifier or mac address (e.g. 'Cam_A1' or '06:00:01:bb:77:2e')

    **ring_brightness** Ring light brightness (%) to use for the capture, restored to idle afterwards

    **proj_brightness** Projector light brightness (%) to use for the capture, restored to idle
    afterwards

    Args:
        camera (str):
        body (BodyCaptureCameraImageApiV2SystemCamerasCameraCapturePost | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        camera=camera,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    camera: str,
    *,
    client: AuthenticatedClient,
    body: BodyCaptureCameraImageApiV2SystemCamerasCameraCapturePost | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Capture Camera Image

     Capture a single ad-hoc image from one camera, for testing purposes.

    **camera** Camera identifier or mac address (e.g. 'Cam_A1' or '06:00:01:bb:77:2e')

    **ring_brightness** Ring light brightness (%) to use for the capture, restored to idle afterwards

    **proj_brightness** Projector light brightness (%) to use for the capture, restored to idle
    afterwards

    Args:
        camera (str):
        body (BodyCaptureCameraImageApiV2SystemCamerasCameraCapturePost | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        camera=camera,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    camera: str,
    *,
    client: AuthenticatedClient,
    body: BodyCaptureCameraImageApiV2SystemCamerasCameraCapturePost | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Capture Camera Image

     Capture a single ad-hoc image from one camera, for testing purposes.

    **camera** Camera identifier or mac address (e.g. 'Cam_A1' or '06:00:01:bb:77:2e')

    **ring_brightness** Ring light brightness (%) to use for the capture, restored to idle afterwards

    **proj_brightness** Projector light brightness (%) to use for the capture, restored to idle
    afterwards

    Args:
        camera (str):
        body (BodyCaptureCameraImageApiV2SystemCamerasCameraCapturePost | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        camera=camera,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    camera: str,
    *,
    client: AuthenticatedClient,
    body: BodyCaptureCameraImageApiV2SystemCamerasCameraCapturePost | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Capture Camera Image

     Capture a single ad-hoc image from one camera, for testing purposes.

    **camera** Camera identifier or mac address (e.g. 'Cam_A1' or '06:00:01:bb:77:2e')

    **ring_brightness** Ring light brightness (%) to use for the capture, restored to idle afterwards

    **proj_brightness** Projector light brightness (%) to use for the capture, restored to idle
    afterwards

    Args:
        camera (str):
        body (BodyCaptureCameraImageApiV2SystemCamerasCameraCapturePost | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            camera=camera,
            client=client,
            body=body,
        )
    ).parsed
