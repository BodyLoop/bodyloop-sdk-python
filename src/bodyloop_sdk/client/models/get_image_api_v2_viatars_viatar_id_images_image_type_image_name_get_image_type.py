from typing import Literal, cast

GetImageApiV2ViatarsViatarIdImagesImageTypeImageNameGetImageType = Literal["geometry", "texture"]

GET_IMAGE_API_V2_VIATARS_VIATAR_ID_IMAGES_IMAGE_TYPE_IMAGE_NAME_GET_IMAGE_TYPE_VALUES: set[
    GetImageApiV2ViatarsViatarIdImagesImageTypeImageNameGetImageType
] = {
    "geometry",
    "texture",
}


def check_get_image_api_v2_viatars_viatar_id_images_image_type_image_name_get_image_type(
    value: str,
) -> GetImageApiV2ViatarsViatarIdImagesImageTypeImageNameGetImageType:
    if value in GET_IMAGE_API_V2_VIATARS_VIATAR_ID_IMAGES_IMAGE_TYPE_IMAGE_NAME_GET_IMAGE_TYPE_VALUES:
        return cast(GetImageApiV2ViatarsViatarIdImagesImageTypeImageNameGetImageType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_IMAGE_API_V2_VIATARS_VIATAR_ID_IMAGES_IMAGE_TYPE_IMAGE_NAME_GET_IMAGE_TYPE_VALUES!r}"
    )
