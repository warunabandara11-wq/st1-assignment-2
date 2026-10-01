class Practitioner:
    def __init__(self, practitioner_id: str, name: str, specialty: str):
        self._practitioner_id = self._require_text(practitioner_id, "Practitioner ID")
        self._name = self._require_text(name, "Practitioner name")
        self._specialty = self._require_text(specialty, "Specialty")

    @staticmethod
    def _require_text(value: str, field_name: str) -> str:
        if value is None or not str(value).strip():
            raise ValueError(f"{field_name} cannot be empty")
        return str(value).strip()

    @property
    def practitioner_id(self) -> str:
        return self._practitioner_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def specialty(self) -> str:
        return self._specialty

    def __repr__(self) -> str:
        return f"Practitioner({self.practitioner_id!r}, {self.name!r}, {self.specialty!r})"
