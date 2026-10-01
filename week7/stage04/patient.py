class Patient:
    def __init__(self, patient_id: str, name: str):
        self._patient_id = self._require_text(patient_id, "Patient ID")
        self._name = self._require_text(name, "Patient name")

    @staticmethod
    def _require_text(value: str, field_name: str) -> str:
        if value is None or not str(value).strip():
            raise ValueError(f"{field_name} cannot be empty")
        return str(value).strip()

    @property
    def patient_id(self) -> str:
        return self._patient_id

    @property
    def name(self) -> str:
        return self._name

    def __repr__(self) -> str:
        return f"Patient({self.patient_id!r}, {self.name!r})"
