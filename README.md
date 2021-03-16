# A Random Family Tree Generator and Vizualizer

## Installation:

* Clone the repo

## Instructions:
* In the `src` directory modify the `input.yaml` file with chosen attributes for a starting couple, which is formatted below. 
```
num_years: <duration of the simulation>
start_year: <starting year for the simulation>
father: [<first name>, <last name>, <age at start_year>, <birth date>]
mother: [<first name>, <last name>, <age at start_year>, <birth date>]
```
* In the `src` directory, run the command `python3 runner.py`. This creates a .txt file representation of the family tree (`family_tree.txt`), as well as a (`family_tree.png`) file image of the family tree. The tree looks like:

![Test Image 6](/src/test.png)








## Sources:

Source for baby-names UK:
https://webarchive.nationalarchives.gov.uk/20150908130922/http://www.ons.gov.uk/ons/publications/re-reference-tables.html?edition=tcm%3A77-243767

Source for surnames UK:
https://britishsurnames.co.uk/site/about

Source for mean average age at marriage:
https://www.statista.com/statistics/557962/average-age-at-marriage-england-and-wales/

Source for UK life expectancy:
https://www.statista.com/statistics/1040159/life-expectancy-united-kingdom-all-time/

