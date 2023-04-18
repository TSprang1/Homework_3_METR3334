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
* Once the data was stored in a dataframe (6 total, one for each city), I defined 3 more methods to break up the data in each city's main dataframe into 3 "sub" dataframes. One method would take the years between 1950-95 during which warm phase ENSO occurred and sum the snowfall totals during the midwinter periods of these years (Dec 01 - March 01, not including March 01; additionally, years in this case start and end on October 1st, which marks the start of the "ENSO year"). The individual sums from each warm ENSO year were then stored in another dataframe, which was returned by the method. The same was done for cold and neutral phase ENSO midwinters snowfall totals.
