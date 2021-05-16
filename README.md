# surfs_up

# Overview of Surfs Up Analysis

This analysis evaluates the weather conditions in Oahu, Hawaii in efforts to supplement a business plan for opening an ice cream surf shop on the island of Oahu. Specifically, the analysis assesses temperature and precipitation during the months of June and December to determine if the ice cream surf shop can be a sustainable business year-round. Using Python, Pandas functions and methods, and SQLAlchemy this analysis retrieves weather data from the Hawaii.sqlite database and presents a statistical analysis on that data.

# Resources
Data Source: Hawaii.sqlite
Software: Python 3.8.5, Jupyter Notebook 6.1.4, SQLAlchemy 1.3.2, SQLite 3.33.0

# Results

Three significant results were identified that shed light on the year-round sustainability of the ice cream surf shop business.

1. The statistical summaries generated for the temperatures in June and December demonstrate that the average temperatures for these two months are very close. The average temperature in June is 74 F ° and in December the average temperature is 71 F°: only a 3 F° difference.

2. The statistical summaries demonstrate that the maximum temperatures for June and December are also very close. The maximum temperature in June is 85 F° and in December that maximum temperature is 83 F°: only as 2 F° difference.

3. The statistical summaries demonstrate that the minimum temperatures for June and December more spread out. The minimum temperature in June is 64 F° whereas the minimum temperature in December is 56 F°, an 8 F° difference. 

![june_temp_df](/Resources/june_temp_df.png)

![december_temp_df](/Resources/december_temp_df.png)


Overall, the statistical summaries for the temperatures during the month of June and December show temperatures are mostly similar, where December temperatures are slightly cooler by 2-4 F°. This is advantages as it indicates that, for the most part, an ice cream surf shop is sustainable year-round. However, due to the low minimum temperature observed in December and the standard deviation at 3.7 it should be noted that December will have cooler temperatures throughout the month that will affect buyers’ spending, and the business will likely see lower profits compared to those in peak season months. 

# Summary of Precipitation Data

To supplement the statistical analysis on the temperatures during June and December, a statistical analysis on the precipitation during these months is also considered. 

- The average level of precipitation in June is 0.136 inches and in December the average level is 0.216 inches, a difference of 0.08 inches. 
- The maximum level of precipitation in June is 4.43 inches and 6.42 inches in December, a difference of 1.99 inches. 
- the minimum level of precipitation and the 25% quartile are the same for both months 0.00 inches. 

Ultimately, although the month of December shows to have more rain compared to the month of June, the statistics show December does not have a significantly more rain. This is positive as it indicates that the from a precipitation stand point, the ice cream surf shop business is sustainable year-round.


![june_prcp_df](/Resources/june_prcp_df.png)

![ december_prcp_df](/Resources/december_prcp_df.png)
![image](https://user-images.githubusercontent.com/80020390/118411367-2b091d80-b662-11eb-8d95-92db61cc9e5b.png)
