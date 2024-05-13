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
7. Once we have "got" a word, all other sentences that include that word are easy to translate - in the same way GPT can "guess" a sentence based on the previous words it's generated - we might be able to do the same thing here. A bit like how crossword gets easier the more words you have.
8. If a million monkeys in a room can write Shakespeare, then surely a billion GPT-4s can brute-force Homer?

Plus, if this method words we might be able to apply it to other languages. Pretty neat.

## Main Problems

1. It's time consuming to manually translate a tablet from [here](https://sigla.phis.me/browse.html) into the correct [unicode characters](https://en.wikipedia.org/wiki/Template:Unicode_chart_Linear_A). Perhaps we could implement a scraper/AI that could be trained on the unicode characters and spit out the correct translation based on images of the tablets?
2. It's expensive and slow to run right now, although I'm hoping this will change as models get cheaper/faster.
3. The script doesn't take into consideration the "bad translations" from results; As context increases, it might worth passing all the dictionaries back to the AI, so it doesn't keep guessing the same words.
4. At the moment we ask the AI to just guess the translation, but instead it might be better to ask it to guess the entire dictionary, and then pass that dictionary back. This way, it could keep running through all the sentences in a loop, until it's got all the words and all the sentences make sense.

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
2. **Install Dependencies**:
   ```bash
   pip install openai
   ```
3. **API Key**: Set up your OpenAI API key. It is recommended to set this as an environment variable for security reasons:
   ```bash
   export OPENAI_API_KEY='your_api_key_here'
   ```
4. **Download the Script**: Clone or download this repository to your local machine.

## Usage

Run the script from your command line by navigating to the script's directory and running:

```bash
python3 main.py
```

### Data Format

The script expects data in the following format:

```python
# A list of sentences partially translated, directly from tablets
data = [
    {"sentence": ["𐘀", "𐘁", "𐘂", "known1"], "translation": ["", "", "", "water"]},
    {"sentence": ["𐘃", "𐘄", "𐘅", "known2"], "translation": ["", "", "", "tree"]}
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
