
import streamlit as st
import base64
import textwrap

def render_svg(svg_string):
    """Renders the given svg string."""
    b64 = base64.b64encode(svg_string.encode('utf-8')).decode("utf-8")
    html = r'<img src="data:image/svg+xml;base64,%s"/>' % b64
    st.write(html, unsafe_allow_html=True)



def load_to_svg_string(svg_path):
    with open(svg_path,"r") as f:
        lines = f.readlines()
        svg_string=''.join(lines)
        return svg_string