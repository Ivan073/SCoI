import re
import constants


def process_abbreviations(text: str) -> str:
    """Remove all dots in middle sentence abbreviations,
        Remove dots in rest of abbreviations, if next word starts with capital add a dot.
        In process also handles transition to next line, changing it to space.
        """

    for abbr in constants.MIDDLE_SENTENCE_ABBREVIATIONS:
        text = text.replace(abbr, abbr.replace('.', ''))

    word_list = text.split()
    for index, word in enumerate(word_list):
        if word in constants.END_OF_SENTENCE_ABBREVIATIONS and index+1 != len(word_list) and\
                word_list[index+1][0].islower():
            word_list[index] = word.replace('.', '')
        elif word in constants.END_OF_SENTENCE_ABBREVIATIONS:
            word_list[index] = word.replace('.', '')+'.'
    text = ' '.join(word_list)

    return text


def get_word_list(text: str) -> list[str]:
    """List of words from text"""
    word_list = re.split(r"\.|,|:|\\n|\s|;|!|\?|\"|\(|\)", text)
    return [word for word in word_list if not (word.isnumeric() or (word == ''))]


def get_sentence_list(text: str) -> list[str]:
    """List of sentences from text"""
    word_list = re.split(r"\.|!|\?", text)
    return [word for word in word_list if not (word.isnumeric() or (word == ''))]

