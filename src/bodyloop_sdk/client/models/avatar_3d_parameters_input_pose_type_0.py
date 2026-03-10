from typing import Literal, cast

Avatar3DParametersInputPoseType0 = Literal["A-Pose", "FreeScan"]

AVATAR_3D_PARAMETERS_INPUT_POSE_TYPE_0_VALUES: set[Avatar3DParametersInputPoseType0] = {
    "A-Pose",
    "FreeScan",
}


def check_avatar_3d_parameters_input_pose_type_0(value: str) -> Avatar3DParametersInputPoseType0:
    if value in AVATAR_3D_PARAMETERS_INPUT_POSE_TYPE_0_VALUES:
        return cast(Avatar3DParametersInputPoseType0, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AVATAR_3D_PARAMETERS_INPUT_POSE_TYPE_0_VALUES!r}")
