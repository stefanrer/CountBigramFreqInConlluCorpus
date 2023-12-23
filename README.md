# CountBigramFreqInConlluCorpus
Count Bigram frequency in a conllu format corpus

1)Place your conllu files into directory named **Texts**

2)Launch count_bigram_freq.py script

  2.1)Script works for large files (reads them in 1gb chunks)
  
  2.2)Script creates 2 json files:
  
    bigram_freq.json - dictionary of bigram frequency in corpus
    unigram_freq.json - dictionary of unigram frequency in corpus
    
3)Optional:

sort_freq_dict.py - sorts dicts by frequency and creates freq_sorted.json files


# CalculateTscoreForBigramsBasedOnFrequency
Calculate Tscores for bigrams based on their frequency

1)Launch bigrams_t_score.py script

  1.1)If you want to use sorted dicts replace filenames in script to sorted

  1.2)Script creates 1 json file:

    bigram_t_scores.json - dictionary of bigram t_scores

**Formula used:**
```math
\frac{B_f - \frac{U1_f + U2_f}{N}}{\sqrt{B_f}}
```
- $N$ - words in corpus (sum of unigram values/frequencies in our case)
- $B_f$ - bigram frequency
- $U1_f$ - 1st unigram frequency
- $U2_f$ - 2nd unigram frequency
