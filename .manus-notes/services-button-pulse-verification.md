# Services Button Pulse Verification

## 2026-05-18 Preview check

The Services catalog was regenerated after updating `generate_service_pages.py` to add a recurring sweep animation to `.ref-service-link`.

| Check | Result | Notes |
| --- | --- | --- |
| Sweep animation present | Passed | The button pseudo-element reports `animation-name: ref-service-link-sweep`. |
| Animation cadence | Passed | The pseudo-element reports `animation-duration: 3s` and `animation-iteration-count: infinite`. |
| Motion evidence in live preview | Passed | Timed samples taken from the first visible Services button show the pseudo-element transform changing over time, confirming the sweep is actively moving through the button. |
| Visual treatment preserved | Passed | The gold pill button, circular arrow badge, and hover lift remain intact after the animation update. |
| Reduced-motion fallback | Passed | The generator now disables the sweep animation inside `prefers-reduced-motion: reduce`. |

The effect is currently configured as a subtle gold-cream sheen that travels through the button roughly once every three seconds.
