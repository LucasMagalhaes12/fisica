import pygame
from math import sqrt
class Circle:
    def __init__(self, screenSize):
        self.color = 'black'
        self.radius = 18
        self.positions = []#[[[200, 0], 2, True], [[200, -200], 2, True]]
        self.ACCELERATION = 10
        self.MAXACCELERATION = 500
        self.screenSizeY = screenSize[1]


    # def circleCollisions(self, aPosition, index):
    #     if aPosition["state"]:
    #         for indexB, posB in enumerate(self.positions[index+1:]):
    #             # print(self.radius*2, aPosition["pos"][1], posB["pos"][1], aPosition["pos"][1] - posB["pos"][1])
    #             if posB["state"]:
    #                 if self.radius*2 >= aPosition["pos"][1] - posB["pos"][1]:
    #                     # print("Colidiu")
    #                     aPosition["state"] = False
    #                     break

    def circleCollisions(self, aPosition, index):
        if aPosition["state"]:
            for i, bPosition in enumerate(self.positions):
                if i != index:
                    if abs(sqrt((bPosition["pos"][0] - aPosition["pos"][0])**2 + (bPosition["pos"][1] - aPosition["pos"][1])**2)) <= self.radius*2:
                        # if aPosition["pos"][0] - bPosition["pos"][0] < 0:
                        #     aPosition["pos"][0] += 10
                        # else:
                        #     aPosition["pos"][0] -= 10
                        aPosition["state"] = False
                        break

    def update(self, screen, dt):
        for i, position in enumerate(self.positions):
            pygame.draw.circle(screen, self.color, position["pos"], self.radius, width=2)
            # if position[2]:
            #     print(position) ##

            self.circleCollisions(position, i)


            if position["pos"][1] > self.screenSizeY - self.radius:
                position["pos"][1] = self.screenSizeY - self.radius
                position["state"] = False
            
            if position["state"]:
                if position["acceleration"] <= self.MAXACCELERATION:
                    position["acceleration"] += self.ACCELERATION
                position["pos"][1] += position["acceleration"] * dt

    
    def add(self, position:tuple):
        self.positions.append({"pos":list(position), "acceleration":2, "state":True})


    # def positions(self):
    #     return self.positions
    
    
    # def radius(self):
    #     return self.radius
