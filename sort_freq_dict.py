import json
from collections import defaultdict

with open("bigram_freq.json", "r", encoding='UTF8') as in_b_f:
    bigrams = defaultdict(int, json.load(in_b_f))
with open("bigram_freq_sorted.json", "w", encoding="UTF8") as out_b_f:
    json.dump(dict(sorted(bigrams.items(), key=lambda kv: kv[1], reverse=True)), out_b_f, ensure_ascii=False)
bigrams = defaultdict(int, "")
with open("unigram_freq.json", "r", encoding='UTF8') as in_u_f:
    unigrams = defaultdict(int, json.load(in_u_f))
with open("unigram_freq_sorted.json", "w", encoding="UTF8") as out_u_f:
    json.dump(dict(sorted(unigrams.items(), key=lambda kv: kv[1], reverse=True)), out_u_f, ensure_ascii=False)