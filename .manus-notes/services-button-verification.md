# Services Button Verification

## 2026-05-18 Preview check

The Services catalog was regenerated after updating `generate_service_pages.py`.

Observed in preview on `/services/`:

| Check | Result | Notes |
| --- | --- | --- |
| Pill-shaped CTA visible | Passed | The first visible `Open service page` control now renders as a rounded pill rather than a plain text link. |
| Gold border and gradient treatment | Passed | The button shows a soft gold outline with a subtle warm gradient fill that matches the dark editorial palette. |
| Arrow badge visible | Passed | A circular arrow badge appears at the right side of the control. |
| Hover/focus motion | Passed in preview inspection | The hovered state shows a brighter button treatment and the arrow badge appears shifted to the right. |
| Mobile full-width rule | Pending direct narrow-viewport verification | The generator CSS now includes a max-width 767px rule that sets `.ref-service-link` to `width: 100%` with `justify-content: space-between`. |

The current preview screenshot confirms that the refreshed CTA is more visually prominent and better aligned with the site's gold-accented brand language.
