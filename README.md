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
Martha Stewart (id=0, F, birthday=1857, deathday=1892) 
Snoop Dogg (id=1, M, birthday=1857, deathday=1891) 
	Morris Dogg (id=2, M, birthday=1881, deathday=1929) 
	Lily Dogg (id=3, F, birthday=1885, deathday=1947) 

Lily Dogg (id=3, F, birthday=1885, deathday=1947) 
Vincent Reed (id=5, M, birthday=1888, deathday=1937) 
	Evelyn Reed (id=7, F, birthday=1921) 

Ivy Bennett (id=4, F, birthday=1881, deathday=1917) 
Morris Dogg (id=2, M, birthday=1881, deathday=1929) 
	Richard Dogg (id=6, M, birthday=1915) 

Evelyn Reed (id=7, F, birthday=1921) 
Martyn Young (id=10, M, birthday=1930) 
	Kevin Young (id=11, M, birthday=1960) 

Christina Bates (id=8, F, birthday=1906) 
Richard Dogg (id=6, M, birthday=1915) 
	Christopher Dogg (id=9, M, birthday=1942) 
```

Each married couple is represented as a pair, with their children indented below.






## Sources:

[UK baby-names](
https://webarchive.nationalarchives.gov.uk/20150908130922/http://www.ons.gov.uk/ons/publications/re-reference-tables.html?edition=tcm%3A77-243767)

[UK surnames](https://britishsurnames.co.uk/site/about)

[UK mean age at marriage](https://www.statista.com/statistics/557962/average-age-at-marriage-england-and-wales/)

[UK life expectancy](https://www.statista.com/statistics/1040159/life-expectancy-united-kingdom-all-time/)

