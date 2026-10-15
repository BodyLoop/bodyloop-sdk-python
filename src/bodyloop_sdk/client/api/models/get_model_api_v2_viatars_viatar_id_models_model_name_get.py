from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_model_api_v2_viatars_viatar_id_models_model_name_get_convention_type_0 import (
    GetModelApiV2ViatarsViatarIdModelsModelNameGetConventionType0,
)
from ...models.get_model_api_v2_viatars_viatar_id_models_model_name_get_forward_type_0 import (
    GetModelApiV2ViatarsViatarIdModelsModelNameGetForwardType0,
)
from ...models.get_model_api_v2_viatars_viatar_id_models_model_name_get_up_type_0 import (
    GetModelApiV2ViatarsViatarIdModelsModelNameGetUpType0,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    viatar_id: int,
    model_name: str,
    *,
    convention: GetModelApiV2ViatarsViatarIdModelsModelNameGetConventionType0 | None | Unset = UNSET,
    scale: float | None | Unset = UNSET,
    up: GetModelApiV2ViatarsViatarIdModelsModelNameGetUpType0 | None | Unset = UNSET,
    forward: GetModelApiV2ViatarsViatarIdModelsModelNameGetForwardType0 | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_convention: None | str | Unset
    if isinstance(convention, Unset):
        json_convention = UNSET
    elif isinstance(convention, str):
        json_convention = convention
    else:
        json_convention = convention
    params["convention"] = json_convention

    json_scale: float | None | Unset
    if isinstance(scale, Unset):
        json_scale = UNSET
    else:
        json_scale = scale
    params["scale"] = json_scale

    json_up: None | str | Unset
    if isinstance(up, Unset):
        json_up = UNSET
    elif isinstance(up, str):
        json_up = up
    else:
        json_up = up
    params["up"] = json_up

    json_forward: None | str | Unset
    if isinstance(forward, Unset):
        json_forward = UNSET
    elif isinstance(forward, str):
        json_forward = forward
    else:
        json_forward = forward
    params["forward"] = json_forward

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
    convention: GetModelApiV2ViatarsViatarIdModelsModelNameGetConventionType0 | None | Unset = UNSET,
    scale: float | None | Unset = UNSET,
    up: GetModelApiV2ViatarsViatarIdModelsModelNameGetUpType0 | None | Unset = UNSET,
    forward: GetModelApiV2ViatarsViatarIdModelsModelNameGetForwardType0 | None | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Get Model

     Returns the model specified model of the matching viatar. **(Do not use this endpoint via
    RTKQuery)**

    **BodyLoop's own space** is what you get if you ask for nothing: **`+z` up, `-y` forward**
    (the subject faces `-y`), right-handed, in **metres** - a 1.78 m scan is 1.78 units tall.
    Every model is stored and measured in it, and it is the frame every option below is relative
    to. Its name in the table is `bodyloop_blender_m`; Blender's default space is the same one.

    The model can be reoriented and rescaled on the way out, in one of two ways - never both:

    * `convention=<name>` asks for a target space as a whole, axes **and** unit together. There is
      one entry per distinct space, and its name ends in the unit it produces:

      | name | up | forward | scale | unit |
      |---|---|---|---|---|
      | `bodyloop_blender_m` | `+z` | `-y` | 1 | m - **BodyLoop's own space**, and Blender's; the
    default |
      | `gltf_unity_m` | `+y` | `+z` | 1 | m (glTF 2.0 section 3.4; also three.js, Godot, Unity) |
      | `clo3d_mm` | `+y` | `+z` | 1000 | mm |
      | `3ds_max_cm` | `+z` | `-y` | 100 | cm (3ds Max, system unit assumed to be cm) |
      | `unreal_cm` | `+z` | `+x` | 100 | cm |

      `scale` is the factor applied to BodyLoop's metres, so it *is* the unit: **1 = metres,
      100 = centimetres, 1000 = millimetres**. A preset's unit applies to every format, `.glb`
      included.

    * `up` / `forward` / `scale` describe a target relative to BodyLoop's space by hand. Give one
      axis and the other is derived, so `up=+y` alone (or `forward=+z` alone) is the glTF frame.
      `scale` picks the unit the same way (`1` m, `100` cm, `1000` mm - the example picker next to
      the field lists them), so `scale=1000` alone converts metres to millimetres without rotating.

    Combining `convention` with any of `up` / `forward` / `scale` is a 400. Asking for nothing at
    all - or for a target that is BodyLoop's own space, such as `convention=bodyloop_blender_m` -
    is answered with the stored file as it is.

    Rig, skins and custom vertex attributes survive the transform in the `.glb` format. The
    derived obj/stl/ply carry the body mesh of the default scene only.

    A transformed file says what was done to it: a `.glb` carries the frame, the scale and the
    unit under `asset.extras.bodyloop_export`, and an OBJ zip carries the same as
    `bodyloop_export.json` next to the `.obj`. Its `source` block names the space it came from
    (`bodyloop_blender_m`) with that space's axes and unit, so a file that has left the archive
    still says what BodyLoop's own convention is. That block also declares the units of the custom
    per-vertex attributes (`_DepthMap` in mm, the curvatures in 1/mm and 1/mm²), which are
    absolute and deliberately **not** rescaled with `scale`.

    Errors: 422 for a malformed parameter, 400 for a mixed request or a combination that is not a
    valid frame (e.g. `up=+y&forward=+y`), 500 if the stored model cannot be converted.

    Args:
        viatar_id (int):
        model_name (str):
        convention (GetModelApiV2ViatarsViatarIdModelsModelNameGetConventionType0 | None | Unset):
            Target space of an application, axes **and** unit at once - the unit is part of the name.
            `bodyloop_blender_m` is BodyLoop's own space (+z up, -y forward, metres) and the default.
            Mutually exclusive with `up`/`forward`/`scale`.
        scale (float | None | Unset): Multiplies every length of BodyLoop's metre-based model, so
            it picks the unit of the result: `1` = metres (m), `100` = centimetres (cm), `1000` =
            millimetres (mm). Any other positive factor up to 1e6 works too, e.g. `39.3701` for
            inches.
        up (GetModelApiV2ViatarsViatarIdModelsModelNameGetUpType0 | None | Unset): Up axis of the
            target frame.
        forward (GetModelApiV2ViatarsViatarIdModelsModelNameGetForwardType0 | None | Unset): Axis
            the front of the model points along.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        viatar_id=viatar_id,
        model_name=model_name,
        convention=convention,
        scale=scale,
        up=up,
        forward=forward,
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
    convention: GetModelApiV2ViatarsViatarIdModelsModelNameGetConventionType0 | None | Unset = UNSET,
    scale: float | None | Unset = UNSET,
    up: GetModelApiV2ViatarsViatarIdModelsModelNameGetUpType0 | None | Unset = UNSET,
    forward: GetModelApiV2ViatarsViatarIdModelsModelNameGetForwardType0 | None | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Get Model

     Returns the model specified model of the matching viatar. **(Do not use this endpoint via
    RTKQuery)**

    **BodyLoop's own space** is what you get if you ask for nothing: **`+z` up, `-y` forward**
    (the subject faces `-y`), right-handed, in **metres** - a 1.78 m scan is 1.78 units tall.
    Every model is stored and measured in it, and it is the frame every option below is relative
    to. Its name in the table is `bodyloop_blender_m`; Blender's default space is the same one.

    The model can be reoriented and rescaled on the way out, in one of two ways - never both:

    * `convention=<name>` asks for a target space as a whole, axes **and** unit together. There is
      one entry per distinct space, and its name ends in the unit it produces:

      | name | up | forward | scale | unit |
      |---|---|---|---|---|
      | `bodyloop_blender_m` | `+z` | `-y` | 1 | m - **BodyLoop's own space**, and Blender's; the
    default |
      | `gltf_unity_m` | `+y` | `+z` | 1 | m (glTF 2.0 section 3.4; also three.js, Godot, Unity) |
      | `clo3d_mm` | `+y` | `+z` | 1000 | mm |
      | `3ds_max_cm` | `+z` | `-y` | 100 | cm (3ds Max, system unit assumed to be cm) |
      | `unreal_cm` | `+z` | `+x` | 100 | cm |

      `scale` is the factor applied to BodyLoop's metres, so it *is* the unit: **1 = metres,
      100 = centimetres, 1000 = millimetres**. A preset's unit applies to every format, `.glb`
      included.

    * `up` / `forward` / `scale` describe a target relative to BodyLoop's space by hand. Give one
      axis and the other is derived, so `up=+y` alone (or `forward=+z` alone) is the glTF frame.
      `scale` picks the unit the same way (`1` m, `100` cm, `1000` mm - the example picker next to
      the field lists them), so `scale=1000` alone converts metres to millimetres without rotating.

    Combining `convention` with any of `up` / `forward` / `scale` is a 400. Asking for nothing at
    all - or for a target that is BodyLoop's own space, such as `convention=bodyloop_blender_m` -
    is answered with the stored file as it is.

    Rig, skins and custom vertex attributes survive the transform in the `.glb` format. The
    derived obj/stl/ply carry the body mesh of the default scene only.

    A transformed file says what was done to it: a `.glb` carries the frame, the scale and the
    unit under `asset.extras.bodyloop_export`, and an OBJ zip carries the same as
    `bodyloop_export.json` next to the `.obj`. Its `source` block names the space it came from
    (`bodyloop_blender_m`) with that space's axes and unit, so a file that has left the archive
    still says what BodyLoop's own convention is. That block also declares the units of the custom
    per-vertex attributes (`_DepthMap` in mm, the curvatures in 1/mm and 1/mm²), which are
    absolute and deliberately **not** rescaled with `scale`.

    Errors: 422 for a malformed parameter, 400 for a mixed request or a combination that is not a
    valid frame (e.g. `up=+y&forward=+y`), 500 if the stored model cannot be converted.

    Args:
        viatar_id (int):
        model_name (str):
        convention (GetModelApiV2ViatarsViatarIdModelsModelNameGetConventionType0 | None | Unset):
            Target space of an application, axes **and** unit at once - the unit is part of the name.
            `bodyloop_blender_m` is BodyLoop's own space (+z up, -y forward, metres) and the default.
            Mutually exclusive with `up`/`forward`/`scale`.
        scale (float | None | Unset): Multiplies every length of BodyLoop's metre-based model, so
            it picks the unit of the result: `1` = metres (m), `100` = centimetres (cm), `1000` =
            millimetres (mm). Any other positive factor up to 1e6 works too, e.g. `39.3701` for
            inches.
        up (GetModelApiV2ViatarsViatarIdModelsModelNameGetUpType0 | None | Unset): Up axis of the
            target frame.
        forward (GetModelApiV2ViatarsViatarIdModelsModelNameGetForwardType0 | None | Unset): Axis
            the front of the model points along.

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
        convention=convention,
        scale=scale,
        up=up,
        forward=forward,
    ).parsed


async def asyncio_detailed(
    viatar_id: int,
    model_name: str,
    *,
    client: AuthenticatedClient,
    convention: GetModelApiV2ViatarsViatarIdModelsModelNameGetConventionType0 | None | Unset = UNSET,
    scale: float | None | Unset = UNSET,
    up: GetModelApiV2ViatarsViatarIdModelsModelNameGetUpType0 | None | Unset = UNSET,
    forward: GetModelApiV2ViatarsViatarIdModelsModelNameGetForwardType0 | None | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Get Model

     Returns the model specified model of the matching viatar. **(Do not use this endpoint via
    RTKQuery)**

    **BodyLoop's own space** is what you get if you ask for nothing: **`+z` up, `-y` forward**
    (the subject faces `-y`), right-handed, in **metres** - a 1.78 m scan is 1.78 units tall.
    Every model is stored and measured in it, and it is the frame every option below is relative
    to. Its name in the table is `bodyloop_blender_m`; Blender's default space is the same one.

    The model can be reoriented and rescaled on the way out, in one of two ways - never both:

    * `convention=<name>` asks for a target space as a whole, axes **and** unit together. There is
      one entry per distinct space, and its name ends in the unit it produces:

      | name | up | forward | scale | unit |
      |---|---|---|---|---|
      | `bodyloop_blender_m` | `+z` | `-y` | 1 | m - **BodyLoop's own space**, and Blender's; the
    default |
      | `gltf_unity_m` | `+y` | `+z` | 1 | m (glTF 2.0 section 3.4; also three.js, Godot, Unity) |
      | `clo3d_mm` | `+y` | `+z` | 1000 | mm |
      | `3ds_max_cm` | `+z` | `-y` | 100 | cm (3ds Max, system unit assumed to be cm) |
      | `unreal_cm` | `+z` | `+x` | 100 | cm |

      `scale` is the factor applied to BodyLoop's metres, so it *is* the unit: **1 = metres,
      100 = centimetres, 1000 = millimetres**. A preset's unit applies to every format, `.glb`
      included.

    * `up` / `forward` / `scale` describe a target relative to BodyLoop's space by hand. Give one
      axis and the other is derived, so `up=+y` alone (or `forward=+z` alone) is the glTF frame.
      `scale` picks the unit the same way (`1` m, `100` cm, `1000` mm - the example picker next to
      the field lists them), so `scale=1000` alone converts metres to millimetres without rotating.

    Combining `convention` with any of `up` / `forward` / `scale` is a 400. Asking for nothing at
    all - or for a target that is BodyLoop's own space, such as `convention=bodyloop_blender_m` -
    is answered with the stored file as it is.

    Rig, skins and custom vertex attributes survive the transform in the `.glb` format. The
    derived obj/stl/ply carry the body mesh of the default scene only.

    A transformed file says what was done to it: a `.glb` carries the frame, the scale and the
    unit under `asset.extras.bodyloop_export`, and an OBJ zip carries the same as
    `bodyloop_export.json` next to the `.obj`. Its `source` block names the space it came from
    (`bodyloop_blender_m`) with that space's axes and unit, so a file that has left the archive
    still says what BodyLoop's own convention is. That block also declares the units of the custom
    per-vertex attributes (`_DepthMap` in mm, the curvatures in 1/mm and 1/mm²), which are
    absolute and deliberately **not** rescaled with `scale`.

    Errors: 422 for a malformed parameter, 400 for a mixed request or a combination that is not a
    valid frame (e.g. `up=+y&forward=+y`), 500 if the stored model cannot be converted.

    Args:
        viatar_id (int):
        model_name (str):
        convention (GetModelApiV2ViatarsViatarIdModelsModelNameGetConventionType0 | None | Unset):
            Target space of an application, axes **and** unit at once - the unit is part of the name.
            `bodyloop_blender_m` is BodyLoop's own space (+z up, -y forward, metres) and the default.
            Mutually exclusive with `up`/`forward`/`scale`.
        scale (float | None | Unset): Multiplies every length of BodyLoop's metre-based model, so
            it picks the unit of the result: `1` = metres (m), `100` = centimetres (cm), `1000` =
            millimetres (mm). Any other positive factor up to 1e6 works too, e.g. `39.3701` for
            inches.
        up (GetModelApiV2ViatarsViatarIdModelsModelNameGetUpType0 | None | Unset): Up axis of the
            target frame.
        forward (GetModelApiV2ViatarsViatarIdModelsModelNameGetForwardType0 | None | Unset): Axis
            the front of the model points along.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        viatar_id=viatar_id,
        model_name=model_name,
        convention=convention,
        scale=scale,
        up=up,
        forward=forward,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    viatar_id: int,
    model_name: str,
    *,
    client: AuthenticatedClient,
    convention: GetModelApiV2ViatarsViatarIdModelsModelNameGetConventionType0 | None | Unset = UNSET,
    scale: float | None | Unset = UNSET,
    up: GetModelApiV2ViatarsViatarIdModelsModelNameGetUpType0 | None | Unset = UNSET,
    forward: GetModelApiV2ViatarsViatarIdModelsModelNameGetForwardType0 | None | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Get Model

     Returns the model specified model of the matching viatar. **(Do not use this endpoint via
    RTKQuery)**

    **BodyLoop's own space** is what you get if you ask for nothing: **`+z` up, `-y` forward**
    (the subject faces `-y`), right-handed, in **metres** - a 1.78 m scan is 1.78 units tall.
    Every model is stored and measured in it, and it is the frame every option below is relative
    to. Its name in the table is `bodyloop_blender_m`; Blender's default space is the same one.

    The model can be reoriented and rescaled on the way out, in one of two ways - never both:

    * `convention=<name>` asks for a target space as a whole, axes **and** unit together. There is
      one entry per distinct space, and its name ends in the unit it produces:

      | name | up | forward | scale | unit |
      |---|---|---|---|---|
      | `bodyloop_blender_m` | `+z` | `-y` | 1 | m - **BodyLoop's own space**, and Blender's; the
    default |
      | `gltf_unity_m` | `+y` | `+z` | 1 | m (glTF 2.0 section 3.4; also three.js, Godot, Unity) |
      | `clo3d_mm` | `+y` | `+z` | 1000 | mm |
      | `3ds_max_cm` | `+z` | `-y` | 100 | cm (3ds Max, system unit assumed to be cm) |
      | `unreal_cm` | `+z` | `+x` | 100 | cm |

      `scale` is the factor applied to BodyLoop's metres, so it *is* the unit: **1 = metres,
      100 = centimetres, 1000 = millimetres**. A preset's unit applies to every format, `.glb`
      included.

    * `up` / `forward` / `scale` describe a target relative to BodyLoop's space by hand. Give one
      axis and the other is derived, so `up=+y` alone (or `forward=+z` alone) is the glTF frame.
      `scale` picks the unit the same way (`1` m, `100` cm, `1000` mm - the example picker next to
      the field lists them), so `scale=1000` alone converts metres to millimetres without rotating.

    Combining `convention` with any of `up` / `forward` / `scale` is a 400. Asking for nothing at
    all - or for a target that is BodyLoop's own space, such as `convention=bodyloop_blender_m` -
    is answered with the stored file as it is.

    Rig, skins and custom vertex attributes survive the transform in the `.glb` format. The
    derived obj/stl/ply carry the body mesh of the default scene only.

    A transformed file says what was done to it: a `.glb` carries the frame, the scale and the
    unit under `asset.extras.bodyloop_export`, and an OBJ zip carries the same as
    `bodyloop_export.json` next to the `.obj`. Its `source` block names the space it came from
    (`bodyloop_blender_m`) with that space's axes and unit, so a file that has left the archive
    still says what BodyLoop's own convention is. That block also declares the units of the custom
    per-vertex attributes (`_DepthMap` in mm, the curvatures in 1/mm and 1/mm²), which are
    absolute and deliberately **not** rescaled with `scale`.

    Errors: 422 for a malformed parameter, 400 for a mixed request or a combination that is not a
    valid frame (e.g. `up=+y&forward=+y`), 500 if the stored model cannot be converted.

    Args:
        viatar_id (int):
        model_name (str):
        convention (GetModelApiV2ViatarsViatarIdModelsModelNameGetConventionType0 | None | Unset):
            Target space of an application, axes **and** unit at once - the unit is part of the name.
            `bodyloop_blender_m` is BodyLoop's own space (+z up, -y forward, metres) and the default.
            Mutually exclusive with `up`/`forward`/`scale`.
        scale (float | None | Unset): Multiplies every length of BodyLoop's metre-based model, so
            it picks the unit of the result: `1` = metres (m), `100` = centimetres (cm), `1000` =
            millimetres (mm). Any other positive factor up to 1e6 works too, e.g. `39.3701` for
            inches.
        up (GetModelApiV2ViatarsViatarIdModelsModelNameGetUpType0 | None | Unset): Up axis of the
            target frame.
        forward (GetModelApiV2ViatarsViatarIdModelsModelNameGetForwardType0 | None | Unset): Axis
            the front of the model points along.

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
            convention=convention,
            scale=scale,
            up=up,
            forward=forward,
        )
    ).parsed
