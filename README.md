# Predicting Outcomes of Rubber Sets in Professional Badminton Matches
In badminton, matches are played as a best-of-three format, with outcomes decided either in straight sets (2–0) or in a third and final set, commonly known as the "rubber set" (2–1). For the latter, the eventual winner is sometimes difficult to predict until the last few points.

This project aims to investigate the factors that influence the outcomes of rubber sets in professional badminton matches. Using data from BWF-sanctioned tournaments, the goal is explore prediction models and uncover insights into player performance under pressure.


## Process
1. **Data Collection**
    Scrape data from websites that host Badminton World Federation (BWF) historical tournament records and players' statistics.

2. **Data Wrangling**
        Clean and structure data - including match scores, player ranks, game durations - to prepare for analysis.

3. **Exploratory Data Analysis (EDA)**
Explore trends in rubber sets, such as prior set score margins, win-loss ratios by player ranking, etc.

4. **Modelling**
    Build predictive models (e.g. logistic regression, random forest) and evaluate model performance.

5. **Results & Insights**
    Present predictive accuracy and highlight key factors contributing to third-set wins.


## Current Status
- [x] Project idea and setup
- [ ] Web scraping implementation
- [ ] Initial EDA
- [ ] Modelling
- [ ] Results


## Tools & Technologies
- **Python**: pandas, numpy, scikit-learn, matplotlib, seaborn
- **Web scraping**: BeautifulSoup / Selenium
- **SQL**: to manage, manipulate and query data
- **Git & GitHub**: for version control and documentation
