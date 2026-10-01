from smartcare_v01 import appointments, book_appointment

appointments.clear()
print("TEST 1 normal appointment")
print(book_appointment("Test Patient", "Dr Test", "2026-09-04 09:00"))

print("\nTEST 2 blank patient")
try:
    book_appointment("", "Dr Test", "2026-09-04 09:30")
except ValueError as exc:
    print(type(exc).__name__ + ":", exc)

print("\nTEST 3 duplicate practitioner/time (known Stage 1 limitation)")
print(book_appointment("Patient A", "Dr Test", "2026-09-04 10:00"))
print(book_appointment("Patient B", "Dr Test", "2026-09-04 10:00"))
print("duplicate accepted in v0.1 -> limitation confirmed")

print("\nTEST 4 None appointment time (known Stage 1 limitation)")
print(book_appointment("Patient C", "Dr Other", None))
print("None time accepted in v0.1 -> limitation confirmed")
