from enum import Enum
from patient import Patient
from practitioner import Practitioner


class AppointmentStatus(Enum):
    SCHEDULED = "SCHEDULED"
    CANCELLED = "CANCELLED"


class Appointment:
    """Stage 3 skeleton only. Full cancellation behaviour is deferred to Stage 4."""
    def __init__(self, appointment_id: str, patient: Patient, practitioner: Practitioner, appointment_time: str):
        self.appointment_id = appointment_id
        self.patient = patient
        self.practitioner = practitioner
        self.appointment_time = appointment_time
        self.status = AppointmentStatus.SCHEDULED

    def __repr__(self) -> str:
        return (f"Appointment({self.appointment_id!r}, patient={self.patient.patient_id!r}, "
                f"practitioner={self.practitioner.practitioner_id!r}, time={self.appointment_time!r}, "
                f"status={self.status.value!r})")
