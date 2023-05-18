# This is a string that contains the titles, poets, and publication dates of several highlighted poems.
highlighted_poems = "Afterimages:Audre Lorde:1997, The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925, Georgia Dusk:Jean Toomer:1923, Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

# This splits the original string into a list of individual poems.
highlighted_poems_list = highlighted_poems.split(',')

# This creates a new list with any whitespace around the individual poems removed.
highlighted_poems_stripped = []
for poem in highlighted_poems_list:
  highlighted_poems_stripped.append(poem.strip())

# This creates a new list with each individual poem further split into its title, poet, and publication date.
highlighted_poems_details = []
for poem in highlighted_poems_stripped:
  highlighted_poems_details.append(poem.split(':'))

# These create three separate lists for the titles, poets, and publication dates of the individual poems.
titles = []
poets = []
dates = []
for poem in highlighted_poems_details:
  titles.append(poem[0])
  poets.append(poem[1])
  dates.append(poem[2])

# This prints out each individual poem's title, poet, and publication date in a formatted string.
for i in range(0,len(highlighted_poems_details)):
    print('The poem {} was published by {} in {}'.format(titles[i], poets[i], dates[i]))