# A Random Family Tree Generator and Vizualizer
* Note that the visualization portion of this project is taken from Adrien Verge's familytreemaker repo (https://github.com/adrienverge/familytreemaker). Many thanks.

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

![Test Image 6](/src/family_tree.png)

and the text representation looks like:

```
Martha Stewart (id=0, F, birthday=1857, deathday=1897) 
Bertram Fielding (id=1, M, birthday=1857, deathday=1896) 
	Eileen Fielding (id=2, F, birthday=1882, deathday=1920) 
	Mark Fielding (id=3, M, birthday=1895, deathday=1937) 

Eileen Fielding (id=2, F, birthday=1882, deathday=1920) 
Alfred Hogg (id=4, M, birthday=1882, deathday=1932) 
	Christopher Hogg (id=5, M, birthday=1910, deathday=1968) 

Dorothy Vaughan (id=6, F, birthday=1890, deathday=1949) 
Mark Fielding (id=3, M, birthday=1895, deathday=1937) 

Sheila Forbes (id=7, F, birthday=1918, deathday=1985) 
Christopher Hogg (id=5, M, birthday=1910, deathday=1968) 
	Sarah Hogg (id=8, F, birthday=1964, deathday=2010) 

Sarah Hogg (id=8, F, birthday=1964, deathday=2010) 
Connor Bradshaw (id=9, M, birthday=1967, deathday=2010) 
	Benjamin Bradshaw (id=10, M, birthday=1995, deathday=2010) 
```

Each married couple is represented as a pair, with their children indented below.






## Sources:

Source for baby-names UK:
https://webarchive.nationalarchives.gov.uk/20150908130922/http://www.ons.gov.uk/ons/publications/re-reference-tables.html?edition=tcm%3A77-243767

Source for surnames UK:
https://britishsurnames.co.uk/site/about

Source for mean average age at marriage:
https://www.statista.com/statistics/557962/average-age-at-marriage-england-and-wales/

Source for UK life expectancy:
https://www.statista.com/statistics/1040159/life-expectancy-united-kingdom-all-time/

