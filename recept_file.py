from pprint import pprint
file_path = "recipes.txt" 
def file_name(file_path):
    with open(file_path) as file:
        cook_book = {}
        for line in file:
            food_name = line.strip()
            number_of_ingredients = file.readline()
            ingredients = []
            x = []
            for num in range(int(number_of_ingredients)):
                ingredient = file.readline()
                ingredients = ingredient.split(' | ')
                ingredient_dict = {}
                ingredient_dict['ingredient_name'] = ingredients[0]
                ingredient_dict['quantity'] = int(ingredients[1])
                ingredient_dict['measure'] = ingredients[2].strip()
                x.append(ingredient_dict)
            cook_book[food_name] = x
            file.readline()
        return cook_book
pprint(file_name(file_path))

def list_transformation_dict(dishes):
    dishes_d = {}
    for i in range(len(dishes)):
        dishes_d.update({dishes[i]:dishes.count(dishes[i])})
    return dishes_d


def get_shop_list_by_dishes(dishes, person_count):
    dishes_dict = {}
    dishes_dict_all = {}
    dishes_dict_tr = list_transformation_dict(dishes)
    for key, value in dishes_dict_tr.items():
        #print(value)
        for key_1, value_1 in file_name(file_path).items():
            if key == key_1:
                for a in value_1:
                    if a['ingredient_name'] not in dishes_dict.keys():
                        dishes_dict[a['ingredient_name']] = {'measure':a['measure'], 'quantity':a['quantity']*int(person_count)*value}
                        dishes_dict_all.update(dishes_dict)
                    else:
                        dishes_dict[a['ingredient_name']] = {'measure':a['measure'], 'quantity':(a['quantity']+a['quantity'])*int(person_count)*value}
                        dishes_dict_all.update(dishes_dict)
                        print(dishes_dict[a['ingredient_name']])   
                
                                             
                    
    return dishes_dict_all
#get_shop_list_by_dishes(['Омлет','Фахитос'] ,2)
pprint(get_shop_list_by_dishes(['Омлет','Омлет'] ,2))

