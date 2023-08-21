import pandas as pd
from matplotlib import pyplot
from datetime import datetime

# Created by Alex P Silva

# read csv file
date_parser = lambda x:datetime.strptime(x, "%d.%m.%Y")
historic = pd.read_csv("USD_BRL_hist.csv",header=0 , parse_dates=["Data"], date_parser=date_parser)
historic.sort_values(by='Data', ascending = True, inplace = True)

# plot figure 1 of the 3
ax1 = pyplot.subplot(311)
ax1.set_title('Ranking Currency 2010 - 2019')

ax1.plot(historic["Data"],historic["USD_BRL"])

# split data by date , make average and group by year
historic['year'] = historic['Data'].map(lambda x: x.year )
historic['month'] = historic['Data'].map(lambda x: x.month)
historic['month_year'] = historic['Data'].map(lambda x: 100*x.year + x.month)
df_year = historic.groupby(['year']).mean().reset_index()
ax2 = pyplot.subplot(312)
ax2.bar( df_year["year"], df_year["USD_BRL"])

ax2.set_title('Ranking mean currency 2010-2019')

# in this third chart I separate by year and compare the variation of the currency during the months of the year
df_2010 = historic[(2010 == historic["year"])]
df_2011 = historic[(2011 == historic["year"])]
df_2012 = historic[(2012 == historic["year"])]
df_2013 = historic[(2013 == historic["year"])]
df_2014 = historic[(2014 == historic["year"])]
df_2015 = historic[(2015 == historic["year"])]
df_2016 = historic[(2016 == historic["year"])]
df_2017 = historic[(2017 == historic["year"])]
df_2018 = historic[(2018 == historic["year"])]
df_2019 = historic[(2019 == historic["year"])]
ax3 = pyplot.subplot(313)

ax3.set_title('Ranking mean currency 2010-2019 monthly comparison')
ax3.plot(df_2019["month"], df_2019["USD_BRL"], label ='2019')
ax3.plot(df_2018["month"], df_2018["USD_BRL"], label ='2018')
ax3.plot(df_2017["month"], df_2017["USD_BRL"], label ='2017')
ax3.plot(df_2016["month"], df_2016["USD_BRL"], label ='2016')
ax3.plot(df_2015["month"], df_2015["USD_BRL"], label ='2015')
ax3.plot(df_2014["month"], df_2014["USD_BRL"], label ='2014')
ax3.plot(df_2013["month"], df_2013["USD_BRL"], label ='2013')
ax3.plot(df_2012["month"], df_2012["USD_BRL"], label ='2012')
ax3.plot(df_2011["month"], df_2011["USD_BRL"], label ='2011')
ax3.plot(df_2010["month"], df_2010["USD_BRL"], label ='2010')

ax3.legend(bbox_to_anchor=(0, -0.3), loc='upper left',ncols=5, )

pyplot.tight_layout()
pyplot.show()