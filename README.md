# Pitt NSBE chapter website

Static site for the Pitt chapter of the National Society of Black Engineers.
No build step, no framework &mdash; plain HTML/CSS/JS, ready for GitHub Pages.

## Site structure

**Main navigation:**
- `index.html` &mdash; Home: photo hero, mission, member of the month, announcements,
  upcoming/past events, current newsletter + subscribe, contact us (chapter, regional, national)
- `about.html` &mdash; About us: national + Pitt chapter history, current e-board, awards won
- `membership.html` &mdash; Membership: steps to join, alumni network, announcements, conferences
- `programs.html` (+ dropdown) &mdash; Programs: overview, plus dedicated pages for:
  - `programs-aex.html` &mdash; AEX chair
  - `programs-mentor-mentee.html` &mdash; Mentor-mentee
  - `programs-freshman-reps.html` &mdash; Freshman reps

**Hidden pages** (linked from the footer only, not the main nav &mdash; marked `noindex` so search
engines don't surface them ahead of your main pages, but they're fully public if someone has the link):
- `donation.html`
- `sponsorship.html`
- `newsletter.html` (full archive &mdash; separate from the "current issue" preview on Home)
- `merch.html`

**Shared files:**
- `css/style.css` &mdash; all styling, one file, CSS variables for colors
- `js/main.js` &mdash; mobile menu, dropdown, and event tab behavior
- `assets/` &mdash; logo files + where your chapter photo goes (see below)
- `build_site.py` &mdash; regenerates every page from shared templates; edit this instead of
  hand-editing 11 files whenever you change the nav, footer, or add a page

## Adding your Home page photo

You mentioned you'd provide a photo for the Home hero. Once you have it:

1. Save it as `assets/hero-photo.jpg` (any image works, but a wide/landscape photo looks best).
2. Open `build_site.py`, find the `hero()` function, and replace this line:
   ```python
   fig = ('<div class="hero-figure"><div class="photo-block" style="aspect-ratio:4/3;">'
          'Chapter photo &mdash; replace assets/hero-photo.jpg</div></div>')
   ```
   with:
   ```python
   fig = '<div class="hero-figure"><img src="assets/hero-photo.jpg" alt="Pitt NSBE chapter photo" style="border-radius:6px;"></div>'
   ```
3. Run `python3 build_site.py` to regenerate `index.html` with the real photo.

(Or, if you don't want to touch the script: just open `index.html`, search for the same
placeholder `<div class="photo-block"...>` near the top, and swap it for an `<img>` tag by hand
&mdash; it'll get overwritten next time you run the build script, though, so the script edit is more durable.)

## Publishing to GitHub Pages

1. Create a new GitHub repository (e.g. `pitt-nsbe-website`).
2. Upload every file in this folder, keeping the same folder structure.
3. In the repo: **Settings &rarr; Pages &rarr; Build and deployment**.
4. Set **Source** to "Deploy from a branch," branch `main`, folder `/ (root)`. Save.
5. GitHub gives you a live URL (`https://yourusername.github.io/pitt-nsbe-website/`) within a couple minutes.

## Before you launch: placeholder checklist

- [ ] Home page photo (see above)
- [ ] Mission statement (Home + About)
- [ ] Chapter founding year, member count, event count, sponsor count (Home stats)
- [ ] Member of the month (Home)
- [ ] Announcements (Home + Membership)
- [ ] Upcoming + past events (Home)
- [ ] Current newsletter issue + subscribe form connection (Home + newsletter.html)
- [ ] Meeting day/time/location (Home contact, Membership steps)
- [ ] Regional contact name (Home contact &mdash; check nsbe.org/regions for the current Region II chair)
- [ ] Chapter + national history details (About)
- [ ] E-board names/photos (About)
- [ ] Awards won (About)
- [ ] Alumni network details (Membership)
- [ ] Conference dates + travel process (Membership)
- [ ] Program chair names + current initiatives (programs-*.html)
- [ ] Donation platform link (donation.html)
- [ ] Sponsor tiers + logos (sponsorship.html)
- [ ] Merch items + ordering link (merch.html)
- [ ] Instagram / LinkedIn links (footer, every page)
- [ ] Contact form + newsletter form: both currently placeholders. The contact form opens the
      user's email client (`mailto:`); for real form submissions without opening email, connect
      to a free service like Formspree or Google Forms and update the `<form action="...">`.

## Notes on branding compliance

This site uses an original chapter logo (not the official NSBE Torch mark, not any
University of Pittsburgh logo) and spells out "National Society of Black Engineers"
in the nav and footer on every page per NSBE's chapter naming policy. If you swap in
different imagery later, keep in mind:
- Don't add the official NSBE Torch artwork without going through NSBE's Logo Usage
  Approval Form (National Public Relations Chairperson).
- Don't add Pitt's Script Pitt mark, shield, or institutional logo without going through
  Pitt's Office of University Communications and Marketing / Trademark Licensing.
