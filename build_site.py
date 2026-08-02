#!/usr/bin/env python3
import os

OUT = os.path.dirname(os.path.abspath(__file__))

MAIN_NAV = [
    ("index.html", "Home"),
    ("about.html", "About us"),
    ("membership.html", "Membership"),
]

PROGRAMS_DROPDOWN = [
    ("programs.html", "About"),
    ("programs-aex.html", "AEX chair"),
    ("programs-mentor-mentee.html", "Mentor-Mentee"),
    ("programs-freshman-reps.html", "Freshman Representative"),
]

HIDDEN_PAGES = [
    ("donation.html", "Donate"),
    ("sponsorship.html", "Sponsorship"),
    ("newsletter.html", "Newsletter archive"),
    ("merch.html", "Merch"),
]


def nav_html(active):
    def li(href, label):
        cls = ' class="active"' if href == active else ''
        return f'<li{cls}><a href="{href}">{label}</a></li>'

    items = "".join(li(h, l) for h, l in MAIN_NAV)
    prog_active = active.startswith("programs")
    dropdown_links = "".join(f'<a href="{h}">{l}</a>' for h, l in PROGRAMS_DROPDOWN)
    prog_li = (
        f'<li class="has-dropdown{" active" if prog_active else ""}">'
        f'<button type="button">Programs &#9662;</button>'
        f'<div class="dropdown">{dropdown_links}</div></li>'
    )

    return f"""<nav class="site-nav">
  <div class="nav-inner">
    <a class="brand" href="index.html">
      <img src="assets/logo-nav.png" alt="Pitt NSBE logo">
      <span class="brand-text">Pitt NSBE<small>National Society of Black Engineers</small></span>
    </a>
    <button class="nav-toggle" type="button" aria-label="Toggle menu">Menu</button>
    <ul class="nav-links">
      {items}
      {prog_li}
    </ul>
  </div>
</nav>"""


def footer_html():
    hidden_links = "".join(f'<li><a href="{h}">{l}</a></li>' for h, l in HIDDEN_PAGES)
    return f"""<footer>
  <div class="wrap">
    <div>
      <h4>National Society of Black Engineers &ndash; Pitt Chapter</h4>
      <p style="font-size:0.9rem;max-width:280px;">Empowering Black engineers at the University of Pittsburgh through community, professional development, and academic excellence.</p>
    </div>
    <div>
      <h4>Explore</h4>
      <ul>
        <li><a href="index.html">Home</a></li>
        <li><a href="about.html">About us</a></li>
        <li><a href="membership.html">Membership</a></li>
        <li><a href="programs.html">Programs</a></li>
      </ul>
    </div>
    <div>
      <h4>Support the chapter</h4>
      <ul>
        {hidden_links}
      </ul>
    </div>
    <div>
      <h4>Follow along</h4>
      <ul>
        <li><a href="#">Instagram</a></li>
        <li><a href="#">LinkedIn</a></li>
        <li><a href="mailto:pittnsbe@pitt.edu">pittnsbe@pitt.edu</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">
    <span>&copy; <span id="year"></span> Pitt Chapter, National Society of Black Engineers</span>
    <span>University of Pittsburgh &middot; placeholder content, update before launch</span>
  </div>
</footer>
<script>document.getElementById('year').textContent = new Date().getFullYear();</script>
<script src="js/main.js"></script>"""


def page(title, active, body, description, noindex=False):
    robots = '<meta name="robots" content="noindex">\n' if noindex else ''
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} &middot; Pitt NSBE</title>
<meta name="description" content="{description}">
{robots}<link rel="icon" href="assets/logo-nav.png">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
{nav_html(active)}
{body}
{footer_html()}
</body>
</html>"""


def hero(eyebrow, h1, lead, actions="", photo=False):
    if photo:
        fig = ('<div class="hero-figure"><div class="photo-block" style="aspect-ratio:4/3;">'
               'Chapter photo &mdash; replace assets/hero-photo.jpg</div></div>')
    else:
        fig = '<div class="hero-figure"><img src="assets/logo-hero.png" alt="Pitt NSBE logo"></div>'
    return f"""<header class="hero">
  <div class="wrap">
    <div class="hero-copy">
      <span class="eyebrow on-navy">{eyebrow}</span>
      <h1>{h1}</h1>
      <p class="lead">{lead}</p>
      {f'<div class="hero-actions">{actions}</div>' if actions else ''}
    </div>
    {fig}
  </div>
</header>
<span class="torn"></span>"""


def jumpnav(items):
    links = "".join(f'<a href="#{i}" class="btn on-paper outline" style="padding:8px 14px;font-size:0.7rem;">{l}</a>' for i, l in items)
    return f'<section class="tight alt"><div class="wrap" style="display:flex;gap:10px;flex-wrap:wrap;">{links}</div></section>'


# ============================================================= HOME
home_sections = [
    ("mission", "Mission"),
    ("motm", "Member of the month"),
    ("announcements", "Announcements"),
    ("events", "Upcoming events"),
    ("newsletter", "Newsletter"),
    ("contact", "Contact us"),
]

home_body = hero(
    "Pitt chapter &middot; est. [year]",
    "Engineering&nbsp;the future,<br>together.",
    "The Pitt chapter of the National Society of Black Engineers supports Black engineering students at the University of Pittsburgh through community, mentorship, professional development, and academic excellence.",
    '<a class="btn" href="membership.html">Join us</a><a class="btn outline" href="#events">See upcoming events</a>',
    photo=True,
) + jumpnav(home_sections) + """

<section id="mission">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Our mission</span>
      <h2>Why we're here</h2>
      <p>[Placeholder: one paragraph on the chapter's mission &mdash; academic excellence, professional development, community, and increasing the number of Black engineers who study, graduate, and thrive at Pitt. Replace with your chapter's real mission statement.]</p>
      <a class="btn on-paper outline" href="about.html#history">Read our full history</a>
    </div>
    <div class="grid cols-4">
      <div class="stat"><div class="num">[N]</div><div class="label">Active members</div></div>
      <div class="stat"><div class="num">[N]</div><div class="label">Events per semester</div></div>
      <div class="stat"><div class="num">[N]</div><div class="label">Corporate partners</div></div>
      <div class="stat"><div class="num">[YEAR]</div><div class="label">Chapter founded</div></div>
    </div>
  </div>
</section>

<section id="motm" class="alt">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Spotlight</span>
      <h2>Member of the month</h2>
    </div>
    <div class="card" style="max-width:520px;display:flex;gap:20px;align-items:flex-start;flex-wrap:wrap;">
      <div class="photo-block" style="width:140px;height:140px;flex:0 0 140px;margin-bottom:0;">Photo</div>
      <div>
        <h3>[Member name]</h3>
        <p class="meta">[Year] &middot; [Major]</p>
        <p>[Placeholder: a short highlight &mdash; what this member has been working on, an award, a project, or why they were nominated.]</p>
      </div>
    </div>
  </div>
</section>

<section id="announcements">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Latest</span>
      <h2>Announcements</h2>
    </div>
    <div class="grid cols-3">
      <div class="card"><span class="tag rust">Update</span><p class="meta">[Date]</p><p>[Placeholder announcement.]</p></div>
      <div class="card"><span class="tag">Reminder</span><p class="meta">[Date]</p><p>[Placeholder announcement.]</p></div>
      <div class="card"><span class="tag mustard">Deadline</span><p class="meta">[Date]</p><p>[Placeholder announcement.]</p></div>
    </div>
  </div>
</section>

<section id="events" class="alt">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Calendar</span>
      <h2>Upcoming events</h2>
    </div>
    <div class="tabs">
      <button class="tab-btn active" data-tab="ev-upcoming">Upcoming</button>
      <button class="tab-btn" data-tab="ev-past">Past</button>
    </div>
    <div class="tab-panel active" id="ev-upcoming">
      <div class="grid cols-3">
        <div class="card"><span class="tag rust">GBM</span><h3>General body meeting</h3><p class="meta">[Date] &middot; [Location]</p><p>[Placeholder description.]</p></div>
        <div class="card"><span class="tag">Workshop</span><h3>Resume &amp; LinkedIn workshop</h3><p class="meta">[Date] &middot; [Location]</p><p>[Placeholder description.]</p></div>
        <div class="card"><span class="tag mustard">Social</span><h3>Chapter social</h3><p class="meta">[Date] &middot; [Location]</p><p>[Placeholder description.]</p></div>
      </div>
    </div>
    <div class="tab-panel" id="ev-past">
      <div class="grid cols-3">
        <div class="card"><span class="tag rust">GBM</span><h3>Kickoff meeting</h3><p class="meta">[Date] &middot; [Location]</p><p>[Placeholder description.]</p></div>
        <div class="card"><span class="tag">Info session</span><h3>Corporate info session</h3><p class="meta">[Date] &middot; [Location]</p><p>[Placeholder description.]</p></div>
      </div>
    </div>
  </div>
</section>

<section id="newsletter">
  <div class="wrap">
    <div class="grid cols-2">
      <div>
        <span class="eyebrow">Just dropped</span>
        <h2>Current newsletter</h2>
        <div class="card">
          <span class="tag">[Month, Year]</span>
          <h3>[Newsletter issue title]</h3>
          <p>[Placeholder: one-line teaser of what's inside this issue.]</p>
          <a href="newsletter.html">Read the full issue &rarr;</a>
        </div>
      </div>
      <div>
        <span class="eyebrow">Don't miss the next one</span>
        <h2>Subscribe</h2>
        <form action="#" method="post">
          <label for="home-nl-email">Email address</label>
          <input id="home-nl-email" name="email" type="email" required>
          <p class="form-note">[Placeholder: connect to Mailchimp/Google Forms.] See the <a href="newsletter.html">newsletter archive</a> for past issues.</p>
          <button class="btn" type="submit" style="margin-top:14px;">Subscribe</button>
        </form>
      </div>
    </div>
  </div>
</section>

<section id="contact" class="navy-band">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow on-navy">Reach out</span>
      <h2>Contact us</h2>
    </div>
    <div class="grid cols-3">
      <div class="card">
        <span class="tag">Chapter</span>
        <h3>Pitt NSBE</h3>
        <p>Email: <a href="mailto:pittnsbe@pitt.edu">pittnsbe@pitt.edu</a></p>
        <p>Meetings: [Placeholder: day, time, room/building]</p>
      </div>
      <div class="card">
        <span class="tag olive">Regional</span>
        <h3>NSBE Region II &mdash; Mid-Atlantic</h3>
        <p>Covers PA, DC, DE, MD, NC, SC, VA, WV, and parts of Europe/North Africa/Middle East.</p>
        <p>Regional contact: [Placeholder &mdash; check nsbe.org/regions for the current Region II chair's contact info, since this changes each term.]</p>
      </div>
      <div class="card">
        <span class="tag rust">National</span>
        <h3>NSBE headquarters</h3>
        <p>205 Daingerfield Road<br>Alexandria, VA 22314</p>
        <p>Phone: 703-549-2207<br>Email: <a href="mailto:membership@nsbe.org">membership@nsbe.org</a></p>
      </div>
    </div>
    <form action="mailto:pittnsbe@pitt.edu" method="post" enctype="text/plain" style="margin-top:36px;max-width:560px;">
      <label for="c-name" style="color:#fff;">Name</label>
      <input id="c-name" name="name" type="text" required>
      <label for="c-email" style="color:#fff;">Email</label>
      <input id="c-email" name="email" type="email" required>
      <label for="c-msg" style="color:#fff;">Message</label>
      <textarea id="c-msg" name="message" required></textarea>
      <button class="btn" type="submit" style="margin-top:16px;">Send message</button>
    </form>
  </div>
</section>
"""

# ============================================================= ABOUT US
about_sections = [("history", "History"), ("eboard", "E-board"), ("awards", "Awards")]

about_body = hero(
    "About us", "Our story",
    "From the national NSBE mission to the Pitt chapter's own history &mdash; here's where we come from.",
) + jumpnav(about_sections) + """

<section id="history">
  <div class="wrap">
    <div class="grid cols-2">
      <div>
        <span class="eyebrow">National history</span>
        <h2>National Society of Black Engineers</h2>
        <p>NSBE was founded in 1975 and has grown into one of the largest student-managed organizations in the country, dedicated to increasing the number of culturally responsible Black engineers who excel academically, succeed professionally, and positively impact the community. [Placeholder: expand with more national history detail if you'd like.]</p>
      </div>
      <div>
        <span class="eyebrow">Pitt chapter history</span>
        <h2>Our chapter at Pitt</h2>
        <p>[Placeholder: when the Pitt chapter was founded, key milestones, and what makes it distinct. Replace with your chapter's real history.]</p>
      </div>
    </div>
  </div>
</section>

<section id="eboard" class="alt">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Leadership</span>
      <h2>Current e-board</h2>
    </div>
    <div class="grid cols-4">
      __OFFICER_CARDS__
    </div>
  </div>
</section>

<section id="awards">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Recognition</span>
      <h2>Awards won</h2>
    </div>
    <div class="grid cols-3">
      <div class="card"><span class="tag mustard">[Year]</span><h3>[Award name]</h3><p>[Placeholder: awarding body and what it recognized &mdash; e.g. regional or national conference award.]</p></div>
      <div class="card"><span class="tag mustard">[Year]</span><h3>[Award name]</h3><p>[Placeholder award description.]</p></div>
      <div class="card"><span class="tag mustard">[Year]</span><h3>[Award name]</h3><p>[Placeholder award description.]</p></div>
    </div>
  </div>
</section>
"""

def officer_card(role):
    return f'<div class="card"><div class="photo-block">Photo</div><h3>[Name]</h3><p class="meta">{role}</p></div>'

officer_roles = ["President", "Vice President", "Secretary", "Treasurer",
                  "Programs Chair", "Senator / Delegate", "AEX Chair", "Freshman Rep Coordinator"]
about_body = about_body.replace("__OFFICER_CARDS__", "".join(officer_card(r) for r in officer_roles))

# ============================================================= MEMBERSHIP
membership_sections = [("steps", "Steps"), ("alumni", "Alumni"), ("updates", "Announcements"), ("conferences", "Conferences")]

membership_body = hero(
    "Get involved", "Membership",
    "How to join, what alumni support looks like, and where membership can take you &mdash; conferences included.",
) + jumpnav(membership_sections) + """

<section id="steps">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Getting started</span>
      <h2>Steps toward membership</h2>
    </div>
    <div class="grid cols-3">
      <div class="card"><span class="tag">Step 1</span><h3>Join NSBE nationally</h3><p>Register directly with National Society of Black Engineers at <a href="https://nsbe.org" target="_blank" rel="noopener">nsbe.org</a> and pay national dues.</p></div>
      <div class="card"><span class="tag">Step 2</span><h3>Register with the chapter</h3><p>[Placeholder: chapter sign-up process &mdash; a form, GroupMe, or sign-up sheet at a GBM.]</p></div>
      <div class="card"><span class="tag">Step 3</span><h3>Come to a GBM</h3><p>General body meetings happen [Placeholder: day/time/location]. Best way to meet the chapter.</p></div>
    </div>
  </div>
</section>

<section id="alumni" class="alt">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Stay connected</span>
      <h2>Alumni network</h2>
      <p>[Placeholder: how alumni stay involved &mdash; a LinkedIn group, mentorship availability, homecoming events, or a mailing list. Add a signup link once set up.]</p>
    </div>
    <div class="grid cols-3">
      <div class="card"><h3>Mentorship</h3><p>[Placeholder: alumni offering career mentorship to current members.]</p></div>
      <div class="card"><h3>Networking events</h3><p>[Placeholder: annual alumni mixer, homecoming meetup, etc.]</p></div>
      <div class="card"><h3>Giving back</h3><p>[Placeholder: how alumni can speak at GBMs, sponsor events, or donate. See <a href="donation.html">donations</a>.]</p></div>
    </div>
  </div>
</section>

<section id="updates">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Member updates</span>
      <h2>Announcements</h2>
    </div>
    <div class="grid cols-3">
      <div class="card"><span class="tag rust">Dues</span><p class="meta">[Date]</p><p>[Placeholder: dues deadline or renewal reminder.]</p></div>
      <div class="card"><span class="tag">Recruitment</span><p class="meta">[Date]</p><p>[Placeholder: rush event or interest form deadline.]</p></div>
    </div>
  </div>
</section>

<section id="conferences" class="alt">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">On the road</span>
      <h2>Conferences</h2>
    </div>
    <div class="grid cols-3">
      <div class="card"><span class="tag rust">Upcoming</span><h3>Fall Regional Conference</h3><p class="meta">[Date] &middot; [City]</p><p>[Placeholder: registration deadline and travel info.]</p></div>
      <div class="card"><span class="tag">Upcoming</span><h3>NSBE National Convention</h3><p class="meta">[Date] &middot; [City]</p><p>[Placeholder: registration deadline and travel info.]</p></div>
      <div class="card"><span class="tag mustard">Info</span><h3>How to attend</h3><p>[Placeholder: chapter funding process, number of funded spots, interest form link.]</p></div>
    </div>
  </div>
</section>
"""

# ============================================================= PROGRAMS
programs_body = hero(
    "How members grow", "Programs",
    "Pitt NSBE runs focused programs so every member finds a path that fits.",
) + """
<section>
  <div class="wrap">
    <div class="grid cols-3">
      <div class="card"><span class="tag">Academic</span><h3>AEX</h3><p>Academic Excellence &mdash; [placeholder description].</p><a href="programs-aex.html">Learn more &rarr;</a></div>
      <div class="card"><span class="tag rust">Mentorship</span><h3>Mentor-mentee</h3><p>[Placeholder description.]</p><a href="programs-mentor-mentee.html">Learn more &rarr;</a></div>
      <div class="card"><span class="tag mustard">Community</span><h3>Freshman Reps</h3><p>[Placeholder description.]</p><a href="programs-freshman-reps.html">Learn more &rarr;</a></div>
    </div>
  </div>
</section>
"""

def program_page(eyebrow, title, lead, chair_label):
    return hero(eyebrow, title, lead) + f"""
<section>
  <div class="wrap">
    <div class="grid cols-2">
      <div>
        <span class="eyebrow">Overview</span>
        <h2>What this program does</h2>
        <p>[Placeholder: 2-3 sentences on the program's purpose and what a typical semester looks like.]</p>
      </div>
      <div>
        <span class="eyebrow">Chair contact</span>
        <h2>{chair_label}</h2>
        <div class="card"><div class="photo-block">Photo</div><h3>[Name]</h3><p class="meta">{chair_label}</p><p><a href="mailto:pittnsbe@pitt.edu">Email the chair</a></p></div>
      </div>
    </div>
    <hr class="divider">
    <div class="section-head">
      <span class="eyebrow">This semester</span>
      <h2>Current initiatives</h2>
      <p>[Placeholder: list current initiatives, upcoming sessions, or how to get involved.]</p>
    </div>
  </div>
</section>
"""

programs_aex_body = program_page("Programs &middot; Academic", "AEX &mdash; Academic Excellence",
    "Supporting members' academic success through study sessions, tutoring, and accountability.", "AEX Chair")
programs_mentor_body = program_page("Programs &middot; Mentorship", "Mentor-mentee program",
    "Pairing upperclassmen with underclassmen for guidance, support, and community.", "Mentor-mentee coordinator")
programs_freshman_body = program_page("Programs &middot; Community", "Freshman representatives",
    "First-year members who represent their class and help plan programming for new students.", "Freshman Rep coordinator")

# ============================================================= HIDDEN PAGES

donation_body = hero(
    "Support the chapter", "Donate",
    "Your support helps fund conference travel, workshops, and programming for our members.",
) + """
<section>
  <div class="wrap">
    <div class="grid cols-3">
      <div class="card"><span class="tag mustard">$25</span><h3>Supporter</h3><p>[Placeholder: what this covers, e.g. one member's workshop materials.]</p></div>
      <div class="card"><span class="tag olive">$100</span><h3>Advocate</h3><p>[Placeholder: e.g. partial conference travel support.]</p></div>
      <div class="card"><span class="tag rust">$250+</span><h3>Champion</h3><p>[Placeholder: e.g. full conference registration for a member.]</p></div>
    </div>
    <div style="margin-top:30px;">
      <a class="btn on-paper outline" href="#">[Placeholder: link to donation platform, e.g. a Pitt giving page or Venmo]</a>
    </div>
    <p class="form-note" style="margin-top:18px;">If the chapter uses its own tax ID or the University's giving platform for donations, link that here instead of a personal payment app.</p>
  </div>
</section>
"""

sponsorship_body = hero(
    "Partner with us", "Sponsorship",
    "Corporate and community partners help make our programming, travel, and events possible.",
) + """
<section>
  <div class="wrap">
    <div class="grid cols-3">
      <div class="card"><span class="tag mustard">Tier 1</span><h3>[Sponsorship tier name]</h3><p>[Placeholder: benefits &mdash; logo placement, tabling, resume book access, GBM info session slot, etc.]</p></div>
      <div class="card"><span class="tag olive">Tier 2</span><h3>[Sponsorship tier name]</h3><p>[Placeholder benefits.]</p></div>
      <div class="card"><span class="tag rust">Tier 3</span><h3>[Sponsorship tier name]</h3><p>[Placeholder benefits.]</p></div>
    </div>
    <hr class="divider">
    <div class="section-head">
      <span class="eyebrow">Current partners</span>
      <h2>Thank you to our sponsors</h2>
    </div>
    <div class="grid cols-4">
      <div class="photo-block">Logo</div><div class="photo-block">Logo</div>
      <div class="photo-block">Logo</div><div class="photo-block">Logo</div>
    </div>
    <p style="margin-top:26px;">Interested in partnering with us? Email <a href="mailto:pittnsbe@pitt.edu">pittnsbe@pitt.edu</a>.</p>
  </div>
</section>
"""

newsletter_body = hero(
    "Stay updated", "Newsletter archive",
    "Chapter news, events, and opportunities &mdash; every past issue, all in one place.",
) + """
<section>
  <div class="wrap grid cols-2">
    <div>
      <span class="eyebrow">Subscribe</span>
      <h2>Join the mailing list</h2>
      <form action="#" method="post">
        <label for="nl-email">Email address</label>
        <input id="nl-email" name="email" type="email" required>
        <p class="form-note">[Placeholder: connect this form to Mailchimp, Google Forms, or your platform of choice.]</p>
        <button class="btn" type="submit" style="margin-top:16px;">Subscribe</button>
      </form>
    </div>
    <div>
      <span class="eyebrow">Archive</span>
      <h2>Past issues</h2>
      <div class="grid cols-1" style="gap:14px;">
        <div class="card"><p class="meta">[Month, Year]</p><h3>[Issue title]</h3><a href="#">Read issue &rarr;</a></div>
        <div class="card"><p class="meta">[Month, Year]</p><h3>[Issue title]</h3><a href="#">Read issue &rarr;</a></div>
        <div class="card"><p class="meta">[Month, Year]</p><h3>[Issue title]</h3><a href="#">Read issue &rarr;</a></div>
      </div>
    </div>
  </div>
</section>
"""

merch_body = hero(
    "Rep the chapter", "Merch",
    "Pitt NSBE gear &mdash; browse what's available and how to order.",
) + """
<section>
  <div class="wrap">
    <div class="grid cols-3">
      <div class="card"><div class="photo-block">Product photo</div><h3>[Item name]</h3><p class="meta">$[Price]</p><p>[Placeholder: sizes/colors available.]</p></div>
      <div class="card"><div class="photo-block">Product photo</div><h3>[Item name]</h3><p class="meta">$[Price]</p><p>[Placeholder details.]</p></div>
      <div class="card"><div class="photo-block">Product photo</div><h3>[Item name]</h3><p class="meta">$[Price]</p><p>[Placeholder details.]</p></div>
    </div>
    <div class="section-head" style="margin-top:36px;">
      <span class="eyebrow">How to order</span>
      <h2>Ordering isn't automated here</h2>
      <p>This page can showcase items, but this static site doesn't include real checkout. The straightforward options: link out to a free Google Form (with Venmo/Zelle payment instructions), or set up a simple storefront on a platform like Shopify or Bonfire and link it below.</p>
      <a class="btn on-paper outline" href="#">[Placeholder: link to order form or storefront]</a>
    </div>
  </div>
</section>
"""

# ============================================================= WRITE FILES
pages = {
    "index.html": ("Home", "index.html", home_body, "Pitt chapter of the National Society of Black Engineers.", False),
    "about.html": ("About us", "about.html", about_body, "History, e-board, and awards of the Pitt NSBE chapter.", False),
    "membership.html": ("Membership", "membership.html", membership_body, "How to join Pitt NSBE, alumni network, and conferences.", False),
    "programs.html": ("Programs", "programs.html", programs_body, "Pitt NSBE programs overview.", False),
    "programs-aex.html": ("AEX", "programs.html", programs_aex_body, "Academic Excellence program.", False),
    "programs-mentor-mentee.html": ("Mentor-Mentee", "programs.html", programs_mentor_body, "Mentor-Mentee program.", False),
    "programs-freshman-reps.html": ("Freshman Representatives", "programs.html", programs_freshman_body, "Freshman Representatives Program.", False),
    "donation.html": ("Donate", "donation.html", donation_body, "Support the Pitt NSBE chapter.", True),
    "sponsorship.html": ("Sponsorship", "sponsorship.html", sponsorship_body, "Partner with the Pitt NSBE chapter.", True),
    "newsletter.html": ("Newsletter archive", "newsletter.html", newsletter_body, "Pitt NSBE newsletter archive.", True),
    "merch.html": ("Merch", "merch.html", merch_body, "Pitt NSBE merchandise.", True),
}

for fname, (title, active, body, desc, noindex) in pages.items():
    html = page(title, active, body, desc, noindex)
    with open(os.path.join(OUT, fname), "w") as f:
        f.write(html)

print(f"Wrote {len(pages)} pages to {OUT}")
