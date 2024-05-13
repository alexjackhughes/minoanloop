# MinoanLoop: Using GPT for Linear A Translation

What is this?

I've been fascinated with ancient greece for as long as I can remember, and particularly fascinated with Linear A. We have a whole body of tablets that we can't read, and being able to read them might add tremendously to our understanding of the ancient world.

This is a project to try to utilise OpenAI's GPT-4 to "guesstimate" specific words given the context of the sentence, and the words we do know. It then builds out it's dictionary on the fly, against increasingly difficult sentences from real tablets. We also use AI to "review" the translation, in this way we can be more confident that we are on the right track

My main thoughts about why I _think_ this could work:

1. We can assume the tablets aren't random sentences, there is meaning here
2. We know the structure of the sentences, i.e. the order of the symbols to be read
3. Some of the characters are known from Linear B, so we aren't starting from scratch
4. Most of the characters appear to represent entire words, and some are even pictoral, helping us make educated guesses
5. A lot of the tablets appears to be short inventory lists, which adds context to the sentence we are translating
6. This isn't a highly developed languages; some of the sentences probably do mean something like "10 sheep" or "5 jars oil"
7. Once we have "got" a word, all other sentences that include that word are easy to translate. It's a bit like crossword where it gets easier the more words you have, or how GPT can guess the next token, given the tokens before it.
8. If a million monkeys in a room can write Shakespeare, then surely a billion GPT-4s can brute-force Homer?

Plus, if this method words we might be able to apply it to other languages. Pretty neat.

## Main Problems

1. It's time consuming to manually translate a tablet from [here](https://sigla.phis.me/browse.html) into the correct [unicode characters](https://en.wikipedia.org/wiki/Template:Unicode_chart_Linear_A). Perhaps we could implement a scraper/AI that could be trained on the unicode characters and spit out the correct unicode translation based on an image of the tablets?
2. It's expensive and dumb and slow to run right now, although I'm hoping this will change as models get cheaper/faster.
3. The script doesn't take into consideration the "bad translations" from results; As context increases, it might worth passing all the previous dictionaries back to the AI, so it doesn't keep guessing the same words.
4. At the moment we ask the AI to guess only the translation, but instead it might be better to ask it to guess the entire dictionary and pass that whole dictionary back. This way, it would be able to update even the words it thinks it knows.
5. It might be worth implementing some kind of "confidence" score, so we can see how confident the AI is in it's translation. This could be used to filter out bad translations, or to know when to stop. Like words we know could be 100% so it knows not to change them, and then the guesses could be 50% or 25%.
6. It might be better to review _all_ the sentences at the end of each cycle, rather than just the last one. Then it could run infinitely, and exit only when it passes a certain threshold of looks correct translations.

## Features

- **Custom Glossary and Symbol Dictionary**: Manage and utilize a custom dictionary specifically tailored for Linear A symbols.
- **AI-Driven Translation**: Use GPT-4 to translate sentences based on the context provided and the known glossary.
- **AI-Driven Review**: GPT-4 reviews the plausibility of translations, improving the accuracy and reliability of the translation process.

## Prerequisites

To use this script, you need:

- Python 3.8 or later.
- OpenAI API access with an API key for GPT-4.
- The `openai` Python library installed in your environment.

## Setup

1. **Install Python**: Ensure Python 3.8+ is installed on your system.
2. **Install Dependencies**
3. **Download the Script**: Clone or download this repository to your local machine.
4. **API Key**: Copy the `.env.example` file to `.env` and add your OpenAI API key.

## Usage

Run the script from your command line by navigating to the script's directory and running:

```bash
python3 main.py
```

### Data Format

The script expects data in the following format:

```python
# A list of sentences from the tablets, both untranslated and partially-translated
data = [
    {"sentence": ["𐘀", "𐘁", "𐘂", "3"], "translation": ["", "person", "", "3"]},
    {"sentence": ["𐘃", "𐘄", "𐘅", "3"], "translation": ["dog", "", "", "3"]}
]

# A dictionary of all known words
linear_a_dict = {"𐘃": "", "𐘄": ""}
```

### Extending the Dictionary

To add more symbols to the dictionary or update translations, modify the `linear_a_dict` in the script.

## Contributions

Contributions are welcome, particular to add:

1. More untranslated sentences to data
2. Add more known words to the dictionary
3. Ideas for how to solve any of the problems outlined above

If you have suggestions or enhancements, please fork the repository and submit a pull request.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Alex Hughes - classics fan

GitHub: [@alexjackhughes](https://github.com/alexjackhughes)

Twitter: [@alexjackhughes](https://x.com/alexjackhughes)
