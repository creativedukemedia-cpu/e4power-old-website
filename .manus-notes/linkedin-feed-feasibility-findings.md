# LinkedIn feed feasibility findings

## Official LinkedIn options observed so far

1. The official LinkedIn Plugins catalog currently shows website plugins for:
   - Add to Profile
   - Follow Company
   - Share

   No official native website plugin for an automatically updating company post feed was listed in the current plugin catalog snapshot.

2. The official LinkedIn Posts API documentation states that the Posts API supports creation and retrieval of organic and sponsored posts.

3. The Posts API documentation indicates that retrieving organization posts is possible, but it is permission-based and part of LinkedIn's controlled developer/API ecosystem rather than a simple public website embed.

## Interim implication for E4

A live branded feed is likely possible, but not as a simple built-in LinkedIn widget for company posts. The practical paths appear to be:
- a restricted API-backed custom feed, or
- a third-party feed/aggregation service embedded into the site.

4. LinkedIn Help confirms that LinkedIn officially supports embedding individual public posts outside LinkedIn via an `Embed this post` option on desktop. It also notes limitations: only public posts can be embedded, multi-photo posts and reposts with commentary are not supported, and the embedded content remains visibly LinkedIn-branded.

5. LinkedIn's official Page Management product page states that access is application-based and reviewed, and explicitly says supported solutions may not be used to "display social feeds."

## Updated implication for E4

- **Official simple option:** embed individual public posts manually. This is supported, but it is not an automatically updating feed.
- **Official custom API option:** potentially possible only through gated developer access and likely poor fit for a straightforward website feed because LinkedIn flags social-feed display as a disallowed or unsupported use case in the Page Management qualification text.
- **Most realistic auto-updating option:** use a third-party LinkedIn feed widget/service that handles collection and rendering, then style the container to fit E4 branding.
