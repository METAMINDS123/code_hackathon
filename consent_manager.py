import streamlit as st
from datetime import datetime

def request_consent(scope: str, description: str) -> bool:
    """
    Ask user for explicit consent. Return True if accepted.
    """
    with st.expander(f"🔒 Consent Required: {scope}", expanded=True):
        st.write(description)
        give = st.checkbox(f"I give consent for: {scope}", key=scope)
        if give:
            log_consent(scope)
        return give

def log_consent(scope: str):
    if "consent_log" not in st.session_state:
        st.session_state.consent_log = []

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.consent_log.append(f"[{timestamp}] ✅ Consent granted: {scope}")
