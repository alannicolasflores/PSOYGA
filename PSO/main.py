# -*- coding: utf-8 -*-

from optimizer.pso import ParticleSwarmOptimizer
from optimizer.objective_function import rastrigin, rosenbrock_function, constraint_example

if __name__ == "__main__":
    bounds = [(-5, 5), (-5, 5)]
    optimizer = ParticleSwarmOptimizer(
        objective_function=rastrigin,
        bounds=bounds,
        num_particles=100,
        max_iterations=500,
        phi1=2.0,
        phi2=2.0,
        vmax=0.5,
        constraints=[constraint_example]
    )
    
    best_position, best_value = optimizer.optimize()
    print(f"Mejor posici�n encontrada: {best_position}")
    print(f"Mejor valor encontrado: {best_value}")
    