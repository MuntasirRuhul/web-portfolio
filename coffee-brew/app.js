// Brew method data. `steps` times are seconds from start of brew.
const METHODS = {
  "Pour Over": {
    ratio: 16, grind: "Medium-fine", temp: "93–96 °C", time: "3:00",
    steps: [
      { t: 0,   text: "Rinse filter, add coffee, then bloom with 2× coffee weight in water." },
      { t: 45,  text: "Pour in slow circles up to 60% of total water." },
      { t: 90,  text: "Pour remaining water gently." },
      { t: 150, text: "Let it drain fully." },
      { t: 180, text: "Done — swirl and enjoy!" }
    ]
  },
  "French Press": {
    ratio: 15, grind: "Coarse", temp: "93–95 °C", time: "4:00",
    steps: [
      { t: 0,   text: "Add coffee, pour all the water, and stir gently." },
      { t: 30,  text: "Place the lid on without plunging." },
      { t: 210, text: "Break the crust with a spoon and skim the foam." },
      { t: 240, text: "Plunge slowly and serve right away." }
    ]
  },
  "AeroPress": {
    ratio: 14, grind: "Medium-fine", temp: "85–92 °C", time: "2:00",
    steps: [
      { t: 0,   text: "Add coffee and pour all the water. Stir 3 times." },
      { t: 60,  text: "Insert plunger to create a seal." },
      { t: 90,  text: "Press gently for about 30 seconds." },
      { t: 120, text: "Done — dilute to taste if needed." }
    ]
  },
  "Espresso": {
    ratio: 2, grind: "Fine", temp: "92–94 °C", time: "0:28",
    steps: [
      { t: 0,  text: "Start the shot (18g in → 36g out)." },
      { t: 8,  text: "Look for a honey-like flow." },
      { t: 25, text: "Watch the scale — stop near your target weight." },
      { t: 28, text: "Done — taste and adjust your grind." }
    ]
  },
  "Cold Brew": {
    ratio: 8, grind: "Coarse", temp: "Room temp / fridge", time: "12–18 h",
    steps: [
      { t: 0,  text: "Combine coffee and cold water, stir well." },
      { t: 5,  text: "Cover and refrigerate 12–18 hours (timer here is a short demo)." },
      { t: 10, text: "Strain through a filter. Dilute 1:1 with water or milk." }
    ]
  }
};

const $ = (id) => document.getElementById(id);
const names = Object.keys(METHODS);
let current = names[0];

// ----- Method tabs -----
function renderMethod() {
  const m = METHODS[current];
  $("tabs").innerHTML = "";
  names.forEach((n) => {
    const b = document.createElement("button");
    b.className = "tab";
    b.textContent = n;
    b.setAttribute("role", "tab");
    b.setAttribute("aria-selected", n === current);
    b.onclick = () => selectMethod(n);
    $("tabs").appendChild(b);
  });
  $("method-card").innerHTML = `
    <h3>${current}</h3>
    <div class="stats">
      <div class="stat">Ratio<b>1:${m.ratio}</b></div>
      <div class="stat">Grind<b>${m.grind}</b></div>
      <div class="stat">Water temp<b>${m.temp}</b></div>
      <div class="stat">Brew time<b>${m.time}</b></div>
    </div>
    <ol>${m.steps.map((s) => `<li>${s.text}</li>`).join("")}</ol>`;
  $("timer-method").textContent = `Method: ${current}`;
  $("calc-method").value = current;
  calc("coffee");
  resetTimer();
}

function selectMethod(n) {
  current = n;
  renderMethod();
}

// ----- Calculator -----
names.forEach((n) => {
  const o = document.createElement("option");
  o.value = o.textContent = n;
  $("calc-method").appendChild(o);
});
$("calc-method").onchange = (e) => selectMethod(e.target.value);

function calc(mode) {
  const r = METHODS[current].ratio;
  const coffee = $("calc-coffee"), water = $("calc-water");
  if (mode === "coffee") water.value = Math.round(+coffee.value * r);
  else coffee.value = (+water.value / r).toFixed(1);
  $("calc-result").textContent =
    `${coffee.value} g coffee + ${water.value} ml water (1:${r})`;
}
document.querySelectorAll("[data-mode]").forEach((b) => (b.onclick = () => calc(b.dataset.mode)));

// ----- Timer -----
let tick = null, elapsed = 0;
const fmt = (s) => `${Math.floor(s / 60)}:${String(s % 60).padStart(2, "0")}`;

function updateTimer() {
  $("clock").textContent = fmt(elapsed);
  const steps = METHODS[current].steps;
  const active = [...steps].reverse().find((s) => elapsed >= s.t) || steps[0];
  $("timer-step").textContent = active.text;
  if (elapsed >= steps[steps.length - 1].t) stopTimer(true);
}

function stopTimer(done) {
  clearInterval(tick);
  tick = null;
  $("t-start").textContent = done ? "Start again" : "Resume";
  if (done && navigator.vibrate) navigator.vibrate(200);
}

function resetTimer() {
  clearInterval(tick);
  tick = null;
  elapsed = 0;
  $("clock").textContent = "0:00";
  $("timer-step").textContent = "Press start when you begin pouring.";
  $("t-start").textContent = "Start";
}

$("t-start").onclick = () => {
  if (tick) return stopTimer(false);
  if (elapsed >= METHODS[current].steps.slice(-1)[0].t) elapsed = 0;
  $("t-start").textContent = "Pause";
  updateTimer();
  tick = setInterval(() => { elapsed++; updateTimer(); }, 1000);
};
$("t-reset").onclick = resetTimer;

$("year").textContent = new Date().getFullYear();
renderMethod();
