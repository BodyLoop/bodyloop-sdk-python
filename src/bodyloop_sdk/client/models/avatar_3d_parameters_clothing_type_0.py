from typing import Literal, cast

Avatar3DParametersClothingType0 = Literal["Loose", "Tight"]

AVATAR_3D_PARAMETERS_CLOTHING_TYPE_0_VALUES: set[Avatar3DParametersClothingType0] = {
    "Loose",
    "Tight",
}


def check_avatar_3d_parameters_clothing_type_0(value: str) -> Avatar3DParametersClothingType0:
    if value in AVATAR_3D_PARAMETERS_CLOTHING_TYPE_0_VALUES:
        return cast(Avatar3DParametersClothingType0, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AVATAR_3D_PARAMETERS_CLOTHING_TYPE_0_VALUES!r}")
