from typing import Literal, cast

UploadCredentialsMethodType0 = Literal["POST", "PUT"]

UPLOAD_CREDENTIALS_METHOD_TYPE_0_VALUES: set[UploadCredentialsMethodType0] = {
    "POST",
    "PUT",
}


def check_upload_credentials_method_type_0(value: str) -> UploadCredentialsMethodType0:
    if value in UPLOAD_CREDENTIALS_METHOD_TYPE_0_VALUES:
        return cast(UploadCredentialsMethodType0, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPLOAD_CREDENTIALS_METHOD_TYPE_0_VALUES!r}")
