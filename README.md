### MinoanLoop: Using GPT for Linear A Translation

````markdown
# Linear A Translation Project

This Python script utilizes OpenAI's GPT-4 to assist in translating Linear A texts, an undeciphered script from the ancient Minoan civilization. The script leverages a combination of a custom glossary and symbol dictionary, alongside AI-driven translation and review processes, to attempt plausible translations of Linear A sentences.

My main thoughts about why I _think_ this could work:

1. We know the structure of the sentences, i.e. the order of the symbols to be read
2. We know some of the words, as they have the same meaning in Linear B
3. We know that most of the tablets are some kind of inventory, which allows us to make educated guesses on certain tablets
4. It's not a highly developed language, some of the sentences probably do mean something like "10 sheep" or "5 jars of oil"
5. If a million monkeys in a room can write Shakespeare, then surely a million GPT-4s can brute-force translate Linear A

If we can get it to work for Linear A, there's no reason we couldn't brute force other languages. Which would be neat.

## Main Problems

1. It's difficult to manually translate a tablet from [here](https://sigla.phis.me/browse.html) into the correct [unicode characters](https://en.wikipedia.org/wiki/Template:Unicode_chart_Linear_A).
2. It's expensive to run right now, given we are trying to brute force the translation of Linear A.
3. There's no way currently of checking previous bad translations, so that we don't get stuck trying the same words constantly.

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
````

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
data = [
    {"sentence": ["𐘀", "𐘁", "𐘂", "known1"], "translation": ["", "", "", "water"]},
    {"sentence": ["𐘃", "𐘄", "𐘅", "known2"], "translation": ["", "", "", "tree"]}
]
glossary = {"known1": "water", "known2": "tree"}
```

### Extending the Dictionary

To add more symbols to the dictionary or update translations, modify the `linear_a_dict` in the script.

## Contributions

Contributions are welcome, particular to add:

1. More untranslated sentences, to the data
2. To add any known words I've missed to the dictionary
3. To work on the problems listed at the top

If you have suggestions or enhancements, please fork the repository and submit a pull request.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Alex Hughes - classics fan
GitHub: [@alexjackhughes](https://github.com/alexjackhughes)
Twitter: [@alexjackhughes](https://x.com/alexjackhughes)
