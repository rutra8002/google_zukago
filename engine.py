import json
from fuzzywuzzy import fuzz, process

class SearchEngine:
    def __init__(self):
        self.options = {}
        self.load_options()

    def load_options(self):
        with open('options.json') as f:
            self.options = json.load(f)

    def search(self, query):
        query = query.lower()
        search_results = []

        # Perform fuzzy matching with the options
        choices = list(self.options.keys())
        matches = process.extract(query, choices, scorer=fuzz.ratio, limit=99999)

        for match in matches:
            name = match[0]
            if fuzz.ratio(query, name.lower()) >= 45:
                search_results.append(self.options[name])

        return search_results

    def add_result(self, name, url):
        with open('customoptions.txt', 'a') as f:
            f.write(f"{name}:{url}\n")
        return "Option successfully requested!"
