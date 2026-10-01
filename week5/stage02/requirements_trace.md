# Stage 2 Requirement-to-Prototype Trace

| Requirement | Prototype evidence |
|---|---|
| FR-01 maintain patient records | `register_patient()` |
| FR-02 locate patient records | `search_patient()` |
| FR-03 maintain practitioner records | `register_practitioner()` |
| FR-04 visibility of practitioner schedule | `practitioner_schedule()` |
| FR-05 create appointment | `book_appointment()` |
| FR-06 prevent duplicate practitioner/time bookings | duplicate check in `book_appointment()` |
| FR-07 consistent appointment status | `SCHEDULED` / `CANCELLED` values |
| FR-08 cancel while retaining history | `cancel_appointment()` changes status rather than deleting |
| FR-09 reject illegal repeated cancellation | transition check in `cancel_appointment()` |
| FR-10 basic operational reporting | `appointment_summary()` |

This is an in-memory prototype only. Persistence, GUI, payments, diagnosis and notifications are intentionally not added.
