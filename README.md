### MinoanLoop: Using GPT for Linear A Translation

````markdown
# Linear A Translation Project

This Python script utilizes OpenAI's GPT-4 to assist in translating Linear A texts, an undeciphered script from ancient Minoan civilization. The script leverages a combination of a custom glossary and symbol dictionary, alongside AI-driven translation and review processes, to attempt plausible translations of Linear A sentences.

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
python translate_linear_a.py
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

If you have suggestions or enhancements, please fork the repository and submit a pull request.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Alex Hughes - classics fan
GitHub: [@alexjackhughes](https://github.com/alexjackhughes)
Twitter: [@alexjackhughes](https://x.com/alexjackhughes)
