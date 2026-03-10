from typing import Literal, cast

Avatar3DParametersInputClothingType0 = Literal["Loose", "Tight"]

AVATAR_3D_PARAMETERS_INPUT_CLOTHING_TYPE_0_VALUES: set[Avatar3DParametersInputClothingType0] = {
    "Loose",
    "Tight",
}


def check_avatar_3d_parameters_input_clothing_type_0(value: str) -> Avatar3DParametersInputClothingType0:
    if value in AVATAR_3D_PARAMETERS_INPUT_CLOTHING_TYPE_0_VALUES:
        return cast(Avatar3DParametersInputClothingType0, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AVATAR_3D_PARAMETERS_INPUT_CLOTHING_TYPE_0_VALUES!r}"
    )
