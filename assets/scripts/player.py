"""Class to describe a player of this game"""
from dataclasses import dataclass, astuple, asdict

@dataclass
class Player :
    """Describes a player in the fighting game"""
    name: str
    health: int
    is_jumping : bool

def main() -> None :
    """test if a player can be created"""
    fighter = Player('Luke Skywalker', 100, False)
    print(fighter)
    print(astuple(fighter))
    print(asdict(fighter))

if __name__ == '__main__' :
    main()