import time


class ModelCache:

    def __init__(self, model_class, lookup_field):
        self.lookup_field = lookup_field
        self.model_class = model_class
        self.cache = {}

    def get(self, lookup_value):
        instance = self.cache.get(lookup_value)
        if instance is None:
            self.cache[lookup_value] = self.model_class.objects \
                .filter(**{self.lookup_field: lookup_value}) \
                .first()
        instance = self.cache.get(lookup_value)
        return instance


