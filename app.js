/* =====================================================================
   LOGICAL REASONING TUTOR — Main Application Logic
   ===================================================================== */

// ── State ──────────────────────────────────────────────────────────────────
const state = {
  currentPage: 'home',   // 'home' | 'numbers' | 'shapes' | 'alphabets'
  difficulty:  'all',    // 'all' | 'easy' | 'medium' | 'hard'
  answered:    {},       // { questionId: true }
};

// ── Persist state ──────────────────────────────────────────────────────────
function loadState() {
  try {
    const saved = JSON.parse(localStorage.getItem('lrt-state') || '{}');
    if (saved.difficulty) state.difficulty = saved.difficulty;
    if (saved.answered)   state.answered   = saved.answered;
  } catch (e) {}
}

function saveState() {
  localStorage.setItem('lrt-state', JSON.stringify({
    difficulty: state.difficulty,
    answered:   state.answered,
  }));
}

// ── Navigation ─────────────────────────────────────────────────────────────
function navigate(page) {
  state.currentPage = page;

  // Show correct page
  document.querySelectorAll('.page').forEach(function(p) {
    p.classList.remove('active');
  });
  document.getElementById('page-' + page).classList.add('active');

  // Highlight nav link
  document.querySelectorAll('.nav-links a').forEach(function(a) {
    a.classList.toggle('active', a.dataset.page === page);
  });

  window.scrollTo({ top: 0, behavior: 'smooth' });

  if (page !== 'home') renderSection(page);
  updateProgress();
}

// ── Difficulty Filter ──────────────────────────────────────────────────────
function setDifficulty(level) {
  state.difficulty = level;
  saveState();

  document.querySelectorAll('.diff-btn').forEach(function(btn) {
    btn.classList.toggle('active', btn.dataset.level === level);
  });

  if (state.currentPage !== 'home') {
    renderSection(state.currentPage);
  }
  updateProgress();
}

// ── Section Renderer ───────────────────────────────────────────────────────
function renderSection(section) {
  var grid = document.getElementById(section + '-grid');
  if (!grid) return;
  grid.innerHTML = '';

  var questions;
  if (section === 'numbers')        questions = numberQuestions;
  else if (section === 'shapes')    questions = shapeQuestions;
  else if (section === 'alphabets') questions = alphabetQuestions;
  else return;

  var filtered = state.difficulty === 'all'
    ? questions
    : questions.filter(function(q) { return q.difficulty === state.difficulty; });

  if (filtered.length === 0) {
    grid.innerHTML =
      '<div class="empty-state">' +
        '<span class="empty-icon">🔍</span>' +
        'No questions for <strong>' + state.difficulty + '</strong> difficulty.<br>' +
        'Try a different level.' +
      '</div>';
    updateProgress();
    return;
  }

  filtered.forEach(function(q, idx) {
    var card = buildCard(q, idx, section);
    grid.appendChild(card);
  });

  updateProgress();
}

// ── Card Builder ───────────────────────────────────────────────────────────
function buildCard(q, idx, section) {
  var card = document.createElement('div');
  var isAnswered = !!state.answered[q.id];
  card.className = 'question-card' + (isAnswered ? ' answered' : '');
  card.id = 'card-' + q.id;
  card.style.animationDelay = (idx * 0.06) + 's';

  var badgeClass = 'badge-' + q.difficulty;
  var badgeLabel = q.difficulty.charAt(0).toUpperCase() + q.difficulty.slice(1);
  var diffDot    = q.difficulty === 'easy' ? '🟢' : q.difficulty === 'medium' ? '🟡' : '🔴';

  // ── Question display
  var questionHTML = '';
  if (section === 'shapes') {
    questionHTML = buildShapeSequence(q);
  } else {
    questionHTML =
      '<div class="question-text">' + q.question + '</div>' +
      '<div class="question-label">What comes next?</div>';
  }

  // ── Options
  var optionsGridClass = section === 'shapes' ? 'options-grid options-grid--shapes' : 'options-grid';
  var optionsHTML = q.options.map(function(opt, i) {
    var isCorrect = isAnswered && String(opt) === String(q.answer);
    var optClass  = 'option-btn' + (section === 'shapes' ? ' option-btn--shape' : '') + (isCorrect ? ' correct' : '');
    var label     = section === 'shapes'
      ? getShapeSVG(opt, i, 44)   // pure SVG — no text label
      : opt;
    return '<button' +
      ' class="' + optClass + '"' +
      ' id="opt-' + q.id + '-' + i + '"' +
      ' data-qid="' + q.id + '"' +
      ' data-opt="' + opt + '"' +
      ' onclick="selectOption(this)"' +
      ' title="' + opt + '"' +
      (isAnswered ? ' disabled' : '') +
      '>' + label + '</button>';
  }).join('');

  // ── Answer display
  var answerDisplay = section === 'shapes'
    ? getShapeSVG(q.answer, 0, 56)   // pure SVG — no text name
    : q.answer;

  card.innerHTML =
    '<div class="card-top">' +
      '<span class="q-number">Q' + (idx + 1) + '</span>' +
      '<span class="difficulty-badge ' + badgeClass + '">' + diffDot + ' ' + badgeLabel + '</span>' +
    '</div>' +

    questionHTML +

    '<div class="' + optionsGridClass + '">' + optionsHTML + '</div>' +

    '<button' +
      ' class="btn btn-answer' + (isAnswered ? ' revealed' : '') + '"' +
      ' id="ans-btn-' + q.id + '"' +
      ' onclick="revealAnswer(\'' + q.id + '\', this)"' +
    '>' + (isAnswered ? '✅ Answer Shown' : '💡 Display Answer') + '</button>' +

    '<div class="answer-reveal' + (isAnswered ? ' show' : '') + '" id="reveal-' + q.id + '">' +
      '<div class="answer-box">' +
        '<div class="answer-label">✨ Answer</div>' +
        '<div class="answer-value" style="display:flex;align-items:center;gap:0.5rem;">' + answerDisplay + '</div>' +
        '<div class="explanation">' + q.explanation + '</div>' +
      '</div>' +
    '</div>';

  return card;
}

// ── Shape Sequence Builder ─────────────────────────────────────────────────
function buildShapeSequence(q) {
  var items = q.sequence.map(function(sh, i) {
    if (sh === '?') {
      return '<div class="shape-item"><div class="shape-q">?</div></div>';
    }
    return '<div class="shape-item">' + getShapeSVG(sh, i % 6, 40) + '</div>';
  });

  var withSeps = [];
  items.forEach(function(item, i) {
    withSeps.push(item);
    if (i < items.length - 1) withSeps.push('<span class="shape-sep">→</span>');
  });

  return '<div class="question-label" style="margin-bottom:0.5rem;">' + q.question + '</div>' +
         '<div class="shape-sequence">' + withSeps.join('') + '</div>';
}

// ── Option Selection ───────────────────────────────────────────────────────
function selectOption(btn) {
  var qid = btn.dataset.qid;

  // Guard: already answered
  if (state.answered[qid]) return;

  // Find the question
  var allQs = [].concat(numberQuestions, shapeQuestions, alphabetQuestions);
  var q = null;
  for (var i = 0; i < allQs.length; i++) {
    if (allQs[i].id === qid) { q = allQs[i]; break; }
  }
  if (!q) return;

  // Mark options correct/wrong
  var card = document.getElementById('card-' + qid);
  card.querySelectorAll('.option-btn').forEach(function(b) {
    b.disabled = true;
    if (String(b.dataset.opt) === String(q.answer)) {
      b.classList.add('correct');
    } else if (b === btn) {
      b.classList.add('wrong');
    }
  });

  // Auto-reveal
  revealAnswer(qid, document.getElementById('ans-btn-' + qid));
}

// ── Answer Reveal ──────────────────────────────────────────────────────────
function revealAnswer(qid, btn) {
  // Guard: already revealed
  if (state.answered[qid]) return;

  var reveal = document.getElementById('reveal-' + qid);
  if (!reveal) return;

  reveal.classList.add('show');
  btn.textContent = '✅ Answer Shown';
  btn.classList.add('revealed');

  // Disable all options
  var card = document.getElementById('card-' + qid);
  card.querySelectorAll('.option-btn').forEach(function(b) { b.disabled = true; });
  card.classList.add('answered');

  state.answered[qid] = true;
  saveState();
  updateProgress();
}

// ── Progress ───────────────────────────────────────────────────────────────
function updateProgress() {
  var allSections = {
    numbers:   numberQuestions,
    shapes:    shapeQuestions,
    alphabets: alphabetQuestions,
  };

  var totalAnswered = 0;

  Object.keys(allSections).forEach(function(sec) {
    var qs       = allSections[sec];
    var answered = qs.filter(function(q) { return !!state.answered[q.id]; }).length;
    totalAnswered += answered;

    // Home category card counter  e.g. "3/15"
    var homeEl = document.getElementById('progress-' + sec);
    if (homeEl) homeEl.textContent = answered + '/' + qs.length;

    // Section progress bar  e.g. numbers-done / numbers-total
    var doneEl  = document.getElementById(sec + '-done');
    var totalEl = document.getElementById(sec + '-total');
    if (doneEl && totalEl) {
      var filtered     = state.difficulty === 'all'
        ? qs
        : qs.filter(function(q) { return q.difficulty === state.difficulty; });
      var filteredDone = filtered.filter(function(q) { return !!state.answered[q.id]; }).length;
      doneEl.textContent  = filteredDone;
      totalEl.textContent = filtered.length;
    }
  });

  // Home "Completed Today" stat
  var totalAllEl = document.getElementById('progress-total-all');
  if (totalAllEl) totalAllEl.textContent = totalAnswered;
}

// ── Reset Section ──────────────────────────────────────────────────────────
function resetSection() {
  if (!confirm('Reset all answered questions in this section?')) return;

  var qs;
  if (state.currentPage === 'numbers')        qs = numberQuestions;
  else if (state.currentPage === 'shapes')    qs = shapeQuestions;
  else if (state.currentPage === 'alphabets') qs = alphabetQuestions;
  else return;

  qs.forEach(function(q) { delete state.answered[q.id]; });
  saveState();
  renderSection(state.currentPage);
}

// ── Init ───────────────────────────────────────────────────────────────────
function init() {
  loadState();

  // Activate the saved difficulty button
  document.querySelectorAll('.diff-btn').forEach(function(btn) {
    btn.classList.toggle('active', btn.dataset.level === state.difficulty);
  });

  navigate('home');
}

document.addEventListener('DOMContentLoaded', init);
