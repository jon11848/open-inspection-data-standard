# 9. API Behaviors and Lifecycle Events

The OpenAPI file defines standard behaviors, not a required internal architecture. Implementations may expose additional endpoints and may support only declared capability subsets.

A capability document identifies supported entity operations, package import/export, change feeds, and event delivery.

Standard write behavior SHOULD support idempotency keys. Updates SHOULD use optimistic concurrency through entity versions or HTTP conditional requests. Deletion of evidentiary records SHOULD normally be represented by tombstoning or supersession rather than silent destruction.

Lifecycle events use CloudEvents-compatible envelopes. Event names indicate meaningful state transitions such as creation, review, assignment, status change, resolution, supersession, import, or export. An event consumer must still retrieve the current resource when the event payload is only a reference.
