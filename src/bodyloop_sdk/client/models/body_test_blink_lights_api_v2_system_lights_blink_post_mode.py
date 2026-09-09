from typing import Literal

BodyTestBlinkLightsApiV2SystemLightsBlinkPostMode = Literal["crazy_blinking", "default", "slow"]

BODY_TEST_BLINK_LIGHTS_API_V2_SYSTEM_LIGHTS_BLINK_POST_MODE_VALUES: set[
    BodyTestBlinkLightsApiV2SystemLightsBlinkPostMode
] = {
    "crazy_blinking",
    "default",
    "slow",
}


def check_body_test_blink_lights_api_v2_system_lights_blink_post_mode(
    value: str,
) -> BodyTestBlinkLightsApiV2SystemLightsBlinkPostMode:
    if value in BODY_TEST_BLINK_LIGHTS_API_V2_SYSTEM_LIGHTS_BLINK_POST_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BODY_TEST_BLINK_LIGHTS_API_V2_SYSTEM_LIGHTS_BLINK_POST_MODE_VALUES!r}"
    )
