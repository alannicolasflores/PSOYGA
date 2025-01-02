import random
import math

class Particle:
    def __init__(self, position, velocity, bounds):
        self.position = position
        self.velocity = velocity
        self.best_position = position[:]
        self.best_value = float('inf')
        self.bounds = bounds

    def update_velocity(self, global_best, neighbor_best, phi1, phi2, vmax):
        r1 = [random.random() for _ in self.position]
        r2 = [random.random() for _ in self.position]
        for i in range(len(self.position)):
            cognitive_component = phi1 * r1[i] * (self.best_position[i] - self.position[i])
            social_component = phi2 * r2[i] * (neighbor_best[i] - self.position[i])
            self.velocity[i] += cognitive_component + social_component
            if abs(self.velocity[i]) > vmax:
                self.velocity[i] = vmax * (self.velocity[i] / abs(self.velocity[i]))

    def update_position(self):
        for i in range(len(self.position)):
            self.position[i] += self.velocity[i]
            self.position[i] = max(min(self.position[i], self.bounds[i][1]), self.bounds[i][0])
    