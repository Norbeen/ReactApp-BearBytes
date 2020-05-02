import app, os
import unittest
import models

class socketio_test(unittest.TestCase):
    
    # def test_menu_list(self):
    #     client =app.socketio.test_client(app.app)
        
    #     response = client.get_received()
        
    #     self.assertEqual(len(response), 1)
    #     from_server_connected = response[0]
    #     self.assertEqual(from_server_connected['name'], "menu loaded")
        
    #     data = from_server_connected['args'][0]
    #     self.assertEqual(data['breakfast_items'][0]['bf_title'], "Blueberry Pancakes")
        
    # def test_launch_list1(self):
    #     client =app.socketio.test_client(app.app)
        
    #     response = client.get_received()
        
    #     self.assertEqual(len(response), 1)
    #     from_server_connected = response[0]
    #     self.assertEqual(from_server_connected['name'], "menu loaded")
        
    #     data = from_server_connected['args'][0]
    #     print(data)
    #     self.assertEqual(data['lunch_items'][0]['lunch_title'], "Batter Fried Cod ")
        
    # def test_dinner_list(self):
    #     client =app.socketio.test_client(app.app)
        
    #     response = client.get_received()
        
    #     self.assertEqual(len(response), 1)
    #     from_server_connected = response[0]
    #     self.assertEqual(from_server_connected['name'], "menu loaded")
        
    #     data = from_server_connected['args'][0]
    #     self.assertEqual(data['dinner_items'][0]['din_title'], "Texas Pot Roast ")
        
    def test_server_disconnecting(self):
        
        client = app.socketio.test_client(app.app)
        client.emit('disconnect', {'I am disconnecting': 'disconnected'})
        response = client.get_received()
        self.assertEqual(len(response), 2)
        
        from_server = response[1]
        self.assertEqual(from_server['name'], 'disconnecting')
        
        data = from_server['args'][0]
        self.assertEqual(data['disconnect status'], True)
        
    def test_on_connect_breakfast(self):
        client = app.socketio.test_client(app.app)
        response = client.get_received()
       
        self.assertEqual(len(response), 1)
        from_server = response[0]
        self.assertEqual(
        from_server["name"],
        "menu loaded"
        )
        breakfast_data = models.menuItem.query.filter_by(Utypes='breakfast').all()
        breakfast_list = []
        for bf_item in breakfast_data:
            breakfast_list.append({
                'bf_title' : bf_item.Utitle,
                'bf_averageRating' : bf_item.Urating,
                'bf_calories' : bf_item.Unutrition,
                'bf_reviews' : bf_item.Ureviews,
                'bf_time' : bf_item.Utypes,
                'bf_location' : bf_item.Ulocation,
                'bf_imageLink' : bf_item.Uimage
            })
           
        data = from_server["args"][0]
        self.assertEqual(data["breakfast_items"], breakfast_list)
        
    def test_on_connect_lunch(self):
        client = app.socketio.test_client(app.app)
        response = client.get_received()
       
        self.assertEqual(len(response), 1)
        from_server = response[0]
        self.assertEqual(
        from_server["name"],
        "menu loaded"
        )
        lunch_data = models.menuItem.query.filter_by(Utypes='lunch').all()
        lunch_list = []
        for lunch_item in lunch_data:
            lunch_list.append({
                'lunch_title' : lunch_item.Utitle,
                'lunch_averageRating' : lunch_item.Urating,
                'lunch_calories' : lunch_item.Unutrition,
                'lunch_reviews' : lunch_item.Ureviews,
                'lunch_time' : lunch_item.Utypes,
                'lunch_location' : lunch_item.Ulocation,
                'lunch_imageLink' : lunch_item.Uimage
            })
           
        data = from_server["args"][0]
        self.assertEqual(data["lunch_items"], lunch_list)
        
    def test_on_connect_dinner(self):
        client = app.socketio.test_client(app.app)
        response = client.get_received()
       
        self.assertEqual(len(response), 1)
        from_server = response[0]
        self.assertEqual(
        from_server["name"],
        "menu loaded"
        )
        dinner_data = models.menuItem.query.filter_by(Utypes='dinner').all()
        dinner_list = []
        for dinner_item in dinner_data:
            dinner_list.append({
                'din_title' : dinner_item.Utitle,
                'din_averageRating' : dinner_item.Urating,
                'din_calories' : dinner_item.Unutrition,
                'din_reviews' : dinner_item.Ureviews,
                'din_time' : dinner_item.Utypes,
                'din_location' : dinner_item.Ulocation,
                'din_imageLink' : dinner_item.Uimage
        })
           
        data = from_server["args"][0]
        self.assertEqual(data["dinner_items"], dinner_list)
        
        
if __name__ == '__main__':
    unittest.main()