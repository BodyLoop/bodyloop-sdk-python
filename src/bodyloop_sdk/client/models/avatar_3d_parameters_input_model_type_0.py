from typing import Literal, cast

Avatar3DParametersInputModelType0 = Literal["A-Pose (Female)", "A-Pose (Male)", "No Model"]

AVATAR_3D_PARAMETERS_INPUT_MODEL_TYPE_0_VALUES: set[Avatar3DParametersInputModelType0] = {
    "A-Pose (Female)",
    "A-Pose (Male)",
    "No Model",
}


def check_avatar_3d_parameters_input_model_type_0(value: str) -> Avatar3DParametersInputModelType0:
    if value in AVATAR_3D_PARAMETERS_INPUT_MODEL_TYPE_0_VALUES:
        return cast(Avatar3DParametersInputModelType0, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AVATAR_3D_PARAMETERS_INPUT_MODEL_TYPE_0_VALUES!r}")
