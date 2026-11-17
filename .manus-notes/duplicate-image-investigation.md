# Duplicate image investigation

On the preview Services page, the user reported that the **Readiness Assessments — Engage** card and the **Intellectual Property — Empower** card display the same photo.

The generator currently maps those cards to different managed-storage paths:

- `/manus-storage/readiness-assessments-engage_a98215f4.jpg`
- `/manus-storage/intellectual-property-empower_7ace54f6.jpg`

A first DOM extraction attempt from the browser did not recover the image sources, so the next step is to inspect the generated HTML and/or compare the rendered cards directly.
