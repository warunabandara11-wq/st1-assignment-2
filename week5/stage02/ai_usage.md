# Stage 2 AI Requirements Review Evidence

**AI tool:** ChatGPT (OpenAI)  
**Purpose:** Requirements critique for ambiguity, inconsistency, unsupported assumptions and testability.

The review was constrained to the SmartCare case-study evidence. Suggestions were not treated as requirements unless they could be supported by the supplied client problem or were kept explicitly as questions/assumptions.

## Main decisions
- Define duplicate booking for the prototype as the same practitioner and appointment time so the requirement can be tested.
- Preserve cancelled appointments so the system can maintain reliable history.
- Keep SMS reminders, payments, facial recognition and AI diagnosis out of scope because they have no client evidence.
- Leave exact report formats, security roles, date/time format and measurable performance thresholds as open questions.

The resulting decisions are recorded in the completed SmartCare v0.2 Requirements Specification and verified by the Stage 2 prototype tests.
