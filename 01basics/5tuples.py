
tea_types = ("Black", "White")
more_teas = ("Herbal","Earl Grey")

# more_teas[0] = "Lemon"
# # error

all_teas = tea_types + more_teas
print(all_teas)

more_teas = ("Herbal", "Herbal", "Earl Grey")
print(more_teas.count("Herbal"))

(black, white) = tea_types
print(black,white)