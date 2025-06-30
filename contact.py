import streamlit as st

def show_contact():
    st.title("Contact Me")

    st.markdown("### Mirko Balli")
    st.markdown("If you'd like to connect, collaborate, or have any questions, feel free to reach out.")



    # HTML + CSS per bottone personalizzato
    button_html = """
    <div style="text-align: left; margin-top: 1.5em;">
        <a href="https://www.linkedin.com/in/mirko-balli-06592012a/" target="_blank" style="
            display: inline-block;
            padding: 0.6em 1.2em;
            font-size: 16px;
            font-weight: 500;
            color: white;
            background-color: #0077b5;
            border: none;
            border-radius: 5px;
            text-decoration: none;
        ">
            Connect on LinkedIn
        </a>
    </div>
    """
    st.markdown(button_html, unsafe_allow_html=True)
    # Spazio verticale
    st.markdown("")
    st.markdown("---")
    st.caption("© 2025 – Intermarket Analysis App")