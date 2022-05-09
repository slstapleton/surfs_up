# Surf and Ice Cream Start Up Weather Analysis
## Overview of the analysis 
### Explain the purpose of this analysis
Beginning a business comes with many risk factors. An entrepreneur needs to explore every avenue related to their business to ensure a prosperous start up and continued success. W. Avy has expressed concerns in regards to the weather with the startup of a surf shop also serving ice cream in Oahu. Provided with a SQLite database of Hawaii weather, we are able to analyze the weather trends to ease the fears of any investors in regards to poor weather.
## Results 
### Provide a bulleted list with three major points from the two analysis deliverables
The database that was provided contains information on temperature and rainfall in Hawaii from 2010 to 2017. In order to get a quick glimps of the most extreme months, we are analysing the month of June and December. W. Avy had a main concern with the temperature being ideal for hitting the waves, followed by a sweet ice cream treat. Below is the basic statistical analysis of the temperature data:

![june_temp](https://user-images.githubusercontent.com/100329223/167330401-d94f9687-6ac9-4483-a540-4c8768009b45.png)
![Dec_temps](https://user-images.githubusercontent.com/100329223/167330419-3eaaef1e-2d25-4076-84f0-9e6888d6a4ee.png)

-	From these charts we can come to a few conclusions. With over 1,500 values collected over 7 years, we have a fairly large set of data and should feel like the analysis is a true representation of the weather in Hawaii.
-	The average temperature in June is approximately 75°F and the average temperature in December is approximately 71°F. This seems to be a fairly moderate temperature and appealing to those who choose to surf, eat ice cream, or both!
-	The standard deviations are fairly low, meaning the majority of the data is close to the average temperature for both December and June.  The minimum temperature in December is 56°F, but this shouldn’t be too concerning with the smaller standard deviation. Any temperature less than 69°F could be considered an outlier being that it would be located in the 25th percentile. The maximum temperature in June is 85°F.Much like the minimum temperature, this shouldn’t be too concerning. Any temperature greater than 77°F could be considered an outlier being that it would be located in the 75th percentile. Since ice cream consumption and water activities are a warm weather activity, I think there would still be a fair amount of business on the warmer days.
Below is a visual representation of the temperatures in June:

![june_temp_graph](https://user-images.githubusercontent.com/100329223/167330462-c4370e5a-7671-4023-ac32-19c1ff45ba0c.png)

-	As we can see, the majority of the data is between 73°F and 77°F and the graph represents a standard bell curve.
Below is a visual representation of the temperatures in December:

![dec_temp_graph](https://user-images.githubusercontent.com/100329223/167330480-82eb0677-371d-46fc-ba96-0f5252a36900.png)

-	Although temperatures are slightly lower, this graph also represents a standard bell curve. The majority of the data is between 69°F and 74°F
Overall, based on the temperatures provided in the database over a 7-year span in the most extreme months, this should be prime weather for a surf shop that dabbles in ice cream. Like any business, there will be slumps, but based on the data, there will always be surfers. At the lower temperatures, there are still the diehards that will surf in thermos wetsuits. If there are waves, they will be surfed. The only thing that might drop in profits on a colder day would be ice cream.

## Summary 
### Two additional queries to perform to gather more weather data for June and December
Much like the temperature, another aspect of the weather that would drive customer volume would be rainfall.  After running a couple more queries, we were able to produce tables much like that of temperature. Below are the tables for rainfall from 2010 to 2017 in the months of June and December.

![june_precip](https://user-images.githubusercontent.com/100329223/167330512-9b9843db-ccda-4c13-909e-73c89bb3e5ec.png)
![dec_precip](https://user-images.githubusercontent.com/100329223/167330514-da8bdd89-5c5d-4545-9614-bf5191c9eb48.png)

-	This is another decent set of data with over 1,400 values. 
-	The average rainfall in December is approximately 0.2 inches. This data has a lower standard deviation meaning the data is more condensed around the average.
-	The minimum being 0 inches and the maximum is around 6.4 inches. Sunshine seems to a factor that really brings out the crowds, and the majority of the data shows that rainfall is on the lower end in Hawaii. The 75th percentile of data states that anything over 0.15 inches. With the mean being higher and in the top quarter of data, there appears to be some outliers impacting the data and creating a right skew.  Like any place in the world, there will be major storms that cause a heavy rainfall.  In the grand scheme of the business, this shouldn’t cause any concern with one day of poor weather.

![dec_precip_graph](https://user-images.githubusercontent.com/100329223/167330646-8696276c-9c21-4812-86ea-f9b89e6da77b.png)

The data presented for June depicts a very similar story, with similar values.

![june_precip_graph](https://user-images.githubusercontent.com/100329223/167330656-4e3fbfcc-e6d8-462c-9691-e11b84746840.png)


After looking through all the data, I would confidently say to investors that weather, although there may be the occasional bad day, would be a driving factor in why one should invest.  Hawaii seems to be the prime location for this type of business, and pending other factors it takes to run a business, has the possibility for major growth throughout the island.
