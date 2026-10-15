from typing import Literal

GetModelApiV2ViatarsViatarIdModelsModelNameGetUpType0 = Literal["+x", "+y", "+z", "-x", "-y", "-z"]

GET_MODEL_API_V2_VIATARS_VIATAR_ID_MODELS_MODEL_NAME_GET_UP_TYPE_0_VALUES: set[
    GetModelApiV2ViatarsViatarIdModelsModelNameGetUpType0
] = {
    "+x",
    "+y",
    "+z",
    "-x",
    "-y",
    "-z",
}


def check_get_model_api_v2_viatars_viatar_id_models_model_name_get_up_type_0(
    value: str,
) -> GetModelApiV2ViatarsViatarIdModelsModelNameGetUpType0:
    if value in GET_MODEL_API_V2_VIATARS_VIATAR_ID_MODELS_MODEL_NAME_GET_UP_TYPE_0_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_MODEL_API_V2_VIATARS_VIATAR_ID_MODELS_MODEL_NAME_GET_UP_TYPE_0_VALUES!r}"
    )
