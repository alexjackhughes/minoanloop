import openai
from completion import generate_completion

linear_a_dict = {
    '𐘀': '', '𐘁': '', '𐘂': '', '𐘃': '', '𐘄': '', '𐘅': '', '𐘆': '', '𐘇': '',
    '𐘈': '', '𐘉': '', '𐘊': '', '𐘋': '', '𐘌': '', '𐘍': '', '𐘎': '', '𐘏': 'sheep',
    '𐘐': 'ewe', '𐘑': 'ram', '𐘒': 'goat', '𐘓': 'she-goat', '𐘔': 'he-goat', '𐘕': 'bovine', '𐘖': 'ox/bull', '𐘗': '',
    '𐘘': '', '𐘙': '', '𐘚': '', '𐘛': '', '𐘜': '', '𐘝': 'figs', '𐘞': '', '𐘟': '',
    '𐘠': '', '𐘡': '', '𐘢': '', '𐘣': '', '𐘤': '', '𐘥': '', '𐘦': '', '𐘧': '',
    '𐘨': '', '𐘩': '', '𐘪': '', '𐘫': '', '𐘬': '', '𐘭': '', '𐘮': 'cloth', '𐘯': '',
    '𐘰': '', '𐘱': '', '𐘲': '', '𐘳': '', '𐘴': '', '𐘵': '', '𐘶': '', '𐘷': '',
    '𐘸': '', '𐘹': '', '𐘺': '', '𐘻': '', '𐘼': '', '𐘽': '', '𐘾': '', '𐘿': '',
    '𐙀': '', '𐙁': '', '𐙂': '', '𐙃': '', '𐙄': 'pig', '𐙅': 'fish', '𐙆': '', '𐙇': 'person',
    '𐙈': '', '𐙉': 'wheat', '𐙊': 'wheat', '𐙋': 'olives', '𐙌': '', '𐙍': 'wine', '𐙎': 'wine', '𐙏': 'wine',
    '𐙐': '', '𐙑': '', '𐙒': '', '𐙓': '', '𐙔': 'helmet', '𐙕': '', '𐙖': 'oil', '𐙗': 'cyperus',
    '𐙘': '', '𐙙': '', '𐙚': '', '𐙛': '', '𐙜': '', '𐙝': '', '𐙞': '', '𐙟': '',
    '𐙠': '', '𐙡': '', '𐙢': '', '𐙣': '', '𐙤': '', '𐙥': '', '𐙦': '', '𐙧': '',
    '𐙨': '', '𐙩': '', '𐙪': '', '𐙫': '', '𐙬': '', '𐙭': '', '𐙮': '', '𐙯': '',
    '𐙰': '', '𐙱': '', '𐙲': '', '𐙳': '', '𐙴': '', '𐙵': '', '𐙶': '', '𐙷': '',
    '𐙸': '', '𐙹': '', '𐙺': '', '𐙻': '', '𐙼': '', '𐙽': '', '𐙾': '', '𐙿': '',
    '𐚀': '', '𐚁': '', '𐚂': '', '𐚃': '', '𐚄': '', '𐚅': '', '𐚆': '', '𐚇': '',
    '𐚈': '', '𐚉': '', '𐚊': '', '𐚋': '', '𐚌': '', '𐚍': '', '𐚎': '', '𐚏': '',
    '𐚐': '', '𐚑': '', '𐚒': '', '𐚓': '', '𐚔': '', '𐚕': '', '𐚖': '', '𐚗': '',
    '𐚘': '', '𐚙': '', '𐚚': '', '𐚛': '', '𐚜': '', '𐚝': '', '𐚞': '', '𐚟': '',
    '𐚠': 'vessel', '𐚡': 'vessel', '𐚢': 'vessel', '𐚣': 'vessel', '𐚤': 'vessel', '𐚥': 'vessel', '𐚦': 'vessel', '𐚧': 'vessel',
    '𐚨': 'vessel', '𐚩': 'vessel', '𐚪': 'vessel', '𐚫': 'vessel', '𐚬': 'vessel', '𐚭': 'vessel', '𐚮': 'vessel', '𐚯': 'vessel',
    '𐚰': 'vessel', '𐚱': 'vessel', '𐚲': 'vessel', '𐚳': '', '𐚴': '', '𐚵': '', '𐚶': '', '𐚷': '',
    '𐚸': '', '𐚹': '', '𐚺': '', '𐚻': '', '𐚼': '', '𐚽': '', '𐚾': '', '𐚿': '',
    '𐛀': '', '𐛁': '', '𐛂': '', '𐛃': '', '𐛄': '', '𐛅': '', '𐛆': '', '𐛇': '',
    '𐛈': '', '𐛉': '', '𐛊': '', '𐛋': '', '𐛌': '', '𐛍': '', '𐛎': '', '𐛏': '',
    '𐛐': '', '𐛑': '', '𐛒': '', '𐛓': '', '𐛔': '', '𐛕': '', '𐛖': '', '𐛗': '',
    '𐛘': '', '𐛙': '', '𐛚': '', '𐛛': '', '𐛜': '', '𐛝': '', '𐛞': '', '𐛟': '',
    '𐛠': '', '𐛡': '', '𐛢': '', '𐛣': '', '𐛤': '', '𐛥': '', '𐛦': '', '𐛧': '',
    '𐛨': '', '𐛩': '', '𐛪': '', '𐛫': '', '𐛬': '', '𐛭': '', '𐛮': '', '𐛯': '',
    '𐛰': '', '𐛱': '', '𐛲': '', '𐛳': '', '𐛴': '', '𐛵': '', '𐛶': '', '𐛷': '',
    '𐛸': '', '𐛹': '', '𐛺': '', '𐛻': '', '𐛼': '', '𐛽': '', '𐛾': '', '𐛿': '',
    '𐜀': '', '𐜁': '', '𐜂': '', '𐜃': '', '𐜄': '', '𐜅': '', '𐜆': '', '𐜇': '',
    '𐜈': '', '𐜉': '', '𐜊': '', '𐜋': '', '𐜌': '', '𐜍': '', '𐜎': '', '𐜏': '',
    '𐜐': '', '𐜑': '', '𐜒': '', '𐜓': '', '𐜔': '', '𐜕': '', '𐜖': '', '𐜗': '',
    '𐜘': '', '𐜙': '', '𐜚': '', '𐜛': '', '𐜜': '', '𐜝': '', '𐜞': '', '𐜟': '',
    '𐜠': '', '𐜡': '', '𐜢': '', '𐜣': '', '𐜤': '', '𐜥': '', '𐜦': '', '𐜧': '',
    '𐜨': '', '𐜩': '', '𐜪': '', '𐜫': '', '𐜬': '', '𐜭': '', '𐜮': '', '𐜯': '',
    '𐜰': '', '𐜱': '', '𐜲': '', '𐜳': '', '𐜴': '', '𐜵': '', '𐜶': '',
    '𐝀': '', '𐝁': '', '𐝂': '', '𐝃': '', '𐝄': '', '𐝅': '', '𐝆': '', '𐝇': '',
    '𐝈': '', '𐝉': '', '𐝊': '', '𐝋': '', '𐝌': '', '𐝍': '', '𐝎': '', '𐝏': '',
    '𐝐': '', '𐝑': '', '𐝒': '', '𐝓': '', '𐝔': '', '𐝕': '',
    '𐝠': '', '𐝡': '', '𐝢': '', '𐝣': '', '𐝤': '', '𐝥': '', '𐝦': '', '𐝧': '',
}

# Function to update the dictionary
def update_symbol(symbol, description):
    if symbol in linear_a_dict:
        linear_a_dict[symbol] = description
        return "Symbol updated successfully."
    else:
        return "Symbol not found in dictionary."


# Simulate AI translation using GPT-4
def ai_translate(sentence, glossary):
    """Use GPT-4 to translate by filling in blanks based on the entire known glossary."""
    # Prepare the context for GPT-4
    glossary_context = " ".join([f"{k} means {v}." for k, v in glossary.items() if v])
    context_hint = "This is likely a sentence about agricultural audit. Please fill in the blanks based on the glossary and the context."
    prompt = f"{glossary_context} {context_hint} Translate the following Linear A sentence: {' '.join(sentence)}"

    try:
        response = openai.Completion.create(
            engine="text-davinci-002",  # Use the appropriate GPT-4 model
            prompt=prompt,
            max_tokens=150,  # Adjust tokens based on expected sentence length
            temperature=0.5  # Adjust for creativity vs. accuracy
        )
        translated = response.choices[0].text.strip().split()
    except Exception as e:
        print(f"Error during AI translation: {e}")
        translated = ["unknown"] * len(sentence)  # Default to 'unknown' for all words if error occurs

    # Format the result to match the original sentence structure
    formatted_translation = []
    for original_word, translated_word in zip(sentence, translated):
        if original_word in glossary:
            formatted_translation.append(glossary[original_word])
        elif translated_word and translated_word != "unknown":
            formatted_translation.append(translated_word)
            update_symbol(original_word, translated_word)
        else:
            formatted_translation.append("guess")
    return formatted_translation

# Simulate AI review using GPT-4
def ai_review(translated_sentence):
    """Use GPT-4 to review the plausibility of the translated sentence."""
    prompt = f"I've attempted to translate a Linear A transcription: {' '.join(translated_sentence)}"
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=50,
            temperature=0.7
        )
        review = response.choices[0].text.strip()
        return "plausible" in review.lower()
    except Exception as e:
        print(f"Error during AI review: {e}")
        return False

def save_glossary(glossary):
    """Save the glossary to a text file."""
    with open('glossary.txt', 'w') as file:
        for key, value in glossary.items():
            file.write(f"{key}: {value}\n")

# Main function to process the data
def main(data, glossary):
    for entry in data:
        sentence = entry['sentence']
        known_translation = entry['translation']
        print("Original:", sentence)
        print("Known Translations:", known_translation)

        translation_attempt = ai_translate(sentence, glossary)
        print("AI Translation Attempt:", translation_attempt)

        if ai_review(translation_attempt):
            print("Translation approved.")
            # Update the glossary and save
            for sym, trans in zip(sentence, translation_attempt):
                update_symbol(sym, trans)
        else:
            print("Translation disapproved, retrying...")
            continue

        print("Current Glossary State:", glossary)
        print("Current Linear A Dictionary State:", linear_a_dict)
        print("\n")

if __name__ == "__main__":
    # Example data setup
    data = [
        {"sentence": ["𐘀", "𐘁", "𐘂", "known1"], "translation": ["", "", "", "water"]},
        {"sentence": ["𐘃", "𐘄", "𐘅", "known2"], "translation": ["", "", "", "tree"]}
    ]
    glossary = {"known1": "water", "known2": "tree"}
    main(data, glossary)