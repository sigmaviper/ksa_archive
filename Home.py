import streamlit as st
import pandas as pd
import json
import sidebar

st.set_page_config(
    page_title="Home",
    page_icon="🗂️",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        "About": "This app is an archive of kicksomeacid's curiouscat, created to search and filter responses. All content and images used in the application belong to their respective owners and the creater of this app does not claim any right over them.",
        "Report a Bug": "https://github.com/sigmaviper/ksaarchive/issues",
    },
)

filter_map = {
    "Headcanons": "headcanon",
    "Losin' End": "le",
    "DNA (None of this is a coincidence)": "dna",
    "Contra Spem Spero": "css",
    "[Series] The Nearness of You": "noy",
    "[Series] A Calendar Year": "cy",
    "you know I have no chingu!": "chingu",
    "[Series] If you love me, let me know": "iylm",
    "skillshare (use code: FUCKOFF for one month free!)": "skillshare",
}


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def increaseIndexCount(total_values):
    if st.session_state["count"] < total_values:
        st.session_state["count"] += 10


def filterChanged(search_phrase, dropdown_values, sort_order):
    if (
        st.session_state["search_phrase"] != search_phrase
        or st.session_state["dropdown_values"] != dropdown_values
        or st.session_state["sort_order"] != sort_order
    ):
        return True
    return False


def setSessionStateValues():
    st.session_state["count"] = 10
    st.session_state["search_phrase"] = None
    st.session_state["dropdown_values"] = None
    st.session_state["sort_order"] = None
    st.session_state["indices"] = None


def resetSessionStateValues(search_phrase, dropdown_values, sort_order, filter_changed):

    if st.session_state["search_phrase"] != search_phrase:
        st.session_state["search_phrase"] = search_phrase

    if st.session_state["dropdown_values"] != dropdown_values:
        st.session_state["dropdown_values"] = dropdown_values

    if st.session_state["sort_order"] != sort_order:
        st.session_state["sort_order"] = sort_order

    if filter_changed:
        st.session_state["count"] = 10


def getPageData(filters, data):
    search_phrase, dropdown_values, sort_order = filters[0], filters[1], filters[2]
    indices = data.index.tolist()

    if dropdown_values:
        indices = [
            index
            for index, _ in data.iterrows()
            for fic in dropdown_values
            if filter_map[fic] in data["Keywords"][index]
        ]

    if search_phrase:
        if dropdown_values:
            indices = [
                index
                for index in indices
                if (
                    search_phrase.lower() in str(data["Message"][index]).lower()
                    or search_phrase.lower() in str(data["Reply"][index]).lower()
                )
            ]
        else:
            indices = [
                index
                for index, _ in data.iterrows()
                if (
                    search_phrase.lower() in str(data["Message"][index]).lower()
                    or search_phrase.lower() in str(data["Reply"][index]).lower()
                )
            ]

    if sort_order and sort_order == "Older Replies First":
        indices = indices[::-1]
    return indices


def loadPage(data):
    # set column widths for search filters
    search_filter, dropdown_filter, sort_filter = st.columns([0.5, 0.35, 0.15])

    # display filters
    search_phrase = search_filter.text_input("Search")
    dropdown_values = dropdown_filter.multiselect(
        "By Fic Title",
        filter_map.keys(),
    )
    sort_order = sort_filter.selectbox(
        "Sort By", ["Latest Replies First", "Older Replies First"]
    )

    # get indices of data to display
    indices = []
    # if filter didnt change, keep the same indices and keep using that.
    filter_changed = filterChanged(search_phrase, dropdown_values, sort_order)

    if not filter_changed:
        indices = st.session_state["indices"]
    # if filter changed, reset session count, indices
    if filter_changed:
        resetSessionStateValues(search_phrase, dropdown_values, sort_order, True)
        indices = getPageData([search_phrase, dropdown_values, sort_order], data)
        st.session_state["indices"] = indices

    index_count = 0
    total_indices = len(indices)

    # display each Message and Reply
    for index in indices:
        message = str(data["Message"][index]).strip()
        reply = str(data["Reply"][index])
        media = str(data["Media"][index])
        time = str(data["Time"][index])
        reply_id = data["ID"][index]
        link = f"[Open in CuriousCat](https://curiouscat.live/kicksomeacid/post/{reply_id})"

        if media != "nan":
            media = json.loads(str(data["Media"][index]))

        with st.expander(message, expanded=True):
            author_profile, author_reply = st.columns([0.1, 0.9])

            author_profile.image("images/kicksomeacid_avatar.jpg")

            if reply != "nan":
                reply = "> " + reply.replace("\n", "\n> ")
                author_reply.markdown(reply)

            if type(media) != str:
                author_reply.image(media["img"])

            author_reply.write("")  # empty line

            date_column, cc_link_column = author_reply.columns([0.8, 0.2])

            date_column.caption("Posted on " + time)
            cc_link_column.caption(link)

        index_count += 1

        if index_count == st.session_state["count"] or index_count + 1 == total_indices:
            break

    if len(indices) == 0:
        st.info("No results found", icon="😞")
    elif len(indices) > st.session_state["count"]:
        st.button("Show More", on_click=increaseIndexCount(total_indices))
    else:
        st.info(
            "You've reached the end! Change the filter to view other messages.",
        )


if __name__ == "__main__":

    local_css("styles/home.css")

    if "count" not in st.session_state:
        st.toast(
            "Data isn't updated in real time. It will be updated every weekend.",
            icon="ℹ",
        )
        setSessionStateValues()

    QnA = pd.read_csv("ksaanswers.csv")
    total_entries = len(QnA)

    customItems = {
        "About": [
            "This app is an archive of kicksomeacid's curiouscat.",
            """You can use the search functionality to look for specific phrases in the questions and replies. 
                    A filter can be selected to get results from a particular fic, and you can sort the results by date.""",
            f"Please be patient as there are {total_entries} questions in total.",
        ]
    }

    sidebar.renderSidebar(st, customItems)
    loadPage(QnA)
