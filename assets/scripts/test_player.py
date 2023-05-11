"""
This is a unit test for the player class. 

"""

from player import Player

def test_can_create_new_player():
    random_name = "Luke Skywaker"
    random_health_value = 50
    random_jump_state = False
     
    model =  Player(random_name, random_health_value, random_jump_state)

    assert  isinstance(model, Player)