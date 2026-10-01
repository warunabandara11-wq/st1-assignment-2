# Stage 2 Reflection

The AI review helped me notice that some requirements sounded reasonable but were still too vague to test. For example, “the system should be fast” does not say what operation is being measured, what dataset is used or what response time is acceptable. It also highlighted that “practitioner availability” needs a clearer definition because the client brief describes the problem but does not specify working hours, leave or appointment-slot rules.

The AI also suggested features such as reminders and stronger security controls. I did not automatically add these because they were not stated by the client. The most useful change was tightening the duplicate-booking requirement so that the prototype rejects two active appointments for the same practitioner at the same time. I also made cancellation preserve the appointment record because SmartCare has a problem with unreliable history.

Requirements need evidence because otherwise the development team can accidentally build assumptions instead of the system the client actually asked for. Evidence also makes later design, coding and testing decisions traceable and easier to justify.
