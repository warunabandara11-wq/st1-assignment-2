from smartcare_v02 import (
    reset_data, register_patient, register_practitioner, search_patient,
    book_appointment, cancel_appointment, practitioner_schedule, appointment_summary
)

reset_data()
print("Register patient/practitioner")
patient = register_patient("P001", "Alice Smith")
practitioner = register_practitioner("PR001", "Dr John Doe", "GP")
print(patient)
print(practitioner)
assert patient["patient_id"] == "P001"
assert practitioner["practitioner_id"] == "PR001"

print("\nSearch patient")
found = search_patient("P001")
print(found)
assert found == patient

print("\nBook valid appointment")
appointment = book_appointment("A001", "P001", "PR001", "2026-09-11 10:00")
print(appointment)
assert appointment["status"] == "SCHEDULED"

print("\nReject duplicate practitioner/time")
register_patient("P002", "Bob Johnson")
duplicate_rejected = False
try:
    book_appointment("A002", "P002", "PR001", "2026-09-11 10:00")
except ValueError as exc:
    duplicate_rejected = True
    print(type(exc).__name__ + ":", exc)
assert duplicate_rejected

print("\nCancel and retain appointment")
cancelled = cancel_appointment("A001")
print(cancelled)
schedule = practitioner_schedule("PR001")
print(schedule)
assert cancelled["status"] == "CANCELLED"
assert schedule[0]["appointment_id"] == "A001"
assert schedule[0]["status"] == "CANCELLED"

print("\nReject repeated cancellation")
repeat_rejected = False
try:
    cancel_appointment("A001")
except ValueError as exc:
    repeat_rejected = True
    print(type(exc).__name__ + ":", exc)
assert repeat_rejected

print("\nOperational summary")
summary = appointment_summary()
print(summary)
assert summary == {"total": 1, "scheduled": 0, "cancelled": 1}

print("\nAll Stage 2 prototype checks completed.")
