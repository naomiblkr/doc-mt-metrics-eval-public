# Master's Thesis on Evaluation of Document-level MT Metrics

This repository contains the code utilized for experiments and obtaining the results of my master's thesis.

## 1: Creating Contrasting Translations (Pronoun Mistranslations)
The directory ```pro_mistranslations/``` contains the code that was used to create pronoun mistranslations as well as the resulting data. See [README](https://github.com/naomiblkr/doc-mt-metrics-eval/blob/main/pro_mistranslations/README.md) of the corresponding directory for more information.

## 2: Context Usage in Document-level MT Metrics

The directory ```doc_metrics_experiments/``` contains scripts used to examine context usage in the document-level MT metrics proposed in the paper
[Embarrassingly Easy Document-Level MT Metrics: How to Convert Any Pretrained Metric Into a Document-Level Metric](https://statmt.org/wmt22/pdf/2022.wmt-1.6.pdf). For the experiments, I used [Doc-MT-Metrics](https://github.com/amazon-science/doc-mt-metrics) and made minor adjustments to corrupt the added context sentences before scores and correlations with human judgments are computed. The ```doc_metrics_experiments/``` directory only contains the scripts I added and changed. Thus, to reproduce the results of my thesis, [Doc-MT-Metrics](https://github.com/amazon-science/doc-mt-metrics) needs to be installed and the scripts in the ```doc_metrics_experiments/``` directory need to be added.

For more detailed instructions on how to reproduce results, see [README](https://github.com/naomiblkr/doc-mt-metrics-eval/blob/main/doc_metrics_context/README.md) in the ```doc_metrics_experiments/``` folder.

## 3: Scoring Pronoun Mistranslations with Doc-MT-Metrics
...

## 4: Document-level GEMBA (Correlations with Human Judgments)

To compute pair-wise accuracy for the document-level version of [GEMBA](https://github.com/MicrosoftTranslator/GEMBA), the fork [Doc-GEMBA](https://github.com/naomiblkr/Doc-GEMBA) was created. Doc-GEMBA extends GEMBA to the document-level by adding two preceding context sentences (to the hypothesis, reference and source sentence) when scoring each sentence.

To obtain the results reported in my thesis, I used the OpenAI API, thus if using the Azure API,
changes to the script might be necessary. Only en-de data was used. To extend GEMBA to the document-level, the following scripts were adapted: ```prompt.py``` and ```testset.py``` were adjusted to include the updated prompts and to add the context sentences. The script ```gpt_api.py``` was also slightly adapted due to changes to the API.

The resulting segment- and system-level scores from experiments can be found in the directory ```mt-metrics-eval-v2/wmt22/metrics-scores/en-de```. The corresponding file names start with ```sent-GEMBA``` (i.e. scores obtained with the original GEMBA metrics) or ```doc-GEMBA``` (i.e. scores obtained with the document-level version of GEMBA). In both cases, reference B was used. 

### Score distribution and comparison

Scripts in the directory ```score_distribution/``` were used for the analyses in chapters 6.3 and 6.4 of my thesis which explore the scoring behavior of document-level GEMBA. The scripts are expected to be run from within the ```score_distribution/``` directory.

The script ```score_distribution.py``` computes the distribution of segment-level scores assigned by doc-GEMBA. The resulting absolute and relative frequency of segment-level scores are stored in csv files in the same directory.

The script ```compare_scores.py``` extracts sentences where sentence-level GEMBA and document-level GEMBA assigned scores with large discrepancies (score differences of 25 and more than 40). The respective hypothesis and source sentence along with the scores assigned by the two metrics are saved in json files the ```score_distribution/``` directory.


## 5: Scoring Pronoun Mistranslations with Doc-GEMBA

In the directory ```GPT_score_contrastive/```, the required code to score contrasting translations (i.e. the same translations with and without pronoun errors) can be found. For more information and instructions on how to reproduce results, see [README](https://github.com/naomiblkr/doc-mt-metrics-eval/blob/main/GPT_score_contrastive/README.md) in the respective directory.

## 6: Scoring Output of Sentence-level vs. Document-level MT systems with Doc-GEMBA

The directory ```GPT_doc_metric/```contains required code and data to reproduce results of the final experiments, i.e. to score MT output (from a sentence-level and two document-level MT systems) with Doc-GEMBA. Again, code from [GEMBA](https://github.com/MicrosoftTranslator/GEMBA) is utilized.

See [README](https://github.com/naomiblkr/doc-mt-metrics-eval/blob/main/GPT_doc_metric/README.md) in the corresponding directory for more information on how to obtain scores. Scores might vary from results reported in my thesis as there is some randomness in the prompt responses (because the temperature is gradually increased if no response is given).