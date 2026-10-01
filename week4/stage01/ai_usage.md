# Stage 1 AI Use - Ask, Check, Explain

**AI tool:** ChatGPT (OpenAI)  
**Purpose:** Tutor-style explanation and critique of the Stage 1 prototype.

## Before AI
I expected the code to store patient, practitioner and appointment time in a list and print the records. I could already see that duplicate bookings, missing practitioner/time values, status, cancellation, search and persistence were not handled.

## Prompt / request
Act as a Python tutor. Explain the small appointment-booking function, identify limitations, suggest improvements, do not add a database or GUI, and ask questions that help me reason about the solution.

## Significant suggestions and decisions
| Suggestion | Decision | Reason / verification |
|---|---|---|
| Reject blank patient name | Accept | Easy to verify; prevents an obviously unusable appointment record. |
| Reject blank practitioner name | Keep unverified for Stage 1 final | Reasonable, but Part G asks for exactly one controlled improvement. |
| Parse/validate date-time format | Modify / defer | Useful, but the required format has not been confirmed. |
| Prevent duplicate practitioner/time bookings | Accept as a later requirement | The case study explicitly identifies duplicate bookings as a problem; implementation belongs in the next iteration. |
| Add a database/GUI/notifications | Reject | Outside the Stage 1 task and the client wants a manageable first version. |

## Verification
The final program was run with a normal appointment, a blank patient name, a duplicate practitioner/time and `None` appointment time. The results are saved in `test_output.txt`.

## Explain
I can explain the final list, dictionary, functions and validation without relying on the AI response. I still need to learn stronger date/time validation and persistence, which are intentionally outside this stage.
