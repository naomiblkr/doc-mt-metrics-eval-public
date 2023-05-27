# Master's Thesis on Evaluation of Document-level MT Metrics

This repository contains the code utilized for experiments and obtaining the results of my master's thesis.

## Creating Contrasting Translations (Pronoun Mistranslations)
The directory ```pro_mistranslations/``` contains the code that was used to create pronoun mistranslations as well as the resulting data. See [README](https://github.com/naomiblkr/doc-mt-metrics-eval/blob/main/pro_mistranslations/README.md) of the corresponding directory for more information.

## Context Usage in Document-level MT metrics

The directory ```doc_metrics_experiments``` contains scripts used to examine context usage in the document-level MT metrics proposed in the paper
[Embarrassingly Easy Document-Level MT Metrics: How to Convert Any Pretrained Metric Into a Document-Level Metric](https://statmt.org/wmt22/pdf/2022.wmt-1.6.pdf). For the experiments, I used [Doc-MT-Metrics](https://github.com/amazon-science/doc-mt-metrics) and made minor adjustments to corrupt the added context sentences before scores and correlations with human judgments are computed. The ```doc_metrics_experiments``` directory only contains the scripts I added and changed. Thus, to reproduce the results of my thesis, [Doc-MT-Metrics](https://github.com/amazon-science/doc-mt-metrics) needs to be installed and the script ```corrupt_context.py``` should be added to the main directory and ```score_doc-metrics.py``` should be replaced.

For more detailed instructions on how to reproduce results, see [README](https://github.com/naomiblkr/doc-mt-metrics-eval/blob/main/doc_metrics_context/README.md) in the ```doc_metrics_experiments``` folder.

## Document-level GEMBA

To compute pair-wise accuracy for the document-level version of [GEMBA](https://github.com/MicrosoftTranslator/GEMBA), the fork [Doc-GEMBA](https://github.com/naomiblkr/Doc-GEMBA) was created. The fork also contains the scripts utilized to obtain a score distribution and to extract sentences with large score discrepancies between GEMBA and Doc-GEMBA in the directory ```score_distribution/```. The resulting data which was used for the qualitative analysis is saved in the same directory.
