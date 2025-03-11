from urllib.parse import urlparse
from urllib.request import urlopen
import re
import sys

LINK_REGEX = re.compile(r'<a [^>]*href=[\'"]([^\'"]+)[\'"][^>]*>')


class LinkCollector:
    def __init__(self, url):
        self.url = "http://" + urlparse(url).netloc
        self.collected_links = {}
        self.visited_links = set()

    def normalize_url(self, path: str, link: str):
        if link.startswith("http://"):
            return link
        elif link.startswith("/"):
            return self.url + link
        else:
            return self.url + path.rpartition("/")[0] + "/" + link

    def collect_links(self, path="/"):
        full_url = self.url + path
        self.visited_links.add(full_url)
        page = str(urlopen(full_url).read())
        links = LINK_REGEX.findall(page)
        links = {self.normalize_url(path, link) for link in links}
        self.collected_links[full_url] = links
        for link in links:
            self.collected_links.setdefault(link, set())
        unvisited_links = links.difference(self.visited_links)
        # print("Links:", links)
        # print("Visited Links:", self.visited_links)
        # print("Unvisited Links:", unvisited_links)
        for link in unvisited_links:
            if link.startswith(self.url):
                self.collect_links(urlparse(link).path)


if __name__ == "__main__":
    link_collector = LinkCollector("http://127.0.0.1:8000")
    link_collector.collect_links()
    for link in link_collector.collected_links:
        print(link)
    print(len(link_collector.collected_links))
