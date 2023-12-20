from gameobjectclass import*

friction_force = 2
max_speed = 0.7

def sign(val):
    if val < 0:
        return -1
    return 1

def lerp(a, b, t):

    if abs(a-b) < 0.001:
        return b 

    return (1 - t) * a + t * b

def clamp(val, min, max):

    if val < min:
        return min
    
    if val > max:
        return max
    
    return val

class player(gameobject):

    def __init__(self, speed, jump):

        super().__init__(
            pos=[0,0], 
            vel=[0,0], 
            width=114, 
            height=190, 
            scale=1, 
            image_path="Sprites/Mario", 
            is_animated=True, 
            static=False
        )
        
        self.speed = speed
        self.jump_velocity = jump

        self.powered_up = False

        self.is_moving = False

    def jump(self):
        
        if(self.grounded == True):
            self.velocity[1] = -self.jump_velocity
            self.grounded = False

    def move(self, direction):
        self.is_moving = True
        self.direction = direction
        self.velocity[0] += self.speed*direction

    def update_position(self, gravity):

        #Clamp velocity to max speed
        self.velocity[0] = clamp(self.velocity[0], -max_speed, max_speed)

        #Move Horizontal Velocity towards 0
        if self.is_moving == False and self.velocity[0] != 0:
            self.velocity[0] = lerp(self.velocity[0], 0, (abs(self.velocity[0])/max_speed)/friction_force)

        self.position[1] = clamp(self.position[1], 0, 270)

        super().update_position(gravity)