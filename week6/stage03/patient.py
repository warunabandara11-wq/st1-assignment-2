class Patient:
    """Stage 3 skeleton: patient identity and name only."""
    def __init__(self, patient_id: str, name: str):
        self.patient_id = patient_id
        self.name = name

    def __repr__(self) -> str:
        return f"Patient({self.patient_id!r}, {self.name!r})"
