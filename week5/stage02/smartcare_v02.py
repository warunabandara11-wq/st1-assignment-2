"""SmartCare v0.2 - Requirements/prototype coding evidence.
Student ID: u3314395

This is still a simple in-memory prototype. It implements only capabilities supported by
SmartCare requirements and avoids database, GUI, payment, diagnosis and notification features.
"""

patients = {}
practitioners = {}
appointments = []


def _require_text(value, field_name):
    if value is None or not str(value).strip():
        raise ValueError(f"{field_name} cannot be empty")
    return str(value).strip()


def register_patient(patient_id, name):
    patient_id = _require_text(patient_id, "Patient ID")
    name = _require_text(name, "Patient name")
    if patient_id in patients:
        raise ValueError("Patient ID already exists")
    patients[patient_id] = {"patient_id": patient_id, "name": name}
    return patients[patient_id]


def register_practitioner(practitioner_id, name, specialty):
    practitioner_id = _require_text(practitioner_id, "Practitioner ID")
    name = _require_text(name, "Practitioner name")
    specialty = _require_text(specialty, "Specialty")
    if practitioner_id in practitioners:
        raise ValueError("Practitioner ID already exists")
    practitioners[practitioner_id] = {
        "practitioner_id": practitioner_id,
        "name": name,
        "specialty": specialty,
    }
    return practitioners[practitioner_id]


def search_patient(patient_id):
    return patients.get(str(patient_id).strip())


def book_appointment(appointment_id, patient_id, practitioner_id, appointment_time):
    appointment_id = _require_text(appointment_id, "Appointment ID")
    appointment_time = _require_text(appointment_time, "Appointment time")

    if patient_id not in patients:
        raise ValueError("Patient does not exist")
    if practitioner_id not in practitioners:
        raise ValueError("Practitioner does not exist")
    if any(a["appointment_id"] == appointment_id for a in appointments):
        raise ValueError("Appointment ID already exists")

    for appointment in appointments:
        same_slot = (
            appointment["practitioner_id"] == practitioner_id
            and appointment["appointment_time"] == appointment_time
            and appointment["status"] == "SCHEDULED"
        )
        if same_slot:
            raise ValueError("Practitioner already has a scheduled appointment at this time")

    appointment = {
        "appointment_id": appointment_id,
        "patient_id": patient_id,
        "practitioner_id": practitioner_id,
        "appointment_time": appointment_time,
        "status": "SCHEDULED",
    }
    appointments.append(appointment)
    return appointment


def cancel_appointment(appointment_id):
    for appointment in appointments:
        if appointment["appointment_id"] == appointment_id:
            if appointment["status"] != "SCHEDULED":
                raise ValueError("Only a scheduled appointment can be cancelled")
            appointment["status"] = "CANCELLED"
            return appointment
    raise ValueError("Appointment not found")


def practitioner_schedule(practitioner_id):
    if practitioner_id not in practitioners:
        raise ValueError("Practitioner does not exist")
    return [a.copy() for a in appointments if a["practitioner_id"] == practitioner_id]


def appointment_summary():
    scheduled = sum(1 for a in appointments if a["status"] == "SCHEDULED")
    cancelled = sum(1 for a in appointments if a["status"] == "CANCELLED")
    return {"total": len(appointments), "scheduled": scheduled, "cancelled": cancelled}


def reset_data():
    patients.clear()
    practitioners.clear()
    appointments.clear()
