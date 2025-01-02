import random
from optimizer.particle import Particle

class ParticleSwarmOptimizer:
    def __init__(self, objective_function, bounds, num_particles=30, max_iterations=100,
                 phi1=2.0, phi2=2.0, vmax=0.5, neighborhood_size=3, constraints=None):
        self.objective_function = objective_function
        self.bounds = bounds
        self.num_particles = num_particles
        self.max_iterations = max_iterations
        self.phi1 = phi1
        self.phi2 = phi2
        self.vmax = vmax
        self.neighborhood_size = neighborhood_size
        self.constraints = constraints or []
        self.particles = self._initialize_particles()
        self.global_best_position = None
        self.global_best_value = float('inf')

    def _initialize_particles(self):
        particles = []
        for _ in range(self.num_particles):
            position = [random.uniform(low, high) for low, high in self.bounds]
            velocity = [random.uniform(-1, 1) for _ in self.bounds]
            particles.append(Particle(position, velocity, self.bounds))
        return particles

    def optimize(self):
        for iteration in range(self.max_iterations):
            for particle in self.particles:
                value = self.objective_function(particle.position)
                if all(constraint(particle.position) for constraint in self.constraints):
                    if value < particle.best_value:
                        particle.best_value = value
                        particle.best_position = particle.position[:]
                if value < self.global_best_value:
                    self.global_best_value = value
                    self.global_best_position = particle.position[:]

            for particle in self.particles:
                neighbors = sorted(self.particles, key=lambda p: self._euclidean_distance(p.position, particle.position))
                neighbor_best = neighbors[0].best_position if neighbors else particle.best_position
                particle.update_velocity(self.global_best_position, neighbor_best, self.phi1, self.phi2, self.vmax)
                particle.update_position()
        return self.global_best_position, self.global_best_value

    def _euclidean_distance(self, pos1, pos2):
        return sum((x - y) ** 2 for x, y in zip(pos1, pos2)) ** 0.5
    