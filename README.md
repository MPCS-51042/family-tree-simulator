Proposal:
Procedurally Generate Lineages Program:
Given two names, a sub-region, and a century value (in the last 1000 years), procedurally generate a family tree (of names, dobs, marriages, deaths, cause of death) for the next 10 generations taking into account birth rates, mortality rates, economic booms/busts, the probability of various life events at different points in history, name frequencies/naming conventions, etc. Also including historical events taken from Wikipedia (i.e., historically accurate deaths in the plague years, during wars, etc.). Aim to encompass ~200 unique historically accurate death events. Probably will build this out for a modern nation state, i.e. England/France/US. 
Not sure which tools this would use from outside the class, but I’m sure it could be something. Maybe some sort of web-scraping tool for Wikipedia to find death rates? 

Given To-Do List:
1. Proof of concept on your integrations. Where are you getting the data from? Are there databases or APIs you can get this info from, or are you forced to get it by scraping Wikipedia?
2. Figure out your UI. Is this a command line tool or does it have a graphical interface? You could use something like Flask or Bottle if you wanted a graphical interface.
3. Implement the logic to take in the user inputs (two names, subregion, century value) and get to an output.
4. Experiment with how to display the output

I think you might have slightly misunderstood what I wanted to do with my project -- my fault, I think I explained it a little wrong. Basically, I want to generate aka simulate a fictional family tree for the next 10 generations, with some degree of realism. I don't really need like a huge amount of data from an API (besides a names database), becasue the rest I'll just scrape from wikipedia.

My to do list:
1. by 2/8: Develop a name generator. Need to find database of historical names, decide how to generate fictional names based on those historical names.
2. by 2/15: Develop a person class, with attributes like dates of birth and death, reason of death, marriages, number of children, etc. Each of these attributes should be filled by a probabilistic analysis of a random variable -- i.e., someone born in 1500 more likely to die as a child than someone born in 1950. Also include random name. 
3. by 2/22: Develop way to link person objects together from parent to child, so that they form a contiguous family tree. Account for name transfers, increases probability of death for children if both parents die, stuff like that.
4. by 3/1: Build out database of historical calamities (~200), i.e. plague, so that death events are not just probabilistic. 
5. by 3/8: Develop a nice way of viewing the family tree in the terminal. Plan thus far is just on getting the functionality of the preceding few weeks. Forsee some problems with later generations being rather large, might want some summary statistics?

 
