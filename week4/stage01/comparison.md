# Stage 1 - Human vs AI Comparison

| Question | Human version | AI alternative |
|---|---|---|
| Easy to understand? | Yes. It uses one list, dictionaries and two short functions. | Yes. The alternative is also short, but it adds more validation. |
| Runs successfully? | Yes for normal appointments. | Yes for normal appointments. |
| Uses only required features? | Yes. It stores patient, practitioner and time only. | Yes. It does not add a database, GUI or unrelated features. |
| Adds assumptions? | Very few. Duplicate bookings and time format are deliberately unresolved. | It assumes all three values must be non-empty. That is reasonable but still needs client confirmation for exact validation rules. |
| Handles errors? | Only a blank/None patient name is rejected as the one controlled improvement. | Blank patient, practitioner and appointment time are rejected. |
| Could I explain it? | Yes. | Yes, after checking each condition and return value. |

## Five limitations identified
1. Duplicate appointments for the same practitioner and time are still possible.
2. Practitioner names are not validated in the final human version.
3. Appointment time is stored as free text and its format is not checked.
4. There are no patient/practitioner identifiers, appointment status or cancellation operations yet.
5. Data exists only while the program is running; there is no persistence, search, availability view or reporting yet.
