# Homework_3_METR3334

## Original Figure from Smith and O'Brien: ![Hmk3_Research](https://user-images.githubusercontent.com/89486894/232625730-02b9c3ba-be68-49d9-b9bd-d29f005d039f.png)

## My Output: ![Box_Plot](https://user-images.githubusercontent.com/89486894/232625480-c3065039-4995-49c0-94bf-1b7bba777cb8.png)

## What Do the Figures Show?
* Each subplot within the figure represents a different city in the NW United States (specifically cities in Washington or Oregon)
* Each boxplot within every subplot represents midwinter snowfall statistics during Warm, Neutral, and Cold phase ENSO events
* The snowfall statistics are calculated using data from the years between 1950-1995
* The figures show that in these NW US cities, cold phase ENSO midwinters typically demonstrated higher snowfall accumulations

## How Did I Recreate the Figures?
* First, I downloaded snowfall data from between 1950-1995 through the National Climatic Data Center's database for the six cities shown in the figures. The data came from airport stations, and is very similar to (if not the exact same) as the datasets used by Smith and O'Brien in the original figure.
* To read this data in, I created a method within my program that allowed me to read the contents of each city's file (containing their respective snowfall totals between the aforementioned years) and place this data into a Pandas dataframe. Using a method allowed me to avoid writing the same code multiple times for each of the 6 cities.
* Once the data was stored in a dataframe (6 total, one for each city), I defined 3 more methods to break up the data in each city's main dataframe into 3 "sub" dataframes. One method would take the years between 1950-95 during which warm phase ENSO occurred and sum the snowfall totals during the midwinter periods of these years (Dec 01 - March 01, not including March 01; additionally, years in this case start and end on October 1st, which marks the start of the "ENSO year"). The individual sums from each warm ENSO year were then stored in another dataframe, which was returned by the method. The same was done for cold and neutral phase ENSO midwinters snowfall totals. It should be noted that I did not know how to effectively loop through the years in each method to identify cold, warm, or neutral ENSO, so these sections had to be more or less hard-coded.
* After creating the three methods, I stored yearly warm, cold, and neutral phase ENSO snowfall totals into their respective dataframes for each of the six cities. At this point, I had 18 dataframes (6 cities, 3 ENSO phases for each).
* At this point, I could begin creating my figure: after designing appropriate colors and fonts for the figure, I constructed one that would have 6 subplots. These would be arranged into two rows and three columns.
* Once the figure was set up, for each subplot I created 3 boxplots corresponding to the warm, cold, and neutral phase ENSO yearly midwinter snowfall totals for one of the cities. In this way, each subplot represented a city, and each boxplot therein represented snowfall statistics for that city during one of the three ENSO phases.
* Once each subplot was defined and formatted as I desired, I saved the figure. The result is shown above. It corresponds quite well to the figure from the paper by Smith and O'Brien, with the only real distinctions being superficial formatting differences (font sizes, whisker formatting, tick mark formatting, etc). Thus, I considered the recreation a success.

## Difficulties and Differences
* This was my first time using boxplots, so I spent most of my time figuring out how to use them via Matplotlib.
* The code in my Warm, Cold, and Neutral phase methods were inelegant, as I could not figure out how to loop through the discontinuous data therein.
* The dataset I used came from the NCEI/NCDC, just like the data from the paper. The paper, however, used first order summaries of the day. I could not access this data, but knew that those measurements generally came from airport stations and therefore used airport data from the cities. If the datasets are not the exact same, they are very similar, as evidenced by the coherence between my figure's boxplot calculations and those from the paper.
* Every other difference (as mentioned in the previous section) was superficial and small, consisting of only slight formatting variations.

# Thus concludes My Analysis of My Homework 3 for METR3334
