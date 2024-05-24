import streamlit as st
import requests

def get_google_results(query, api_key, cx, filetype=None):
    url = f"https://www.googleapis.com/customsearch/v1?q={query}"
    if filetype:
        url += f"+filetype:{filetype}"
    url += f"&key={api_key}&cx={cx}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            search_results = response.json()
            return search_results
        else:
            st.error(f"Error {response.status_code}: {response.json().get('error', {}).get('message', 'No detailed message')}")
            return None
    except Exception as e:
        st.error(f"Exception: {e}")
        return None

def handle_query(query, api_key, cx):
    study_keywords = ["study", "learn", "education", "tutorial", "course"]
    if any(keyword in query.lower() for keyword in study_keywords):
        return get_google_results(query, api_key, cx)
    else:
        if "amna akram" in query.lower():
            st.markdown("**Amna Akram**")
            st.write("Amna Akram is an expert in AI, Data Analysis, Machine Learning, Streamlit, and Web Development. She is the founder of Study Helper.")
            st.write("[Fiverr Profile](https://www.fiverr.com/amnaa21?public_mode=true)")
            st.write("[Upwork Profile](https://upwork.com/freelancers/amnaa37)")
            st.write("[GitHub Profile](https://github.com/amna2001-23)")
        else:
            st.write("Searching for related links and definitions...")
            return get_google_results(query, api_key, cx)

def search_pdfs(query, api_key, cx):
    st.write("Searching for PDFs...")
    search_results = get_google_results(query, api_key, cx, filetype="pdf")
    if search_results:
        items = search_results.get("items", [])
        if items:
            st.markdown("**PDF Results:**")
            for item in items:
                title = item.get("title")
                link = item.get("link")
                st.write(f"**Title:** {title}")
                st.write(f"**Link:** [Download PDF]({link})")
                st.write("---")
        else:
            st.write("No PDFs found.")
    else:
        st.write("Failed to retrieve search results.")

def main():
    st.set_page_config(page_title="Study Helper", page_icon=":books:", layout="wide")
    
    st.title("Study Helper")
    st.markdown("Welcome to the Study Helper!")

    page = st.sidebar.selectbox("Select a page", ["Chatbot", "PDFs"])

    if page == "Chatbot":
        st.markdown("### Chatbot")
        query = st.text_input("Enter your question:")
        if st.button("Ask"):
            predefined_response = handle_query(query, api_key, cx)
            if predefined_response:
                if isinstance(predefined_response, dict):
                    items = predefined_response.get("items", [])
                    if items:
                        st.markdown("**Search Results:**")
                        for item in items:
                            title = item.get("title")
                            link = item.get("link")
                            snippet = item.get("snippet")
                            st.write(f"**Title:** {title}")
                            st.write(f"**Link:** [Visit Website]({link})")
                            st.write(f"**Snippet:** {snippet}")
                            st.write("---")
                    else:
                        st.write("No search results found.")
                else:
                    st.write(predefined_response)
                
    elif page == "PDFs":
        st.markdown("### PDFs")
        query = st.text_input("Enter your query:")
        if st.button("Search"):
            search_pdfs(query, api_key, cx)

if __name__ == "__main__":
    # Add your API key and CX here
    api_key = "AIzaSyAINArq2oUaJ2FDjqhm6n6cGWR8LBmC-Es"
    cx = "739203c215d974dde"  # Replace with your Custom Search Engine ID

    main()
