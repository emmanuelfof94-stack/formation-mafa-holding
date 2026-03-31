
// ── Navigation Overlay ──────────────────────────────────
var _currentModule = null;

function openModule(mid) {
  var overlay = document.getElementById('overlay-' + mid);
  overlay.classList.add('open');
  overlay.scrollTop = 0;
  document.body.style.overflow = 'hidden';
  _currentModule = mid;
  showModuleTab(mid, 'cours');
}

function closeModule() {
  if (_currentModule) {
    document.getElementById('overlay-' + _currentModule).classList.remove('open');
    document.body.style.overflow = '';
    _currentModule = null;
  }
}

function showModuleTab(moduleId, tabName) {
  var overlay = document.getElementById('overlay-' + moduleId);
  if (!overlay) return;
  overlay.querySelectorAll('.tab-section').forEach(function(s) { s.style.display = 'none'; });
  var tab = document.getElementById('tab-' + moduleId + '-' + tabName);
  if (tab) tab.style.display = 'block';
  overlay.scrollTo({ top: 0, behavior: 'smooth' });
  var bar = overlay.querySelector('.module-tabs-clean');
  if (bar) {
    bar.querySelectorAll('[data-tab]').forEach(function(btn) {
      btn.classList.remove('active-red');
    });
    var active = bar.querySelector('[data-tab="' + tabName + '"]');
    if (active) active.classList.add('active-red');
  }
}

// Fermer avec Échap
document.addEventListener('keydown', function(e) {
  if (e.key === 'Escape') closeModule();
});

// ── Fonctions Quiz ──────────────────────────────────────


// ══════════════════════════════════════════════
// NAVIGATION PRINCIPALE — Formation Complete
// ══════════════════════════════════════════════













/* fragment supprimé */


/* ── Quiz M4 — OM Business ── */
let scoresM4 = { q1:null, q2:null, q3:null, q4:null, q5:null };
function answerM4(el, qid, correct, feedback) {
  const block = document.getElementById(qid);
  if (block.querySelector('.correct') || block.querySelector('.incorrect')) return;
  block.querySelectorAll('.quiz-option').forEach(o => o.classList.add('disabled'));
  el.classList.add(correct ? 'correct' : 'incorrect');
  const fb = document.getElementById('fb-' + qid);
  fb.textContent = (correct ? '✅ ' : '❌ ') + feedback;
  fb.className = 'quiz-feedback show ' + (correct ? 'fb-correct' : 'fb-incorrect');
  scoresM4[qid] = correct;
  const total = Object.values(scoresM4).filter(v => v === true).length;
  const answered = Object.values(scoresM4).filter(v => v !== null).length;
  var s4 = total + ' <span style="font-size:16px;color:#888">/ 5</span>';
  ['m4-score-display','m4-score-display-r'].forEach(function(id){var e=document.getElementById(id);if(e)e.innerHTML=s4;});
  ['m4-prog-label','m4-prog-label-r'].forEach(function(id){var e=document.getElementById(id);if(e)e.textContent=answered+' / 5';});
  var f4=document.getElementById('m4-prog-fill');if(f4)f4.style.width=(answered/5*100)+'%';
}

/* ── Quiz M5 — Agent & Superviseur ── */
let scoresM5 = { q1:null, q2:null, q3:null, q4:null, q5:null };
function answerM5(el, qid, correct, feedback) {
  const block = document.getElementById(qid);
  if (block.querySelector('.correct') || block.querySelector('.incorrect')) return;
  block.querySelectorAll('.quiz-option').forEach(o => o.classList.add('disabled'));
  el.classList.add(correct ? 'correct' : 'incorrect');
  const fb = document.getElementById('fb-' + qid);
  fb.textContent = (correct ? '✅ ' : '❌ ') + feedback;
  fb.className = 'quiz-feedback show ' + (correct ? 'fb-correct' : 'fb-incorrect');
  scoresM5[qid] = correct;
  const total = Object.values(scoresM5).filter(v => v === true).length;
  const answered = Object.values(scoresM5).filter(v => v !== null).length;
  document.getElementById('m5-score-display').innerHTML = total + ' <span>/ 5</span>';
  document.getElementById('m5-prog-label').textContent = answered + ' / 5';
  document.getElementById('m5-prog-fill').style.width = (answered / 5 * 100) + '%';
}

/* ── Quiz M1 — Call Center ── */
let scoresM1 = { q1:null, q2:null, q3:null, q4:null, q5:null };



function scrollTo(id) {
  setTimeout(() => {
    const el = document.getElementById(id);
    if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }, 100);
}

function answerM1(el, qid, correct, feedback) {
  const block = document.getElementById(qid);
  if (block.querySelector('.correct') || block.querySelector('.incorrect')) return;
  const opts = block.querySelectorAll('.quiz-option');
  opts.forEach(o => o.classList.add('disabled'));
  el.classList.add(correct ? 'correct' : 'incorrect');
  const fb = document.getElementById('fb-' + qid);
  fb.textContent = (correct ? '✅ ' : '❌ ') + feedback;
  fb.className = 'quiz-feedback show ' + (correct ? 'fb-correct' : 'fb-incorrect');
  scoresM1[qid] = correct;
  updateScoreM1();
}

function updateScoreM1() {
  const total = Object.values(scoresM1).filter(v => v === true).length;
  const answered = Object.values(scoresM1).filter(v => v !== null).length;
  document.getElementById('m1-score-display').innerHTML = total + ' <span>/ 5</span>';
  document.getElementById('m1-prog-label').textContent = answered + ' / 5';
  document.getElementById('m1-prog-fill').style.width = (answered / 5 * 100) + '%';
}

/* ── Quiz M2 — Back Office ── */
let scoresM2 = { q1:null, q2:null, q3:null, q4:null, q5:null };
function answerM2(el, qid, correct, feedback) {
  const block = document.getElementById(qid);
  if (block.querySelector('.correct') || block.querySelector('.incorrect')) return;
  block.querySelectorAll('.quiz-option').forEach(o => o.classList.add('disabled'));
  el.classList.add(correct ? 'correct' : 'incorrect');
  const fb = document.getElementById('fb-' + qid);
  fb.textContent = (correct ? '✅ ' : '❌ ') + feedback;
  fb.className = 'quiz-feedback show ' + (correct ? 'fb-correct' : 'fb-incorrect');
  scoresM2[qid] = correct;
  updateScoreM2();
}
function updateScoreM2() {
  const total = Object.values(scoresM2).filter(v => v === true).length;
  const answered = Object.values(scoresM2).filter(v => v !== null).length;
  document.getElementById('m2-score-display').innerHTML = total + ' <span>/ 5</span>';
  document.getElementById('m2-prog-label').textContent = answered + ' / 5';
  document.getElementById('m2-prog-fill').style.width = (answered / 5 * 100) + '%';
}

/* ── Quiz M3 — Inspecteur ── */
let scoresM3 = { q1:null, q2:null, q3:null, q4:null, q5:null, q6:null };
function answerM3(el, qid, correct, feedback) {
  const block = document.getElementById(qid);
  if (block.querySelector('.correct') || block.querySelector('.incorrect')) return;
  block.querySelectorAll('.quiz-option').forEach(o => o.classList.add('disabled'));
  el.classList.add(correct ? 'correct' : 'incorrect');
  const fb = document.getElementById('fb-' + qid);
  fb.textContent = (correct ? '✅ ' : '❌ ') + feedback;
  fb.className = 'quiz-feedback show ' + (correct ? 'fb-correct' : 'fb-incorrect');
  scoresM3[qid] = correct;
  const total = Object.values(scoresM3).filter(v => v === true).length;
  const answered = Object.values(scoresM3).filter(v => v !== null).length;
  document.getElementById('m3-score-display').innerHTML = total + ' <span>/ 6</span>';
  document.getElementById('m3-prog-label').textContent = answered + ' / 6';
  document.getElementById('m3-prog-fill').style.width = (answered / 6 * 100) + '%';
}

