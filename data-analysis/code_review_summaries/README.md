# Generating the code review study summaries

This directory contains the _normalized_ CSV data and scripts needed to generate
the code review study summaries for each participant at the project level.
To generate the summaries, first create a virtual environment and install all the packages as follows:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

Then run the script:

```bash
./main.sh
```

For every `code-review.csv`, you should see a `code-review-summary.csv` in the same directory.
Said summary contains the following columns:

- `number-of-comments`
- `number-of-sentences`
- `number-of-words`
- `number-of-commented-lines`
