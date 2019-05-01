"""
Which NFL division is best?
"""


import pprint
import sys

years = [
    2002,
    2003,
    2004,
    2005,
    2006,
    2007,
    2008,
    2009,
    2010,
    2011,
    2012,
    2013,
    2014,
    2015,
    2016,
    2017,
    2018,
    2019,
]

bills = [2017]
dolphins = [2008, 2016]
patriots = [2003, 2004, 2005, 2006, 2007, 2009, 2010, 2011,
            2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
jets = [2002, 2004, 2006, 2009, 2010]

ravens = [2003, 2006, 2008, 2009, 2010, 2011, 2012, 2014, 2018, 2019]
bengals = [2005, 2009, 2011, 2012, 2013, 2014, 2015]
browns = [2002]
steelers = [2002, 2004, 2005, 2007, 2008, 2010,
            2011, 2014, 2015, 2016, 2017]

texans = [2011, 2012, 2015, 2016, 2018, 2019]
colts = [2002, 2003, 2004, 2005, 2006, 2007, 2007, 2008, 2009,
         2010, 2012, 2013, 2014, 2018, 2019]
jags = [2005, 2007, 2017]
titans = [2002, 2003, 2007, 2008, 2017]

broncos = [2003, 2004, 2005, 2011, 2012, 2013, 2014, 2015]
chiefs = [2003, 2006, 2010, 2013, 2015, 2016, 2017, 2018, 2019]
raiders = [2002, 2016]
chargers = [2004, 2006, 2007, 2008, 2009, 2013, 2019]


cowboys = [2003, 2006, 2007, 2009, 2014, 2016, 2018, 2019]
giants = [2002, 2005, 2006, 2007, 2008, 2011, 2016]
eagles = [2002, 2003, 2004, 2006, 2008, 2009, 2010, 2013, 2017, 2018, 2019]
redskins = [2005, 2007, 2012, 2015]

bears = [2005, 2006, 2010, 2018, 2019]
lions = [2011, 2014, 2016]
packers = [2002, 2003, 2004, 2007, 2009, 2010, 2011,
           2012, 2013, 2014, 2015, 2016]
vikings = [2004, 2008, 2009, 2012, 2015, 2017]

falcons = [2004, 2008, 2010, 2011, 2012, 2016, 2017]
panthers = [2003, 2005, 2008, 2013, 2014, 2015, 2017]
saints = [2006, 2009, 2010, 2011, 2013, 2017, 2018, 2019]
bucs = [2002, 2005, 2007]

cardinals = [2008, 2009, 2014, 2015]
rams = [2001, 2003, 2017, 2018, 2019]
niners = [2002, 2011, 2012, 2013]
seahawks = [2003, 2004, 2005, 2006, 2007, 2010, 2012,
            2013, 2014, 2015, 2016, 2018, 2019]


divisions = {
    "AFC East" : [bills, dolphins, patriots, jets],
    "AFC North" : [ravens, bengals, browns, steelers],
    "AFC South" : [texans, colts, jags, titans],
    "AFC West" : [broncos, chiefs, raiders, chargers],
    "NFC East" : [cowboys, giants, eagles, redskins],
    "NFC North" : [bears, lions, packers, vikings],
    "NFC South" : [falcons, panthers, saints, bucs],
    "NFC West" : [cardinals, rams, niners, seahawks]
}



def best_div(start_year):

    years_sublist = years[years.index(start_year) : ]
    print("Date range: {} - {}".format(start_year, years_sublist[-1]))

    playoff_appearances = []
    for key in divisions:
        playoff_weights = 0
        for team in divisions[key]:
            for year in team:
                if year in years_sublist:

                    year_weight = 2 * len(years_sublist) - abs(year -  years_sublist[-1])
                    playoff_weights += year_weight


        playoff_appearances.append("{}:   {}: {:0.2f}".format(playoff_weights, key,
                                                            float(playoff_weights)/ len(years_sublist)))

    sort = sorted(playoff_appearances)
    sort.reverse()
    return sort



if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("must pass start_year as argument")
        sys.exit(-1)

    start_year = int(sys.argv[1])
    data = best_div(start_year)

    print("Weights:")
    for item in data:
        print(item[4:])
