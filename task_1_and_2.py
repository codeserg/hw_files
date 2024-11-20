from pprint import pprint

def read_book (filename):
    dish ={}
    cook_book={}

    with open (filename, encoding='utf-8') as f:
        
        dish = f.readline().strip()
        while dish:
            ing_count = int(f.readline())
            ingredients=[]
            for _ in range(ing_count):

                ingredient_line = f.readline()
                ingredient_list = ingredient_line.split('|')
                ingredient_list_cleared= [x.strip() for x in ingredient_list]
                
                ingredient={'ingredient_name': ingredient_list_cleared[0], 
                            'quantity': int(ingredient_list_cleared[1]), 
                            'measure': ingredient_list_cleared[2]}
                
                ingredients.append(ingredient)

            
            cook_book[dish] = ingredients
            
            f.readline()  # чтение пустой строки между блюдами
            dish = f.readline().strip() # чтение следующего блюда чтобы правильно сработал цикл
    
    return cook_book  

def get_shop_list_by_dishes(dishes, person_count , cook_book):
    
    shop_list ={}
    
    for dish in dishes:
        for ingredient in cook_book[dish]:
            
            quantity = ingredient['quantity']*person_count
            ing_name = ingredient['ingredient_name']
            if ing_name in shop_list:
                shop_list[ing_name]['quantity'] +=quantity
            else:
                measure = ingredient['measure']
                shop_list[ing_name] = {'measure': measure,'quantity': quantity}
    
    return shop_list

# Решение задачи №1 - функция read_book
my_cook_book = read_book('recipes.txt')

# Решение задачи №2
shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Яичница'], 5, my_cook_book)

pprint(shop_list)

