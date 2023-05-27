# Master's Thesis: Context Usage in Document-Level MT Metrics

This code was used to inspect context usage in the document-level MT metrics proposed in the paper
[Embarrassingly Easy Document-Level MT Metrics: How to Convert Any Pretrained Metric Into a Document-Level Metric](https://statmt.org/wmt22/pdf/2022.wmt-1.6.pdf). It makes use of the original [Doc-MT-Metrics](https://github.com/amazon-science/doc-mt-metrics) code with minor adjustments.

The document-level metrics are built on top of code from [COMET](https://github.com/Unbabel/COMET), [BERTScore](https://github.com/Tiiiger/bert_score) and [Prism](https://github.com/thompsonb/prism) 
repositories.

## Code changes: Context corruption
The script `corrupt_context.py` was added which contains functions to shuffle or remove the added context sentences.

Additionally, the scripts ```score_doc-bert.py```, ```score_doc-prism.py```, ```score_doc-comet.py``` (which compute scores and correlations with human judgments) was added, so that correlations can be computed with the original context as well as with the corrupted context. The flag `--corrupt_context` was added with the options `shuffle` or `remove`. Thus to compute correlations with corrupted context sentences, simply call the script with the `--corrupt_context` flag.

## Reproducing results

Install [Doc-MT-Metrics](https://github.com/amazon-science/doc-mt-metrics) according to the instructions.

Add ```score_doc-bert.py```, ```score_doc-prism.py```, ```score_doc-comet.py``` as well as ```corrupt_context.py``` to the directory of the corresponding metric.

Please not that the doc-mt-metrics code base has been updated since the experiments were carried out, thus other minor changes might be required. 


### Example program calls to compute system-level correlations

Programs are expected to be called from the directory of the corresponding metric (e.g. ```COMET/```).
A GPU is required to run the programs.

```bash
$ export CUDA_VISIBLE_DEVICES=0
$ python score_doc-prism.py --campaign wmt21.news --lp en-de --doc --level sys --corrupt_context shuffle
```

```bash
$ export CUDA_VISIBLE_DEVICES=0
$ python score_bertscore.py --campaign wmt21.news --lp en-de --doc --level sys --corrupt_context remove
```

```bash
$ export CUDA_VISIBLE_DEVICES=0
$ python score_comet.py --campaign wmt21.tedtalks --lp en-de --doc --level sys --corrupt_context remove
```