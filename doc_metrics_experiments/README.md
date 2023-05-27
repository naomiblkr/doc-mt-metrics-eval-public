# Master's Thesis: Context Usage in Document-Level MT Metrics

This code was used to test context usage in the document-level MT metrics proposed in the paper
[Embarrassingly Easy Document-Level MT Metrics: How to Convert Any Pretrained Metric Into a Document-Level Metric](https://statmt.org/wmt22/pdf/2022.wmt-1.6.pdf). It makes use of the original [Doc-MT-Metrics](https://github.com/amazon-science/doc-mt-metrics) code with minor adjustments.

The document-level metrics are built on top of code from [COMET](https://github.com/Unbabel/COMET), [BERTScore](https://github.com/Tiiiger/bert_score) and [Prism](https://github.com/thompsonb/prism) 
repositories.

## Code changes: Context corruption
The script `corrupt_context.py` was added which contains functions to shuffle or remove the added context sentences.

Additionally, the ```score_doc-metrics.py``` script (which computes scores and correlations with human judgments) was adapted, so that correlations can be computed with the original context as well as with the corrupted context. The flag `--corrupt_context` was added with the options `shuffle` or `remove`. Thus to compute correlations with corrupted context sentences, simply call the script with the `--corrupt_context` flag.

## Reproduce results 

Install [Doc-MT-Metrics](https://github.com/amazon-science/doc-mt-metrics) according the instructions.

Replace ```score_doc-metrics.py``` with the script from this directory and add ```corrupt_context.py``` to the main directory of doc-mt-metrics.


### Example program calls to compute system-level correlations

```bash
python score_doc-metrics.py --campaign wmt21.news --lp en-de --model prism --doc --level sys --corrupt_context shuffle
```

```bash
python score_doc-metrics.py --campaign wmt21.news --lp en-de --model bertscore --doc --level sys --corrupt_context remove
```

```bash
python score_doc-metrics.py --campaign wmt21.tedtalks --lp en-de --model comet --doc --level sys --corrupt_context remove