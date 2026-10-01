# Stage 3 AI Design Review

**AI tool:** ChatGPT (OpenAI)  
**Purpose:** Critique candidate classes and relationships using only the current SmartCare requirements.

The design review was asked to support each proposal with requirement evidence. The final model kept `Patient`, `Practitioner` and `Appointment` as the three core domain classes. `AppointmentStatus` is represented as an enum/value rather than a separate entity. Manager/controller/notification classes were not added because they either represent later architectural responsibilities or have no client evidence at this stage.

- **Accepted:** core Patient-Practitioner-Appointment relationships.
- **Modified:** Status represented as `AppointmentStatus` enum rather than a full entity class.
- **Rejected:** `NotificationManager` (unsupported) and `ClinicController`/multiple manager classes (premature architecture).
- **Deferred:** a separate schedule engine; the current duplicate-booking rule does not yet justify an additional domain class.
