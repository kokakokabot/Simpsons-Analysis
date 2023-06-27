import matplotlib.pyplot as plt

# Data
seasons = ['Season 1', 'Season 2', 'Season 3', 'Season 4', 'Season 5', 'Season 6', 'Season 7', 'Season 8', 'Season 9',
           'Season 10', 'Season 11', 'Season 12', 'Season 13', 'Season 14', 'Season 15', 'Season 16', 'Season 17',
           'Season 18', 'Season 19', 'Season 20', 'Season 21', 'Season 22', 'Season 23', 'Season 24', 'Season 25',
           'Season 26', 'Season 27', 'Season 28', 'Season 29', 'Season 30', 'Season 31', 'Season 32', 'Season 33',
           'Season 34']
years = [1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006,
         2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
ratings = [7.7, 8.0, 8.2, 8.3, 8.3, 8.3, 8.4, 8.2, 7.8, 7.6, 7.3, 7.3, 7.1, 7.0, 7.0, 7.0, 6.8, 6.9, 6.9, 6.9, 6.8, 6.7,
           6.7, 6.7, 6.7, 6.6, 6.6, 6.4, 6.6, 6.2, 6.4, 6.4, 6.6, 6.4]
views_in_millions = [27.8, 24.4, 21.8, 22.4, 18.9, 15.6, 15.1, 14.5, 9.1, 7.9, 8.2, 14.7, 12.5, 14.3, 11.0, 10.2, 9.57,
                     9.19, 8.26, 7.08, 7.1, 7.1, 6.3, 5.4, 4.9, 4.8, 4.0, 3.4, 3.11, 2.6, 2.0, 2.0, 1.8, 1.7]
# General Code
figure_1 = plt.figure(figsize=(12, 8))
figure_1.patch.set_facecolor("yellow")
font_style = {'color':'tab:blue', "family":"fantasy", 'weight':'bold'}

# Ratings Graph
axis_ratings = figure_1.add_axes([0.05, 0.05, 0.9, 0.35])
axis_ratings.bar(x=seasons, height=ratings)
axis_ratings.set_xticks([0, 9, 19, 29])
axis_ratings.set_ylim(6, 9)
axis_ratings.set_title("IMDB Ratings", fontdict=font_style)
axis_ratings.text(2,7.5, "Golden Age",size = 16, bbox={'fc':'yellow', 'ec':'tab:blue'}, fontdict=font_style)
axis_ratings.text(19,7,"Zombie Simpsons", size = 16, bbox={'fc':'tab:blue', 'ec':'yellow'}, fontdict={'color':'yellow', "family":"fantasy", 'weight':'bold'})

# Views Graph
axis_views = figure_1.add_axes([0.05, 0.45, 0.9, 0.5])
axis_views.plot(years, views_in_millions, linewidth=4, solid_capstyle='round')
axis_views.set_xticks([])
axis_views.set_title("Views (in millions)", fontdict=font_style)
axis_views.text(1989.2, 27.8, "1989", fontdict=font_style)
axis_views.text(2022.2, 1.7, "2022", fontdict=font_style)

# Styles
for axes in [axis_views, axis_ratings]:
    axes.set_facecolor("yellow")
    axes.tick_params(colors="tab:blue", labelsize=12, width=2)
    for side in ['bottom', 'top', 'left', 'right']:
        axes.spines[side].set_color('tab:blue')
        axes.spines[side].set_linewidth(2)

# Shows the graphs and saves them in the same folder as a .png file
plt.show()
plt.savefig('Simpsons Graphs', facecolor='yellow')
