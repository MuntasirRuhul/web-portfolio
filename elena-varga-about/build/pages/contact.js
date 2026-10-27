// The form: check the three required fields inline, then show the thank-you in its place.
  const $ = id => document.getElementById(id);
  const form = $('ctForm'), checks = [[$('first'), 'e-first'], [$('email'), 'e-email'], [$('msg'), 'e-msg']];
  const check = (el, id) => { const ok = el.checkValidity() && el.value.trim() !== ''; el.setAttribute('aria-invalid', !ok); $(id).classList.toggle('on', !ok); return ok; };
  checks.forEach(([el, id]) => el.addEventListener('input', () => { if (el.getAttribute('aria-invalid') === 'true') check(el, id); }));
  const send = e => {
    e.preventDefault();
    const bad = checks.filter(([el, id]) => !check(el, id));
    if (bad.length) { bad[0][0].focus(); return; }
    $('doneName').textContent = $('first').value.trim(); $('doneMail').textContent = $('email').value.trim();
    form.hidden = true; $('ctDone').hidden = false; $('ctDone').focus();
  };
  // The site runs in a sandboxed frame that blocks form submission, so the button and the Enter key call send() directly.
  form.addEventListener('submit', send);
  form.querySelector('[type="submit"]').addEventListener('click', send);
  form.addEventListener('keydown', e => { if (e.key === 'Enter' && e.target.matches('input:not([type="checkbox"]):not([type="radio"])')) send(e); });
