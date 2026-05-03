# Duplicate image repair verification

The affected image pair was confirmed before the fix by downloading both rendered assets from preview and comparing hashes. The files below were byte-for-byte identical:

- `/manus-storage/readiness-assessments-engage_a98215f4.jpg`
- `/manus-storage/intellectual-property-empower_7ace54f6.jpg`

The generator has now been updated so **Intellectual Property — Empower** uses a new asset instead:

- `/manus-storage/intellectual-property-empower-replacement_64bb49e5.jpg`

The static pages were regenerated and the site rebuilt successfully. A direct DOM extraction from the browser did not return the expected background-image values, so the verification basis is the regenerated HTML source and the successful build after the mapping change.
