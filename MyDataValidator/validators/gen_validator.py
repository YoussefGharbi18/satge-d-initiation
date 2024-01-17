from typing import Any, Dict

class genValidator:
    def __init__(self):
        self.validation_strategies = {}

    def add_validation_strategy(self, key: str, validation_strategy):
        self.validation_strategies[key] = validation_strategy

    def validate(self, data: Dict[str, Any], schema: Dict[str, Any]) -> bool:
        for key, conditions in schema.items():
            if key in self.validation_strategies:
                validation_strategy = self.validation_strategies[key]
                if not validation_strategy(data.get(key), conditions):
                    return False
        return True