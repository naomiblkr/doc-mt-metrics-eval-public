# Creating mistranslations of anaphoric "it"
## Contrastive Evaluation of MT metrics on discourse-level phenomenon

To test the performance of automatic MT metrics on discourse-level phenomena, I created
perturbed German translations of the English pronoun "it" in cases where the pronoun's antecedent
is in a preceding sentence. The errors were added to human reference translations (to avoid presence of other errors).

Data from the WMT 2021 news testset and the 2022 general testset was utilized (for which multiple human references are available).

The perturbed version as well as the original reference can be scored against another human reference
translation of the same source text (see directory ```data/references/```).

The contrasting translations can also be viewed in the file ```pro_errors.json```. The file contains the perturbed reference translation, the correct (reference) translation, a second reference and the source segment, each with the corresponding two context sentences. I didn't use the JSON file for my expiremnts, i.e. it was mainly created for illustration pruposes so that the sentences with the added errors can be viewed easily.

The translation errors were created semi-automatically.


### Example program call
```bash
python3 filter_pronouns.py data/references/newstest2021.en-de.ref.ref-A.de \ data/sources/newstest2021.en-de.src.en
```


### Step 1: Extracting sentences containing translations of "it"

The script, ```filter_pronouns.py``` first tokenizes the respective source and reference text.

In a next step, sentences are extracted (i.e. the indices of the sentences) where the source sentence
contains the English pronoun "it" and the reference translation one of the German pronouns "es", "sie"
or "er".

For the extracted sentences, word alignments were computed using [SimAlign](https://github.com/cisnlp/simalign) to ensure that the German pronoun is in fact the translation of "it" and not of another word.

Finally, I extracted all sentence indices where "it" is aligned with one of the German pronouns. The script ```filter_pronouns.py``` prints the index of the respective sentences along with the word alignments as well as the German pronoun to be changed.


### Step 2: Manually creating perturbed translations of "it"

Because there are only few instances where the antecedent of "it" is not in the same sentence, i.e.
is in a preceding sentence, I decided to manually check whether this was the case for the extracted
sentences using the output from step 1. When I found instances where the antecedent was in a preceding sentence, I changed the German pronoun to one of the other pronouns. E.g. if the correct
translation of "it" is "es", I changed the translation to either "sie" or "er".

The perturbed reference translations were stored in the directory ```data/perturbed_data/```. Note that this includes the whole dataset, i.e. not only the sentences with errors. In this way, errors could easily be added or changed and the number of context sentences as well as the sentence separator token to be used can be adapted. To be able to extract only sentences containing the translation errors (along with the desired context sentences), the indices of the perturbed sentences were stored in the directory ```data/error_indices/```.

Perturbed translations were created for references A, B, C and D of the 2021 News testset as well as
for reference A of the 2022 general testset.

The file ```pro_errors.json``` was created with the script ```extract_error_sents.py```.

