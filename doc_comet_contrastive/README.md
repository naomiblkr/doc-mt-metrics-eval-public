# Scoring pronoun translation mistakes with COMET and Doc-COMET

The scripts are used to test whether [COMET](https://github.com/Unbabel/COMET) and [Doc-COMET](https://github.com/amazon-science/doc-mt-metrics/tree/main/COMET) are susceptible to discourse-level translation errors, specifically mistranslations of anaphoric instances of the English pronoun "it" into German. Contrasting human reference translations (one with an added pronoun mistranslation and one without an error) are scored against a second reference to see whether the higher score is correctly given to the translation without an error.

## Input
The program takes as input the data in the ```data_pro_errors/``` directory which contains original human reference translations (WMT newstest 2021 and generaltest 2022) along with perturbed reference translations, where mistranslations of the English pronoun "it" were added. References (both perturbed and original) are scored against a second reference translation.

To obtain the results reported in the thesis, the reference translations (perturbed and unchanged versions) were scored as follows:

Newstest 2021 data:
* Reference A against Reference B
* Reference B against Reference A
* Reference C against Reference D
* Reference D against Reference C

Generaltest 2022 data:
* Reference A against Reference B

For each perturbed and unchanged reference, the average of all segment-level scores is computed.

## Reproduce results

To reproduce results reported in my thesis, first install the respective version of COMET. The scripts assume that a GPU is available. For both COMET and Doc-COMET the model ```wmt21-comet-mqm``` is utilized.

For computing Doc-COMET scores, move ```doc_comet_score.py```and ```score_doc_comet.sh``` as well as the ```data_pro_errors/``` folder into the main Doc-COMET directory.

Then, simply run:

```bash
bash score_doc_comet.sh
```

For computing scores with the original (sentence-level) version of COMET, move ```sent_comet_score.py```, ```score_comet.sh``` and ```data_pro_errors/``` to the main COMET directory. Alternatively, it should also be possible to run the scripts from with Doc-COMET (without actually enabling the document-level version of COMET), so that only one version of COMET has to be installed. To do so, the model path in ```sent_comet_score.py``` might need to be changed.

Once the scripts and data are in the main COMET directory, run:

```bash
bash score_comet.sh
```


