# Stage 4 AI Engineering Log

**AI tool:** ChatGPT (OpenAI)  
**Purpose:** Pair-programming review of the `Appointment` class under the approved Stage 3 design constraints.

## Pair-programming constraint
Implement only the `Appointment` class from the approved model, with type hints, an `AppointmentStatus` enum and a protected cancellation transition. Keep cancelled appointments as objects. Do not add a database, UI, notification or service layer.

## Contributions reviewed
| AI contribution | Decision | Reason | Verification |
|---|---|---|---|
| `AppointmentStatus` enum with SCHEDULED/CANCELLED | Accept | Matches the approved model and cancellation/history requirement. | Enum assertions in `test_domain.py`. |
| Private `_status` with read-only property | Accept | Protects the domain invariant from public mutation. | Status is changed only by `cancel()`. |
| Guard SCHEDULED -> CANCELLED | Accept | Prevents an illegal repeated transition. | Repeated cancellation raises `InvalidStatusTransitionError`. |
| Add SQL/persistence to `cancel()` | Reject | Domain object should not execute persistence logic; the lab excludes database logic. | No SQL/database dependency exists. |
| Add notification/service dependency | Reject | Unsupported by the client brief and outside the Stage 4 domain layer. | No notification/service import exists. |

The final code was run after review and the console results are saved in `test_output.txt`.
