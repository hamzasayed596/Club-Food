import os
import random
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

bot_token = os.environ.get("SLACK_BOT_TOKEN")
app_token = os.environ.get("SLACK_APP_TOKEN")
app = App(token = bot_token)

food = ["Koshary Small" ,"Falafel Sandwich" ,"Fries" ,"Koshary Large" ,"Egg Sandwich" ,"Cheese Sandwich" ,"Macaroni with Tomato Sauce" ,"Fries with Cheese" ,"Foul Sandwich" ,"Lentil Soup" ,"Alexandrian Liver Sandwich" ,"Hot Dog Sandwich" ,"Alexandrian Sausage Sandwich" ,"Chicken Shawarma Roll" ,"Beef Shawarma Roll" ,"Chicken Crepe" ,"Macaroni Béchamel" ,"Beef Burger" ,"Vegetable Pizza (Small)" ,"Tuna Sandwich" ,"Chicken Burger" ,"Cheese Burger" ,"Chicken Rice Meal" ,"Fried Chicken (1 Piece)" ,"Chicken Pasta" ,"Chicken Noodles"  ,"Fettuccine Alfredo" ,"Grilled Kofta Meal" ,"Chicken Roll" ,"Chicken Shawarma Plate" ,"Rice with Vegetables" ,"Beef Crepe" ,"Spaghetti Bolognese" ,"Crispy Chicken Meal" ,"Meat Shawarma Plate" ,"Grilled Chicken Quarter" ,"Fried Chicken (2 Pieces)" ,"Chicken Pane Meal" ,"Rice with Beef" ,"Shish Tawook" ,"Chicken Curry" ,"BBQ Chicken Wings" ,"Chicken Fajita" ,"Double Burger" ,"Chicken Escalope" ,"Chicken Teriyaki" ,"Chicken Steak" ,"Grilled Chicken Half" ,"Grilled Liver Plate" ,"Beef Steak" ,"Chicken Fillet" ,"Chicken Cordon Bleu" ,"Chicken Parmesan" ,"Beef Stroganoff" ,"Chicken Gratin" ,"Chicken Alfredo" ,"Chicken BBQ Pizza (Medium)" ,"Margherita Pizza (Medium)" ,"Seafood Pasta" ,"Beef Lasagna" ,"Chicken Mushroom Pasta" ,"Chicken Fettuccine" ,"Mix Grill Meal" ,"Grilled Fish Fillet" ,"Chicken Pesto Pasta" ,"Pepperoni Pizza (Medium)" ,"Seafood Rice" ,"Chicken & Shrimp Plate" ,"Fried Shrimp Meal" ,"Shrimp Sandwich" ,"Chicken Tandoori" ,"Grilled Shrimp" ,"Mixed Seafood Pasta" ,"Beef BBQ Pizza (Large)", "Shrimp Fajita" ,"Beef Steak with Rice" ,"Salmon Sandwich" ,"Chicken Risotto" ,"Shrimp Alfredo Pasta" ,"Fried Calamari" ,"Beef Mushroom Sauce Plate" ,"Chicken & Mushroom Pizza (Large)" ,"Chicken Teriyaki Rice Bowl" ,"Seafood Pizza (Large)" ,"Beef Fajita" ,"Chicken Supreme Pizza (Large)" ,"Grilled Salmon", "Shrimp & Calamari Mix", "Beef Pepper Steak", "Grilled Mixed Seafood", "Shrimp & Chicken Combo","Grilled Lamb Chops", "Chicken & Beef Combo","Grilled Beef Ribs", "Chicken & Shrimp Alfredo" ,"Shrimp Risotto", "Beef Tenderloin", "Salmon Fillet with Vegetables", "Mixed Grill Deluxe", "Surf & Turf (Steak + Shrimp)"]
food_cost = [35, 35, 40, 50, 50, 55, 55, 60, 60, 60, 65, 70, 70, 75, 80, 80, 85, 85, 85, 85, 90, 95, 95, 95, 95, 95, 100, 100, 100, 100, 100, 105, 110, 110, 115, 115, 120, 120, 120, 125, 125, 125, 130, 130, 130, 135, 135, 140, 140, 145, 145, 150, 150, 155, 155, 160, 160, 160, 165, 165, 165, 170, 175, 175, 175, 180, 180, 185, 185, 185, 190, 190, 195, 195, 200, 200, 205, 205, 210, 210, 215, 215, 220, 225, 230, 230, 235, 235, 240, 245, 250, 260, 265, 270, 275, 280, 285, 290, 295, 300]
drink = ["Small Water Bottle", "Tea (Black)", "Espresso", "Large Water Bottle", "Juice Box (Small)", "Milk Tea", "Instant Coffee (Small)", "Hummus Drink", "Hot Cocoa", "Mint Tea", "Fresh Lemon Juice", "Sugarcane Juice", "Fresh Mango Juice", "Fresh Orange Juice", "Espresso Double", "Guava Juice", "Strawberry Juice", "Lemon Mint Juice", "Carrot Juice", "Apple Juice", "Mint Lemonade", "Pomegranate Juice", "Watermelon Juice", "Peach Juice Bottle", "Fruit Mix Juice", "Pepsi Can", "Coca-Cola Can", "Fresh Pineapple Juice", "Sprite Can", "7up Can", "Fresh Kiwi Juice", "Fanta Orange Can", "Mirinda Can", "Mountain Dew Can", "Pepsi Bottle (1L)", "Coca-Cola Bottle (1L)", "Lemonade Soda", "Birell (Apple)", "Birell (Lemon)", "Malt Beverage (Non-Alcoholic)", "Schweppes Gold", "Schweppes Lemon", "Schweppes Peach", "Soda Water", "Lipton Iced Tea Bottle", "Tonic Water", "Lactel Milk Drink", "Juhayna Milk", "Yogurt Drink", "Chocolate Milk", "Karkade (Hibiscus)", "Ayran (Salty Yogurt Drink)", "Hot Chocolate", "Tamarind Drink", "Sahlab", "Green Tea", "Nescafe 3in1", "Cappuccino Sachet", "Cold Chocolate Drink", "Turkish Coffee", "Americano", "Energy Shot", "Latte", "Cappuccino", "Iced Americano", "Macchiato", "Flat White", "Cold Brew", "Iced Latte", "Vanilla Milkshake", "Iced Coffee Bottle", "Chocolate Milkshake", "Iced Mocha", "Strawberry Milkshake", "Caramel Latte", "Coconut Water", "Energy Drink (Code Red)", "Coconut Latte", "Smoothie (Strawberry)", "Date Milkshake", "XL Energy Drink", "Power Horse", "Mocha Frappuccino", "Mocha", "Red Bull (Large)", "Monster Energy", "Matcha Latte", "Iced Matcha Latte", "Cold Brew Caramel", "Avocado Smoothie", "Starbucks Bottled Coffee", "Protein Shake", "Iced Spanish Latte", "Pistachio Milkshake", "Taro Latte", "Salted Caramel Frappe", "Cookies & Cream Milkshake", "Dragon Fruit Smoothie", "Pumpkin Spice Latte", "Caramel Frappe"]
drink_cost = [5, 6, 7, 8, 10, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20, 21, 22, 22, 23, 24, 24, 25, 25, 26, 26, 26, 27, 27, 27, 28, 28, 28, 29, 30, 30, 30, 33, 33, 33, 34, 34, 34, 34, 35, 35, 36, 37, 38, 39, 40, 40, 40, 41, 42, 43, 44, 45, 45, 46, 48, 50, 50, 52, 55, 55, 56, 58, 60, 60, 60, 62, 62, 63, 65, 65, 65, 68, 72, 75, 75, 78, 80, 80, 80, 85, 85, 88, 90, 95, 95, 100, 102, 105, 108, 110, 115, 118, 120, 125]
dessert = ["Petit Four", "Maamoul (Date Cookie)", "Kahk (Egyptian Eid Cookie)", "Basbousa", "Konafa Plain", "Rice Pudding (Roz Bel Laban)", "Qatayef", "Baklava Piece", "Ghourayeba", "Balah El Sham", "Eclairs Mini", "Chocolate Chip Cookie", "Vanilla Cupcake", "Brownie Piece", "Chocolate Donut", "Plain Donut", "Pistachio Maamoul", "Chocolate Croissant", "Vanilla Croissant", "Chocolate Muffin", "Vanilla Muffin", "Apple Pie Slice", "Cheesecake Slice (Plain)", "Strawberry Cheesecake Slice", "Carrot Cake Slice", "Tiramisu Cup", "Konafa with Cream", "Konafa with Mango", "Konafa with Nutella", "Konafa with Pistachio", "Basbousa with Cream", "Basbousa with Nuts", "Om Ali", "Molten Chocolate Cake", "Crepe (Sugar & Lemon)", "Crepe (Nutella)", "Crepe (Lotus)", "Chocolate Mousse Cup", "Mango Mousse Cup", "Fruit Tart", "Mini Cheesecake", "Lotus Cheesecake", "Oreo Cheesecake", "Caramel Cheesecake", "Tiramisu Slice", "Strawberry Tart", "Chocolate Tart", "Cupcake with Frosting", "Nutella Brownie", "Triple Chocolate Brownie", "Chocolate Soufflé", "Ice Cream Scoop", "Ice Cream 2 Scoops", "Ice Cream Sundae", "Waffle (Plain)", "Waffle (Nutella)", "Waffle (Lotus)", "Pancake (Honey)", "Pancake (Nutella)", "Pancake (Lotus)", "Banoffee Pie Slice", "Apple Crumble", "Creme Caramel", "Custard Cup", "Mahalabia", "Chocolate Truffle", "Cinnamon Roll", "Donut with Filling", "Baklava Mix Box (Small)", "Baklava Mix Box (Large)", "Cookies Box (Small)", "Cookies Box (Large)", "Mini Cupcake Box", "Nutella Konafa Cup", "Lotus Konafa Cup", "Oreo Konafa Cup", "Mango Konafa Cup", "Pistachio Konafa Cup", "Chocolate Tartlet", "Mini Tiramisu Jar", "Chocolate Eclair (Large)", "French Pastry Box (Small)", "French Pastry Box (Large)", "Macaron Piece", "Macaron Box (6 pcs)", "Macaron Box (12 pcs)", "Cheesecake Jar", "Lotus Jar Dessert", "Nutella Jar Dessert", "Brownie Jar", "Chocolate Lava Jar", "Ice Cream Jar", "Mini Cake (Vanilla)", "Mini Cake (Chocolate)", "Mini Cake (Lotus)", "Mini Cake (Nutella)", "Special Cake Slice", "Premium Cake Slice", "Full Cake (Medium)", "Full Cake (Large)"]
dessert_cost = [5, 6, 7, 8, 8, 9, 10, 10, 11, 12, 13, 14, 15, 15, 16, 16, 17, 18, 18, 19, 20, 22, 24, 25, 25, 26, 27, 28, 29, 30, 30, 32, 35, 36, 38, 40, 42, 45, 46, 48, 49, 50, 52, 54, 55, 56, 58, 59, 60, 62, 65, 70, 75, 78, 80, 82, 85, 88, 90, 92, 95, 98, 100, 100, 102, 104, 105, 108, 110, 115, 118, 120, 122, 125, 128, 130, 132, 135, 138, 140, 142, 145, 148, 150, 152, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 210, 220, 230, 250, 280]
snack = ["Salted Peanuts", "Plain Chips", "Popcorn (Salted)", "Sesame Sticks", "Breadsticks", "Mini Pretzels", "Cheese Puffs (Small)", "Nachos (Small Pack)", "Tuc Crackers", "Potato Chips (Small)", "Wafers (Small)", "Biscuits (Plain)", "Digestive Biscuit", "Marie Biscuit", "Tea Biscuit", "Oat Cookies (Small)", "Choco Sticks", "Cream Crackers", "Cheese Crackers", "Caramel Popcorn (Small)", "Chipsy (Small)", "Doritos (Small)", "Tiger Chips", "Flutes (Small)", "Mini Croissant", "Chocolate Wafer", "Caramel Wafer", "Vanilla Wafer", "Coconut Wafer", "Chocolate Bar (Mini)", "Bounty Mini", "Twix Mini", "KitKat Mini", "Galaxy Mini", "Lion Mini", "Snickers Mini", "Maltesers Small", "Nut Bar (Small)", "Energy Bar (Small)", "Date Bar", "Protein Bar (Small)", "Granola Bar", "Cereal Bar", "Coconut Bar", "Chocolate Croissant", "Zainy Croissant", "Molto Croissant", "7 Days Croissant", "Mini Muffin", "Chocolate Donut", "Vanilla Donut", "Cupcake (Small)", "Mini Brownie", "Mini Cake Roll", "Oreo Pack (Small)", "Chocolate Cookies", "Butter Cookies", "Digestive Chocolate", "Chocolate Fingers", "Choco Pie", "Rice Cakes", "Mini Crackers", "Mixed Nuts (Small)", "Popcorn (Cheese)", "Nachos with Dip", "Peanut Butter Biscuit", "Stuffed Dates", "Roasted Almonds", "Salted Cashews", "Caramelized Peanuts", "Trail Mix (Small)", "Corn Flakes Snack", "Mini Sandwich Crackers", "Chocolate Chip Cookies", "Mini Brownie Bites", "Mini Pancake Bites", "Mini Donuts Box", "Cheese Balls (Large)", "Popcorn (Large)", "Chipsy (Large)", "Doritos (Large)", "Pringles (Small)", "Pringles (Large)", "Cheese Crackers Box", "Pretzels (Large)", "Mixed Nuts (Medium)", "Roasted Almonds (Medium)", "Cashews (Medium)", "Trail Mix (Medium)", "Protein Bar (Large)", "Energy Bar (Large)", "Nut Mix (Large)", "Roasted Pistachios", "Mixed Nuts (Large)", "Protein Cookies", "Chocolate Covered Almonds", "Premium Trail Mix", "Assorted Nuts Jar", "Luxury Snack Box", "Gourmet Snack Basket"]
snack_cost = [5, 6, 7, 7, 8, 8, 9, 9, 10, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 15, 16, 16, 17, 17, 18, 18, 18, 19, 19, 20, 20, 20, 21, 21, 22, 23, 24, 25, 26, 26, 27, 27, 28, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 42, 43, 45, 46, 48, 50, 52, 54, 55, 56, 58, 60, 62, 63, 65, 66, 68, 70, 72, 74, 75, 78, 80, 82, 85, 88, 90, 92, 95, 98, 100, 105, 110, 115, 120, 130, 140, 150, 160, 180, 200, 220, 250]

fo = False
dr = False
de = False
sn = False

@app.event("app_mention")
def mention_event(event,say):
    user = event.get("user")
    say(
        text = "Hello <@" + user + ">Select Option:",
        blocks = [
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": "Hello <@" + user + "> \nPlease select an option:"},
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {"type": "plain_text", "text": "Food"},
                        "action_id": "food_selected",
                    },
                    {
                        "type": "button",
                        "text": {"type": "plain_text", "text": "Drink"},
                        "action_id": "drink_selected",
                    },
                    {
                        "type": "button",
                        "text": {"type": "plain_text", "text": "Dessert"},
                        "action_id": "dessert_selected",
                    },
                    {
                        "type": "button",
                        "text": {"type": "plain_text", "text": "Snack"},
                        "action_id": "snack_selected",
                    }
                ]
            }
        ]
    )

@app.action("food_selected")
def food_selected(ack, body, client):
    global fo
    ack()
    fo = True
    channel_id = body["channel"]["id"]
    client.views_open(
        trigger_id=body["trigger_id"],
        view={
            "type": "modal",
            "callback_id": "food_input",
            "private_metadata": channel_id,
            "title": {"type": "plain_text", "text": "Food Selection"},
            "submit": {"type": "plain_text", "text": "Submit"},
            "blocks": [
                {
                    "type": "input",
                    "block_id": "input_block",
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "user_input"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Please send number of people then '--' then your budget then 'EGP' without any spaces please:)"
                    }
                },
                {
                    "type": "context",
                    "elements": [
                        {"type": "mrkdwn", "text": "Example: `200--100EGP`"}
                    ]
                }
            ]
        }
    )
@app.view("food_input")
def handle_food(ack, body, client):
    global fo, food, food_cost
    ack()
    channel_id = body["view"]["private_metadata"]
    user_id = body["user"]["id"]
    message = body["view"]["state"]["values"]["input_block"]["user_input"]["value"]
    if message.find("EGP") > -1 and message.find("--") > -1 and fo == True:
        ppl = int(message[:message.find("--")])
        money = int(message[message.find("--") + 2:message.find("EGP")])
        budget = int(money / ppl)
        mx = 0
        for idx,price in enumerate(food_cost):
            if price <= budget:
                mx = idx
        choice = random.randint(0, mx)
        client.chat_postMessage(
            channel=channel_id,
            text="<@" + user_id + "> I suggest to have: " + food[choice] + "\nWhich Costs: " + str(food_cost[choice]) + " for one\nTotal: " + str(food_cost[choice]*ppl)
        )
        dm_response = client.conversations_open(users=user_id)
        dm_channel = dm_response["channel"]["id"]
        client.chat_postMessage(
            channel=dm_channel,
            text="I suggest to have: " + food[choice] + "\nWhich Costs: " + str(food_cost[choice]) + " for one\nTotal: " + str(food_cost[choice]*ppl)
        )

@app.action("drink_selected")
def drink_selected(ack, body, client):
    global dr
    ack()
    dr = True
    channel_id = body["channel"]["id"]
    client.views_open(
        trigger_id=body["trigger_id"],
        view={
            "type": "modal",
            "callback_id": "drink_input",
            "private_metadata": channel_id,
            "title": {"type": "plain_text", "text": "Drink Selection"},
            "submit": {"type": "plain_text", "text": "Submit"},
            "blocks": [
                {
                    "type": "input",
                    "block_id": "input_block",
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "user_input"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Please send number of people then '--' then your budget then 'EGP' without any spaces please:)"
                    }
                },
                {
                    "type": "context",
                    "elements": [
                        {"type": "mrkdwn", "text": "Example: `200--100EGP`"}
                    ]
                }
            ]
        }
    )
@app.view("drink_input")
def handle_drink(ack, body, client):
    global dr, drink, drink_cost
    ack()
    channel_id = body["view"]["private_metadata"]
    user_id = body["user"]["id"]
    message = body["view"]["state"]["values"]["input_block"]["user_input"]["value"]
    if message.find("EGP") > -1 and message.find("--") > -1 and dr == True:
        ppl = int(message[:message.find("--")])
        money = int(message[message.find("--") + 2:message.find("EGP")])
        budget = int(money / ppl)
        mx = 0
        for idx,price in enumerate(drink_cost):
            if price <= budget:
                mx = idx
        choice = random.randint(0, mx)
        client.chat_postMessage(
            channel=channel_id,
            text="<@" + user_id + "> I suggest to have: " + drink[choice] + "\nWhich Costs: " + str(drink_cost[choice]) + " for one\nTotal: " + str(drink_cost[choice]*ppl)
        )
        dm_response = client.conversations_open(users=user_id)
        dm_channel = dm_response["channel"]["id"]
        client.chat_postMessage(
            channel=dm_channel,
            text="I suggest to have: " + drink[choice] + "\nWhich Costs: " + str(drink_cost[choice]) + " for one\nTotal: " + str(drink_cost[choice]*ppl)
        )

@app.action("dessert_selected")
def dessert_selected(ack, body, client):
    global de
    ack()
    de = True
    channel_id = body["channel"]["id"]
    client.views_open(
        trigger_id=body["trigger_id"],
        view={
            "type": "modal",
            "callback_id": "dessert_input",
            "private_metadata": channel_id,
            "title": {"type": "plain_text", "text": "Dessert Selection"},
            "submit": {"type": "plain_text", "text": "Submit"},
            "blocks": [
                {
                    "type": "input",
                    "block_id": "input_block",
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "user_input"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Please send number of people then '--' then your budget then 'EGP' without any spaces please:)"
                    }
                },
                {
                    "type": "context",
                    "elements": [
                        {"type": "mrkdwn", "text": "Example: `200--100EGP`"}
                    ]
                }
            ]
        }
    )
@app.view("dessert_input")
def handle_dessert(ack, body, client):
    global de, dessert, dessert_cost
    ack()
    channel_id = body["view"]["private_metadata"]
    user_id = body["user"]["id"]
    message = body["view"]["state"]["values"]["input_block"]["user_input"]["value"]
    if message.find("EGP") > -1 and message.find("--") > -1 and de == True:
        ppl = int(message[:message.find("--")])
        money = int(message[message.find("--") + 2:message.find("EGP")])
        budget = int(money / ppl)
        mx = 0
        for idx,price in enumerate(dessert_cost):
            if price <= budget:
                mx = idx
        choice = random.randint(0, mx)
        client.chat_postMessage(
            channel=channel_id,
            text="<@" + user_id + "> I suggest to have: " + dessert[choice] + "\nWhich Costs: " + str(dessert_cost[choice]) + " for one\nTotal: " + str(dessert_cost[choice]*ppl)
        )
        dm_response = client.conversations_open(users=user_id)
        dm_channel = dm_response["channel"]["id"]
        client.chat_postMessage(
            channel=dm_channel,
            text="I suggest to have: " + dessert[choice] + "\nWhich Costs: " + str(dessert_cost[choice]) + " for one\nTotal: " + str(dessert_cost[choice]*ppl)
        )

@app.action("snack_selected")
def snack_selected(ack, body, client):
    global sn
    ack()
    sn = True
    channel_id = body["channel"]["id"]
    client.views_open(
        trigger_id=body["trigger_id"],
        view={
            "type": "modal",
            "callback_id": "snack_input",
            "private_metadata": channel_id,
            "title": {"type": "plain_text", "text": "Snack Selection"},
            "submit": {"type": "plain_text", "text": "Submit"},
            "blocks": [
                {
                    "type": "input",
                    "block_id": "input_block",
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "user_input"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Please send number of people then '--' then your budget then 'EGP' without any spaces please:)"
                    }
                },
                {
                    "type": "context",
                    "elements": [
                        {"type": "mrkdwn", "text": "Example: `200--100EGP`"}
                    ]
                }
            ]
        }
    )
@app.view("snack_input")
def handle_snack(ack, body, client):
    global sn, snack, snack_cost
    ack()
    channel_id = body["view"]["private_metadata"]
    user_id = body["user"]["id"]
    message = body["view"]["state"]["values"]["input_block"]["user_input"]["value"]
    if message.find("EGP") > -1 and message.find("--") > -1 and sn == True:
        ppl = int(message[:message.find("--")])
        money = int(message[message.find("--") + 2:message.find("EGP")])
        budget = int(money / ppl)
        mx = 0
        for idx,price in enumerate(snack_cost):
            if price <= budget:
                mx = idx
        choice = random.randint(0, mx)
        client.chat_postMessage(
            channel=channel_id,
            text="<@" + user_id + "> I suggest to have: " + snack[choice] + "\nWhich Costs: " + str(snack_cost[choice]) + " for one\nTotal: " + str(snack_cost[choice]*ppl)
        )
        dm_response = client.conversations_open(users=user_id)
        dm_channel = dm_response["channel"]["id"]
        client.chat_postMessage(
            channel=dm_channel,
            text="I suggest to have: " + snack[choice] + "\nWhich Costs: " + str(snack_cost[choice]) + " for one\nTotal: " + str(snack_cost[choice]*ppl)

        )



if __name__ == "__main__":
    handler = SocketModeHandler(app, app_token)
    handler.start()

