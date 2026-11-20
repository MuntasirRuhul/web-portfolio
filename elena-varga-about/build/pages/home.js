  // Newsletter: check the address, then thank them in place (the sandboxed preview blocks real form submission, so the button and Enter call it directly).
  const news = document.getElementById('newsForm'), email = document.getElementById('newsEmail'), msg = document.getElementById('newsMsg');
  const join = e => {
    e.preventDefault();
    const ok = email.checkValidity() && email.value.trim() !== '';
    email.setAttribute('aria-invalid', !ok);
    msg.classList.toggle('ok', ok);
    msg.textContent = ok ? 'Thank you. The lesson is on its way to ' + email.value.trim() + '.' : 'Add an email address, like marta@example.com.';
    if (!ok) email.focus();
  };
  news.addEventListener('submit', join);
  news.querySelector('button').addEventListener('click', join);
  email.addEventListener('keydown', e => { if (e.key === 'Enter') join(e); });
