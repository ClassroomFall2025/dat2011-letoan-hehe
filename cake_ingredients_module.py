def calculate_ingredients(number_of_bean_cakes, number_of_mix_cake, number_of_other_cake):
    ingredients = {
        "Sugar" : "",
        "Beans": "" 
        }
    ingredients["Sugar"] = round((number_of_bean_cakes * 0.04 + number_of_mix_cake *0.06 + number_of_other_cake * 0.05),1)
    ingredients["Beans"] = round((number_of_bean_cakes * 0.07 + number_of_mix_cake *0 + number_of_other_cake * 0.02),1)
    return ingredients