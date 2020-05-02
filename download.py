from download_pubmed import save_abstracts

save_abstracts(['atopic dermatitis', 'eczema', 'dermatitis'], 'ad_abstracts.csv', retmax=100000, term_in_title=True)