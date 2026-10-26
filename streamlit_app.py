import streamlit as st
from data import NUMBER_QUESTIONS, SHAPE_QUESTIONS, ALPHABET_QUESTIONS
from shapes import get_shape_svg, SHAPE_LABELS

# ── Page config ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Pattern Master — Logical Reasoning Tutor",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Global CSS ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Outfit', sans-serif !important;
}

/* Dark background */
.stApp {
    background: linear-gradient(135deg, #0a0a1a 0%, #0f0c29 50%, #1a1040 100%);
    background-attachment: fixed;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: rgba(15, 12, 41, 0.95) !important;
    border-right: 1px solid rgba(255,255,255,0.08);
}

/* Hide default Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1.5rem !important; padding-bottom: 3rem !important; }

/* ── Question card ── */
.q-card {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 16px;
    padding: 1.4rem 1.5rem;
    margin-bottom: 1.2rem;
    backdrop-filter: blur(10px);
    transition: border-color 0.3s;
}
.q-card:hover { border-color: rgba(168,85,247,0.3); }
.q-card.answered { border-color: rgba(34,197,94,0.3); background: rgba(34,197,94,0.04); }

.q-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.8rem;
}
.q-num { font-size: 0.72rem; font-weight: 700; color: #475569; text-transform: uppercase; letter-spacing: 0.05em; }

.badge {
    font-size: 0.68rem; font-weight: 700;
    padding: 0.2rem 0.65rem; border-radius: 50px;
    text-transform: uppercase; letter-spacing: 0.05em;
}
.badge-easy   { background: rgba(34,197,94,0.15);  color: #22c55e; }
.badge-medium { background: rgba(251,191,36,0.15); color: #fbbf24; }
.badge-hard   { background: rgba(249,115,22,0.15); color: #f97316; }

.q-text { font-size: 1.55rem; font-weight: 800; letter-spacing: 0.06em; color: #f1f5f9; margin-bottom: 0.3rem; }
.q-label { font-size: 0.82rem; color: #94a3b8; margin-bottom: 1rem; }

/* sequence row */
.seq-row {
    display: flex; align-items: center; gap: 0.6rem; flex-wrap: wrap;
    padding: 0.8rem; background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.08); border-radius: 10px; margin-bottom: 1rem;
}
.seq-arrow { color: #475569; font-size: 1.1rem; }
.seq-q {
    width: 44px; height: 44px;
    border: 2px dashed #a855f7; border-radius: 8px;
    display: flex; align-items: center; justify-content: center;
    color: #a855f7; font-size: 1.3rem; font-weight: 800;
}

/* answer box */
.answer-box {
    background: rgba(6,182,212,0.08);
    border: 1px solid rgba(6,182,212,0.2);
    border-radius: 10px; padding: 1rem; margin-top: 0.8rem;
}
.ans-label { font-size: 0.68rem; font-weight: 700; text-transform: uppercase;
             letter-spacing: 0.1em; color: #06b6d4; margin-bottom: 0.35rem; }
.ans-value { font-size: 1.5rem; font-weight: 900; color: #f1f5f9; margin-bottom: 0.4rem;
             display: flex; align-items: center; gap: 0.4rem; }
.ans-expl  { font-size: 0.86rem; color: #94a3b8; line-height: 1.6; }
.ans-expl strong { color: #06b6d4; }

/* hero */
.hero-badge {
    display: inline-flex; align-items: center; gap: 0.4rem;
    background: rgba(168,85,247,0.15); border: 1px solid rgba(168,85,247,0.3);
    border-radius: 50px; padding: 0.35rem 1rem;
    font-size: 0.85rem; font-weight: 600; color: #a855f7;
    margin-bottom: 1rem;
}
.hero-title {
    font-size: 3.2rem; font-weight: 900; line-height: 1.1;
    color: #f1f5f9; margin-bottom: 0.8rem;
}
.hero-gradient {
    background: linear-gradient(135deg, #a855f7, #06b6d4, #f97316);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero-sub { font-size: 1.05rem; color: #94a3b8; margin-bottom: 2rem; max-width: 560px; }

/* stat cards */
.stat-row { display: flex; gap: 1.5rem; flex-wrap: wrap; margin-bottom: 2rem; }
.stat-card {
    background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08);
    border-radius: 14px; padding: 1.2rem 1.8rem; text-align: center; flex: 1; min-width: 130px;
}
.stat-num {
    font-size: 2.2rem; font-weight: 900;
    background: linear-gradient(135deg, #a855f7, #06b6d4);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
}
.stat-lbl { font-size: 0.78rem; color: #94a3b8; font-weight: 500; }

/* category cards */
.cat-card {
    background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.1);
    border-radius: 20px; padding: 2rem 1.8rem; text-align: center; cursor: pointer;
    transition: all 0.3s; position: relative; overflow: hidden;
}
.cat-card:hover { border-color: rgba(255,255,255,0.22); transform: translateY(-4px);
                  box-shadow: 0 12px 40px rgba(0,0,0,0.4); }
.cat-icon { font-size: 3rem; margin-bottom: 0.8rem; display: block; }
.cat-title { font-size: 1.35rem; font-weight: 800; color: #f1f5f9; margin-bottom: 0.5rem; }
.cat-desc  { font-size: 0.88rem; color: #94a3b8; line-height: 1.5; }

/* section header */
.sec-title { font-size: 2rem; font-weight: 900; color: #f1f5f9; margin-bottom: 0.3rem; }
.sec-sub   { font-size: 0.9rem; color: #94a3b8; margin-bottom: 1.5rem; }
.progress-pill {
    display: inline-flex; align-items: center; gap: 1rem;
    background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1);
    border-radius: 50px; padding: 0.6rem 1.4rem;
    font-size: 0.82rem; font-weight: 600; color: #94a3b8; margin-bottom: 1.5rem;
}
.progress-pill span { color: #f1f5f9; font-size: 0.95rem; }

/* Streamlit button overrides */
.stButton > button {
    font-family: 'Outfit', sans-serif !important;
    font-weight: 600 !important; border-radius: 10px !important;
    transition: all 0.2s !important;
}
div[data-testid="column"] .stButton > button {
    width: 100%;
}

/* shapes grid option buttons */
.shape-opt-grid {
    display: grid; grid-template-columns: repeat(4, 1fr); gap: 0.7rem; margin-bottom: 1rem;
}
.shape-opt-btn {
    background: rgba(255,255,255,0.04); border: 2px solid rgba(255,255,255,0.1);
    border-radius: 12px; padding: 0.75rem; cursor: pointer;
    display: flex; align-items: center; justify-content: center;
    transition: all 0.2s; aspect-ratio: 1;
}
.shape-opt-btn:hover { border-color: #a855f7; background: rgba(168,85,247,0.12);
                       box-shadow: 0 0 14px rgba(168,85,247,0.25); }
.shape-opt-btn.correct { border-color: #22c55e; background: rgba(34,197,94,0.15);
                          box-shadow: 0 0 14px rgba(34,197,94,0.3); }
.shape-opt-btn.wrong   { border-color: #f97316; background: rgba(249,115,22,0.15);
                          box-shadow: 0 0 14px rgba(249,115,22,0.3); }
</style>
""", unsafe_allow_html=True)


# ── Session state defaults ─────────────────────────────────────────────────
def init_state():
    if "page"       not in st.session_state: st.session_state.page       = "home"
    if "difficulty" not in st.session_state: st.session_state.difficulty = "All"
    if "answered"   not in st.session_state: st.session_state.answered   = {}
    if "selected"   not in st.session_state: st.session_state.selected   = {}

init_state()


# ── Helpers ────────────────────────────────────────────────────────────────
DIFF_COLORS = {"Easy": "🟢", "Medium": "🟡", "Hard": "🔴"}

def filter_questions(questions):
    d = st.session_state.difficulty
    return questions if d == "All" else [q for q in questions if q["difficulty"] == d]

def mark_answered(qid, choice=None):
    st.session_state.answered[qid] = True
    if choice is not None:
        st.session_state.selected[qid] = choice

def total_answered():
    return sum(1 for q in NUMBER_QUESTIONS + SHAPE_QUESTIONS + ALPHABET_QUESTIONS
               if st.session_state.answered.get(q["id"]))


# ── Shape sequence HTML builder ────────────────────────────────────────────
def shape_seq_html(sequence):
    parts = []
    for i, sh in enumerate(sequence):
        if sh == "?":
            parts.append('<div class="seq-q">?</div>')
        else:
            parts.append(get_shape_svg(sh, i % 6, 44))
        if i < len(sequence) - 1:
            parts.append('<span class="seq-arrow">→</span>')
    return f'<div class="seq-row">{"".join(parts)}</div>'


# ── Number / Alphabet question card ───────────────────────────────────────
def render_text_card(q, idx, section_key):
    qid        = q["id"]
    is_done    = st.session_state.answered.get(qid, False)
    chosen     = st.session_state.selected.get(qid)
    diff_dot   = DIFF_COLORS.get(q["difficulty"], "")
    badge_cls  = f'badge-{q["difficulty"].lower()}'

    card_cls = "q-card answered" if is_done else "q-card"

    st.markdown(f"""
    <div class="{card_cls}">
      <div class="q-header">
        <span class="q-num">Q{idx+1}</span>
        <span class="badge {badge_cls}">{diff_dot} {q['difficulty']}</span>
      </div>
      <div class="q-text">{q['question']}</div>
      <div class="q-label">What comes next?</div>
    </div>
    """, unsafe_allow_html=True)

    # Options as columns
    if not is_done:
        opts = q["options"]
        cols = st.columns(len(opts))
        for i, (col, opt) in enumerate(zip(cols, opts)):
            with col:
                if st.button(str(opt), key=f"{qid}-opt-{i}", use_container_width=True):
                    mark_answered(qid, str(opt))
                    st.rerun()

        if st.button("💡 Display Answer", key=f"{qid}-reveal", use_container_width=True,
                     type="secondary"):
            mark_answered(qid)
            st.rerun()
    else:
        # Show result colours
        opts = q["options"]
        cols = st.columns(len(opts))
        for i, (col, opt) in enumerate(zip(cols, opts)):
            with col:
                is_correct = str(opt) == str(q["answer"])
                is_chosen  = chosen == str(opt)
                if is_correct:
                    st.success(str(opt), icon="✅")
                elif is_chosen:
                    st.error(str(opt), icon="❌")
                else:
                    st.markdown(f'<div style="padding:0.5rem;text-align:center;color:#475569;">{opt}</div>',
                                unsafe_allow_html=True)

        st.markdown(f"""
        <div class="answer-box">
          <div class="ans-label">✨ Answer</div>
          <div class="ans-value">{q['answer']}</div>
          <div class="ans-expl">{q['explanation']}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")


# ── Shape question card ────────────────────────────────────────────────────
def render_shape_card(q, idx):
    qid       = q["id"]
    is_done   = st.session_state.answered.get(qid, False)
    chosen    = st.session_state.selected.get(qid)
    diff_dot  = DIFF_COLORS.get(q["difficulty"], "")
    badge_cls = f'badge-{q["difficulty"].lower()}'
    card_cls  = "q-card answered" if is_done else "q-card"

    seq_html = shape_seq_html(q["sequence"])

    st.markdown(f"""
    <div class="{card_cls}">
      <div class="q-header">
        <span class="q-num">Q{idx+1}</span>
        <span class="badge {badge_cls}">{diff_dot} {q['difficulty']}</span>
      </div>
      <div class="q-label">What shape comes next?</div>
      {seq_html}
    </div>
    """, unsafe_allow_html=True)

    opts = q["options"]

    if not is_done:
        # Shape option buttons as SVG grid
        cols = st.columns(len(opts))
        for i, (col, opt) in enumerate(zip(cols, opts)):
            with col:
                svg = get_shape_svg(opt, i, 52)
                label = SHAPE_LABELS.get(opt, opt)
                btn_html = f"""
                <form action="" method="get" style="margin:0;">
                  <button type="submit" name="__streamlit_shape_pick_{qid}" value="{opt}"
                    style="background:rgba(255,255,255,0.04);border:2px solid rgba(255,255,255,0.1);
                    border-radius:12px;padding:0.75rem;cursor:pointer;width:100%;
                    display:flex;align-items:center;justify-content:center;
                    transition:all 0.2s;" title="{label}">
                    {svg}
                  </button>
                </form>"""
                # Use st.button with SVG inside markdown + overlay trick
                st.markdown(f'<div style="text-align:center;">{svg}</div>', unsafe_allow_html=True)
                if st.button(label, key=f"{qid}-shp-{i}", use_container_width=True):
                    mark_answered(qid, opt)
                    st.rerun()

        if st.button("💡 Display Answer", key=f"{qid}-reveal", use_container_width=True,
                     type="secondary"):
            mark_answered(qid)
            st.rerun()
    else:
        # Show options with correct/wrong highlights
        cols = st.columns(len(opts))
        for i, (col, opt) in enumerate(zip(cols, opts)):
            with col:
                svg        = get_shape_svg(opt, i, 52)
                is_correct = opt == q["answer"]
                is_chosen  = chosen == opt
                if is_correct:
                    border = "#22c55e"; bg = "rgba(34,197,94,0.15)"; glyph = "✅"
                elif is_chosen:
                    border = "#f97316"; bg = "rgba(249,115,22,0.15)"; glyph = "❌"
                else:
                    border = "rgba(255,255,255,0.08)"; bg = "transparent"; glyph = ""
                st.markdown(f"""
                <div style="background:{bg};border:2px solid {border};border-radius:12px;
                  padding:0.75rem;text-align:center;">
                  {svg}<br>
                  <small style="color:#94a3b8;font-size:0.7rem;">{glyph}</small>
                </div>""", unsafe_allow_html=True)

        ans_svg = get_shape_svg(q["answer"], 0, 60)
        st.markdown(f"""
        <div class="answer-box">
          <div class="ans-label">✨ Answer</div>
          <div class="ans-value">{ans_svg}</div>
          <div class="ans-expl">{q['explanation']}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")


# ── Sidebar ────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="text-align:center;padding:1rem 0 1.5rem;">
      <div style="font-size:2.5rem;">🧠</div>
      <div style="font-size:1.3rem;font-weight:900;
        background:linear-gradient(135deg,#a855f7,#06b6d4);
        -webkit-background-clip:text;-webkit-text-fill-color:transparent;
        background-clip:text;">Pattern Master</div>
      <div style="font-size:0.75rem;color:#475569;margin-top:0.25rem;">Logical Reasoning Tutor</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📍 Navigate")
    pages = {
        "🏠 Home":              "home",
        "🔢 Number Series":    "numbers",
        "🔷 Shape Sequences":  "shapes",
        "🔤 Alphabet Sequences":"alphabets",
    }
    for label, key in pages.items():
        active = st.session_state.page == key
        btn_type = "primary" if active else "secondary"
        if st.button(label, key=f"nav-{key}", use_container_width=True, type=btn_type):
            st.session_state.page = key
            st.rerun()

    st.markdown("### 🎚️ Difficulty")
    diff = st.radio(
        "Filter by difficulty",
        ["All", "Easy", "Medium", "Hard"],
        index=["All","Easy","Medium","Hard"].index(st.session_state.difficulty),
        label_visibility="collapsed",
    )
    if diff != st.session_state.difficulty:
        st.session_state.difficulty = diff
        st.rerun()

    st.markdown("---")

    # Progress summary
    all_qs = NUMBER_QUESTIONS + SHAPE_QUESTIONS + ALPHABET_QUESTIONS
    done   = sum(1 for q in all_qs if st.session_state.answered.get(q["id"]))
    pct    = int(done / len(all_qs) * 100)
    st.markdown(f"### 📊 Progress")
    st.progress(pct / 100)
    st.markdown(f"<div style='color:#94a3b8;font-size:0.85rem;text-align:center;'>"
                f"{done} / {len(all_qs)} questions answered</div>", unsafe_allow_html=True)

    if done > 0:
        if st.button("↺ Reset All Progress", use_container_width=True):
            st.session_state.answered = {}
            st.session_state.selected = {}
            st.rerun()


# ══════════════════════════════════════════════════════════════════════════
#  PAGES
# ══════════════════════════════════════════════════════════════════════════

page = st.session_state.page

# ── HOME ──────────────────────────────────────────────────────────────────
if page == "home":
    st.markdown("""
    <div style="padding:1rem 0 0.5rem;">
      <div class="hero-badge">🎓 Logical Reasoning Tutor</div>
      <div class="hero-title">Train Your<br><span class="hero-gradient">Pattern Brain</span></div>
      <div class="hero-sub">
        Master logical reasoning through interactive puzzles.<br>
        Number series, shape sequences &amp; alphabet patterns — with instant, clear explanations.
      </div>
    </div>
    """, unsafe_allow_html=True)

    all_qs = NUMBER_QUESTIONS + SHAPE_QUESTIONS + ALPHABET_QUESTIONS
    done   = sum(1 for q in all_qs if st.session_state.answered.get(q["id"]))

    st.markdown(f"""
    <div class="stat-row">
      <div class="stat-card"><div class="stat-num">45</div><div class="stat-lbl">Total Questions</div></div>
      <div class="stat-card"><div class="stat-num">3</div><div class="stat-lbl">Pattern Types</div></div>
      <div class="stat-card"><div class="stat-num">3</div><div class="stat-lbl">Difficulty Levels</div></div>
      <div class="stat-card"><div class="stat-num">{done}</div><div class="stat-lbl">Completed</div></div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    def done_count(qs):
        return sum(1 for q in qs if st.session_state.answered.get(q["id"]))

    with c1:
        n_done = done_count(NUMBER_QUESTIONS)
        st.markdown(f"""
        <div class="cat-card">
          <span class="cat-icon">🔢</span>
          <div class="cat-title">Number Series</div>
          <div class="cat-desc">Arithmetic, Fibonacci, primes, factorials &amp; more.</div>
          <div style="margin-top:1rem;color:#a855f7;font-weight:700;">{n_done}/15 done</div>
        </div>""", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Start Numbers →", key="go-numbers", use_container_width=True, type="primary"):
            st.session_state.page = "numbers"; st.rerun()

    with c2:
        s_done = done_count(SHAPE_QUESTIONS)
        st.markdown(f"""
        <div class="cat-card">
          <span class="cat-icon">🔷</span>
          <div class="cat-title">Shape Sequences</div>
          <div class="cat-desc">Visual SVG patterns — alternating, growing &amp; repeating shapes.</div>
          <div style="margin-top:1rem;color:#f97316;font-weight:700;">{s_done}/15 done</div>
        </div>""", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Start Shapes →", key="go-shapes", use_container_width=True, type="primary"):
            st.session_state.page = "shapes"; st.rerun()

    with c3:
        a_done = done_count(ALPHABET_QUESTIONS)
        st.markdown(f"""
        <div class="cat-card">
          <span class="cat-icon">🔤</span>
          <div class="cat-title">Alphabet Sequences</div>
          <div class="cat-desc">Forward, reverse, skip &amp; interlaced letter patterns.</div>
          <div style="margin-top:1rem;color:#ec4899;font-weight:700;">{a_done}/15 done</div>
        </div>""", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Start Alphabets →", key="go-alphabets", use_container_width=True, type="primary"):
            st.session_state.page = "alphabets"; st.rerun()


# ── NUMBER SERIES ─────────────────────────────────────────────────────────
elif page == "numbers":
    filtered = filter_questions(NUMBER_QUESTIONS)
    done_f   = sum(1 for q in filtered if st.session_state.answered.get(q["id"]))

    st.markdown(f"""
    <div class="sec-title">🔢 Number Series</div>
    <div class="sec-sub">Find the pattern and predict the next number.</div>
    <div class="progress-pill">✅ Answered: <span>{done_f}/{len(filtered)}</span></div>
    """, unsafe_allow_html=True)

    if not filtered:
        st.info("No questions match the selected difficulty. Use the sidebar to change the filter.", icon="🔍")
    else:
        for i, q in enumerate(filtered):
            render_text_card(q, i, "numbers")


# ── SHAPE SEQUENCES ────────────────────────────────────────────────────────
elif page == "shapes":
    filtered = filter_questions(SHAPE_QUESTIONS)
    done_f   = sum(1 for q in filtered if st.session_state.answered.get(q["id"]))

    st.markdown(f"""
    <div class="sec-title">🔷 Shape Sequences</div>
    <div class="sec-sub">Study the visual pattern and choose what comes next.</div>
    <div class="progress-pill">✅ Answered: <span>{done_f}/{len(filtered)}</span></div>
    """, unsafe_allow_html=True)

    if not filtered:
        st.info("No questions match the selected difficulty. Use the sidebar to change the filter.", icon="🔍")
    else:
        for i, q in enumerate(filtered):
            render_shape_card(q, i)


# ── ALPHABET SEQUENCES ─────────────────────────────────────────────────────
elif page == "alphabets":
    filtered = filter_questions(ALPHABET_QUESTIONS)
    done_f   = sum(1 for q in filtered if st.session_state.answered.get(q["id"]))

    st.markdown(f"""
    <div class="sec-title">🔤 Alphabet Sequences</div>
    <div class="sec-sub">Crack the letter pattern and find the missing letter.</div>
    <div class="progress-pill">✅ Answered: <span>{done_f}/{len(filtered)}</span></div>
    """, unsafe_allow_html=True)

    if not filtered:
        st.info("No questions match the selected difficulty. Use the sidebar to change the filter.", icon="🔍")
    else:
        for i, q in enumerate(filtered):
            render_text_card(q, i, "alphabets")
