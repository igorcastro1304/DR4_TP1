hotel_rooms = {
    "standard": 150.00,
    "deluxe": 185.00,
    "king": 250.00,
    "queen": 285.00,
    "master": 375.00
}

for room, price in hotel_rooms.items():
    print(f"Room {room.capitalize()} - R$ {price:.2f}".replace(".", ","))

