class Practitioner:
    """Stage 3 skeleton: practitioner identity, name and specialty."""
    def __init__(self, practitioner_id: str, name: str, specialty: str):
        self.practitioner_id = practitioner_id
        self.name = name
        self.specialty = specialty

    def __repr__(self) -> str:
        return f"Practitioner({self.practitioner_id!r}, {self.name!r}, {self.specialty!r})"
