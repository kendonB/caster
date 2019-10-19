from castervoice.lib import settings
from castervoice.lib.ccr.recording.alias.base_alias import BaseAliasRule
from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.const import CCRType

class Alias(BaseAliasRule):
    pronunciation = "alias"

    def __init__(self, **kwargs):
        super(Alias, self).__init__(settings.settings(["paths", "SM_ALIAS_PATH"]), **kwargs)

    def get_pronunciation(self):
        return Alias.pronunciation


def get_rule():
    details = RuleDetails(name = "alias", 
                          transformer_exclusion=True)
    return [Alias, details]
