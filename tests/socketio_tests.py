import app, os
import unittest
import models

class socketio_test(unittest.TestCase):
    
    def test_menu_list(self):
        client =app.socketio.test_client(app.app)
        
        response = client.get_received()
        
        self.assertEqual(len(response), 1)
        from_server_connected = response[0]
        self.assertEqual(from_server_connected['name'], "menu loaded")
        
        data = from_server_connected['args'][0]
        self.assertEqual(data['breakfast_items'][0]['bf_title'], "Blueberry Pancakes")
        
    def test_launch_list1(self):
        client =app.socketio.test_client(app.app)
        
        response = client.get_received()
        
        self.assertEqual(len(response), 1)
        from_server_connected = response[0]
        self.assertEqual(from_server_connected['name'], "menu loaded")
        
        data = from_server_connected['args'][0]
        print(data)
        self.assertEqual(data['lunch_items'][0]['lunch_title'], "Batter Fried Cod ")
        
    def test_dinner_list(self):
        client =app.socketio.test_client(app.app)
        
        response = client.get_received()
        
        self.assertEqual(len(response), 1)
        from_server_connected = response[0]
        self.assertEqual(from_server_connected['name'], "menu loaded")
        
        data = from_server_connected['args'][0]
        self.assertEqual(data['dinner_items'][0]['din_title'], "Texas Pot Roast ")
        
    def test_server_disconnecting(self):
        
        client = app.socketio.test_client(app.app)
        client.emit('disconnect', {'I am disconnecting': 'disconnected'})
        response = client.get_received()
        self.assertEqual(len(response), 2)
        
        from_server = response[1]
        self.assertEqual(from_server['name'], 'disconnecting')
        
        data = from_server['args'][0]
        self.assertEqual(data['disconnect status'], 'disconnected')
        
        
if __name__ == '__main__':
    unittest.main()