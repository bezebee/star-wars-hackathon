"""
This is a unit test for the player class. 
"""

from player import Player

def test_can_create_new_player():
    """test if player can be created """
    random_position= (200,300)
    random_color =  "blue"

    model =  Player(random_position, random_color)

    assert  isinstance(model, Player)
