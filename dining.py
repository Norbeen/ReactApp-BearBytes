
'''This python file contains the JSON format for the dining food into 3 parts  **************************

*************************** Breakfast/ Launch/ Dinner for each days Monday through Friday respectively '''


import json, random,requests

from image import*


'''This is the JSON format **************************

***************************for the breakfast at the dining'''


dining_breakfast= '''
{
    "breakfast":[
        {"monday":[
        
            {
            "title":"Blueberry Pancakes",
            "calories":"2 e.a (113 cal)"
          
            },
            
            {
            "title":"Pork Bacon",
            "calories":"2 slices(87 cal)" 
          

            },
            
            {
            "title":"Turkey Sausage Patty ",
            "calories":" 2 oz(86.4 cal)"
       

            },
            
            
            {
            "title":"Tator Tots ",
            "calories": " 1/2 cup(202.3 cal)"
           
            },
            
            {
            "title":"Scrambled Eggs ",
            "calories":" 1/2 cup(202.3 cal)"
           
            },
            
            {
            "title":"Broccoli Quiche 1 slice",
            "calories":" (311.3 cal)"
       
            },
            
            
            {
            "title":"Oatmeal ",
            "calories":"4 oz(71.6 cal) "
          
            },
            
            
            {
            "title":"Grits ",
            "calories":" 4 oz(72.7 cal)"
           
            }
        ]
        }
        ,

        { "tuesday":[
            {
            "title":"Biscuits ",
            "calories":" 1 ea (198.5 cal)"
          
            },

            {
            "title":"Country Ham ",
            "calories":" 20z meat(67.2 cal)"
            

            },
            
            
            {
            "title":"Turkey Sausage Links ",
            "calories":" 1 ea(34.4 cal)"
           

            },
            
            
            {
            "title":"Potatoes O'Brien ",
            "calories":"1/2 cup(101.6 cal) "
            
            },
            
            
            {
            "title":"Scrambled Eggs ",
            "calories":" 1/2 cup(202.3 cal)"
           
            },
            
            
            {
            "title":"Scrambled Eggs with Cheese ",
            "calories":" 1/2 cup(246.3 cal)"
           
            },
            
            
            {
            "title":"Oatmeal ",
            "calories":" 4 oz(71.6 cal)"
           
            },
            
            
            {
            "title":"Grits ",
            "calories":"4 oz(72.7 cal) "
          
            }
        ]
        }
            ,
        { "wednesday":[
        
            {
            "title":"Crispy Stuffed French Toast ",
            "calories":"1 ea(563 cal) "
            
            },

            {
            "title":"Corned Beef Hash",
            "calories":" 1 serving(204 cal)"
            

            },
            
            
            {
            "title":"Turkey Sausage Patty ",
            "calories":" 2 oz(86.4 cal)"
         

            },
            
            
            {
            "title":"Crispy Hashbrowns ",
            "calories":"1/2 cup(202.3 cal) "
        
            },
            
            
            {
            "title":"Scrambled Eggs ",
            "calories":" 1/2 cup(202.3 cal)"
          
            },
            
            
            {
            "title":"Denver Scrambled Eggs ",
            "calories":" 1/2 cup(141.7 cal)"
          
            },
            
            
            {
            "title":"Oatmeal ",
            "calories":" 4 oz(71.6 cal)"
          
            },
            
            
            {
            "title":"Grits ",
            "calories":"4 oz(72.7 cal) "
          
            }
            
        ]
        }
            ,
        {"thursday":[
        
            {
            "title":"Banana Pancakes ",
            "calories":"2 ea(173.8 cal) "
          
            },

            {
            "title":"Pork Bacon",
            "calories":" 2 slice(87 cal)"
         

            },
            
            
            {
            "title":"Turkey Sausage Links ",
            "calories":" 2 ea(68.9 cal)"
           

            },
            
            
            {
            "title":"Scrambled Eggs ",
            "calories":"1/2 cup(202.3 cal) "
           
            },
            
            
             {
            "title":"Potatoes O'Brien ",
            "calories":" 1/2 cup(101.6 cal)"
          
            },

            {
            "title":"Onion and Cheese Quiche ",
            "calories":"1 slice(180.7 cal) "
       

            },
            
            
            {
            "title":"Oatmeal ",
            "calories":" 4 oz(71.6 cal)"
           

            },
            
            
            {
            "title":"Grits ",
            "calories":" 4oz(72.7 cal)"
            
            }]
            
        }
            ,
        {"friday":[
        
             {
            "title":"Biscuits ",
            "calories":" 1 ea (198.5 cal)"
          
            },

            {
            "title":"Country Ham ",
            "calories":"20z meat(67.2 cal) "
           

            },
            
            
            {
            "title":"Turkey Sausage Patty ",
            "calories":" 2 0z(86.4 cal)"
           

            },
            
            
            {
            "title":"Tator Tots ",
            "calories":" 1/2 cup(168.7 cal)"
          
            },
            
            
             {
            "title":"Scrambled Eggs ",
            "calories":" 1/2 cup(202.3 cal)"
          
            },
            
            
            {
            "title":"Scrambled Eggs with Cheese ",
            "calories":"1/2 cup(246.3 cal) "
            
            },
            
            
            {
            "title":"Oatmeal ",
            "calories":" 4 oz(71.6 cal)"
           
            },
            
            
            {
            "title":"Grits ",
            "calories":" 4 oz(72.7 cal)"
           
            }
        ]}
    ]

}
'''

# # storing data for breakfast 
# ranNum = random.randint(0,2)
# data= json.loads(dining_breakfast)
# mondayList = data["breakfast"][0]["monday"][ranNum]
# print(mondayList)
# # data["breakfast"][0]["monday"][0]["title"])





'''This is the JSON format **************************

***************************for the launch at the dining'''




dining_launch= '''
{
    "launch":[
        {"monday":[
        
            {
            "title":"Batter Fried Cod ",
            "calories":"4 oz (295 cal) "
           
            },

            {
            "title":"Chicken Breast Newport ",
            "calories":" 4 oz(150.9 cal)"
            

            },
            
            
            {
            "title":"Herbed Rice Pilaf ",
            "calories":"4 oz(144cal) "
          

            },
            
            
            {
            "title":"Parmesan Roasted Carrots ",
            "calories":"4 oz(92.7cal)"
           
            },
            
            
            {
            "title":"Cabbage Rolls ",
            "calories":" 4 oz(87.2 cal)"
     
            },
            
            
            {
            "title":"Sauteed Kale ",
            "calories":" 4 oz(92.7 cal)"
           
            },
            
            
            {
            "title":"Parmesan Roasted Potatoes ",
            "calories":" 4 oz(92.7 cal)"
          
            },
            
            
            {
            "title":"Pasta Bar ",
            "calories":" 6 oz(345 cal)"
          
            },
            
            {
            "title":"Hamburger on Bun 1 sandwich",
            "calories":"(426.9 cal) "
          
            },

            {
            "title":"Caramelized Onions ",
            "calories":" 1 oz(36.1 cal)"
          

            },
            
            
            {
            "title":"American Cheese Slice ",
            "calories":"1 slice(51.9 cal) "
           

            },
            
            
            {
            "title":"Sauteed Mushrooms ",
            "calories":"1 oz(20.4 cal) "
           
            },
            
            
            {
            "title":"Coleslaw ",
            "calories":" 1/2 oz(9.7 cal)"
           
            },
            
            
            {
            "title":"Sliced Jalapeno ",
            "calories":" 1/2 oz(3.8 cal)"
           
            },
            
            
            {
            "title":"Hard Fried Eggs ",
            "calories":" 1 ea(83 cal)"
     
            },
            
            
            {
            "title":"Pork Bacon ",
            "calories":" 2 slices(87 cal)"
        
            },
            
            
            {
            "title":"French Fries",
            "calories":" 4 oz(224.3 cal)"
          
            },
            
            
            {
            "title":"Garden Burger",
            "calories":" 1 ea(151.4 cal)"
          
            }]
        }
        ,

        {"tuesday":[
        
            {
            "title":"Grilled Cheese Sandwich ",
            "calories":" 1 sandwich(378 cal)"
          
            },

            {
            "title":"French Frie ",
            "calories":"4oz(224.3 cal) "
      

            },
            
            
            {
            "title":"Garden Burger ",
            "calories":"1 ea(362.5 cal) "

            },
            
            
            {
            "title":"Turkey Burger ",
            "calories":" 1 sandwitch(362.5 cal)"
            
            },
            
            
            {
            "title":"Chana Masala ",
            "calories":" 4 oz(122.1 cal)"
   
            },
            
            
            {
            "title":"Lyonnaise Zucchini & Summer Squash ",
            "calories":"4 oz(150.7 cal) "
       
            },
            
            
            {
            "title":"Sour Cream Chives Mashed Potatoes ",
            "calories":" 4 oz(150.7 cal)"
        
            },
            
            
            {
            "title":"Herb Roasted Pork ",
            "calories":"4 oz meat(254 cal)"
          
            },
            
            {
            "title":"Au Jus ",
            "calories":" 1 oz(1.7 cal)"
         
            },

            {
            "title":"Grilled Onions ",
            "calories":" 2tbsp(37.1 cal)"
           

            },
            
            
            {
            "title":"Baked Apples ",
            "calories":" 1 ea(252.1 cal)"
      

            },
            
            
            {
            "title":"Dinner Roll ",
            "calories":" 1 ea(87.9 cal)"
         
            },
            
            
            {
            "title":"Fish Sandwich ",
            "calories":" 1 ea464.3 cal)"
       
            },
            
            
            {
            "title":"Garden Burger ",
            "calories":" 1 ea(151.4 cal)"
         
            },
            
            
            {
            "title":"Turkey Burger ",
            "calories":" 1 sandwich(362.5 cal)"
     
            }]
        }
            ,
            
          {"wednesday":[
          
            {
            "title":"Braized Beef Tips ",
            "calories":"6oz(227.9 cal)"
           
            },

            {
            "title":"Baked Fish ",
            "calories":" 4 oz(264.7 cal)"
           

            },
            
            
            {
            "title":"Garlic Mashed ",
            "calories":"4 oz(124.6 cal) "
      

            },
            
            
            {
            "title":"Fried Brussels Sprouts ",
            "calories":"4 oz(130.1 cal) "
           
            },
            
            
            {
            "title":"Tofu Marsala ",
            "calories":"4 oz(112.8 cal) "
          
            },
            
            
            {
            "title":"Broccoli Rice Casserole ",
            "calories":"4 oz(134.6 cal) "
         
            },
            
            
            {
            "title":"Lemon & Parsley Roasted Cauliflower ",
            "calories":"4 oz(100.8 cal) "
           
            },
            
            
            {
            "title":"Pasta Bar ",
            "calories":" 6 oz(345 cal)"
        
            },
            
            {
            "title":"Cheese Quesadillas ",
            "calories":"1 ea (445.9 cal)"
         
            },

            {
            "title":"Fresh Fried Chipotle BBQ Chips ",
            "calories":" 4 oz(281.8 cal)"
          

            },
            
            
            {
            "title":"Spicy Tomato Habanero Salsa ",
            "calories":"1 floz (7.1 cal) "
    

            },
            
            
            {
            "title":"Garden Burger ",
            "calories":" 1 ea (151.4 cal)"
          
            },
            
            
            {
            "title":"Turkey Burger ",
            "calories":" 1 sandwich(362.5 cal)"
          
            
        }]
           
          }
            ,
        {"thursday":[
        
            {
            "title":"Thai BBQ Chicken ",
            "calories":" 1 ea(215.7 cal)"
          
            },

            {
            "title":"Stuffed Shells Florentine ",
            "calories":"2 ea(231.7 cal) "
           

            },
            
            
            {
            "title":"Jasmine Pilaf with Mushrooms and Peas ",
            "calories":"4 oz(109.3 cal) "
           

            },
            
            
            {
            "title":"Cheese Ravioli ",
            "calories":"1/2 cup(238.6 cal) "
      
            },
            
            
            {
            "title":"Sauteed Spinach ",
            "calories":" 4 oz(60cal)"
        
            },
            
            
            {
            "title":"Roasted Mixed Vegetables ",
            "calories":"4 oz(60cal) "
         
            },
            
            
            {
            "title":"Chicken Fried Rice ",
            "calories":" 1 cup(280.1 cal)"
         
            },
            
            
            {
            "title":"Pulled Pork Sandwich ",
            "calories":" 1 serving(632.5 cal)"
          
            },
            
            {
            "title":"Onion Rings ",
            "calories":" 4 oz(320.7 cal)"
           
            },

            {
            "title":"Garden Burger ",
            "calories":"1 ea(151.4 cal) "
      

            },
            
            
            {
            "title":"Turkey Burger ",
            "calories":" 1 ea(362.5 cal)"
      

            }]
        }
            ,
        {"friday":[
        
            {
            "title":"Sesame Garlic Shrimp ",
            "calories":"4 oz(266.8 cal) "
          
            },

            {
            "title":"Garlic Rosemary Pork Loin ",
            "calories":" 4 oz(246.3 cal)"
         

            },
            {
            "title":"Basmati Rice ",
            "calories":"4 oz(147.4 cal) "
          

            },
            
            
            {
            "title":"Chard and Spring Pea Risotto ",
            "calories":" 4 oz(71 cal)"
            
            },
            
            
            {
            "title":"Cauliflower and Snow Peas ",
            "calories":"4 oz(64.3 cal)"
      
            },
            
            
            {
            "title":"Carrots with Ginger ",
            "calories":" 4 oz(61.5 cal)"
         
            },
            
            
            {
            "title":"Ice Cream Sundae Bar ",
            "calories":"1 serving(48.1 cal) "
       
            },
            
            
            {
            "title":"Red Velvet Cake ",
            "calories":" 1 slice(583.1 cal)"
           
            },
            
            {
            "title":"Barbeque Chicken Sub ",
            "calories":" 1 ea(669.3 cal)"
      
            },
            {
            "title":"French Fries ",
            "calories":"4 oz(224.3 cal) "
          
            },
            
            
            {
            "title":"Garden Burger ",
            "calories":" 1 ea(151.4 cal)"


            },
            
            
            {
            "title":"Turkey Burger ",
            "calories":" 1 ea(362.5 cal)"
           

            }
            ]
        }
    ]

}
'''



'''This is the JSON format **************************

***************************for the dinner at the dining'''



dining_dinner = '''
{
    "dinner":[
        {"monday":[
        
            {
            "title":"Texas Pot Roast ",
            "calories":" 4 oz(138.6 cal)"
        
            },

            {
            "title":"Barbecued Pork Chop ",
            "calories":" 1 ea(252.2 cal)"


            },
            
            
            {
            "title":"Steamed Brown Rice ",
            "calories":" 4 oz(137 cal)"
         

            },
            
            
            {
            "title":"Vegetarian Boston Baked Beans ",
            "calories":"4 oz(144.1 cal) "
            
            },
            
            
            {
            "title":"Beef Gravy ",
            "calories":" 1 oz(9.2 cal)"
            
            },
            
            
            {
            "title":"Carrots and Broccoli ",
            "calories":"4 oz(59 cal) "
      
            },
            
            
            {
            "title":"Eggplant Creole ",
            "calories":" 4 oz(32.6 cal)"
          
            },
            
            
            {
            "title":"Vegetable Fried Rice ",
            "calories":" 4 oz(158 cal)"
      
            },
            
            {
            "title":"Asian Vegetable Blend ",
            "calories":" 4 oz(41.8 cal)"
            }]
        }
        ,

        {"tuesday":[
            {
            "title":"Hard Shell Beef Tacos ",
            "calories":"1 ea(285.9 cal) "

            },

            {
            "title":"Grilled Adobo Chicken ",
            "calories":"4 oz(254.6 cal) "
      

            },
            
            
            {
            "title":"Mexican Rice ",
            "calories":" 4 oz(140.3 cal)"
    

            },
            
            
            {
            "title":"Grilled Corn ",
            "calories":"1 ea(163.4 cal) "
    
            },
            
            
            {
            "title":"Chipotle Pinto Beans ",
            "calories":"4oz(109.1 cal) "
           
            },
            
            
            {
            "title":"Tofu and Veggie Scampi ",
            "calories":"4 oz(164.3 cal) "
     
            }]
        }
            ,
            
        {"wednesday":[
        
            {
            "title":"Southern Fried Chicken ",
            "calories":" 1 serving(534.7 cal)"
        
            },

            {
            "title":"Baked Chicken ",
            "calories":"1 ea(160.7 cal) "
           

            },
            
            
            {
            "title":"Salisbury Steak ",
            "calories":" 1 ea(275.5 cal)"


            },
            
            
            {
            "title":"Beef Gravy ",
            "calories":"1 oz(9.2 cal) "
           
            },
            
            
            {
            "title":"White Rice ",
            "calories":" 4oz(150.4 cal)"
          
            },
            
            
            {
            "title":"Signature Macaroni and Cheese ",
            "calories":" 4 oz(63.2 cal)"
          
            },
            
            
            {
            "title":"Vegetarian Collard Greens ",
            "calories":"4oz (63.2 cal) "
        
            },
            
            
            {
            "title":"Steamed Broccoli ",
            "calories":"4oz(38.7 cal) "
        
            },
            
            {
            "title":"Crispy Vegan Chicken Tenders ",
            "calories":"2 ea(180 cal) "
       
            },

            {
            "title":"Vegetarian Collard Greens ",
            "calories":"4oz (63.2 cal) "
           

            },
            
            
            {
            "title":"Baked Sweet Potato ",
            "calories":" 1 ea (135.9 cal)"
        

            }]
        }
            ,
        {"thursday":[
        
            {
            "title":"Beef Lo Mein ",
            "calories":"4 oz(242.5 cal) "
      
            },

            {
            "title":"Honey Ginger Glazed Chicken ",
            "calories":"4 oz(267.6 cal) "
       

            },
            
            
            {
            
            "title":"Brown Fried Rice ",
            "calories":" 4 oz(181.4 cal)"
       

            },
            
            
            {
            "title":"Squash, Zucchini Peppers and Carrots ",
            "calories":"4 oz(51 cal) "
      
            },
            
            
            {
            "title":"Asparagus with Garlic ",
            "calories":" 4 oz(53.9 cal)"
        
            },
            
            
            {
            "title":"Southwestern Black Bean Pot Pie ",
            "calories":"4 oz(133.6 cal) "
        
            }]
        }
            ,
        {"friday":[
        
            {
            "title":"Fried Fish ",
            "calories":" 1 ea(254.4 cal)"

            },

            {
            "title":"Creole Spaghetti ",
            "calories":"4 oz(140.2 cal) "
    

            },
            
            
            {
            "title":"Classic Fried Green Tomatoes ",
            "calories":" 3 slice(314.6 cal)"
 

            },
            
            
            {
            "title":"Cheese Grits ",
            "calories":"4 oz(82.9 cal) "
 
            },
            
            
            {
            "title":"Corn with Pimento ",
            "calories":"4 oz(37.6 cal) "
         
            },
            
            
            {
            "title":"Vegan Meatballs ",
            "calories":"3 ea(150 cal) "
            },
            
            
            {
            "title":"Chickpeas and Spinach ",
            "calories":"4 oz(134 cal) "
            
            },
            
            
            {
            "title":"Spaghetti ",
            "calories":"4 oz(178 cal) "
            },
            
            {
            "title":"Marinara Sauce ",
            "calories":" 1 oz(13.8 cal)"
           
            }]
        }
    ]

}
'''


# **********************      Extracting the required item from the JSON format      ********************************

# loading data from the json file using json loads

# data= json.loads(dining_breakfast)



#******************** Trying to append all the titles  and calories together to make a list  **************************

def title_list(food_time, num, day, title, calories):
    
    
    # ***************************************
    # ********** This is the list for breakfast title and calories ******************** #
    # ****************************************
    
    breakfast_monday_list = []
    breakfast_tuesday_list = []
    breakfast_wednesday_list = []
    breakfast_thursday_list = []
    breakfast_friday_list = []
    
    
    # ***************************************
    # ********** This is the list for launch title and calories ********************* #
    # ****************************************
    
    launch_monday_list = []
    launch_tuesday_list = []
    launch_wednesday_list = []
    launch_thursday_list = []
    launch_friday_list = []
    
    
    # ***************************************
    # ********** This is the list for dinner title and calories ********************* #
    # ****************************************
    
    dinner_monday_list = []
    dinner_tuesday_list = []
    dinner_wednesday_list = []
    dinner_thursday_list = []
    dinner_friday_list = []
    
    
    day_title_list = []
    day_calories_list = []
    
# This if - else statement loads the json data based on what is passed- like dinner/ launch/ breakfast 

    if food_time == "breakfast":
        data= json.loads(dining_breakfast)
        list_size= len(data[food_time][num][day])
    elif food_time == "launch":
        data= json.loads(dining_launch)
        list_size= len(data[food_time][num][day])
    elif food_time =="dinner":
        data= json.loads(dining_dinner)
        list_size= len(data[food_time][num][day])
        
        
        
# This function can be used for all the launch, dinner and breakfast for mon- fri, just have to pass value to the parameters in the title_list function 


    for i in range(list_size):
        day_title = data[food_time][num][day][i][title]
        day_calories = data[food_time][num][day][i][calories]
        day_title_list.append(day_title)
        day_calories_list.append(day_calories)
    return day_title_list, day_calories_list
        
 

breakfast_monday_list = title_list("breakfast", 0, "monday", "title", "calories")
breakfast_tuesday_list = title_list("breakfast", 1, "tuesday", "title", "calories")
breakfast_wednesday_list = title_list("breakfast", 2, "wednesday", "title", "calories")
breakfast_thursday_list = title_list("breakfast", 3, "thursday", "title", "calories")
breakfast_friday_list = title_list("breakfast", 4, "friday","title", "calories")
 
 
#Adding all the breakfast titles to breakfast_title
 
breakfast_title= []
breakfast_calories = []
breakfast_title = breakfast_monday_list[0] + breakfast_tuesday_list[0] + breakfast_wednesday_list[0] +breakfast_thursday_list[0] +  breakfast_friday_list[0]
breakfast_calories = breakfast_monday_list[1] + breakfast_tuesday_list[1] + breakfast_wednesday_list[1] +breakfast_thursday_list[1] +  breakfast_friday_list[1]
# print(breakfast_title)
# print(breakfast_calories)

 
 
 
# **************************************************************************************************************************************************************
# *********************************   This is for the launch **********************************************************************************************

# **************************************************************************************************************************************************************



launch_monday_list = title_list("launch", 0, "monday", "title", "calories")
launch_tuesday_list = title_list("launch", 1, "tuesday", "title", "calories")
launch_wednesday_list = title_list("launch", 2, "wednesday", "title", "calories")
launch_thursday_list = title_list("launch", 3, "thursday", "title", "calories")
launch_friday_list = title_list("launch", 4, "friday","title", "calories")
 
 
#Adding all the breakfast titles to breakfast_title
 
launch_title= []
launch_calories = []
launch_title = launch_monday_list[0] + launch_tuesday_list[0] + launch_wednesday_list[0] + launch_thursday_list[0] +  launch_friday_list[0]
launch_calories = launch_monday_list[1] + launch_tuesday_list[1] + launch_wednesday_list[1] + launch_thursday_list[1] +  launch_friday_list[1]
# print(launch_title)
# print(launch_calories)


 
# **************************************************************************************************************************************************************
# *********************************   This is for the dinner **********************************************************************************************

# **************************************************************************************************************************************************************


dinner_monday_list = title_list("dinner", 0, "monday", "title", "calories")
dinner_tuesday_list = title_list("dinner", 1, "tuesday", "title", "calories")
dinner_wednesday_list = title_list("dinner", 2, "wednesday", "title", "calories")
dinner_thursday_list = title_list("dinner", 3, "thursday", "title", "calories")
dinner_friday_list = title_list("dinner", 4, "friday","title", "calories")
 
 
#Adding all the breakfast titles to breakfast_title
 
dinner_title= []
dinner_calories = []
dinner_title = dinner_monday_list[0] + dinner_tuesday_list[0] + dinner_wednesday_list[0] + dinner_thursday_list[0] +  dinner_friday_list[0]
dinner_calories = dinner_monday_list[1] + dinner_tuesday_list[1] + dinner_wednesday_list[1] + dinner_thursday_list[1] +  dinner_friday_list[1]
# print(dinner_title)
# print(dinner_calories)


# *******************************************************************************************************************************************************
# ********************* HERE ARE THE IMPORTANT VAIRBALES THAT CONATAINS VALUES ***************************************************************************

# *******************************************************************************************************************************************************
'''
breakfast_title             ***********contains ******      list of title served in breakfast

breakfast_calories          ***********contains ******      list of calories served in breakfast

launch_title                ***********contains ******      list of title served in breakfast

launch_calories             ***********contains ******      list of calories served in breakfast

dinner_title                ***********contains ******      list of title served in breakfast 

dinner_calories             ***********contains ******      list of calories served in breakfast

'''


# **********************************************************************************************************************************************************



#Adding all the title together and calories together 
# So we know the length of title for breakfast is - 0 to 39 
# Length of title for launch is - 40 - 108
#Length of title for dinenr is -  109 - 150


joined_title = breakfast_title + launch_title + dinner_title
joined_calorie = breakfast_calories + launch_calories + dinner_calories 


# print("Length of title for breakfast is", len(breakfast_title))
# print("Length of title for launch is", len(launch_title))
# print("Length of title for dinner is", len(dinner_title))


#function to fetch image for all the items, works, already fetched image

# def image_list(name):
#     image_list = []
#     url ="https://api.unsplash.com/search/photos?query="+ name + "&client_id=sjauyr_gDNXxASXnt9fH3hCPitColEzzz8DVssM12SI"
#     response = requests.get(url)
#     json_body = response.json()
#     image = json_body["results"][0]["urls"]["small"]
#     image_list.append(image)
#     return image_list

# for i in range(len(launch_title)):
#     name= launch_title[i]
#     print(image_list(name))
    
#passed image list from image.py file used as passed_image_list, it contains the list of image combined for breakfast, launch and dinenr

passed_image_list = image_list()


def combined_list():
    return joined_title , joined_calorie, passed_image_list
    
# print(combined_list())