def initialize():
    with open('twelve.txt') as data:
        return [line.strip() for line in data]

class Boat():
    def __init__(self):
        self.position = [0,0]
        self.compass = {'N':[1,1],'E':[0,1],'S':[1,-1],'W':[0,-1]}
        self.facing = 1
        
    def rotate(self,move):
        rotation = 1
        if move.type == 'L':
            rotation *= -1
        self.facing = int(self.facing + move.value*rotation/90) % 4
    
    def move(self,move):
        
        self.position[self.compass[move.type][0]] += self.compass[move.type][1]*move.value
        
    def advance(self,move):
        if self.facing == 0: 
            self.position[1] += move.value
        if self.facing == 1:
            self.position[0] += move.value
        if self.facing == 2:
            self.position[1] -= move.value
        if self.facing ==3:
            self.position[0] -= move.value
        if self.facing >= 4 or self.facing < 0:
            print('ERROR')
    
    def distance(self):
        return abs(self.position[0])+abs(self.position[1])
        
        
class Move():
    def __init__(self,move):
        self.type = move[0]
        self.value = int(move[1:])
        
def main():
    b = Boat()
    
    directions = initialize()
    #directions = ['F10','N3','F7','R90','F11']
    
    for direction in directions:
        move = Move(direction)
        if move.type in 'LR' :
            b.rotate(move)
        elif move.type in b.compass:
            b.move(move)
        else:
            b.advance(move)
    
    print(b.distance())
            
    
main()
