class ManagedRule(object):

    def __init__(self, rule_class, details):
        self._rule_class = rule_class
        self._details = details

    def get_rule_class_name(self):
        return self._rule_class.__name__

    def get_rule_instance(self):
        return self._rule_class(name=self._details.name)

    def get_details(self):
        return self._details