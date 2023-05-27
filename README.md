# Master's Thesis on Evaluation of Document-level MT Metrics

This repository contains the code utilized for experiments and obtaining the results of my master's thesis.

## Creating contrasting translations (pronoun mistranslations)
The directory ```pro_mistranslations/``` contains the code that was used to create pronoun mistranslations as well as the resulting data. See [README](https://github.com/naomiblkr/doc-mt-metrics-eval/blob/main/pro_mistranslations/README.md) of the corresponding directory for more information.

## Document-level MT metrics
...

## Document-level GEMBA

To compute pair-wise accuracy for the document-level version of [GEMBA](https://github.com/MicrosoftTranslator/GEMBA), the fork [Doc-GEMBA](https://github.com/naomiblkr/Doc-GEMBA) was created. The fork also contains the scripts utilized to obtain a score distribution and to extract sentences with large score discrepancies between GEMBA and Doc-GEMBA in the directory ```score_distribution/```. The resulting data which was used for the qualitative analysis is saved in the same directory.
