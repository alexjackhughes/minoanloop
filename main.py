import re
import os
from completion import generate_completion

linear_a_dict = {
    '𐘀': '', '𐘁': '', '𐘂': '', '𐘃': '', '𐘄': '', '𐘅': '', '𐘆': '', '𐘇': '',
    '𐘈': '', '𐘉': '', '𐘊': '', '𐘋': '', '𐘌': '', '𐘍': '', '𐘎': '', '𐘏': 'sheep',
    '𐘐': 'ewe', '𐘑': 'ram', '𐘒': 'goat', '𐘓': 'she-goat', '𐘔': 'he-goat', '𐘕': 'bovine', '𐘖': 'ox/bull', '𐘗': '',
    '𐘘': '', '𐘙': '', '𐘚': '', '𐘛': '', '𐘜': '', '𐘝': 'figs', '𐘞': '', '𐘟': '',
    '𐘠': '', '𐘡': '', '𐘢': '', '𐘣': '', '𐘤': '', '𐘥': '', '𐘦': '', '𐘧': '',
    '𐘨': '', '𐘩': '', '𐘪': '', '𐘫': '', '𐘬': 'sheppard', '𐘭': '', '𐘮': 'cloth', '𐘯': '',
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

data = [
    {"sentence": ["𐘿", "𐘠", "𐙇", "𐘚", "𐘱", "3"], "translation": ["", "", "person", "", "", "3"]}, # HT 7a
    {"sentence": ["𐘬", "𐘱", "4"], "translation": ["", "", '4']}, # HT 7a
    # {"sentence": [], "translation": []},
]

# Function to update the dictionary
def update_symbol(symbol, description):
    if symbol in linear_a_dict:
        linear_a_dict[symbol] = description
        return "Symbol updated successfully."
    else:
        return "Symbol not found in dictionary."

# Simulate AI translation using GPT-4
def ai_translate(sentence):
    glossary_context = " ".join([f"{k} means {v}." for k, v in linear_a_dict.items() if v])
    context_hint = """
You are a world famous linguist, known for your specialisation in Ancient Greek, Linear B, and excited at the challenge of being the first to translate Linear A.

I’ve provided you with an incomplete glossary of Linear A, where some of the symbols have been translated. I’m also going to provide you with two sentences in this format:      {
"sentence": ["𐘿", "𐘠", "𐙇", "𐘚", "𐘱", "3"],
"translation": ["", "", "person", "", "", "3"]
},

Where sentence is the sentence be translated, and translation is what you’ll be adding to, where I’ve provided the known translations and I want you to guess the ‘’ empty spaces. This might seem difficult, but remember, it's likely that this is an audit by an administrator of a bronze age kingdom, so make sure it makes sense in that context; maybe they are talking about storing food, or going to war. It’s also a pictorial language, so maybe the icon looks like something.

You must provide your answer within brackets, so as an example for the above, I would expect something like this: [“fruit”, “cut”, "person", “picked, “store’, “3”]
    """
    prompt = f"{glossary_context} {context_hint} Translate the following Linear A sentence: {' '.join(sentence)}"

    response = generate_completion(prompt)
    print("full response from AI:", response)
    translated = extract_content_from_brackets(response)
    print("translated (should be brackets): ", response)

    # Format the result to match the original sentence structure
    formatted_translation = []
    for original_word, translated_word in zip(sentence, translated):
        if original_word in linear_a_dict:
            formatted_translation.append(linear_a_dict[original_word])
        elif translated_word and translated_word != "unknown":
            formatted_translation.append(translated_word)
            update_symbol(original_word, translated_word)
        else:
            formatted_translation.append("guess")

    return translated

def extract_content_from_brackets(text):
    """Extract and return the content inside the first pair of square brackets in the provided text."""
    match = re.search(r'\[(.*?)\]', text)
    if match:
        return match.group(1)  # Returns the content within the brackets
    return "No content found"  # Returns a message if no brackets are found

# Simulate AI review using GPT-4
def ai_review(translated_sentence, empty_sentence=''):
    prompt = f"I've attempted to translate a Linear A transcription here: {' '.join(translated_sentence)}, based on this: {empty_sentence}. What I want you to do is review whether this translation looks like it could be 'correct'. You'll know it's correct if the following is true. Does the sentence make sense in the context of an administrator looking after a bronze age city state? Perhaps it's talking about agriculture or counting items, talking about war or history. If it does, I want you to say '[TRUE]' at the end of your thought process, otherwise say '[FALSE]'."
    try:
        response = generate_completion(prompt)
        answer = check_true_false(response)

        if answer is None:
            raise ValueError("AI review response not recognized.")
        if answer:
            return True
    except:
        print("AI review response not recognized.")

        return False

def save_glossary(glossary):
    directory = 'results'
    os.makedirs(directory, exist_ok=True)  # Ensure the directory exists

    # Find the next available file number
    i = 1
    while os.path.exists(os.path.join(directory, f"glossary{i}.txt")):
        i += 1

    # Create the file path with the new file number
    file_path = os.path.join(directory, f"glossary{i}.txt")

    # Write the glossary to the file
    with open(file_path, 'w') as file:
        for key, value in glossary.items():
            file.write(f"{key}: {value}\n")

    print(f"Glossary saved to {file_path}")

def check_true_false(answer):
    if '[TRUE]' in answer:
        return True
    elif '[FALSE]' in answer:
        return False
    else:
        # Return None or raise an exception if neither is found
        return None

# Main function to process the data
def main(data):
    for entry in data:
        sentence = entry['sentence']
        known_translation = entry['translation']
        print("Original:", sentence)
        print("Known Translations:", known_translation)

        translation_attempt = ai_translate(sentence)
        print("AI Translation Attempt:", translation_attempt)

        if ai_review(translation_attempt):
            print("Translation approved.")
            # Update the glossary and save
            for sym, trans in zip(sentence, translation_attempt):
                update_symbol(sym, trans)

            save_glossary(linear_a_dict)
        else:
            print("Translation disapproved, retrying...")
            continue

        print("Current Linear A Dictionary State:", linear_a_dict)
        print("\n")

if __name__ == "__main__":
    main(data)