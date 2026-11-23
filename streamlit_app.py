import re

import streamlit as st


st.set_page_config(page_title="Why Are You Happy?", page_icon="🔍", layout="centered")

PEOPLE = [
    {
        "name": "Eric",
        "emotion": "worried",
        "reason": "Because he lost his homework.",
        "blank": "reason",
    },
    {
        "name": "Sujin",
        "emotion": "sad",
        "reason": "Because she dropped her ice cream.",
        "blank": "emotion",
    },
    {
        "name": "Minho",
        "emotion": "happy",
        "reason": "Because he got a nice present.",
        "blank": "reason",
    },
    {
        "name": "Yuna",
        "emotion": "tired",
        "reason": "Because she ran a long race.",
        "blank": "emotion",
    },
    {
        "name": "Kevin",
        "emotion": "angry",
        "reason": "Because his brother ate his cake.",
        "blank": "reason",
    },
]

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@600;700;800;900&display=swap');

    :root {
        --page-bg: #fff8ee;
        --ink: #4a4458;
    }

    html, body, [data-testid="stAppViewContainer"], .stApp {
        background: var(--page-bg);
        color: var(--ink);
        font-family: "Nunito", "Arial Rounded MT Bold", "Trebuchet MS", sans-serif;
        font-weight: 700;
    }

    [data-testid="stHeader"], footer, #MainMenu, .stDeployButton {
        display: none !important;
    }

    .block-container {
        max-width: 900px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    h1, h2, h3, p, label, .stMarkdown {
        color: var(--ink);
        font-family: "Nunito", "Arial Rounded MT Bold", "Trebuchet MS", sans-serif;
    }

    h1 {
        text-align: center;
        font-size: clamp(2.2rem, 6vw, 3.4rem) !important;
        font-weight: 900 !important;
        margin: 0.4rem 0 2rem !important;
    }

    div.stButton > button {
        min-height: 3.4rem;
        border: 3px solid white;
        border-radius: 22px;
        color: var(--ink);
        font-family: "Nunito", "Arial Rounded MT Bold", "Trebuchet MS", sans-serif;
        font-size: 1.12rem;
        font-weight: 900;
        box-shadow: 0 5px 0 rgba(74, 68, 88, 0.14);
        transition: transform 120ms ease, box-shadow 120ms ease;
    }

    div.stButton > button:hover {
        color: var(--ink);
        border-color: white;
        transform: translateY(-2px);
        box-shadow: 0 7px 0 rgba(74, 68, 88, 0.14);
    }

    div.stButton > button:active {
        transform: translateY(2px);
        box-shadow: 0 2px 0 rgba(74, 68, 88, 0.14);
    }

    .st-key-student_a div.stButton > button { background: #cfe8ff; }
    .st-key-student_b div.stButton > button { background: #ffd6e0; }
    .st-key-check_answers div.stButton > button { background: #d4f5d9; }
    .st-key-try_again div.stButton > button { background: #fff3b8; }
    .st-key-go_back div.stButton > button { background: #e4d9ff; }

    .warning-box {
        margin: 0.4rem 0 1.7rem;
        padding: 1rem 1.2rem;
        border: 4px dashed #ef5350;
        border-radius: 20px;
        background: #fff0ef;
        color: #d93636;
        text-align: center;
        font-size: clamp(1.2rem, 4vw, 1.8rem);
        font-weight: 900;
        animation: pulse 1.5s ease-in-out infinite;
    }

    @keyframes pulse {
        0%, 100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(239, 83, 80, 0.2); }
        50% { transform: scale(1.015); box-shadow: 0 0 0 8px rgba(239, 83, 80, 0); }
    }

    .st-key-card_0, .st-key-card_1, .st-key-card_2,
    .st-key-card_3, .st-key-card_4 {
        padding: 1rem 1.1rem 0.8rem;
        margin-bottom: 1rem;
        border: 4px solid white;
        border-radius: 24px;
        box-shadow: 0 7px 0 rgba(74, 68, 88, 0.12);
    }
    .st-key-card_0 { background: #ffd6e0; }
    .st-key-card_1 { background: #cfe8ff; }
    .st-key-card_2 { background: #fff3b8; }
    .st-key-card_3 { background: #d4f5d9; }
    .st-key-card_4 { background: #e4d9ff; }

    .sentence {
        padding: 0.55rem 0.7rem;
        border-radius: 13px;
        background: rgba(255, 255, 255, 0.68);
        font-size: 1.04rem;
        font-weight: 800;
        line-height: 1.5;
    }

    .sentence-label {
        font-weight: 900;
    }

    [data-testid="stTextInput"] input {
        min-height: 2.45rem;
        border: 2px solid rgba(74, 68, 88, 0.2);
        border-radius: 12px;
        background: white;
        color: var(--ink);
        font-family: "Nunito", "Arial Rounded MT Bold", "Trebuchet MS", sans-serif;
        font-size: 1rem;
        font-weight: 800;
    }

    .answer-feedback {
        padding: 0.25rem 0.7rem 0.5rem;
        font-size: 1.05rem;
        font-weight: 900;
    }

    .score {
        margin: 1rem 0 1.4rem;
        padding: 0.9rem;
        border-radius: 18px;
        background: white;
        text-align: center;
        font-size: 1.5rem;
        font-weight: 900;
        box-shadow: 0 5px 0 rgba(74, 68, 88, 0.1);
    }

    @media (max-width: 600px) {
        .block-container { padding: 1rem 0.8rem 2rem; }
        .st-key-card_0, .st-key-card_1, .st-key-card_2,
        .st-key-card_3, .st-key-card_4 { padding: 0.7rem; }
        .sentence { font-size: 0.92rem; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def normalize_answer(text: str) -> str:
    text = re.sub(r"[.!?]", "", text)
    return " ".join(text.casefold().split())


def select_student(student: str) -> None:
    st.session_state.student = student
    st.session_state.screen = "activity"
    st.session_state.checked = False


def check_answers() -> None:
    student = st.session_state.student
    results = []
    for index, person in enumerate(PEOPLE):
        blank = person["blank"]
        if student == "B":
            blank = "emotion" if blank == "reason" else "reason"
        expected = person["emotion"] if blank == "emotion" else person["reason"][len("Because ") :]
        key = f"{student}_{'e' if blank == 'emotion' else 'r'}_{index}"
        results.append(normalize_answer(st.session_state.get(key, "")) == normalize_answer(expected))
    st.session_state.results = results
    st.session_state.checked = True


def try_again() -> None:
    student = st.session_state.student
    for index, person in enumerate(PEOPLE):
        blank = person["blank"]
        if student == "B":
            blank = "emotion" if blank == "reason" else "reason"
        key = f"{student}_{'e' if blank == 'emotion' else 'r'}_{index}"
        st.session_state[key] = ""
    st.session_state.checked = False
    st.session_state.results = []


def go_back() -> None:
    st.session_state.screen = "home"
    st.session_state.checked = False
    st.session_state.results = []


if "screen" not in st.session_state:
    st.session_state.screen = "home"
if "checked" not in st.session_state:
    st.session_state.checked = False
if "results" not in st.session_state:
    st.session_state.results = []


if st.session_state.screen == "home":
    st.title("🔍 Why Are You Happy? 🔍")
    left, right = st.columns(2, gap="large")
    with left:
        st.button(
            "Student A",
            key="student_a",
            on_click=select_student,
            args=("A",),
            use_container_width=True,
        )
    with right:
        st.button(
            "Student B",
            key="student_b",
            on_click=select_student,
            args=("B",),
            use_container_width=True,
        )
else:
    st.markdown(
        '<div class="warning-box">🚫 Do NOT show your screen to your partner! 🚫</div>',
        unsafe_allow_html=True,
    )
    student = st.session_state.student

    for index, person in enumerate(PEOPLE):
        blank = person["blank"]
        if student == "B":
            blank = "emotion" if blank == "reason" else "reason"

        with st.container(key=f"card_{index}"):
            emotion_key = f"{student}_e_{index}"
            reason_key = f"{student}_r_{index}"

            if blank == "emotion":
                before, field, after = st.columns([5.4, 1.4, 0.25], gap="small")
                with before:
                    st.markdown(
                        f'<div class="sentence"><span class="sentence-label">Q:</span> '
                        f'Why is {person["name"]}</div>',
                        unsafe_allow_html=True,
                    )
                with field:
                    st.text_input(
                        "Emotion",
                        key=emotion_key,
                        label_visibility="collapsed",
                        placeholder="emotion",
                    )
                with after:
                    st.markdown('<div class="sentence">?</div>', unsafe_allow_html=True)
            else:
                before, answer, after = st.columns([5.4, 1.4, 0.25], gap="small")
                with before:
                    st.markdown(
                        f'<div class="sentence"><span class="sentence-label">Q:</span> '
                        f'Why is {person["name"]}</div>',
                        unsafe_allow_html=True,
                    )
                with answer:
                    st.markdown(
                        f'<div class="sentence">{person["emotion"]}</div>',
                        unsafe_allow_html=True,
                    )
                with after:
                    st.markdown('<div class="sentence">?</div>', unsafe_allow_html=True)

            if blank == "reason":
                label, because, field, period = st.columns([0.45, 1.05, 3.8, 0.2], gap="small")
                with label:
                    st.markdown('<div class="sentence sentence-label">A:</div>', unsafe_allow_html=True)
                with because:
                    st.markdown('<div class="sentence">Because</div>', unsafe_allow_html=True)
                with field:
                    st.text_input(
                        "Reason",
                        key=reason_key,
                        label_visibility="collapsed",
                        placeholder="type the reason",
                    )
                with period:
                    st.markdown('<div class="sentence">.</div>', unsafe_allow_html=True)
            else:
                st.markdown(
                    f'<div class="sentence"><span class="sentence-label">A:</span> '
                    f'{person["reason"]}</div>',
                    unsafe_allow_html=True,
                )

            if st.session_state.checked:
                if st.session_state.results[index]:
                    st.markdown(
                        '<div class="answer-feedback" style="color:#218838">⭕ Great!</div>',
                        unsafe_allow_html=True,
                    )
                else:
                    st.markdown(
                        '<div class="answer-feedback" style="color:#d93636">'
                        '❌ Ask your partner again!</div>',
                        unsafe_allow_html=True,
                    )

    check_col, again_col, back_col = st.columns(3, gap="small")
    with check_col:
        st.button(
            "✅ Check Answers",
            key="check_answers",
            on_click=check_answers,
            use_container_width=True,
        )
    with again_col:
        st.button(
            "🔄 Try Again",
            key="try_again",
            on_click=try_again,
            use_container_width=True,
        )
    with back_col:
        st.button(
            "↩ Go Back",
            key="go_back",
            on_click=go_back,
            use_container_width=True,
        )

    if st.session_state.checked:
        score = sum(st.session_state.results)
        score_text = "🎉 Perfect!" if score == len(PEOPLE) else f"⭐ {score} / {len(PEOPLE)}"
        st.markdown(f'<div class="score">{score_text}</div>', unsafe_allow_html=True)
