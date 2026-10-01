from enum import Enum
from patient import Patient
from practitioner import Practitioner


class AppointmentStatus(Enum):
    SCHEDULED = "SCHEDULED"
    CANCELLED = "CANCELLED"


class InvalidStatusTransitionError(ValueError):
    pass


class Appointment:
    def __init__(self, appointment_id: str, patient: Patient, practitioner: Practitioner, appointment_time: str):
        self._appointment_id = self._require_text(appointment_id, "Appointment ID")
        if not isinstance(patient, Patient):
            raise TypeError("patient must be a Patient")
        if not isinstance(practitioner, Practitioner):
            raise TypeError("practitioner must be a Practitioner")
        self._patient = patient
        self._practitioner = practitioner
        self._appointment_time = self._require_text(appointment_time, "Appointment time")
        self._status = AppointmentStatus.SCHEDULED

    @staticmethod
    def _require_text(value: str, field_name: str) -> str:
        if value is None or not str(value).strip():
            raise ValueError(f"{field_name} cannot be empty")
        return str(value).strip()

    @property
    def appointment_id(self) -> str:
        return self._appointment_id

    @property
    def patient(self) -> Patient:
        return self._patient

    @property
    def practitioner(self) -> Practitioner:
        return self._practitioner

    @property
    def appointment_time(self) -> str:
        return self._appointment_time

    @property
    def status(self) -> AppointmentStatus:
        return self._status

    def cancel(self) -> None:
        if self._status is not AppointmentStatus.SCHEDULED:
            raise InvalidStatusTransitionError("Only a scheduled appointment can be cancelled")
        self._status = AppointmentStatus.CANCELLED

    def __repr__(self) -> str:
        return (f"Appointment({self.appointment_id!r}, patient={self.patient.patient_id!r}, "
                f"practitioner={self.practitioner.practitioner_id!r}, time={self.appointment_time!r}, "
                f"status={self.status.value!r})")
