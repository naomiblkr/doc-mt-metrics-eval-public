# ! usr/bin/bash
# Assumes you are running from the main directory `GPT_doc_metric`
# For SQM-based prompts, replace prompt-type

echo $'----------------------------------------------------------'
echo $'Scoring perturbed reference A on reference B (newstest 2021)'
echo $'----------------------------------------------------------'
python3 main.py --src data/newstest2021.en-de.src.en --hyp data/corrupted_news2021_refA.de \
    --ref data/newstest2021.en-de.ref.ref-B.de --indices data/idx_errors_news2021_refA.txt \
    --prompt-type doc_DA --save
echo $''

echo $'----------------------------------------------------------'
echo $'Scoring reference A on reference B (newstest 2021)'
echo $'----------------------------------------------------------'
python3 main.py --src data/newstest2021.en-de.src.en --hyp data/newstest2021.en-de.ref.ref-A.de \
    --ref data/newstest2021.en-de.ref.ref-B.de --indices data/idx_errors_news2021_refA.txt \
    --prompt-type doc_DA --save
echo $''

echo $'----------------------------------------------------------'
echo $'Scoring perturbed reference B on reference A (newstest 2021)'
echo $'----------------------------------------------------------'
python3 main.py --src data/newstest2021.en-de.src.en --hyp data/corrupted_news2021_refB.de \
    --ref data/newstest2021.en-de.ref.ref-A.de --indices data/idx_errors_news2021_refB.txt \
    --prompt-type doc_DA --save
echo $''

echo $'----------------------------------------------------------'
echo $'Scoring reference B on reference A (newstest 2021)'
echo $'----------------------------------------------------------'
python3 main.py --src data/newstest2021.en-de.src.en --hyp data/newstest2021.en-de.ref.ref-B.de \
    --ref data/newstest2021.en-de.ref.ref-A.de --indices data/idx_errors_news2021_refB.txt \
    --prompt-type doc_DA --save
echo $''

echo $'----------------------------------------------------------'
echo $'Scoring perturbed reference C on reference D (newstest 2021)'
echo $'----------------------------------------------------------'
python3 main.py --src data/newstest2021.en-de.src.en --hyp data/corrupted_news2021_refC.de \
    --ref data/newstest2021.en-de.ref.ref-D.de --indices data/idx_errors_news2021_refC.txt \
    --prompt-type doc_DA --save
echo $''

echo $'----------------------------------------------------------'
echo $'Scoring reference C on reference D (newstest 2021)'
echo $'----------------------------------------------------------'
python3 main.py --src data/newstest2021.en-de.src.en --hyp data/newstest2021.en-de.ref.ref-C.de \
    --ref data/newstest2021.en-de.ref.ref-D.de --indices data/idx_errors_news2021_refC.txt \
    --prompt-type doc_DA --save
echo $''

echo $'----------------------------------------------------------'
echo $'Scoring perturbed reference D on reference C (newstest 2021)'
echo $'----------------------------------------------------------'
python3 main.py --src data/newstest2021.en-de.src.en --hyp data/corrupted_news2021_refD.de \
    --ref data/newstest2021.en-de.ref.ref-C.de --indices data/idx_errors_news2021_refD.txt \
    --prompt-type doc_DA --save
echo $''

echo $'----------------------------------------------------------'
echo $'Scoring reference D on reference C (newstest 2021)'
echo $'----------------------------------------------------------'
python3 main.py --src data/newstest2021.en-de.src.en --hyp data/newstest2021.en-de.ref.ref-D.de \
    --ref data/newstest2021.en-de.ref.ref-C.de --indices data/idx_errors_news2021_refD.txt \
    --prompt-type doc_DA --save
echo $''

echo $'----------------------------------------------------------'
echo $'Scoring perturbed reference A on reference B (general test 2022)'
echo $'----------------------------------------------------------'
python3 main.py --src data/generaltest2022.en-de.src.en --hyp data/corrupted_generaltest2022.refA.de \
    --ref data/generaltest2022.en-de.ref.refB.de --indices data/idx_errors_generaltest2022_refA.txt \
    --prompt-type doc_DA
echo $''

echo $'----------------------------------------------------------'
echo $'Scoring reference A on reference B (general test 2022)'
echo $'----------------------------------------------------------'
python3 main.py --src data/generaltest2022.en-de.src.en --hyp data/generaltest2022.en-de.ref.refA.de \
    --ref data/generaltest2022.en-de.ref.refB.de --indices data/idx_errors_generaltest2022_refA.txt \
    --prompt-type doc_DA
echo $''

