import scraper
import rating_adj
import copy
import json

print("The program has started...")

# Getting the original top 20 movie
og_top20 = scraper.scrape()

# Writing original top 20 movie into JSON file
with open('top20_movie.json', 'w', encoding='utf-8') as f:
    json.dump(og_top20, f, ensure_ascii=False, indent=4)

# Deep copy the original Top20 movie list with copying every dictionary inside it
copy_top20 = []
for index in og_top20:
    d2 = copy.deepcopy(index)
    copy_top20.append(d2)

# Penalize the Top20 list
p_list = rating_adj.penalizer(copy_top20)

# Modifying movie ratings according to won oscar number
# PO means Penalized and Oscar calculatored
po_list = rating_adj.oscar_calculator(p_list)

# Sorting the penalized and oscar calculated list into descending order
po_list.sort(reverse=True, key=lambda i: i['rating'])

print("PO_LIST:\n")
print(po_list)


print("The program finished running!")
