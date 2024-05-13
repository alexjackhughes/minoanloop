### MinoanLoop: Using GPT for Linear A Translation

What is this?

I've been fascinated with ancient greece for as long as I can remember, and particularly fascinated with Linear A. We have a whole body of tablets that we can't read, and being able to read them might add tremendously to our understanding of the ancient world.

This is a project to try to utilise OpenAI's GPT-4 to "guesstimate" specific words given the context of the sentence, and the words we do know. It then builds out it's dictionary on the fly, against increasingly difficult sentences from real tablets. We also use AI to "review" the translation, in this way we can be more confident that we are on the right track

My main thoughts about why I _think_ this could work:

1. We know the structure of the sentences, i.e. the order of the symbols to be read
2. We know some of the words, as they have the same meaning in Linear B
3. Once we have "got" a word, all other sentences that include that word are easy to translate - it's a bit like the attention paper
4. We can assume the tablets are actually trying to say something, it's not just random symbols
5. We know that most of the tablets are some kind of inventory (they include numbers next to words we know like goat etc), which allows us to make educated guesses on the words for some tablets
6. It's not a highly developed language, some of the sentences probably do mean something like "10 sheep" or "5 jars of oil"
7. If a million monkeys in a room can write Shakespeare, then surely a million GPT-4s can brute-force translate Linear A

If we can get it to work for Linear A, there's no reason we couldn't bruteforce other languages. Super neat.

## Main Problems

1. It's difficult to manually translate a tablet from [here](https://sigla.phis.me/browse.html) into the correct [unicode characters](https://en.wikipedia.org/wiki/Template:Unicode_chart_Linear_A).
2. It's expensive to run right now, given we are trying to brute force the translation of Linear A.
3. There's no way currently of checking previous bad translations, so that we don't get stuck trying the same words constantly. With high enough context, we could actually provide all of the previous "results" to the AI and let it just figure it out.
4. At the moment, the program can't make adjustments to found words mid-cycle. In an ideal world, mid-cycle you would want the translator to be able change words it's found previously, so long as it's other translations still make sense.
5. It might make more sense rather than to pass the translation back, to pass the entire dictionary.
6. If we added more tablet sentences, I think you could structure it so that a found word appears in the next sentence, allowing us to build up the translations more quickly, and hopefully making the more difficult translations easier.

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
