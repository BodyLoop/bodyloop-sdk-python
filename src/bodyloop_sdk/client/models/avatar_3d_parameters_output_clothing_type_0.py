from typing import Literal, cast

Avatar3DParametersOutputClothingType0 = Literal["Loose", "Tight"]

AVATAR_3D_PARAMETERS_OUTPUT_CLOTHING_TYPE_0_VALUES: set[Avatar3DParametersOutputClothingType0] = {
    "Loose",
    "Tight",
}


def check_avatar_3d_parameters_output_clothing_type_0(value: str) -> Avatar3DParametersOutputClothingType0:
    if value in AVATAR_3D_PARAMETERS_OUTPUT_CLOTHING_TYPE_0_VALUES:
        return cast(Avatar3DParametersOutputClothingType0, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AVATAR_3D_PARAMETERS_OUTPUT_CLOTHING_TYPE_0_VALUES!r}"
    )
