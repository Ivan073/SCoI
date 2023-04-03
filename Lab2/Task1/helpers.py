from Lab2.Task1 import constants


def process_abbreviations(text: str) -> str:
    """Remove all dots in middle sentence abbreviations,
        Remove dots in rest of abbreviations if next word starts with capital.
        In process also handles transition to next line, changing it to space.
        """

    for abbr in constants.MIDDLE_SENTENCE_ABBREVIATIONS:
        text = text.replace(abbr, abbr.replace('.', ''))

    word_list = text.split()
    for index, word in enumerate(word_list):
        if word in constants.END_OF_SENTENCE_ABBREVIATIONS and index+1 != len(word_list) and\
                word_list[index+1][0].islower():
            word_list[index] = word.replace('.', '')
    text = ' '.join(word_list)

    return text
