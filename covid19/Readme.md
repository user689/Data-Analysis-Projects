In this project we explore the Covid-19 response in several countries to get some insight into prevention and containment measures.

Main reports:

- exploratory_analysis.html: a file showing how we explored data until reaching conclusions.
- slide_deck.slides: a quick presentation showing the main findings.

### Datasets included:

- **[Covid Containment Dataset][1]:** The dataset was collected from http://epidemicforecasting.org/containment. The description included:
>>Each measure in the database has entries on:
  - Country (and state for the US)
  - Textual description of the measure
  - Start date of measure
  - End date (if available)
  - URL to source of more information
  - Systematic keyword labels (e.g. "travel ban" or "hygiene enforcement")

- **[Covid-19 Dataset][2]:** Collected from the [World Health Organisation][3]. Content includes:
>> This dataset has daily level information on the number of affected cases, deaths and recovery from 2019 novel coronavirus. Please note that this is a time series data and so the number of cases on any given day is the cumulative number.
  - Sno - Serial number
  - ObservationDate - Date of the observation in MM/DD/YYYY
  - Province/State - Province or state of the observation (Could be empty when missing)
  - Country/Region - Country of observation
  - Last Update - Time in UTC at which the row is updated for the given province or country. (Not standardised and so please clean before using it)
  - Confirmed - Cumulative number of confirmed cases till that date
  - Deaths - Cumulative number of of deaths till that date
  - Recovered - Cumulative number of recovered cases till that date
- **[Country population and other data][5]:** Collected from a kaggle dataset. Only specific columns like population and median age are useful to compare countrie.
  
- **Data Specific to Country (Lebanon):** Since I am from Lebanon, I am interested in how this country compares to other countries. Most of the required data is available in the 2nd database. However, additional data was obtained manually from local and [government websites][4].


[1]:https://www.kaggle.com/paultimothymooney/covid19-containment-and-mitigation-measures
[2]:https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-dataset
[3]:https://www.who.int/emergencies/diseases/novel-coronavirus-2019
[4]:http://corona.ministryinfo.gov.lb/
[5]:https://www.kaggle.com/tanuprabhu/population-by-country-2020

## Main Findings 

In this report we took a look at the global spread and containment of the Covid-19 virus. Some of the questions that we were able to answer:

*Q: Which countries are doing better than others and why?*

Many countries were able to reduce the impact of the virus not only by taking suitable measure but also by being able to enforce them quickly after discovering the first case.

*Q: What measures are the most effective against the spread of the virus?*

We have seen that the most common measures taken to limit the spread of the virus include: 'university closure', 'school closure','travel ban'. However, what is more important is being able to enforce them correctly and within time.

*Q: How do the death and recovery rates compare according to population, density and median age of a country?*

In general, countries with high population tend to have a higher number of cases. Median age seem to be weakly correlated with the number of deaths. 

*Q: How does Lebanon compare to other countries regarding measures taken and spread of the virus?*

We saw how Lebanon compared with other countries. It is performing well in general but still has a long battle ahead.

## Resources

https://www.kaggle.com/paultimothymooney/covid19-containment-and-mitigation-measures
https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-dataset
https://www.who.int/emergencies/diseases/novel-coronavirus-2019
http://corona.ministryinfo.gov.lb/
https://www.kaggle.com/tanuprabhu/population-by-country-2020
https://stackoverflow.com/a/53463151/4145941
https://www.datacamp.com/community/tutorials/wordcloud-python
https://youtu.be/54XLXg4fYsc
