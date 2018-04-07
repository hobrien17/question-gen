class Enemy:
    def __init__(self, enemy_type, stamina):
        """Creates a new Enemy object

        Params:
            enemy_type (str) : the type of enemy
            stamina (float) : the enemy's current stamina
        """
        self._type = enemy_type
        self._stamina = enemy_stamina

    def detract_stamina(self, value):
        self._stamina -= value

    def is_strong(self):
        return self._stamina >= 20

Enemy("{monster}", {float}) #correctly creates a new instance of the Enemy class under the variable {var} of type {monster} and stamina {float} #I#
detract_stamina({float}) #correctly removes {float} from the enemy {var}'s stamina, assuming {var} has been correctly initialized #M#
detract_stamina({negfloat}) #correctly adds ${posnegfloat} from the enemy {var}'s stamina, assuming {var} has been correctly initialized #M#
Enemy("{monster}", {lowfloat}) #initializations will ensure the statement {var}.is_strong() returns False #B#