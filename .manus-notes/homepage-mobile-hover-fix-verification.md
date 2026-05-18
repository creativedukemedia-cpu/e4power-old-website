# Homepage Mobile Interaction Verification

## 2026-05-18 verification summary

The homepage hero pillar interaction was updated so mobile users receive a touch-friendly equivalent of the desktop hover preview without changing the existing desktop hover behavior.

| Scenario | Result | Notes |
| --- | --- | --- |
| Desktop hover on Educate pillar | Passed | Hover still opens the preview panel, sets `aria-hidden="false"`, and marks the hovered pillar with `aria-expanded="true"`. |
| Mobile first tap on Educate pillar | Passed | The first tap now opens the service preview sheet, shows the Educate service-group title, and activates the pillar state instead of cancelling itself. |
| Mobile close flow | Passed | The mobile preview closes correctly through the in-panel dismiss control, clearing the active state and restoring `aria-hidden="true"`. |
| Root-cause diagnosis | Passed | The original failure came from duplicate touch events on mobile. The preview opened on the first touch event, then a follow-up mobile event effectively cancelled the state. The fix now deduplicates touch handling while still cancelling duplicate touch events so the mobile preview remains open. |

The final automated verification run confirmed that desktop hover remains intact and the mobile tap interaction now behaves as intended.
