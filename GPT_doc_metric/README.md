# ChatGPT as a document-level MT metric – Scoring output of sentence- and document-level MT systems

This code is built upon the [GEMBA](https://github.com/MicrosoftTranslator/GEMBA) code.
Specifically, the scripts ```gpt_api.py```, ```cache.py``` and ```parse_gpt_answer.py``` are used
from the original GEMBA code with minor adjustments.

The program prompts ChatGPT to score MT output. As opposed to the original GEMBA, it is extended to the document-level by adding two preceding context sentences to the respective source, hypothesis and reference sentence of each prompt.

The program was used to compute and compare scores for the output of document- and sentence-level systems which can be found in the ```data/``` directory. The resulting segment-level scores were saved in the directory ```scores/```. The program prints the system-level scores which are computed by averaging the segment-level scores.

To obtain the results reported in my thesis, I used the OpenAI API, thus if using the Azure API, changes to the script might be necessary. I only computed scores using the DA-based prompt (DA_doc). The script ```gpt_api.py``` was slightly adapted due to changes to the API.

## Usage

Create a virtual environment and install requirements.txt with with python >= 3.8.

```bash
pip install -r requirements.txt
```

Before running the program, update credentials (API key) for API access in ```CREDENTIALS.py```.

Example program call:

```bash
python3 main.py --src data/doc_orig_system/doc_source.src \
--hyp data/doc_orig_system/doc_hypothesis.hyp --ref  data/doc_orig_system/doc_reference.ref \
--docids data/doc_orig_system/doc_ids_en-de.docid --prompt-type DA_doc
```

The flag ```--prompt-type``` can be used to specify which of the following two prompts should be used:
DA_doc (document-level DA-based prompt) or SQM_doc (document-level SQM-based prompt).

The flag ```--docids``` is required because document boundaries are considered when adding the preceding context sentences to the sentence being scored.