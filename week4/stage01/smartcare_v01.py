"""SmartCare v0.1 - Stage 1 beginner prototype.
Student ID: u3314395

The main human-written function stores appointments in a list of dictionaries.
One controlled improvement is included: a blank patient name is rejected.
"""

appointments = []


def book_appointment(patient_name, practitioner_name, appointment_time):
    """Store one appointment using the Stage 1 data fields."""
    if not patient_name:
        raise ValueError("Patient name cannot be empty")

    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time,
    }
    appointments.append(appointment)
    return appointment


def display_appointments():
    """Print all recorded appointments."""
    if not appointments:
        print("No appointments recorded.")
        return

    for appointment in appointments:
        print(
            f"Patient: {appointment['patient']} | "
            f"Practitioner: {appointment['practitioner']} | "
            f"Time: {appointment['time']}"
        )


def ai_alternative_book_appointment(patient_name, practitioner_name, appointment_time):
    """Simple AI-suggested alternative used only for comparison in the lab."""
    if not patient_name:
        raise ValueError("Patient name cannot be empty")
    if not practitioner_name:
        raise ValueError("Practitioner name cannot be empty")
    if not appointment_time:
        raise ValueError("Appointment time cannot be empty")
    return {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time,
    }


def run_demo():
    appointments.clear()
    print("Welcome to SmartCare: Community Clinic Appointment Booking System!")
    book_appointment("Alice Smith", "Dr. John Doe", "2026-09-04 10:00 AM")
    book_appointment("Bob Johnson", "Dr. Jane Roe", "2026-09-04 11:30 AM")
    display_appointments()


if __name__ == "__main__":
    run_demo()
