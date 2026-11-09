# Meridia service requests

T15 course project. Question: when residents rate a service request, does speed matter more than keeping the promised target time?

`meridia_capstone.ipynb` is the deliverable. It loads 31,801 simulated requests (2024-2025), keeps the 31,502 closed ones, and works through four sub-questions. The answer: missing a promise moves the mean rating by 2.86 stars, while department, priority and channel move it by 0.37, 0.02 and 0.11.

The notebook writes nine PNGs in `figures/static/`, five offline plotly pages in `figures/interactive/`, and eleven CSVs in `bi_export/` for the Power BI dashboard in `bi/`. `data/` holds the inputs and the district map helper.

Meridia is fictional and the data are simulated. Needs Python 3, pandas, numpy, matplotlib and plotly.
