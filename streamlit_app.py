import streamlit as st
import requests

class DeadLinkDetectorAgent:
    def __init__(self, urls):
        self.urls = urls
        self.broken_links = []

    # Method to check the status code of a URL
    def check_link(self, url):
        try:
            response = requests.get(url, timeout=5)  # Set timeout to 5 seconds
            if response.status_code >= 400:
                self.broken_links.append((url, response.status_code))
        except requests.exceptions.RequestException as e:
            self.broken_links.append((url, str(e)))  # Capturing any request exceptions

    # Method to scan all URLs and identify broken links
    def scan_links(self):
        for url in self.urls:
            st.write(f"Checking {url}...")
            self.check_link(url)

    # Action: Report broken links
    def report(self):
        if self.broken_links:
            st.write("🚨 **Broken Links Detected:**")
            for url, error in self.broken_links:
                st.write(f" - **{url}** returned error {error}")
        else:
            st.write("✅ **No broken links found.**")

# -------------------------
# Streamlit User Interface
# -------------------------
def run_streamlit_simulation():
    st.title("🔗 Dead Link Detector")

    # Get URLs from the user (via Streamlit input box)
    urls_input = st.text_area("Enter URLs to check (comma separated)", "", height=100)
    
    if st.button("Check Links"):
        if urls_input:
            urls = [url.strip() for url in urls_input.split(',')]
            # Initialize the Dead Link Detector Agent
            agent = DeadLinkDetectorAgent(urls)

            # Run the scan and display the result
            agent.scan_links()
            agent.report()
        else:
            st.warning("Please enter at least one URL to check.")

if __name__ == "__main__":
    run_streamlit_simulation()
