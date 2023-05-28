import unittest
import parser
import helpers


class TestCountSentences(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(parser.count_sentences(""), 0)

    def test_one_sentence(self):
        self.assertEqual(parser.count_sentences(
            helpers.process_abbreviations("They met at 5 a.m. and went to cinema.")), 1)
        self.assertEqual(parser.count_sentences(
            helpers.process_abbreviations("In Apple Inc. we work hard.")), 1)
        self.assertEqual(parser.count_sentences(
            helpers.process_abbreviations("Pi equals 3.14.")), 1)
        self.assertEqual(parser.count_sentences(
            helpers.process_abbreviations("Another style of declarative sentence....")), 1)
        self.assertEqual(parser.count_sentences(
            helpers.process_abbreviations("Cool word: \"a123fgfdf23\".")), 1)
        self.assertEqual(parser.count_sentences(
            helpers.process_abbreviations("Not a word: \"123\".")), 1)
        self.assertEqual(parser.count_sentences(
            helpers.process_abbreviations("What!?")), 1)
        self.assertEqual(parser.count_sentences(
            helpers.process_abbreviations("I live in U.S.A. right now.")), 1)

    def test_two_sentences(self):
        self.assertEqual(parser.count_sentences(
            helpers.process_abbreviations("In Apple Inc. I work hard.")), 2)
        self.assertEqual(parser.count_sentences(
            helpers.process_abbreviations("Scream!!!! What!?")), 2)

    def test_nondeclarative_sentences(self):
        self.assertEqual(parser.count_nondeclarative_sentences(
            helpers.process_abbreviations("Another style of declarative sentence.... Declarative sentence...We have "
                                          "good workers (e.g. Mr. Smith).We have good workers (e.g. Smith).")), 0)
        self.assertEqual(parser.count_nondeclarative_sentences(
            helpers.process_abbreviations("Scream!!!! What!? No! How?")), 4)

    def test_sentence_length(self):
        self.assertEqual(parser.count_average_length_of_sentences(
            helpers.process_abbreviations("Short.")), 1)
        self.assertEqual(parser.count_average_length_of_sentences(
            helpers.process_abbreviations("Short. Also")), 1)
        self.assertEqual(parser.count_average_length_of_sentences(
            helpers.process_abbreviations("Pretty long sentence it is, isnt it?")), 7)

    def test_word_length(self):
        self.assertEqual(parser.count_average_length_of_words("A"), 1)
        self.assertEqual(parser.count_average_length_of_words("AAAAAAAAAAAAAAAAH"), 17)
        self.assertEqual(parser.count_average_length_of_words("how much is that"), 13 / 4)

    def test_k_ngrams(self):
        self.assertEqual(parser.top_k_ngrams(
            helpers.process_abbreviations("Whats the point?"), 0, 0), [])
        self.assertEqual(parser.top_k_ngrams(
            helpers.process_abbreviations("This is obvious"), 1, 3), ["This is obvious"])
        self.assertEqual(parser.top_k_ngrams(
            helpers.process_abbreviations("Its same."), 100, 2), ["Its same"])
        self.assertEqual(parser.top_k_ngrams(
            helpers.process_abbreviations("Its nothing"), 1, 200), [])
        self.assertEqual(parser.top_k_ngrams(
            helpers.process_abbreviations("aa aa aa aa bb"), 2, 2), ["aa aa", "aa bb"])
        self.assertEqual(parser.top_k_ngrams(
            helpers.process_abbreviations("bb aa aa aa bb cc"), 3, 1), ["aa", "bb", "cc"])


if __name__ == '__main__':
    unittest.main()
