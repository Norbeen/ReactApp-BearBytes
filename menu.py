import json
import models
import psycopg2

f = open('dining.json')
menu = json.load(f)
for menu_item in menu:
    food_item = models.menuItem(menu_item['title'],0, menu_item['calories'],None, menu_item['types'],"Rawling's Dining Hall", menu_item['image'])
    models.db.session.add(food_item)
    models.db.session.commit()
f.close()




    
 