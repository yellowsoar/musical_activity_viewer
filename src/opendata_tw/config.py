from opendata_tw import models

field_model_mapping = {
    'unit_perform': models.PerformUnit,
    'unit_host': models.HostUnit,
    'unit_assist': models.AssistUnit,
    'unit_sponsor': models.SponsorUnit,
    'unit_other': models.OtherUnit,
}

field_through_model_mapping = {
    'unit_perform': models.ActivityPerformUnitMapping,
    'unit_host': models.ActivityHostUnitMapping,
    'unit_assist': models.ActivityAssistUnitMapping,
    'unit_sponsor': models.ActivitySponsorUnitMapping,
    'unit_other': models.ActivityOtherUnitMapping,
}
