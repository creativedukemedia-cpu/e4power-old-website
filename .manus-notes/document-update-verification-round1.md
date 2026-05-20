# Document-Driven Website Update Verification

## Round 1 preview findings

| Page | Observation |
| --- | --- |
| Homepage (`/`) | The revised highlight section now exposes four metrics in the extracted content: `>95% Submittal Rate`, `>500M Applied/Secured in Grants/Contracts`, `>80% Efficiency Implementation in Business Acumen`, and `4 AI & Efficiency Pathways`. The updated proposals paragraph also appears in the preview text with the contradictory `$60,000,000` claim removed. |
| Services catalog (`/services/`) | The updated headings now appear for the requested service names, including `Grant Writing (Pre-Award)`, `Intellectual Property Services`, `IT/AI Services`, and `Grant Management (Post-Award)`. The first visible catalog section shows the shortened image treatment, indicating the service-card media height reduction is active. |

## Follow-up check still needed

The homepage screenshot suggests the fourth metric may be wrapping below the first row at some viewport widths, so one more targeted layout check is needed before checkpointing.

## Round 2 targeted layout check

A direct layout measurement on the homepage confirmed that the revised highlight band currently renders **four** metric blocks, but the fourth block (`4 AI & Efficiency Pathways`) wraps onto a second row at the current desktop preview width. The first three boxes share the same top position, while the fourth starts roughly one row lower, so the metric band needs a layout adjustment before checkpointing.

## Round 3 final verification

After the homepage metric-band layout override, the four highlight boxes now sit on a single row in the desktop preview. A live DOM measurement showed all four blocks sharing the same top position with equal widths, confirming that the revised metrics are aligned without wrapping at the current preview size.

The implemented document-driven changes now verified in preview are the homepage metric updates, the revised proposals-funded paragraph, the renamed service labels (`Grant Writing (Pre-Award)`, `Intellectual Property Services`, `IT/AI Services`, and `Grant Management (Post-Award)`), and the smaller service-card images on the Services catalog.
