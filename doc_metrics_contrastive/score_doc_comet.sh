#! /bin/bash

data=data_pro_errors

device=0

export CUDA_VISIBLE_DEVICES=$device

echo $'----------------------------------------------------------'
echo $'Scoring corrupted Ref A on Ref B'
echo $'----------------------------------------------------------'
python3 doc_comet_score.py --src $data/newstest2021.en-de.src.en \
    --hyp $data/corrupted_news2021_refA.de --ref $data/newstest2021.en-de.ref.ref-B.de \
    --indices $data/idx_changes_news2021_refA.txt
echo $''

echo $'----------------------------------------------------------'
echo $'Scoring Ref A on Ref B'
echo $'----------------------------------------------------------'
python3 doc_comet_score.py --src $data/newstest2021.en-de.src.en \
    --hyp $data/newstest2021.en-de.ref.ref-A.de --ref $data/newstest2021.en-de.ref.ref-B.de \
    --indices $data/idx_changes_news2021_refA.txt
echo $''



echo $'----------------------------------------------------------'
echo $'Scoring corrupted Ref B on Ref A'
echo $'----------------------------------------------------------'
python3 doc_comet_score.py --src $data/newstest2021.en-de.src.en \
    --hyp $data/corrupted_news2021_refB.de --ref $data/newstest2021.en-de.ref.ref-A.de \
    --indices $data/idx_changes_news2021_refB.txt
echo $''

echo $'----------------------------------------------------------'
echo $'Scoring Ref B on Ref A'
echo $'----------------------------------------------------------'
python3 doc_comet_score.py --src $data/newstest2021.en-de.src.en \
    --hyp $data/newstest2021.en-de.ref.ref-B.de --ref $data/newstest2021.en-de.ref.ref-A.de \
    --indices $data/idx_changes_news2021_refB.txt
echo $''



echo $'----------------------------------------------------------'
echo $'Scoring corrupted Ref C on Ref D'
echo $'----------------------------------------------------------'
python3 doc_comet_score.py --src $data/newstest2021.en-de.src.en \
    --hyp $data/corrupted_news2021_refC.de --ref $data/newstest2021.en-de.ref.ref-D.de \
    --indices $data/idx_changes_news2021_refC.txt
echo $''

echo $'----------------------------------------------------------'
echo $'Scoring Ref C on Ref D'
echo $'----------------------------------------------------------'
python3 doc_comet_score.py --src $data/newstest2021.en-de.src.en \
    --hyp $data/newstest2021.en-de.ref.ref-C.de --ref $data/newstest2021.en-de.ref.ref-D.de \
    --indices $data/idx_changes_news2021_refC.txt
echo $''



echo $'----------------------------------------------------------'
echo $'Scoring corrupted Ref D on Ref C'
echo $'----------------------------------------------------------'
python3 doc_comet_score.py --src $data/newstest2021.en-de.src.en \
    --hyp $data/corrupted_news2021_refD.de --ref $data/newstest2021.en-de.ref.ref-C.de \
    --indices $data/idx_changes_news2021_refD.txt
echo $''

echo $'----------------------------------------------------------'
echo $'Scoring Ref D on Ref C'
echo $'----------------------------------------------------------'
python3 doc_comet_score.py --src $data/newstest2021.en-de.src.en \
    --hyp $data/newstest2021.en-de.ref.ref-D.de --ref $data/newstest2021.en-de.ref.ref-C.de \
    --indices $data/idx_changes_news2021_refD.txt
echo $''



echo $'----------------------------------------------------------'
echo $'Scoring corrupted Ref A on Ref B (generaltest 2022)'
echo $'----------------------------------------------------------'
python3 doc_comet_score.py --src $data/generaltest2022.en-de.src.en \
    --hyp $data/corrupted_generaltest2022.refA.de --ref $data/generaltest2022.en-de.ref.refB.de \
    --indices $data/idx_changes_generaltest2022_refA.txt
echo $''

echo $'----------------------------------------------------------'
echo $'Scoring Ref A on Ref B (generaltest 2022)'
echo $'----------------------------------------------------------'
python3 doc_comet_score.py --src $data/generaltest2022.en-de.src.en \
    --hyp $data/generaltest2022.en-de.ref.refA.de --ref $data/generaltest2022.en-de.ref.refB.de \
    --indices $data/idx_changes_generaltest2022_refA.txt
echo $''