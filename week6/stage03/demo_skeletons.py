from patient import Patient
from practitioner import Practitioner
from appointment import Appointment

patient = Patient("P001", "Alice Smith")
practitioner = Practitioner("PR001", "Dr John Doe", "GP")
appointment = Appointment("A001", patient, practitioner, "2026-09-18 10:00")

print(patient)
print(practitioner)
print(appointment)
print("Consistency check: Appointment references one Patient and one Practitioner.")
print("Full cancellation/validation behaviour is intentionally deferred to Stage 4.")
