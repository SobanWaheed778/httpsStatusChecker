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
            print(f"Checking {url}...")
            self.check_link(url)

    # Action: Report broken links
    def report(self):
        if self.broken_links:
            print("\n🚨 Broken Links Detected:")
            for url, error in self.broken_links:
                print(f" - {url} returned error {error}")
        else:
            print("\n✅ No broken links found.")

# -------------------------
# User Input / Simulation
# -------------------------
def run_simulation():
    # Get URLs from the user (you can input as a list of URLs)
    urls = input("Enter URLs to check (comma separated): ").split(',')

    # Initialize the Dead Link Detector Agent
    agent = DeadLinkDetectorAgent(urls)

    # Run the scan and report
    agent.scan_links()
    agent.report()

if __name__ == "__main__":
    run_simulation()
