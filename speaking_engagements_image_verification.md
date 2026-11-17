# Speaking Engagements Image Verification

The Speaking Engagements service page in preview now uses the uploaded pillar-specific images in the intended order: Educate uses the whiteboard image, Empower uses the audience image, Elevate uses the collaboration-at-laptop image, and Engage uses the handshake image.

The card media loads from managed storage paths and defaults to a grayscale presentation. The page stylesheet also includes a hover and focus rule that transitions each `.ref-card-media` element from `grayscale(1)` to `grayscale(0)`, confirming the requested black-and-white to color interaction is present.
