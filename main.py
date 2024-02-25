import streamlit as st
from lib import svg_render
from lib import text_utils as tu
# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Genomika", page_icon="img/genomika_logo_trim.ico", layout="centered")

with st.container():
    svg_render.render_svg(svg_string=svg_render.load_to_svg_string("img/GenomikaLogo (1).svg"))

with st.container() as c:
    st.write('')
    st.write('')
    tu.DisTx("Your partner in cutting-edge scientific research", 'center',font='Source Sans Pro').get_text(html_class="H1")
    # st.write('')
    # tu.DisTx(
    #     """
    #     Contact us to find custom solutions for your needs in genetic research.
    #     """,
    #     'center', font="Source Sans Pro").get_text(html_class="H5")

st.write('')

c2,c_mid,c3 = st.columns([5 ,1,5])
with c2:
    svg_render.render_svg(svg_string=svg_render.load_to_svg_string("img/Genomika (1).svg"))
with c3:
    tu.DisTx(
        "Oops!",
        'center',
    font="Source Sans Pro").get_text(html_class="H2")

    tu.DisTx(
        """
        🧬 We accidentally encoded our website into DNA! 🚀 
        """,
        'center',
        font="Source Sans Pro").get_text(html_class="H5")
    tu.DisTx(
    "Help us decode the oldest data storage system!🕵️‍♂️<br><br>"
    "Join us at <span style='color: blue; text-decoration: underline; cursor: pointer;'>info@genomika.lt</span><br><br>",
    font="Source Sans Pro",
    align='center').get_text(html_class="div")

    tu.DisTx(
    "Let's unravel the code together! 🔍"
    "<b>#GenomikaDecode #TechAdventure</b>",
    align='center',
    font="Source Sans Pro"
    ).get_text(html_class="div")