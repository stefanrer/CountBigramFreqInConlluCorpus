import json
from collections import defaultdict


def calc_t_score(freq_bigrams, freq_unigrams):
    N = sum(freq_unigrams.values())  # Amount of words in corpus
    bigram_t = {}
    for bigram, freq in freq_bigrams.items():
        w1, w2 = bigram.split()
        E_xy = (freq_unigrams[w1] + freq_unigrams[w2]) / N
        bigram_t[bigram] = (freq - E_xy) / (freq ** 0.5)
    return bigram_t


if __name__ == '__main__':
    with open("bigram_freq.json", "r", encoding='UTF8') as in_b_f:
        bigrams = defaultdict(int, json.load(in_b_f))
    with open("unigram_freq.json", "r", encoding='UTF8') as in_u_f:
        unigrams = defaultdict(int, json.load(in_u_f))
    bigram_t_scores = calc_t_score(bigrams, unigrams)
    with open("bigram_t_scores.json", "w", encoding='UTF8') as out_f:
        json.dump(bigram_t_scores, out_f, ensure_ascii=False)
