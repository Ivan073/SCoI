from helpers import process_abbreviations
from parser import count_sentences, count_nondeclarative_sentences, count_average_length_of_sentences, \
    count_average_length_of_words, top_k_ngrams
from input import get_text, get_k_n


# ‪D:\Programming\BSUIR\SCOI\Lab2\Task1\sample.txt


def main():
    print("Choose the way to get text:\n" +
          "1. Input text\n" +
          "2. Input path to file")
    text = get_text()

    print("Choose k, n:\n" +
          "1. Default (k = 10, n = 4)\n" +
          "2. Input k, n")
    k, n = get_k_n()

    optimized_text = process_abbreviations(text)
    print("Text:", text)
    print("Sentence amount:", count_sentences(optimized_text))
    print("Non-declarative sentence amount:", count_nondeclarative_sentences(optimized_text))
    print("Average sentence length:", count_average_length_of_sentences(optimized_text))
    print("Average word length:", count_average_length_of_words(optimized_text))
    print("Top k n-grams:", top_k_ngrams(optimized_text, k, n))


if __name__ == '__main__':
    main()
