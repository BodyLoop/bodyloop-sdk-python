from typing import Literal

Avatar3DParametersModelType0 = Literal["A-Pose (Female)", "A-Pose (Male)", "No Model"]

AVATAR_3D_PARAMETERS_MODEL_TYPE_0_VALUES: set[Avatar3DParametersModelType0] = {
    "A-Pose (Female)",
    "A-Pose (Male)",
    "No Model",
}


def check_avatar_3d_parameters_model_type_0(value: str) -> Avatar3DParametersModelType0:
    if value in AVATAR_3D_PARAMETERS_MODEL_TYPE_0_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AVATAR_3D_PARAMETERS_MODEL_TYPE_0_VALUES!r}")
