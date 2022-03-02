import scraper
import rating_adj
import copy

print("The program has started...")

# Getting the original top 20 movie
og_top20 = scraper.scrape()

# Deep copy the original Top20 movie list with copying every dictionary inside it
copy_top20 = []
for index in og_top20:
    d2 = copy.deepcopy(index)
    copy_top20.append(d2)

# Penalize the Top20 list
p_list = rating_adj.penalizer(copy_top20)


print("The program finished running!")
