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
