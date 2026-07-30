# 6. Observations, Findings, and Issues

## 6.1 Observation

An Observation records what was captured, measured, detected, witnessed, or reported. It SHOULD minimize interpretation. Examples include visible cracking, a measured clearance, a sensor reading, or a missing component.

## 6.2 Finding

A Finding records interpretation or classification. It MAY be authored by a human, AI system, software rule, or mixed process. An AI-authored finding is not forced into a proposal state; its authorship, method, confidence, review state, and certification are independently represented.

Severity is not a single universal concept. Findings MAY contain multiple `severityDimensions`, such as physical condition, safety consequence, urgency, extent, probability of failure, regulatory classification, or repair priority. Profiles may recommend specific dimensions.

## 6.3 Issue

An Issue tracks an action, assignment, decision, monitoring obligation, repair, verification, or other workflow outcome. Closing an Issue does not delete or invalidate its underlying Observation or Finding.

## 6.4 Combined vendor objects

A vendor system MAY internally use one task or stamp for all three concepts. On export, the vendor SHOULD create distinct OIDS records where the source contains separable observation, interpretation, and workflow information. On round trip, those records MAY be rendered through one user-interface object if identifiers and relationships are preserved.
