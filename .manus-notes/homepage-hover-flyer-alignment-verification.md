# Homepage hover flyer-alignment verification

Initial verification after updating the hero hover data:

- The homepage loaded successfully after the hover-data update.
- The static hero services list still shows the flyer-aligned 8 services.
- A first browser-side DOM inspection used a broad `.service-preview-shell` selector and captured the persistent Educate preview block lower on the page instead of the hero hover overlay.
- That means the hero hover popup still needs a more targeted verification pass before checkpointing.

A targeted verification pass against the dedicated hero hover shell confirmed the updated popup content is now flyer-aligned.

For the Educate hover state, the popup now lists Grant Writing (Pre-Award), Readiness Assessments, Speaking Engagements, and IT Solutions.

For the Engage hover state, the popup now lists Speaking Engagements, Readiness Assessments, Project Management, and Intellectual Property Services.

These checks confirm that the outdated hover-only labels were removed from the homepage hero popup and replaced with names drawn from the current 8-service flyer set.
