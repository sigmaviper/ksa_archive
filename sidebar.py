def renderSidebar(st, customItems={}):
    st.sidebar.subheader("About")
    if "About" in customItems.keys():
        for string in customItems["About"]:
            st.sidebar.info(string)

    st.sidebar.divider()

    st.sidebar.link_button(
        "Archive of Our Own",
        "https://archiveofourown.org/users/kicksomeacid/",
        use_container_width=True,
    )
    st.sidebar.link_button(
        "Zaqa", "https://zaqa.net/kicksomeacid", use_container_width=True
    )
    st.sidebar.link_button(
        "Twitter", "https://x.com/kicksomeacid", use_container_width=True
    )
    st.sidebar.link_button(
        "CuriousCat", "https://curiouscat.live/kicksomeacid", use_container_width=True
    )
