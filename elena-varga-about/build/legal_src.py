"""Writes terms.main.html and privacy.main.html from the section lists below."""
import sys, re
P = sys.argv[1]

TERMS = dict(
  key='terms', eyebrow='Information', title='Terms and conditions', read='7 min read',
  lead='These terms cover your account with Elena Varga Atelier, the courses you take and the work you share with us. We’ve tried to write them the way Elena teaches: plainly, one thing at a time.',
  sections=[
    ('who', 'Who we are', '''<p>Elena Varga Atelier is an online drawing school run by Elena Varga from her studio at Rua da Graça 4, 3º, 1170-165 Lisboa, Portugal. When these terms say “we” or “the studio”, they mean Elena and the small team that helps her. “You” means the person using the site.</p>
<p>By creating an account or buying a course you agree to these terms. If you don’t agree, please don’t use your account; you can still read the studio notes and watch lesson 1.</p>'''),
    ('account', 'Your account', '''<ul><li>You need to be 16 or older to open an account. Younger students are welcome with a parent or guardian who opens the account for them.</li>
<li>Give us an email address you check. We use it for receipts, course updates and replies from Elena.</li>
<li>Keep your password to yourself. An account is for one student; please don’t share it.</li>
<li>Tell us straight away at the contact page if you think someone else has used your account.</li></ul>'''),
    ('courses', 'Courses and access', '''<p>When you buy a course you get access to its video lessons, exercises and printable sheets for as long as the course is offered, and for at least <b>three years</b> from the day you buy it. If we ever retire a course, we’ll tell you at least 60 days before and let you download the sheets.</p>
<p>Lesson 1 of every course is free and stays free. Live sessions and private critiques are booked separately, and their dates are confirmed by email.</p>'''),
    ('payments', 'Prices and payment', '''<p>Prices are shown in euros and include Portuguese VAT where it applies. You pay once per course; there are no hidden subscriptions. Payments are handled by our payment provider, and we never see or store your full card number.</p>
<p>Gift courses are paid for by the giver and can be redeemed by the person named on the gift, within 12 months.</p>'''),
    ('refunds', 'Changing your mind', '''<p>If a course isn’t right for you, write to us within <b>14 days</b> of buying it and we’ll refund you in full, whether or not you’ve started. This is in addition to your rights under EU consumer law, not instead of them.</p>
<p>Private critiques can be moved or cancelled up to 48 hours before they’re due; after that, the critique is used.</p>'''),
    ('your-work', 'Your drawings', '''<p>Everything you draw is yours. When you upload a drawing for feedback, you let us store it and show it to Elena and, in group critiques, to the other students in that session. That’s all.</p>
<p>We will only show your work anywhere else, for example on this site or in a studio note, if you say yes in writing for that drawing. You can change your mind at any time and we’ll take it down.</p>'''),
    ('our-work', 'Elena’s lessons', '''<p>The videos, drawings, sheets and texts on this site belong to Elena Varga. You may watch them, print the sheets and copy the exercises for your own practice, and you may teach what you learn. Please don’t resell, re-upload or share course files publicly.</p>'''),
    ('conduct', 'In the studio', '''<p>Group sessions and comments work because people are kind about each other’s drawings. We may remove comments, or close an account, if someone is abusive, posts others’ work as their own, or uses the site to sell things. We’ll tell you why, and refund any course you haven’t started.</p>'''),
    ('liability', 'Our responsibility', '''<p>We work hard to keep the site running and the lessons accurate, but we can’t promise the site will never be down. Nothing in these terms limits the rights you have as a consumer, or our responsibility for harm we cause through negligence.</p>'''),
    ('changes', 'Changes and law', '''<p>If we change these terms, we’ll email you at least 30 days before the change takes effect, and you can close your account if you don’t agree. These terms are governed by Portuguese law, and you can bring a claim in the courts where you live.</p>'''),
  ])

PRIVACY = dict(
  key='privacy', eyebrow='Information', title='Privacy policy', read='6 min read',
  lead='We collect as little about you as we can, keep it only as long as we need it and never sell it. This page says what we keep, why, and how to ask for it back.',
  sections=[
    ('controller', 'Who looks after your data', '''<p>Elena Varga Atelier, Rua da Graça 4, 3º, 1170-165 Lisboa, Portugal, is responsible for the personal data described here. You can reach us about privacy through the <a href="contact.html">contact page</a>; choose “Something else” and we’ll answer within a month, usually much sooner.</p>'''),
    ('collect', 'What we keep', '''<ul><li><b>Your account:</b> your first name, email address, password (stored scrambled, never readable) and the level you chose when you joined.</li>
<li><b>Your courses:</b> what you’ve bought, which lessons you’ve finished, and your receipts.</li>
<li><b>Your drawings:</b> photos you upload for feedback, and Elena’s notes on them.</li>
<li><b>Your letters:</b> what you write to us through the contact form, and our replies.</li>
<li><b>Basic site logs:</b> the pages requested and the browser used, kept briefly to keep the site secure.</li></ul>
<p>We don’t ask for your address, your birthday or anything about your health, and we don’t keep card numbers.</p>'''),
    ('why', 'Why we keep it', '''<ul><li>To run your account and give you the courses you bought (to perform our contract with you).</li>
<li>To send receipts and keep invoices (because the law requires it).</li>
<li>To send studio notes, only if you ticked the box (with your consent, which you can withdraw in one click from any email).</li>
<li>To keep the site secure and working (our legitimate interest).</li></ul>'''),
    ('sharing', 'Who else sees it', '''<p>We use a small number of trusted services to run the school: a payment provider, a video host for the lessons, an email service for receipts and studio notes, and a web host. Each only gets what it needs to do its job, under a written agreement, and stores data in the EU or under EU-approved safeguards.</p>
<p>We never sell your data or share it with advertisers.</p>'''),
    ('cookies', 'Cookies', '''<p>The site uses one essential cookie to keep you logged in, and remembers on your device whether you chose “Keep me logged in”. We don’t use advertising or tracking cookies. If we ever add anonymous visit counting, we’ll ask first.</p>'''),
    ('keep', 'How long we keep it', '''<ul><li>Your account and course history: while your account is open, then 12 months after you close it.</li>
<li>Invoices: 10 years, as Portuguese tax law requires.</li>
<li>Uploaded drawings: until you delete them or close your account.</li>
<li>Letters to the studio: two years after the last reply.</li>
<li>Site logs: 30 days.</li></ul>'''),
    ('rights', 'Your rights', '''<p>You can ask to see the data we hold about you, correct it, download it, or have it deleted. You can object to how we use it, or ask us to stop for a while. You can close your account from your settings or by writing to us, and we’ll confirm once it’s done.</p>
<p>If you’re unhappy with how we’ve handled your data, you can complain to the Portuguese data protection authority, the Comissão Nacional de Proteção de Dados (CNPD), or to the authority where you live.</p>'''),
    ('security', 'Keeping it safe', '''<p>The site is served over an encrypted connection, passwords are stored scrambled, and only Elena and the people who help her with student support can see your account. If something ever goes wrong, we’ll tell you and the authorities as the law requires.</p>'''),
    ('changes', 'Changes to this policy', '''<p>When we change this policy we’ll update the date at the top, and if the change matters, we’ll email you before it takes effect.</p>'''),
  ])

for d in (TERMS, PRIVACY):
    other = ('privacy.html', 'privacy policy') if d['key'] == 'terms' else ('terms.html', 'terms and conditions')
    toc = '\n'.join(f'      <li><a href="#{i}"><span class="caption">{n + 1:02d}</span>{t}</a></li>' for n, (i, t, _) in enumerate(d['sections']))
    secs = '\n'.join(f'''    <section id="{i}" aria-labelledby="h-{i}">
      <h2 class="heading-4" id="h-{i}"><span class="caption">{n + 1:02d}</span>{t}</h2>
      {re.sub(chr(10), chr(10) + '      ', body)}
    </section>''' for n, (i, t, body) in enumerate(d['sections']))
    html = f'''<main class="lg">
  <p class="lg-eyebrow label">{d['eyebrow']}</p>
  <h1 class="lg-title heading-1">{d['title']}</h1>
  <p class="lg-meta caption"><span>Last updated 27 October 2026</span><span>{d['read']}</span></p>
  <div class="lg-rule" aria-hidden="true"></div>

  <div class="lg-grid">
    <nav class="lg-toc" aria-label="On this page">
      <p class="label">On this page</p>
      <ol class="body-m">
{toc}
      </ol>
      <p class="lg-ask body-m">See also our <a href="{other[0]}">{other[1]}</a>.</p>
    </nav>

    <article class="lg-body body-m">
    <p class="lg-lead body-l">{d['lead']}</p>
{secs}
    <div class="lg-end">
      <div><p class="heading-4">A question about this page?</p><p class="body-m">Write to the studio. Elena reads letters on Tuesday and Friday mornings.</p></div>
      <a class="btn btn-paper" href="contact.html">Write to us <span class="ar" aria-hidden="true">→</span></a>
    </div>
    </article>
  </div>
</main>
'''
    open(f"{P}/{d['key']}.main.html", 'w').write(html)
    print('wrote', d['key'])
