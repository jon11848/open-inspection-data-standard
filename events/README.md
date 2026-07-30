# Lifecycle Events

Events use a CloudEvents 1.0-compatible envelope. The working-draft event catalog includes:

- `org.openinspection.asset.created.v1`
- `org.openinspection.asset.updated.v1`
- `org.openinspection.inspection.started.v1`
- `org.openinspection.inspection.completed.v1`
- `org.openinspection.observation.created.v1`
- `org.openinspection.observation.updated.v1`
- `org.openinspection.observation.superseded.v1`
- `org.openinspection.finding.created.v1`
- `org.openinspection.finding.reviewed.v1`
- `org.openinspection.finding.rejected.v1`
- `org.openinspection.finding.superseded.v1`
- `org.openinspection.issue.created.v1`
- `org.openinspection.issue.assigned.v1`
- `org.openinspection.issue.status-changed.v1`
- `org.openinspection.issue.resolved.v1`
- `org.openinspection.issue.reopened.v1`
- `org.openinspection.evidence.added.v1`
- `org.openinspection.package.imported.v1`
- `org.openinspection.package.exported.v1`

Event delivery is at least once unless an implementation declares stronger behavior. Consumers must deduplicate on event `id` and should retrieve the current entity when ordering matters.
