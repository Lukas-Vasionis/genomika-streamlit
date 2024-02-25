import streamlit as st


class DisTx:
    def __init__(self, text, align, font='sans serif'):
        self.text = text
        self.align = align
        self.font = font
        self.style = f"'text-align: {self.align}; font-family:{self.font}'"

    def get_text(self, html_class):
        element = st.markdown(
            f"<{html_class} style={self.style}>{self.text}</{html_class}>",
            unsafe_allow_html=True)
        return element



