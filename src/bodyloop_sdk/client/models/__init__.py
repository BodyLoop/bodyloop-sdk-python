"""Contains all the data models used in inputs/outputs"""

from .address import Address
from .analyzed_avatar_3d_parameters import AnalyzedAvatar3DParameters
from .angle import Angle
from .angle_angles_type_0 import AngleAnglesType0
from .avatar_3d_parameters_input import Avatar3DParametersInput
from .avatar_3d_parameters_input_clothing_type_0 import Avatar3DParametersInputClothingType0
from .avatar_3d_parameters_input_model_type_0 import Avatar3DParametersInputModelType0
from .avatar_3d_parameters_input_pose_type_0 import Avatar3DParametersInputPoseType0
from .avatar_3d_parameters_output import Avatar3DParametersOutput
from .avatar_3d_parameters_output_clothing_type_0 import Avatar3DParametersOutputClothingType0
from .avatar_3d_parameters_output_model_type_0 import Avatar3DParametersOutputModelType0
from .axis import Axis
from .axis_rotation_type_0 import AxisRotationType0
from .biomech_system_manager_models_scanner_init_target import BiomechSystemManagerModelsScannerInitTarget
from .biomech_system_manager_models_scanner_init_target_state import BiomechSystemManagerModelsScannerInitTargetState
from .biomech_system_manager_models_scanner_init_target_state_status_type_0 import (
    BiomechSystemManagerModelsScannerInitTargetStateStatusType0,
)
from .biomech_system_manager_models_viatar_target import BiomechSystemManagerModelsViatarTarget
from .biomech_system_manager_models_viatar_target_state import BiomechSystemManagerModelsViatarTargetState
from .biomech_system_manager_models_viatar_target_state_status_type_0 import (
    BiomechSystemManagerModelsViatarTargetStateStatusType0,
)
from .body_apitoken_api_v2_authentification_users_username_api_token_post import (
    BodyApitokenApiV2AuthentificationUsersUsernameApiTokenPost,
)
from .body_apply_preset_api_v2_viatars_viatar_id_preset_put import BodyApplyPresetApiV2ViatarsViatarIdPresetPut
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
from .body_start_target_creation_api_v2_system_initializations_scanner_init_id_targets_post import (
    BodyStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPost,
)
from .body_start_target_creation_api_v2_viatars_viatar_id_targets_post import (
    BodyStartTargetCreationApiV2ViatarsViatarIdTargetsPost,
)
from .body_start_target_creation_api_v2_viatars_viatar_id_targets_post_target_kind import (
    BodyStartTargetCreationApiV2ViatarsViatarIdTargetsPostTargetKind,
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
from .contact import Contact
from .crosssection import Crosssection
from .crosssection_areas_type_0 import CrosssectionAreasType0
from .crosssection_circumferences_type_0 import CrosssectionCircumferencesType0
from .crosssection_contours_type_0 import CrosssectionContoursType0
from .crosssection_skeleton_position_type_0 import CrosssectionSkeletonPositionType0
from .delete_parameters_api_v2_parameters_parameters_id_delete_response_delete_parameters_api_v2_parameters_parameters_id_delete import (
    DeleteParametersApiV2ParametersParametersIdDeleteResponseDeleteParametersApiV2ParametersParametersIdDelete,
)
from .delete_preset_api_v2_presets_preset_id_delete_response_delete_preset_api_v2_presets_preset_id_delete import (
    DeletePresetApiV2PresetsPresetIdDeleteResponseDeletePresetApiV2PresetsPresetIdDelete,
)
from .delete_viatar_api_v2_viatars_viatar_id_delete_response_delete_viatar_api_v2_viatars_viatar_id_delete import (
    DeleteViatarApiV2ViatarsViatarIdDeleteResponseDeleteViatarApiV2ViatarsViatarIdDelete,
)
from .distance import Distance
from .distance_distances_type_0 import DistanceDistancesType0
from .export_options import ExportOptions
from .export_options_avatar_3d_format_type_0 import ExportOptionsAvatar3DFormatType0
from .export_options_measurements_format_type_0 import ExportOptionsMeasurementsFormatType0
from .export_options_mesh_3d_format_type_0 import ExportOptionsMesh3DFormatType0
from .export_options_view_format_type_0 import ExportOptionsViewFormatType0
from .external_authentification_settings import ExternalAuthentificationSettings
from .external_upload_settings import ExternalUploadSettings
from .get_image_api_v2_viatars_viatar_id_images_image_type_image_name_get_image_type import (
    GetImageApiV2ViatarsViatarIdImagesImageTypeImageNameGetImageType,
)
from .get_image_names_api_v2_viatars_viatar_id_images_get_response_get_image_names_api_v2_viatars_viatar_id_images_get import (
    GetImageNamesApiV2ViatarsViatarIdImagesGetResponseGetImageNamesApiV2ViatarsViatarIdImagesGet,
)
from .get_initialization_status_api_v2_system_initializations_scanner_init_id_targets_get_response_get_initialization_status_api_v2_system_initializations_scanner_init_id_targets_get import (
    GetInitializationStatusApiV2SystemInitializationsScannerInitIdTargetsGetResponseGetInitializationStatusApiV2SystemInitializationsScannerInitIdTargetsGet,
)
from .get_model_names_api_v2_viatars_viatar_id_models_get_response_get_model_names_api_v2_viatars_viatar_id_models_get import (
    GetModelNamesApiV2ViatarsViatarIdModelsGetResponseGetModelNamesApiV2ViatarsViatarIdModelsGet,
)
from .get_targets_api_v2_viatars_viatar_id_targets_get_response_get_targets_api_v2_viatars_viatar_id_targets_get import (
    GetTargetsApiV2ViatarsViatarIdTargetsGetResponseGetTargetsApiV2ViatarsViatarIdTargetsGet,
)
from .height import Height
from .http_validation_error import HTTPValidationError
from .image_set_2d_parameters import ImageSet2DParameters
from .images import Images
from .images_geometry_type_0 import ImagesGeometryType0
from .images_texture_type_0 import ImagesTextureType0
from .marker import Marker
from .marker_detail import MarkerDetail
from .marker_detail_marker_type_type_0 import MarkerDetailMarkerTypeType0
from .marker_detail_overriding_type_0 import MarkerDetailOverridingType0
from .marker_detail_refering_measures import MarkerDetailReferingMeasures
from .marker_marker_type_type_0 import MarkerMarkerTypeType0
from .mesh_3d_parameters import Mesh3DParameters
from .mesh_3d_parameters_detail_type_0 import Mesh3DParametersDetailType0
from .meta import Meta
from .models import Models
from .models_dataprocessor_type_0 import ModelsDataprocessorType0
from .models_photogrammetry_type_0 import ModelsPhotogrammetryType0
from .parameters import Parameters
from .parameters_data_input import ParametersDataInput
from .parameters_data_output import ParametersDataOutput
from .preset import Preset
from .proband import Proband
from .proband_data import ProbandData
from .proband_detail import ProbandDetail
from .property_ import Property
from .report import Report
from .report_parameters import ReportParameters
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
from .system_data import SystemData
from .system_data_update_stream_type_0 import SystemDataUpdateStreamType0
from .system_os import SystemOs
from .system_os_data import SystemOsData
from .system_os_network_interfaces_type_0 import SystemOsNetworkInterfacesType0
from .system_os_network_interfaces_type_0_additional_property import SystemOsNetworkInterfacesType0AdditionalProperty
from .system_update_stream_type_0 import SystemUpdateStreamType0
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
from .user_data_user_group import UserDataUserGroup
from .user_user_group import UserUserGroup
from .validation_error import ValidationError
from .viatar import Viatar
from .viatar_angles_type_0 import ViatarAnglesType0
from .viatar_axes_type_0 import ViatarAxesType0
from .viatar_crosssections_type_0 import ViatarCrosssectionsType0
from .viatar_data import ViatarData
from .viatar_data_angles_type_0 import ViatarDataAnglesType0
from .viatar_data_axes_type_0 import ViatarDataAxesType0
from .viatar_data_crosssections_type_0 import ViatarDataCrosssectionsType0
from .viatar_data_distances_type_0 import ViatarDataDistancesType0
from .viatar_data_heights_type_0 import ViatarDataHeightsType0
from .viatar_data_markers_type_0 import ViatarDataMarkersType0
from .viatar_data_markers_type_0_additional_property import ViatarDataMarkersType0AdditionalProperty
from .viatar_data_observations_type_0 import ViatarDataObservationsType0
from .viatar_data_properties_type_0 import ViatarDataPropertiesType0
from .viatar_data_series import ViatarDataSeries
from .viatar_data_series_crosssections_type_0 import ViatarDataSeriesCrosssectionsType0
from .viatar_data_targets_type_0 import ViatarDataTargetsType0
from .viatar_distances_type_0 import ViatarDistancesType0
from .viatar_heights_type_0 import ViatarHeightsType0
from .viatar_markers_type_0 import ViatarMarkersType0
from .viatar_markers_type_0_additional_property import ViatarMarkersType0AdditionalProperty
from .viatar_observations_type_0 import ViatarObservationsType0
from .viatar_properties_type_0 import ViatarPropertiesType0
from .viatar_targets_type_0 import ViatarTargetsType0

__all__ = (
    "Address",
    "AnalyzedAvatar3DParameters",
    "Angle",
    "AngleAnglesType0",
    "Avatar3DParametersInput",
    "Avatar3DParametersInputClothingType0",
    "Avatar3DParametersInputModelType0",
    "Avatar3DParametersInputPoseType0",
    "Avatar3DParametersOutput",
    "Avatar3DParametersOutputClothingType0",
    "Avatar3DParametersOutputModelType0",
    "Axis",
    "AxisRotationType0",
    "BiomechSystemManagerModelsScannerInitTarget",
    "BiomechSystemManagerModelsScannerInitTargetState",
    "BiomechSystemManagerModelsScannerInitTargetStateStatusType0",
    "BiomechSystemManagerModelsViatarTarget",
    "BiomechSystemManagerModelsViatarTargetState",
    "BiomechSystemManagerModelsViatarTargetStateStatusType0",
    "BodyApitokenApiV2AuthentificationUsersUsernameApiTokenPost",
    "BodyApplyPresetApiV2ViatarsViatarIdPresetPut",
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
    "BodyStartTargetCreationApiV2SystemInitializationsScannerInitIdTargetsPost",
    "BodyStartTargetCreationApiV2ViatarsViatarIdTargetsPost",
    "BodyStartTargetCreationApiV2ViatarsViatarIdTargetsPostTargetKind",
    "BodyTlsCertUpdateApiV2SystemTlsCertificatePut",
    "BodyUpdateKeyboardLayoutApiV2SystemSettingsKeyboardLayoutPatch",
    "BodyUpdateUserApiV2AuthentificationUsersUsernamePatch",
    "BodyUpdateUserApiV2AuthentificationUsersUsernamePatchUserGroupType0",
    "BodyUploadImageset2DApiV2ViatarsViatarIdTargetsImageset2DPost",
    "BodyUploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPost",
    "Contact",
    "Crosssection",
    "CrosssectionAreasType0",
    "CrosssectionCircumferencesType0",
    "CrosssectionContoursType0",
    "CrosssectionSkeletonPositionType0",
    "DeleteParametersApiV2ParametersParametersIdDeleteResponseDeleteParametersApiV2ParametersParametersIdDelete",
    "DeletePresetApiV2PresetsPresetIdDeleteResponseDeletePresetApiV2PresetsPresetIdDelete",
    "DeleteViatarApiV2ViatarsViatarIdDeleteResponseDeleteViatarApiV2ViatarsViatarIdDelete",
    "Distance",
    "DistanceDistancesType0",
    "ExportOptions",
    "ExportOptionsAvatar3DFormatType0",
    "ExportOptionsMeasurementsFormatType0",
    "ExportOptionsMesh3DFormatType0",
    "ExportOptionsViewFormatType0",
    "ExternalAuthentificationSettings",
    "ExternalUploadSettings",
    "GetImageApiV2ViatarsViatarIdImagesImageTypeImageNameGetImageType",
    "GetImageNamesApiV2ViatarsViatarIdImagesGetResponseGetImageNamesApiV2ViatarsViatarIdImagesGet",
    "GetInitializationStatusApiV2SystemInitializationsScannerInitIdTargetsGetResponseGetInitializationStatusApiV2SystemInitializationsScannerInitIdTargetsGet",
    "GetModelNamesApiV2ViatarsViatarIdModelsGetResponseGetModelNamesApiV2ViatarsViatarIdModelsGet",
    "GetTargetsApiV2ViatarsViatarIdTargetsGetResponseGetTargetsApiV2ViatarsViatarIdTargetsGet",
    "Height",
    "HTTPValidationError",
    "Images",
    "ImageSet2DParameters",
    "ImagesGeometryType0",
    "ImagesTextureType0",
    "Marker",
    "MarkerDetail",
    "MarkerDetailMarkerTypeType0",
    "MarkerDetailOverridingType0",
    "MarkerDetailReferingMeasures",
    "MarkerMarkerTypeType0",
    "Mesh3DParameters",
    "Mesh3DParametersDetailType0",
    "Meta",
    "Models",
    "ModelsDataprocessorType0",
    "ModelsPhotogrammetryType0",
    "Parameters",
    "ParametersDataInput",
    "ParametersDataOutput",
    "Preset",
    "Proband",
    "ProbandData",
    "ProbandDetail",
    "Property",
    "Report",
    "ReportParameters",
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
    "SystemData",
    "SystemDataUpdateStreamType0",
    "SystemOs",
    "SystemOsData",
    "SystemOsNetworkInterfacesType0",
    "SystemOsNetworkInterfacesType0AdditionalProperty",
    "SystemUpdateStreamType0",
    "Token",
    "UploadCredentials",
    "UploadCredentialsHeadersType0",
    "UploadCredentialsMethodType0",
    "UploadImageset2DApiV2ViatarsViatarIdTargetsImageset2DPostResponseUploadImageset2DApiV2ViatarsViatarIdTargetsImageset2DPost",
    "UploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPostResponseUploadMesh3DApiV2ViatarsViatarIdTargetsMesh3DPost",
    "User",
    "UserApiToken",
    "UserData",
    "UserDataUserGroup",
    "UserUserGroup",
    "ValidationError",
    "Viatar",
    "ViatarAnglesType0",
    "ViatarAxesType0",
    "ViatarCrosssectionsType0",
    "ViatarData",
    "ViatarDataAnglesType0",
    "ViatarDataAxesType0",
    "ViatarDataCrosssectionsType0",
    "ViatarDataDistancesType0",
    "ViatarDataHeightsType0",
    "ViatarDataMarkersType0",
    "ViatarDataMarkersType0AdditionalProperty",
    "ViatarDataObservationsType0",
    "ViatarDataPropertiesType0",
    "ViatarDataSeries",
    "ViatarDataSeriesCrosssectionsType0",
    "ViatarDataTargetsType0",
    "ViatarDistancesType0",
    "ViatarHeightsType0",
    "ViatarMarkersType0",
    "ViatarMarkersType0AdditionalProperty",
    "ViatarObservationsType0",
    "ViatarPropertiesType0",
    "ViatarTargetsType0",
)
