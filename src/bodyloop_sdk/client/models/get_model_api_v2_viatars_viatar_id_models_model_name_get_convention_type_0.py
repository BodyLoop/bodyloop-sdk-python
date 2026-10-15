from typing import Literal

GetModelApiV2ViatarsViatarIdModelsModelNameGetConventionType0 = Literal[
    "3ds_max_cm", "bodyloop_blender_m", "clo3d_mm", "gltf_unity_m", "unreal_cm"
]

GET_MODEL_API_V2_VIATARS_VIATAR_ID_MODELS_MODEL_NAME_GET_CONVENTION_TYPE_0_VALUES: set[
    GetModelApiV2ViatarsViatarIdModelsModelNameGetConventionType0
] = {
    "3ds_max_cm",
    "bodyloop_blender_m",
    "clo3d_mm",
    "gltf_unity_m",
    "unreal_cm",
}


def check_get_model_api_v2_viatars_viatar_id_models_model_name_get_convention_type_0(
    value: str,
) -> GetModelApiV2ViatarsViatarIdModelsModelNameGetConventionType0:
    if value in GET_MODEL_API_V2_VIATARS_VIATAR_ID_MODELS_MODEL_NAME_GET_CONVENTION_TYPE_0_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_MODEL_API_V2_VIATARS_VIATAR_ID_MODELS_MODEL_NAME_GET_CONVENTION_TYPE_0_VALUES!r}"
    )
