// The form: check the required fields inline, show or hide the password, then show the done state in its place.
  const $ = id => document.getElementById(id);
  const form = $('auForm'), checks = [[$('email'), 'e-email'], [$('password'), 'e-password']];
  const check = (el, id) => { const ok = el.type === 'checkbox' ? el.checked : el.checkValidity() && el.value.trim() !== ''; el.setAttribute('aria-invalid', !ok); $(id).classList.toggle('on', !ok); return ok; };
  checks.forEach(([el, id]) => el.addEventListener(el.type === 'checkbox' ? 'change' : 'input', () => { if (el.getAttribute('aria-invalid') === 'true') check(el, id); }));
  document.querySelectorAll('.au-show').forEach(b => b.addEventListener('click', () => {
    const pw = $(b.getAttribute('aria-controls')), show = pw.type === 'password';
    pw.type = show ? 'text' : 'password'; b.textContent = show ? 'Hide' : 'Show'; b.setAttribute('aria-pressed', show);
  }));
  form.addEventListener('submit', e => {
    e.preventDefault();
    const bad = checks.filter(([el, id]) => !check(el, id));
    if (bad.length) { bad[0][0].focus(); return; }
    form.hidden = true; $('auDone').hidden = false; $('auDone').focus();
  });
