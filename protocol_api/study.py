from uuid import UUID


class Study:

    def __init__(self, study_definition: dict):
        self._study_definition = study_definition
        self._reference = None
        self._init()

    @property
    def reference(self)-> UUID:
        return self._reference

    def _init(self):
        self._reference = UUID(self._study_definition['reference_identifier'])

        # remaining implementation elided here for brevity.
        # It generates the study data model from the definition JSON document, which is
        # both computationally and memory extensive
        pass
