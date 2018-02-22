"""
Day 4: High-Entropy Passphrases
"""
import abstract_day
import nltk


class Day41(abstract_day.AbstractDay):

    @staticmethod
    def is_valid(sentence):
        freq_dist = nltk.FreqDist(sentence.split())
        for word, freq in freq_dist.items():
            if freq > 1:
                return False
        return True

    def get_result(self):
        """
        :return: Number of valid passphrases.
        """
        valid_counter = 0
        sentences = self.input_content.split('\n')
        for sentence in sentences:
            valid_counter += 1 if self.is_valid(sentence) else 0
        return valid_counter


class Day42(abstract_day.AbstractDay):

    @staticmethod
    def remove_anagrams(sentence):
        words = sentence.split()
        return ' '.join([''.join(sorted(list(w))) for w in words])

    @staticmethod
    def is_valid(sentence):
        freq_dist = nltk.FreqDist(sentence.split())
        for word, freq in freq_dist.items():
            if freq > 1:
                return False
        return True

    def get_result(self):
        """
        :return: Number of valid passphrases.
        """
        valid_counter = 0
        sentences = self.input_content.split('\n')
        for sentence in sentences:
            valid_counter += 1 if self.is_valid(sentence) and \
                                  self.is_valid(self.remove_anagrams(sentence)) else 0
        return valid_counter
