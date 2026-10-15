"""Contains all the data models used in inputs/outputs"""

from .address import Address
from .analyzed_avatar_3d_parameters import AnalyzedAvatar3DParameters
from .angle import Angle
from .angle_angles_type_0 import AngleAnglesType0
from .angle_detail import AngleDetail
from .angle_detail_angles_type_0 import AngleDetailAnglesType0
from .angle_detail_details import AngleDetailDetails
from .angle_detail_preference_type_0 import AngleDetailPreferenceType0
from .angle_preference_type_0 import AnglePreferenceType0
from .avatar_3d_parameters import Avatar3DParameters
from .avatar_3d_parameters_clothing_type_0 import Avatar3DParametersClothingType0
from .avatar_3d_parameters_model_type_0 import Avatar3DParametersModelType0
from .avatar_3d_parameters_pose_type_0 import Avatar3DParametersPoseType0
from .axis import Axis
from .axis_detail import AxisDetail
from .axis_detail_details import AxisDetailDetails
from .axis_detail_rotation_type_0 import AxisDetailRotationType0
from .axis_rotation_type_0 import AxisRotationType0
from .body_apitoken_api_v2_authentification_users_username_api_token_post import (
    BodyApitokenApiV2AuthentificationUsersUsernameApiTokenPost,
)
from .body_apply_preset_api_v2_viatars_viatar_id_preset_put import BodyApplyPresetApiV2ViatarsViatarIdPresetPut
from .body_capture_camera_image_api_v2_system_cameras_camera_capture_post import (
    BodyCaptureCameraImageApiV2SystemCamerasCameraCapturePost,
)
from .body_create_first_admin_api_v2_authentification_users_first_admin_post import (
    BodyCreateFirstAdminApiV2AuthentificationUsersFirstAdminPost,
)
from .body_create_preset_api_v2_presets_post import BodyCreatePresetApiV2PresetsPost
from .body_create_user_api_v2_authentification_users_post import BodyCreateUserApiV2AuthentificationUsersPost
from .body_diagnostics_api_v2_system_diagnostic_post import BodyDiagnosticsApiV2SystemDiagnosticPost
from .body_factory_reset_api_v2_system_factory_reset_post import BodyFactoryResetApiV2SystemFactoryResetPost
from .body_import_preset_api_v2_presets_import_post import BodyImportPresetApiV2PresetsImportPost
from .body_license_update_api_v2_system_license_update_post import BodyLicenseUpdateApiV2SystemLicenseUpdatePost
from .body_login_api_v2_authentification_token_post import BodyLoginApiV2AuthentificationTokenPost
from .body_override_preset_api_v2_presets_preset_id_put import BodyOverridePresetApiV2PresetsPresetIdPut
from .body_patch_update_stream_api_v2_system_update_update_stream_patch import (
    BodyPatchUpdateStreamApiV2SystemUpdateUpdateStreamPatch,
)
from .body_patch_update_stream_api_v2_system_update_update_stream_patch_update_stream import (
    BodyPatchUpdateStreamApiV2SystemUpdateUpdateStreamPatchUpdateStream,
)
from .body_set_event_api_v2_statistic_event_post import BodySetEventApiV2StatisticEventPost
from .body_set_event_api_v2_statistic_event_post_event_status_type_0 import (
    BodySetEventApiV2StatisticEventPostEventStatusType0,
)
from .body_start_target_creation_api_v2_system_initializations_scanner_init_id_targets_post import (
    BodyStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPost,
)
from .body_start_target_creation_api_v2_system_initializations_scanner_init_id_targets_post_recreate_target_kind_type_0 import (
    BodyStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPostRecreateTargetKindType0,
)
from .body_start_target_creation_api_v2_system_initializations_scanner_init_id_targets_post_target_kind import (
    BodyStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPostTargetKind,
)
from .body_start_target_creation_api_v2_viatars_viatar_id_targets_post import (
    BodyStartTargetCreationApiV2ViatarsViatarIdTargetsPost,
)
from .body_start_target_creation_api_v2_viatars_viatar_id_targets_post_target_kind import (
    BodyStartTargetCreationApiV2ViatarsViatarIdTargetsPostTargetKind,
)
from .body_test_blink_lights_api_v2_system_lights_blink_post import BodyTestBlinkLightsApiV2SystemLightsBlinkPost
from .body_test_blink_lights_api_v2_system_lights_blink_post_mode import (
    BodyTestBlinkLightsApiV2SystemLightsBlinkPostMode,
)
from .body_tls_cert_update_api_v2_system_tls_certificate_put import BodyTlsCertUpdateApiV2SystemTlsCertificatePut
from .body_update_keyboard_layout_api_v2_system_settings_keyboard_layout_patch import (
    BodyUpdateKeyboardLayoutApiV2SystemSettingsKeyboardLayoutPatch,
)
from .body_update_user_api_v2_authentification_users_username_patch import (
    BodyUpdateUserApiV2AuthentificationUsersUsernamePatch,
)
from .body_update_user_api_v2_authentification_users_username_patch_user_group_type_0 import (
    BodyUpdateUserApiV2AuthentificationUsersUsernamePatchUserGroupType0,
)
from .body_upload_imageset_2d_api_v2_viatars_viatar_id_targets_imageset_2d_post import (
    BodyUploadImageset2DApiV2ViatarsViatarIdTargetsImageset2DPost,
)
from .body_upload_mesh_3d_api_v2_viatars_viatar_id_targets_mesh_3d_post import (
    BodyUploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPost,
)
from .body_upload_report_api_v2_reports_post import BodyUploadReportApiV2ReportsPost
from .contact import Contact
from .crosssection import Crosssection
from .crosssection_areas_type_0 import CrosssectionAreasType0
from .crosssection_circumferences_type_0 import CrosssectionCircumferencesType0
from .crosssection_contours_type_0 import CrosssectionContoursType0
from .crosssection_detail import CrosssectionDetail
from .crosssection_detail_areas_type_0 import CrosssectionDetailAreasType0
from .crosssection_detail_circumferences_type_0 import CrosssectionDetailCircumferencesType0
from .crosssection_detail_contours_type_0 import CrosssectionDetailContoursType0
from .crosssection_detail_details import CrosssectionDetailDetails
from .crosssection_detail_plane_type_type_0 import CrosssectionDetailPlaneTypeType0
from .crosssection_detail_preference_type_0 import CrosssectionDetailPreferenceType0
from .crosssection_detail_skeleton_position_type_0 import CrosssectionDetailSkeletonPositionType0
from .crosssection_plane_type_type_0 import CrosssectionPlaneTypeType0
from .crosssection_preference_type_0 import CrosssectionPreferenceType0
from .crosssection_series_point import CrosssectionSeriesPoint
from .crosssection_skeleton_position_type_0 import CrosssectionSkeletonPositionType0
from .delete_angle_api_v2_viatars_viatar_id_angles_angle_path_delete_response_delete_angle_api_v2_viatars_viatar_id_angles_angle_path_delete import (
    DeleteAngleApiV2ViatarsViatarIdAnglesAnglePathDeleteResponseDeleteAngleApiV2ViatarsViatarIdAnglesAnglePathDelete,
)
from .delete_axis_api_v2_viatars_viatar_id_axes_axis_path_delete_response_delete_axis_api_v2_viatars_viatar_id_axes_axis_path_delete import (
    DeleteAxisApiV2ViatarsViatarIdAxesAxisPathDeleteResponseDeleteAxisApiV2ViatarsViatarIdAxesAxisPathDelete,
)
from .delete_crosssection_api_v2_viatars_viatar_id_crosssections_crosssection_path_delete_response_delete_crosssection_api_v2_viatars_viatar_id_crosssections_crosssection_path_delete import (
    DeleteCrosssectionApiV2ViatarsViatarIdCrosssectionsCrosssectionPathDeleteResponseDeleteCrosssectionApiV2ViatarsViatarIdCrosssectionsCrosssectionPathDelete,
)
from .delete_distance_api_v2_viatars_viatar_id_distances_distance_path_delete_response_delete_distance_api_v2_viatars_viatar_id_distances_distance_path_delete import (
    DeleteDistanceApiV2ViatarsViatarIdDistancesDistancePathDeleteResponseDeleteDistanceApiV2ViatarsViatarIdDistancesDistancePathDelete,
)
from .delete_height_api_v2_viatars_viatar_id_heights_height_path_delete_response_delete_height_api_v2_viatars_viatar_id_heights_height_path_delete import (
    DeleteHeightApiV2ViatarsViatarIdHeightsHeightPathDeleteResponseDeleteHeightApiV2ViatarsViatarIdHeightsHeightPathDelete,
)
from .delete_marker_api_v2_viatars_viatar_id_markers_marker_path_delete_response_delete_marker_api_v2_viatars_viatar_id_markers_marker_path_delete import (
    DeleteMarkerApiV2ViatarsViatarIdMarkersMarkerPathDeleteResponseDeleteMarkerApiV2ViatarsViatarIdMarkersMarkerPathDelete,
)
from .delete_parameters_api_v2_parameters_parameters_id_delete_response_delete_parameters_api_v2_parameters_parameters_id_delete import (
    DeleteParametersApiV2ParametersParametersIdDeleteResponseDeleteParametersApiV2ParametersParametersIdDelete,
)
from .delete_polygonal_chain_api_v2_viatars_viatar_id_polygonal_chains_polygonal_chain_path_delete_response_delete_polygonal_chain_api_v2_viatars_viatar_id_polygonal_chains_polygonal_chain_path_delete import (
    DeletePolygonalChainApiV2ViatarsViatarIdPolygonalChainsPolygonalChainPathDeleteResponseDeletePolygonalChainApiV2ViatarsViatarIdPolygonalChainsPolygonalChainPathDelete,
)
from .delete_preset_api_v2_presets_preset_id_delete_response_delete_preset_api_v2_presets_preset_id_delete import (
    DeletePresetApiV2PresetsPresetIdDeleteResponseDeletePresetApiV2PresetsPresetIdDelete,
)
from .delete_property_api_v2_viatars_viatar_id_properties_property_path_delete_response_delete_property_api_v2_viatars_viatar_id_properties_property_path_delete import (
    DeletePropertyApiV2ViatarsViatarIdPropertiesPropertyPathDeleteResponseDeletePropertyApiV2ViatarsViatarIdPropertiesPropertyPathDelete,
)
from .delete_viatar_api_v2_viatars_viatar_id_delete_response_delete_viatar_api_v2_viatars_viatar_id_delete import (
    DeleteViatarApiV2ViatarsViatarIdDeleteResponseDeleteViatarApiV2ViatarsViatarIdDelete,
)
from .distance import Distance
from .distance_contours_type_0 import DistanceContoursType0
from .distance_detail import DistanceDetail
from .distance_detail_contours_type_0 import DistanceDetailContoursType0
from .distance_detail_details import DistanceDetailDetails
from .distance_detail_distances_type_0 import DistanceDetailDistancesType0
from .distance_detail_preference_type_0 import DistanceDetailPreferenceType0
from .distance_distances_type_0 import DistanceDistancesType0
from .distance_preference_type_0 import DistancePreferenceType0
from .export_options import ExportOptions
from .export_options_avatar_3d_format_type_0 import ExportOptionsAvatar3DFormatType0
from .export_options_measurements_format_type_0 import ExportOptionsMeasurementsFormatType0
from .export_options_mesh_3d_format_type_0 import ExportOptionsMesh3DFormatType0
from .export_options_view_format_type_0 import ExportOptionsViewFormatType0
from .external_authentification_settings import ExternalAuthentificationSettings
from .external_upload_settings import ExternalUploadSettings
from .get_event_count_api_v2_statistic_count_get_event_status_type_0 import (
    GetEventCountApiV2StatisticCountGetEventStatusType0,
)
from .get_event_count_api_v2_statistic_count_get_response_get_event_count_api_v2_statistic_count_get import (
    GetEventCountApiV2StatisticCountGetResponseGetEventCountApiV2StatisticCountGet,
)
from .get_image_api_v2_viatars_viatar_id_images_image_type_image_name_get_image_type import (
    GetImageApiV2ViatarsViatarIdImagesImageTypeImageNameGetImageType,
)
from .get_image_names_api_v2_viatars_viatar_id_images_get_response_get_image_names_api_v2_viatars_viatar_id_images_get import (
    GetImageNamesApiV2ViatarsViatarIdImagesGetResponseGetImageNamesApiV2ViatarsViatarIdImagesGet,
)
from .get_initialization_status_api_v2_system_initializations_scanner_init_id_targets_get_response_get_initialization_status_api_v2_system_initializations_scanner_init_id_targets_get import (
    GetInitializationStatusApiV2SystemInitializationsScannerInitIdTargetsGetResponseGetInitializationStatusApiV2SystemInitializationsScannerInitIdTargetsGet,
)
from .get_model_api_v2_viatars_viatar_id_models_model_name_get_convention_type_0 import (
    GetModelApiV2ViatarsViatarIdModelsModelNameGetConventionType0,
)
from .get_model_api_v2_viatars_viatar_id_models_model_name_get_forward_type_0 import (
    GetModelApiV2ViatarsViatarIdModelsModelNameGetForwardType0,
)
from .get_model_api_v2_viatars_viatar_id_models_model_name_get_up_type_0 import (
    GetModelApiV2ViatarsViatarIdModelsModelNameGetUpType0,
)
from .get_model_names_api_v2_viatars_viatar_id_models_get_response_get_model_names_api_v2_viatars_viatar_id_models_get import (
    GetModelNamesApiV2ViatarsViatarIdModelsGetResponseGetModelNamesApiV2ViatarsViatarIdModelsGet,
)
from .get_targets_api_v2_viatars_viatar_id_targets_get_response_get_targets_api_v2_viatars_viatar_id_targets_get import (
    GetTargetsApiV2ViatarsViatarIdTargetsGetResponseGetTargetsApiV2ViatarsViatarIdTargetsGet,
)
from .height import Height
from .height_detail import HeightDetail
from .height_detail_details import HeightDetailDetails
from .http_validation_error import HTTPValidationError
from .image_set_2d_parameters import ImageSet2DParameters
from .marker import Marker
from .marker_detail import MarkerDetail
from .marker_detail_marker_type_type_0 import MarkerDetailMarkerTypeType0
from .marker_detail_overriding_type_0 import MarkerDetailOverridingType0
from .marker_detail_refering_measures import MarkerDetailReferingMeasures
from .marker_marker_type_type_0 import MarkerMarkerTypeType0
from .mesh_3d_parameters import Mesh3DParameters
from .mesh_3d_parameters_detail_type_0 import Mesh3DParametersDetailType0
from .meta import Meta
from .observation_model import ObservationModel
from .observations_parameters import ObservationsParameters
from .parameters import Parameters
from .parameters_data import ParametersData
from .polygonal_chain import PolygonalChain
from .polygonal_chain_contours_type_0 import PolygonalChainContoursType0
from .polygonal_chain_detail import PolygonalChainDetail
from .polygonal_chain_detail_contours_type_0 import PolygonalChainDetailContoursType0
from .polygonal_chain_detail_details import PolygonalChainDetailDetails
from .polygonal_chain_detail_distances_type_0 import PolygonalChainDetailDistancesType0
from .polygonal_chain_detail_preference_type_0 import PolygonalChainDetailPreferenceType0
from .polygonal_chain_distances_type_0 import PolygonalChainDistancesType0
from .polygonal_chain_preference_type_0 import PolygonalChainPreferenceType0
from .preference import Preference
from .preference_data import PreferenceData
from .preset import Preset
from .preset_attributes_external_type_0 import PresetAttributesExternalType0
from .preset_update import PresetUpdate
from .preset_update_attributes_external_type_0 import PresetUpdateAttributesExternalType0
from .proband import Proband
from .proband_attributes_external_type_0 import ProbandAttributesExternalType0
from .proband_data import ProbandData
from .proband_data_attributes_external_type_0 import ProbandDataAttributesExternalType0
from .proband_detail import ProbandDetail
from .proband_detail_attributes_external_type_0 import ProbandDetailAttributesExternalType0
from .property_ import Property
from .report import Report
from .report_parameters import ReportParameters
from .report_report_type import ReportReportType
from .scanner_initalization import ScannerInitalization
from .scanner_initalization_data import ScannerInitalizationData
from .scanner_initalization_data_scanner_type_type_0 import ScannerInitalizationDataScannerTypeType0
from .scanner_initalization_data_targets_type_0 import ScannerInitalizationDataTargetsType0
from .scanner_initalization_scanner_type_type_0 import ScannerInitalizationScannerTypeType0
from .scanner_initalization_targets_type_0 import ScannerInitalizationTargetsType0
from .start_target_creation_api_v2_system_initializations_scanner_init_id_targets_post_response_start_target_creation_api_v2_system_initializations_scanner_init_id_targets_post import (
    StartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPostResponseStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPost,
)
from .start_target_creation_api_v2_viatars_viatar_id_targets_post_response_start_target_creation_api_v2_viatars_viatar_id_targets_post import (
    StartTargetCreationApiV2ViatarsViatarIdTargetsPostResponseStartTargetCreationApiV2ViatarsViatarIdTargetsPost,
)
from .state import State
from .state_acquisition_state import StateAcquisitionState
from .state_backend_state import StateBackendState
from .state_general_state import StateGeneralState
from .state_initialization_state import StateInitializationState
from .system import System
from .system_attributes_external_type_0 import SystemAttributesExternalType0
from .system_data import SystemData
from .system_data_attributes_external_type_0 import SystemDataAttributesExternalType0
from .system_data_update_stream_type_0 import SystemDataUpdateStreamType0
from .system_os import SystemOs
from .system_os_data import SystemOsData
from .system_os_network_interfaces_type_0 import SystemOsNetworkInterfacesType0
from .system_os_network_interfaces_type_0_additional_property import SystemOsNetworkInterfacesType0AdditionalProperty
from .system_preference import SystemPreference
from .system_update_stream_type_0 import SystemUpdateStreamType0
from .target import Target
from .target_state import TargetState
from .target_state_status_type_0 import TargetStateStatusType0
from .token import Token
from .upload_credentials import UploadCredentials
from .upload_credentials_headers_type_0 import UploadCredentialsHeadersType0
from .upload_credentials_method_type_0 import UploadCredentialsMethodType0
from .upload_imageset_2d_api_v2_viatars_viatar_id_targets_imageset_2d_post_response_upload_imageset_2d_api_v2_viatars_viatar_id_targets_imageset_2d_post import (
    UploadImageset2DApiV2ViatarsViatarIdTargetsImageset2DPostResponseUploadImageset2DApiV2ViatarsViatarIdTargetsImageset2DPost,
)
from .upload_mesh_3d_api_v2_viatars_viatar_id_targets_mesh_3d_post_response_upload_mesh_3d_api_v2_viatars_viatar_id_targets_mesh_3d_post import (
    UploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPostResponseUploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPost,
)
from .user import User
from .user_api_token import UserApiToken
from .user_data import UserData
from .user_data_preferences_type_0 import UserDataPreferencesType0
from .user_data_user_group import UserDataUserGroup
from .user_preferences_type_0 import UserPreferencesType0
from .user_user_group import UserUserGroup
from .validation_error import ValidationError
from .validation_error_context import ValidationErrorContext
from .viatar import Viatar
from .viatar_attributes_external_type_0 import ViatarAttributesExternalType0
from .viatar_data import ViatarData
from .viatar_data_attributes_external_type_0 import ViatarDataAttributesExternalType0
from .viatar_data_observations_type_0 import ViatarDataObservationsType0
from .viatar_data_targets_type_0 import ViatarDataTargetsType0
from .viatar_observations_type_0 import ViatarObservationsType0
from .viatar_targets_type_0 import ViatarTargetsType0

__all__ = (
    "Address",
    "AnalyzedAvatar3DParameters",
    "Angle",
    "AngleAnglesType0",
    "AngleDetail",
    "AngleDetailAnglesType0",
    "AngleDetailDetails",
    "AngleDetailPreferenceType0",
    "AnglePreferenceType0",
    "Avatar3DParameters",
    "Avatar3DParametersClothingType0",
    "Avatar3DParametersModelType0",
    "Avatar3DParametersPoseType0",
    "Axis",
    "AxisDetail",
    "AxisDetailDetails",
    "AxisDetailRotationType0",
    "AxisRotationType0",
    "BodyApitokenApiV2AuthentificationUsersUsernameApiTokenPost",
    "BodyApplyPresetApiV2ViatarsViatarIdPresetPut",
    "BodyCaptureCameraImageApiV2SystemCamerasCameraCapturePost",
    "BodyCreateFirstAdminApiV2AuthentificationUsersFirstAdminPost",
    "BodyCreatePresetApiV2PresetsPost",
    "BodyCreateUserApiV2AuthentificationUsersPost",
    "BodyDiagnosticsApiV2SystemDiagnosticPost",
    "BodyFactoryResetApiV2SystemFactoryResetPost",
    "BodyImportPresetApiV2PresetsImportPost",
    "BodyLicenseUpdateApiV2SystemLicenseUpdatePost",
    "BodyLoginApiV2AuthentificationTokenPost",
    "BodyOverridePresetApiV2PresetsPresetIdPut",
    "BodyPatchUpdateStreamApiV2SystemUpdateUpdateStreamPatch",
    "BodyPatchUpdateStreamApiV2SystemUpdateUpdateStreamPatchUpdateStream",
    "BodySetEventApiV2StatisticEventPost",
    "BodySetEventApiV2StatisticEventPostEventStatusType0",
    "BodyStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPost",
    "BodyStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPostRecreateTargetKindType0",
    "BodyStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPostTargetKind",
    "BodyStartTargetCreationApiV2ViatarsViatarIdTargetsPost",
    "BodyStartTargetCreationApiV2ViatarsViatarIdTargetsPostTargetKind",
    "BodyTestBlinkLightsApiV2SystemLightsBlinkPost",
    "BodyTestBlinkLightsApiV2SystemLightsBlinkPostMode",
    "BodyTlsCertUpdateApiV2SystemTlsCertificatePut",
    "BodyUpdateKeyboardLayoutApiV2SystemSettingsKeyboardLayoutPatch",
    "BodyUpdateUserApiV2AuthentificationUsersUsernamePatch",
    "BodyUpdateUserApiV2AuthentificationUsersUsernamePatchUserGroupType0",
    "BodyUploadImageset2DApiV2ViatarsViatarIdTargetsImageset2DPost",
    "BodyUploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPost",
    "BodyUploadReportApiV2ReportsPost",
    "Contact",
    "Crosssection",
    "CrosssectionAreasType0",
    "CrosssectionCircumferencesType0",
    "CrosssectionContoursType0",
    "CrosssectionDetail",
    "CrosssectionDetailAreasType0",
    "CrosssectionDetailCircumferencesType0",
    "CrosssectionDetailContoursType0",
    "CrosssectionDetailDetails",
    "CrosssectionDetailPlaneTypeType0",
    "CrosssectionDetailPreferenceType0",
    "CrosssectionDetailSkeletonPositionType0",
    "CrosssectionPlaneTypeType0",
    "CrosssectionPreferenceType0",
    "CrosssectionSeriesPoint",
    "CrosssectionSkeletonPositionType0",
    "DeleteAngleApiV2ViatarsViatarIdAnglesAnglePathDeleteResponseDeleteAngleApiV2ViatarsViatarIdAnglesAnglePathDelete",
    "DeleteAxisApiV2ViatarsViatarIdAxesAxisPathDeleteResponseDeleteAxisApiV2ViatarsViatarIdAxesAxisPathDelete",
    "DeleteCrosssectionApiV2ViatarsViatarIdCrosssectionsCrosssectionPathDeleteResponseDeleteCrosssectionApiV2ViatarsViatarIdCrosssectionsCrosssectionPathDelete",
    "DeleteDistanceApiV2ViatarsViatarIdDistancesDistancePathDeleteResponseDeleteDistanceApiV2ViatarsViatarIdDistancesDistancePathDelete",
    "DeleteHeightApiV2ViatarsViatarIdHeightsHeightPathDeleteResponseDeleteHeightApiV2ViatarsViatarIdHeightsHeightPathDelete",
    "DeleteMarkerApiV2ViatarsViatarIdMarkersMarkerPathDeleteResponseDeleteMarkerApiV2ViatarsViatarIdMarkersMarkerPathDelete",
    "DeleteParametersApiV2ParametersParametersIdDeleteResponseDeleteParametersApiV2ParametersParametersIdDelete",
    "DeletePolygonalChainApiV2ViatarsViatarIdPolygonalChainsPolygonalChainPathDeleteResponseDeletePolygonalChainApiV2ViatarsViatarIdPolygonalChainsPolygonalChainPathDelete",
    "DeletePresetApiV2PresetsPresetIdDeleteResponseDeletePresetApiV2PresetsPresetIdDelete",
    "DeletePropertyApiV2ViatarsViatarIdPropertiesPropertyPathDeleteResponseDeletePropertyApiV2ViatarsViatarIdPropertiesPropertyPathDelete",
    "DeleteViatarApiV2ViatarsViatarIdDeleteResponseDeleteViatarApiV2ViatarsViatarIdDelete",
    "Distance",
    "DistanceContoursType0",
    "DistanceDetail",
    "DistanceDetailContoursType0",
    "DistanceDetailDetails",
    "DistanceDetailDistancesType0",
    "DistanceDetailPreferenceType0",
    "DistanceDistancesType0",
    "DistancePreferenceType0",
    "ExportOptions",
    "ExportOptionsAvatar3DFormatType0",
    "ExportOptionsMeasurementsFormatType0",
    "ExportOptionsMesh3DFormatType0",
    "ExportOptionsViewFormatType0",
    "ExternalAuthentificationSettings",
    "ExternalUploadSettings",
    "GetEventCountApiV2StatisticCountGetEventStatusType0",
    "GetEventCountApiV2StatisticCountGetResponseGetEventCountApiV2StatisticCountGet",
    "GetImageApiV2ViatarsViatarIdImagesImageTypeImageNameGetImageType",
    "GetImageNamesApiV2ViatarsViatarIdImagesGetResponseGetImageNamesApiV2ViatarsViatarIdImagesGet",
    "GetInitializationStatusApiV2SystemInitializationsScannerInitIdTargetsGetResponseGetInitializationStatusApiV2SystemInitializationsScannerInitIdTargetsGet",
    "GetModelApiV2ViatarsViatarIdModelsModelNameGetConventionType0",
    "GetModelApiV2ViatarsViatarIdModelsModelNameGetForwardType0",
    "GetModelApiV2ViatarsViatarIdModelsModelNameGetUpType0",
    "GetModelNamesApiV2ViatarsViatarIdModelsGetResponseGetModelNamesApiV2ViatarsViatarIdModelsGet",
    "GetTargetsApiV2ViatarsViatarIdTargetsGetResponseGetTargetsApiV2ViatarsViatarIdTargetsGet",
    "Height",
    "HeightDetail",
    "HeightDetailDetails",
    "HTTPValidationError",
    "ImageSet2DParameters",
    "Marker",
    "MarkerDetail",
    "MarkerDetailMarkerTypeType0",
    "MarkerDetailOverridingType0",
    "MarkerDetailReferingMeasures",
    "MarkerMarkerTypeType0",
    "Mesh3DParameters",
    "Mesh3DParametersDetailType0",
    "Meta",
    "ObservationModel",
    "ObservationsParameters",
    "Parameters",
    "ParametersData",
    "PolygonalChain",
    "PolygonalChainContoursType0",
    "PolygonalChainDetail",
    "PolygonalChainDetailContoursType0",
    "PolygonalChainDetailDetails",
    "PolygonalChainDetailDistancesType0",
    "PolygonalChainDetailPreferenceType0",
    "PolygonalChainDistancesType0",
    "PolygonalChainPreferenceType0",
    "Preference",
    "PreferenceData",
    "Preset",
    "PresetAttributesExternalType0",
    "PresetUpdate",
    "PresetUpdateAttributesExternalType0",
    "Proband",
    "ProbandAttributesExternalType0",
    "ProbandData",
    "ProbandDataAttributesExternalType0",
    "ProbandDetail",
    "ProbandDetailAttributesExternalType0",
    "Property",
    "Report",
    "ReportParameters",
    "ReportReportType",
    "ScannerInitalization",
    "ScannerInitalizationData",
    "ScannerInitalizationDataScannerTypeType0",
    "ScannerInitalizationDataTargetsType0",
    "ScannerInitalizationScannerTypeType0",
    "ScannerInitalizationTargetsType0",
    "StartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPostResponseStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPost",
    "StartTargetCreationApiV2ViatarsViatarIdTargetsPostResponseStartTargetCreationApiV2ViatarsViatarIdTargetsPost",
    "State",
    "StateAcquisitionState",
    "StateBackendState",
    "StateGeneralState",
    "StateInitializationState",
    "System",
    "SystemAttributesExternalType0",
    "SystemData",
    "SystemDataAttributesExternalType0",
    "SystemDataUpdateStreamType0",
    "SystemOs",
    "SystemOsData",
    "SystemOsNetworkInterfacesType0",
    "SystemOsNetworkInterfacesType0AdditionalProperty",
    "SystemPreference",
    "SystemUpdateStreamType0",
    "Target",
    "TargetState",
    "TargetStateStatusType0",
    "Token",
    "UploadCredentials",
    "UploadCredentialsHeadersType0",
    "UploadCredentialsMethodType0",
    "UploadImageset2DApiV2ViatarsViatarIdTargetsImageset2DPostResponseUploadImageset2DApiV2ViatarsViatarIdTargetsImageset2DPost",
    "UploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPostResponseUploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPost",
    "User",
    "UserApiToken",
    "UserData",
    "UserDataPreferencesType0",
    "UserDataUserGroup",
    "UserPreferencesType0",
    "UserUserGroup",
    "ValidationError",
    "ValidationErrorContext",
    "Viatar",
    "ViatarAttributesExternalType0",
    "ViatarData",
    "ViatarDataAttributesExternalType0",
    "ViatarDataObservationsType0",
    "ViatarDataTargetsType0",
    "ViatarObservationsType0",
    "ViatarTargetsType0",
)
