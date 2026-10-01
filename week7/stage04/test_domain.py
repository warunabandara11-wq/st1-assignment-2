from patient import Patient
from practitioner import Practitioner
from appointment import Appointment, AppointmentStatus, InvalidStatusTransitionError

print("TEST 1 create valid objects")
patient = Patient("P001", "Alice Smith")
practitioner = Practitioner("PR001", "Dr John Doe", "GP")
appointment = Appointment("A001", patient, practitioner, "2026-09-25 10:00")
print(patient)
print(practitioner)
print(appointment)
assert appointment.status is AppointmentStatus.SCHEDULED

print("\nTEST 2 reject invalid patient name")
try:
    Patient("P002", "")
except ValueError as exc:
    print(type(exc).__name__ + ":", exc)

print("\nTEST 3 reject invalid practitioner specialty")
try:
    Practitioner("PR002", "Dr Jane Roe", "")
except ValueError as exc:
    print(type(exc).__name__ + ":", exc)

print("\nTEST 4 reject wrong object type in Appointment")
try:
    Appointment("A002", "not a Patient", practitioner, "2026-09-25 11:00")
except TypeError as exc:
    print(type(exc).__name__ + ":", exc)

print("\nTEST 5 cancel scheduled appointment")
appointment.cancel()
print(appointment)
assert appointment.status is AppointmentStatus.CANCELLED

print("\nTEST 6 reject illegal repeated cancellation")
try:
    appointment.cancel()
except InvalidStatusTransitionError as exc:
    print(type(exc).__name__ + ":", exc)

print("\nAll Stage 4 manual behaviour checks completed.")
