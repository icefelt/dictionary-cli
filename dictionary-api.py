import requests
from bs4 import BeautifulSoup


def get_definition(word):
    # Replace YOUR_API_KEY with your Merriam-Webster API key
    api_key = "d5198659-22b7-459e-972a-2ae95f9a1551"
    url = f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Find the first definition of the word
        for entry in data:
            if "meta" in entry and "id" in entry["meta"] and entry["meta"]["id"] == word.lower():
                definition = entry["def"][0]["sseq"][0][0][1]["dt"][0][1]
                # Remove any example sentences from the definition
                definition = definition.split(":")[0].strip()
                return definition
    else:
        return None


def main():
    word = input("Enter a word: ")
    definition = get_definition(word)
    if definition:
        print(f"{word}: {definition}")
    else:
        print(f"Unable to find definition for {word}")


if __name__ == "__main__":
    main()
