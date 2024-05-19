import streamlit as st
import pandas as pd
import sidebar

st.set_page_config(
    page_title="Works",
    page_icon="📖",
    initial_sidebar_state="expanded",
    menu_items={
        "About": "This app is an archive of kicksomeacid's curiouscat, created to search and filter responses. All content and images used in the application belong to their respective owners and the creater of this app does not claim any right over them.",
        "Report a Bug": "https://github.com/sigmaviper/ksaarchive/issues",
    },
)

works = [
    "A Calendar Year",
    "The Nearness of You",
    "A flower for each time I think of you",
    "oxy(morons)",
    "DNA (None of this is a coincidence)",
    "Losin' End",
    "you know I have no chingu!",
    "Contra Spem Spero",
]


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def loadPage():
    cy_tab, noy_tab, iylm_tab, skillshare_tab, dna_tab, le_tab, chingu_tab, css_tab = (
        st.tabs(works)
    )

    with cy_tab:
        st.header(works[0])

        st.link_button(
            "_A Year Of Ice Cream, Art, and A Million Other Things_",
            "https://archiveofourown.org/works/28975386",
            use_container_width=True,
        )

        st.link_button(
            "_Another Year, and A Million More Things_",
            "https://archiveofourown.org/works/29781204",
            use_container_width=True,
        )

        st.link_button(
            "_Month by Month, Year to Year_",
            "https://archiveofourown.org/works/30215085",
            use_container_width=True,
        )

        st.link_button(
            "_Year by Year, Month to Month_",
            "https://archiveofourown.org/works/30900728",
            use_container_width=True,
        )

        st.link_button(
            "_Day, Month, Year_",
            "https://archiveofourown.org/works/32610025",
            use_container_width=True,
        )

        st.link_button(
            "_The Calendar Year_",
            "https://archiveofourown.org/works/31641092",
            use_container_width=True,
        )

        st.link_button(
            "_Calendar Year: Interludes_",
            "https://archiveofourown.org/works/34722703",
            use_container_width=True,
        )

    with noy_tab:
        st.header(works[1])

        with st.expander("Leave a memory / To keep me company"):

            st.subheader("Character Visuals")
            col1, col2 = st.columns([0.5, 0.5])
            col1.caption("_Jungkook_")
            col1.image("images/LAM_JK.jpeg")
            col2.caption("_Taehyung_")
            col2.image("images/LAM_Tae.jpeg")

            st.link_button(
                "Open in AO3",
                "https://archiveofourown.org/works/31793152",
                use_container_width=True,
            )

        with st.expander("I'll Be Seeing You"):
            st.subheader("Character Visuals")
            col1, col2 = st.columns([0.5, 0.5])
            col1.caption("_Jungkook_")
            col1.image("images/IBSY_JK.png")
            col2.caption("_Taehyung_")
            col2.image("images/IBSY_Tae.jpeg")

            st.link_button(
                "Open in AO3",
                "https://archiveofourown.org/works/33745558",
                use_container_width=True,
            )

    with iylm_tab:
        st.header(works[2])
        st.image("images/IYLM.jpeg")

        with st.expander("If you love me, let me know "):

            st.link_button(
                "Open in AO3",
                "https://archiveofourown.org/works/33001333",
                use_container_width=True,
            )

        with st.expander("Where all our tears are just from laughter"):
            st.image("images/IYLM_2.jpeg")

            st.link_button(
                "Open in AO3",
                "https://archiveofourown.org/works/43419048",
                use_container_width=True,
            )

    with skillshare_tab:
        st.header(works[3])
        st.image("images/skillshare.jpeg")

        with st.expander("skillshare (use code: FUCKOFF for one month free!)"):
            st.image("images/skillshare1.jpeg")

            st.link_button(
                "Open in AO3",
                "https://archiveofourown.org/works/35214496",
                use_container_width=True,
            )

        with st.expander("keep the heid!"):
            st.image("images/skillshare2.jpeg")

            st.link_button(
                "Open in AO3",
                "https://archiveofourown.org/works/55871308",
                use_container_width=True,
            )

    with dna_tab:
        st.header(works[4])
        st.image("images/DNA.jpeg")

        st.link_button(
            "Open in AO3",
            "https://archiveofourown.org/works/38922264",
            use_container_width=True,
        )

    with le_tab:
        st.header(works[5])
        st.image("images/LE.jpeg")

        st.link_button(
            "Open in AO3",
            "https://archiveofourown.org/works/38942775",
            use_container_width=True,
        )

    with chingu_tab:
        st.header(works[6])
        st.image("images/chingu.jpeg")

        st.link_button(
            "Open in AO3",
            "https://archiveofourown.org/works/43068831",
            use_container_width=True,
        )

    with css_tab:
        st.header(works[7])
        st.image("images/CSS.jpeg")

        st.link_button(
            "Open in AO3",
            "https://archiveofourown.org/works/55334401",
            use_container_width=True,
        )


if __name__ == "__main__":

    local_css("styles/style.css")

    st.markdown("# Works")

    customItems = {"About": ["This page contains links to KSA's works."]}

    sidebar.renderSidebar(st, customItems)
    loadPage()
