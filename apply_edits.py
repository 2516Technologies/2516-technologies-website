#!/usr/bin/env python3
"""
Orr Group Proposal — Apply All Edits
Run from inside the orr-group-proposal folder:
    cd /path/to/orr-group-proposal
    python3 apply_edits.py
"""

import os, re

def read(f):
    with open(f, encoding='utf-8') as fh:
        return fh.read()

def write(f, content):
    with open(f, 'w', encoding='utf-8') as fh:
        fh.write(content)
    print(f"  ✓ {f}")

def remove_em_dashes(html):
    # Replace em dashes (— and --) with commas or clean alternatives
    html = re.sub(r'\s*—\s*', ' ', html)
    html = re.sub(r'\s*–\s*(?=[a-z])', ' ', html)  # mid-sentence en dashes
    return html

def remove_emojis(html):
    # Remove common emojis used as icons in the proposal
    emoji_pattern = re.compile(
        u'[\U0001F300-\U0001F9FF'   # misc symbols
        u'\U0001F600-\U0001F64F'    # emoticons
        u'\U0001F680-\U0001F6FF'    # transport
        u'\u2600-\u26FF'            # misc symbols
        u'\u2700-\u27BF'            # dingbats
        u'\U0001F1E0-\U0001F1FF'    # flags
        u'\u2139'                   # info
        u'\u23CF'                   # eject
        u'\u23E9-\u23F3'            # clocks
        u'\u25AA-\u25AB'
        u'\u25B6'
        u'\u25C0'
        u'\u25FB-\u25FE'
        u'\u2614-\u2615'
        u'\u2648-\u2653'
        u'\u267F'
        u'\u2693'
        u'\u26A1'
        u'\u26AA-\u26AB'
        u'\u26BD-\u26BE'
        u'\u26C4-\u26C5'
        u'\u26CE'
        u'\u26D4'
        u'\u26EA'
        u'\u26F2-\u26F3'
        u'\u26F5'
        u'\u26FA'
        u'\u26FD'
        u'\u2702'
        u'\u2705'
        u'\u2708-\u270D'
        u'\u270F'
        u'\u2712'
        u'\u2714'
        u'\u2716'
        u'\u271D'
        u'\u2721'
        u'\u2728'
        u'\u2733-\u2734'
        u'\u2744'
        u'\u2747'
        u'\u274C'
        u'\u274E'
        u'\u2753-\u2755'
        u'\u2757'
        u'\u2763-\u2764'
        u'\u2795-\u2797'
        u'\u27A1'
        u'\u27B0'
        u'\u27BF'
        u'\u2934-\u2935'
        u'\u2B05-\u2B07'
        u'\u2B1B-\u2B1C'
        u'\u2B50'
        u'\u2B55'
        u'\u3030'
        u'\u303D'
        u'\u3297'
        u'\u3299'
        u'\U0001F004'
        u'\U0001F0CF'
        u'\U0001F170-\U0001F171'
        u'\U0001F17E-\U0001F17F'
        u'\U0001F18E'
        u'\U0001F191-\U0001F19A'
        u'\U0001F1E8-\U0001F1EC'
        u'\U0001F1EE-\U0001F1F0'
        u'\U0001F1F3'
        u'\U0001F1F7-\U0001F1FA'
        u'\U0001F201-\U0001F202'
        u'\U0001F21A'
        u'\U0001F22F'
        u'\U0001F232-\U0001F23A'
        u'\U0001F250-\U0001F251'
        u'⚠★✓✗✅❌'
        u']+', flags=re.UNICODE)
    # Remove emoji followed by optional whitespace at start of div content
    html = emoji_pattern.sub('', html)
    # Clean up any double spaces left behind
    html = re.sub(r'  +', ' ', html)
    return html

def replace_cj(html):
    # Replace standalone "CJ" with "The Orr Group" — case sensitive, whole word
    html = re.sub(r'\bCJ\'s\b', "The Orr Group's", html)
    html = re.sub(r'\bCJ\b', 'The Orr Group', html)
    return html

def fix_mobile_table(html):
    # Wrap tables in overflow-x:auto div if not already wrapped
    html = re.sub(
        r'(<table class="info-table")',
        r'<div style="overflow-x:auto;-webkit-overflow-scrolling:touch;">\1',
        html
    )
    html = re.sub(
        r'(</table>)',
        r'\1</div>',
        html
    )
    # Avoid double-wrapping
    html = html.replace(
        '<div style="overflow-x:auto;-webkit-overflow-scrolling:touch;"><div style="overflow-x:auto;',
        '<div style="overflow-x:auto;'
    )
    return html

def fix_mobile_grid(html):
    # Ensure two-col and three-col collapse on mobile — add max-width:100% safety
    html = html.replace(
        'class="two-col"',
        'class="two-col" style="max-width:100%;"'
    )
    return html

# ── FILE-SPECIFIC EDITS ────────────────────────────────────────────────────

def edit_index(html):
    old = ('This proposal is a direct response to the platform vision you shared. '
           'Below is what you told us, our honest assessment of where the current prototype stands, '
           'and a clear path from where you are today to a platform serving 1,000+ nonprofits '
           '&#8212; reliably, on mobile, with the Orr Group name behind it.')
    new = ('This proposal is submitted for consideration to build and deploy Orr Group\'s nonprofit AI platform. '
           'It includes an assessment of the product vision, the market opportunity, and a proposed path forward '
           '&#8212; delivering a platform that is reliable, stable, auditable, and built to industry standards. '
           'Mobile-first, scalable, and worthy of the Orr Group name.')
    # Try both encoded and literal dash versions
    html = html.replace(
        'This proposal is a direct response to the platform vision you shared. Below is what you told us, our honest assessment of where the current prototype stands, and a clear path from where you are today to a platform serving 1,000+ nonprofits — reliably, on mobile, with the Orr Group name behind it.',
        'This proposal is submitted for consideration to build and deploy Orr Group\'s nonprofit AI platform. It includes an assessment of the product vision, the market opportunity, and a proposed path forward — delivering a platform that is reliable, stable, auditable, and built to industry standards. Mobile-first, scalable, and worthy of the Orr Group name.'
    )
    return html

def edit_next_steps(html):
    # Hero h1
    html = html.replace(
        'The deadline is Friday. <em>Here\'s what happens between now and then.</em>',
        'Ready to build this. <em>Here\'s what happens next.</em>'
    )
    # Hero subhead
    html = html.replace(
        'A decision before Friday means work begins the week after. Other firms are submitting proposals this week too. This one is designed to answer every question before you have to ask it — so when you\'re ready to decide, you already know the answer.',
        'When you\'re ready to move forward, the path is straightforward. Here\'s what the first few weeks look like.'
    )
    html = html.replace(
        'When you\'re ready to move forward, the path is straightforward. Here\'s what the first few weeks look like.',
        'When you\'re ready to move forward, the path is straightforward. Here\'s what the first few weeks look like.'
    )
    # Remove Friday from step 01 description
    html = html.replace(
        'If anything is unclear, reach out directly — a 20-minute call clarifies more than an email chain.',
        'If anything is unclear, reach out directly. A 20-minute call clarifies more than an email chain.'
    )
    # Bottom quote
    html = html.replace(
        'The best proposal isn\'t the one that gets submitted — it\'s the one that makes the decision easy. That\'s what this is designed to be.',
        'This platform matters. The nonprofits that need it are ready. Let\'s build it right.'
    )
    html = html.replace(
        'The nonprofit sector is ready for this. The technology is ready. Orr Group is the right organization to build it. Let\'s not let the deadline pass without a conversation.',
        'This platform matters. The nonprofits that need it are ready. Let\'s build it right.'
    )
    # CTA subhead
    html = html.replace(
        'Mark is available this week for a 30-minute call to answer any questions, discuss the options, or walk through any part of this proposal in detail. The Friday deadline is close — let\'s use the time well.',
        'Mark is available for a call to walk through any part of this proposal, answer questions, or discuss scope.'
    )
    html = html.replace(
        'Mark is available for a call to walk through any part of this proposal in detail, answer questions, or discuss scope before Friday\'s submission.',
        'Mark is available for a call to walk through any part of this proposal, answer questions, or discuss scope.'
    )
    # Remove any remaining Friday references
    html = re.sub(r"[^.]*[Ff]riday[^.]*\.", '', html)
    return html

def edit_opportunity(html):
    # Remove emoji icons from the 4 product surface cards — remove the div with font-size:28px
    html = re.sub(
        r'<div style="font-size:28px;margin-bottom:12px;">[^<]+</div>\s*',
        '',
        html
    )
    return html

def edit_market_sizing(html):
    # Rename Model B section
    html = html.replace(
        'MODEL B — HOW THE BUSINESS WORKS',
        'HOW THE BUSINESS COULD WORK'
    )
    html = html.replace(
        'Model B — how the business works',
        'How the business could work'
    )
    html = html.replace(
        '<span class="eyebrow">Model B — how the business works</span>',
        '<span class="eyebrow">How the business could work</span>'
    )
    # Fix mobile overflow — wrap tables
    html = fix_mobile_table(html)
    # Fix section overflow
    html = html.replace(
        '<section class="section">',
        '<section class="section" style="overflow-x:hidden;">',
        1  # only first occurrence (the main section)
    )
    return html

def edit_assessment(html):
    # Hero subhead
    html = html.replace(
        'This is an honest technical assessment of the prototype, not a criticism of it. Prototypes are supposed to look like this. The question is what it takes to go from here to production.',
        "The hardest part of application development is communication of requirements and expectations, your prototype removes that barrier. This is one of the best prototypes I've seen in the industry, and makes my job a lot easier."
    )
    # Remove quote band block
    html = re.sub(
        r'<div class="quote-band"[^>]*>.*?</div>\s*</section>',
        '</section>',
        html, flags=re.DOTALL
    )
    # Remove inline quote band
    html = re.sub(
        r'<div class="quote-band" style="border-radius:16px.*?</div>',
        '',
        html, flags=re.DOTALL
    )
    # Section title
    html = html.replace(
        'What a Production Rebuild Requires',
        'What Going to Market Requires'
    )
    html = html.replace(
        'WHAT A PRODUCTION REBUILD REQUIRES',
        'WHAT GOING TO MARKET REQUIRES'
    )
    html = html.replace(
        'what a production rebuild requires',
        'what going to market requires'
    )
    # Section body
    html = html.replace(
        "The rebuild isn't just about fixing what's broken. It's about building a foundation that makes the Year 2 and Year 3 features possible without starting over again.",
        "Going to market with a tool of this scale requires building an infrastructure that makes year 2 and 3 happen seamlessly and enables you to easily add features as ideas come to you. My goal is to make your future requirements happen as well."
    )
    # Remove icons from 6-card feature section (font-size:24px icon divs)
    html = re.sub(
        r'<div style="font-size:24px;margin-bottom:12px;">[^<]+</div>\s*',
        '',
        html
    )
    return html

def edit_architecture(html):
    # Section eyebrow/subhead
    html = html.replace(
        'The services, the rationale, and what CJ pays for each.',
        'The service, the rationale, and how much it\'s going to cost.'
    )
    html = html.replace(
        'The services, the rationale, and what The Orr Group pays for each.',
        'The service, the rationale, and how much it\'s going to cost.'
    )
    # Infrastructure ownership paragraph
    html = html.replace(
        'Under all three delivery options, CJ owns the AWS account. These costs are billed directly to Orr Group by Amazon — 2516 has zero financial exposure on infrastructure under any option.',
        'Under all three options, The Orr Group is directly contracted and billed for infrastructure costs. This is industry best practice and ensures legal and compliance protection for The Orr Group\'s stakeholders and customers.'
    )
    html = html.replace(
        'Under all three delivery options, The Orr Group owns the AWS account. These costs are billed directly to Orr Group by Amazon 2516 has zero financial exposure on infrastructure under any option.',
        'Under all three options, The Orr Group is directly contracted and billed for infrastructure costs. This is industry best practice and ensures legal and compliance protection for The Orr Group\'s stakeholders and customers.'
    )
    # Add Claude API cost note to the Phase 2 note / warning box area
    claude_note = (
        '<div class="warning-box" style="margin-top:16px;">'
        '<p><strong style="color:var(--text);">Claude API costs:</strong> '
        'Approximately $38 to $58 per month at 1,000 organizations with prompt caching. '
        'These costs are billed directly to The Orr Group\'s AWS account when Phase 2 AI features are deployed. '
        'Not included in Phase 1 estimates above.</p></div>'
    )
    # Insert after the main table closing div
    html = html.replace(
        '<div class="warning-box" style="margin-top:24px;">',
        claude_note + '\n    <div class="warning-box" style="margin-top:24px;">',
        1
    )
    # Remove icons from 3-card bottom section
    html = re.sub(
        r'<div style="font-size:24px;margin-bottom:12px;">[^<]+</div>\s*',
        '',
        html
    )
    # Fix mobile table overflow
    html = fix_mobile_table(html)
    return html

def edit_roadmap(html):
    # Remove left sidebar on mobile only — add CSS to hide it
    hide_sidebar_css = """
    @media(max-width:768px) {
      .roadmap-sidebar { display:none !important; }
      .roadmap-grid { grid-template-columns:1fr !important; }
    }"""
    html = html.replace('</style>', hide_sidebar_css + '\n  </style>', 1)

    # Add classes to the roadmap grid and sidebar
    html = html.replace(
        '<div style="display:grid;grid-template-columns:200px 1fr;gap:0;max-width:900px;margin:0 auto;">',
        '<div class="roadmap-grid" style="display:grid;grid-template-columns:200px 1fr;gap:0;max-width:900px;margin:0 auto;">'
    )
    html = html.replace(
        '<div style="position:relative;padding-right:32px;">',
        '<div class="roadmap-sidebar" style="position:relative;padding-right:32px;">'
    )

    # Full opacity on all phases — remove opacity inline styles
    html = re.sub(r'style="([^"]*?)opacity:0\.\d+;?\s*([^"]*?)"', r'style="\1\2"', html)
    html = re.sub(r'opacity:0\.\d+;\s*', '', html)

    # Replace Phase 2 warning box
    html = html.replace(
        '<div class="warning-box" style="margin-top:16px;"><p>Phase 2 is a separate contract scoped and priced after Phase 1 is live. Claude API costs (~$38–$58/mo at 1,000 orgs) will be added to CJ\'s AWS bill at this stage.</p></div>',
        '<div class="warning-box" style="margin-top:16px;"><p>Phases 3 and 4 show the potential of what is possible with this infrastructure. This is not written into the current scope of work.</p></div>'
    )
    html = html.replace(
        '<div class="warning-box" style="margin-top:16px;"><p>Phase 2 is a separate contract scoped and priced after Phase 1 is live. Claude API costs (~$38&#8211;$58/mo at 1,000 orgs) will be added to The Orr Group\'s AWS bill at this stage.</p></div>',
        '<div class="warning-box" style="margin-top:16px;"><p>Phases 3 and 4 show the potential of what is possible with this infrastructure. This is not written into the current scope of work.</p></div>'
    )

    return html

def edit_delivery(html):
    # Remove all payment schedule sections
    html = re.sub(
        r'<div style="margin-top:24px;padding-top:24px;border-top:1px solid var\(--border\);">.*?</div>\s*</div>\s*</div>',
        '</div>\n    </div>',
        html, flags=re.DOTALL
    )
    # Remove hourly cap reference
    html = html.replace('+ $175/hr when engaged (cap: 10hrs/mo)', '+ $175/hr when engaged')
    html = html.replace('(cap: 10hrs/mo)', '')
    # Rewrite "phone number" line
    html = html.replace(
        'you have a phone number to call when something breaks',
        'you have direct access to 2516 when something is urgent'
    )
    html = html.replace(
        'You have a phone number to call when something breaks',
        'You have direct access to 2516 when something is urgent'
    )
    # Fix mobile table overflow
    html = fix_mobile_table(html)
    # Remove inc-icon spans (emoji icons in lists)
    html = re.sub(r'<span class="inc-icon">[^<]*</span>', '', html)
    html = re.sub(r'<div class="responsibility-icon">[^<]*</div>', '', html)
    return html

def edit_investment(html):
    # Market rate number
    html = html.replace('$90K–$140K', '$120K–$140K')
    html = html.replace('$90K&#8211;$140K', '$120K&#8211;$140K')
    # Market rate descriptor
    html = html.replace(
        'What a stranger client pays for this exact scope',
        'Market rate for a one-time SaaS engagement'
    )
    # Remove 2516 rate card and scope equivalent card
    # These are the 2nd and 3rd cards in the 3-card grid
    html = re.sub(
        r'<div class="card" style="padding:24px;text-align:center;border-color:var\(--gold\);">.*?</div>\s*'
        r'<div class="card" style="padding:24px;text-align:center;">.*?Scope equivalent.*?</div>',
        '',
        html, flags=re.DOTALL
    )
    # Replace intro copy for the context box
    html = html.replace(
        'This platform requires one person to simultaneously act as cloud architect, senior full-stack developer, DevOps engineer, data engineer, and product lead — for 5 months of part-time work alongside other client obligations. In the market, that scope is typically handled by a 3–5 person team or a senior fractional CTO plus contractors. The pricing below reflects a meaningful discount from what any other firm would charge for equivalent capability.',
        'The following rates reflect a preferred partner engagement — a meaningful discount from standard market rates for this scope.'
    )
    # AWS ownership paragraph
    html = html.replace(
        'CJ owns the AWS account under all three options. These costs are billed directly by Amazon to Orr Group — 2516 has zero financial exposure on infrastructure.',
        'Under all three options, The Orr Group is directly contracted and billed for infrastructure costs. This is industry best practice and ensures legal and compliance protection for The Orr Group\'s stakeholders and customers.'
    )
    html = html.replace(
        'The Orr Group owns the AWS account under all three options. These costs are billed directly by Amazon to Orr Group 2516 has zero financial exposure on infrastructure.',
        'Under all three options, The Orr Group is directly contracted and billed for infrastructure costs. This is industry best practice and ensures legal and compliance protection for The Orr Group\'s stakeholders and customers.'
    )
    # Fix mobile table overflow
    html = fix_mobile_table(html)
    return html

# ── MAIN ──────────────────────────────────────────────────────────────────

FILE_EDITS = {
    'orr-group-index.html':        edit_index,
    'orr-group-next-steps.html':   edit_next_steps,
    'orr-group-opportunity.html':  edit_opportunity,
    'orr-group-market-sizing.html':edit_market_sizing,
    'orr-group-assessment.html':   edit_assessment,
    'orr-group-architecture.html': edit_architecture,
    'orr-group-roadmap.html':      edit_roadmap,
    'orr-group-delivery.html':     edit_delivery,
    'orr-group-investment.html':   edit_investment,
}

folder = '.'
files = [f for f in os.listdir(folder) if f.endswith('.html')]

print(f"\nApplying edits to {len(files)} files...\n")

for fname in files:
    html = read(fname)

    # Global: replace CJ with The Orr Group
    html = replace_cj(html)

    # Global: remove em dashes
    html = remove_em_dashes(html)

    # Global: remove emojis
    html = remove_emojis(html)

    # File-specific edits
    if fname in FILE_EDITS:
        html = FILE_EDITS[fname](html)

    write(fname, html)

print(f"\nDone. All edits applied.")
print("\nNext steps:")
print("  git add .")
print('  git commit -m "Apply proposal edits"')
print("  git push")
