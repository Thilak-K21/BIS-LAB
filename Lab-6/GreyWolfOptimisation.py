import numpy as np

def energy_cost_function(x):
    return np.sum(x**2)

num_wolves = 5
dim = 3 
max_iter = 50
lb = -10 * np.ones(dim) 
ub = 10 * np.ones(dim)

wolves = np.random.uniform(lb, ub, (num_wolves, dim))

for t in range(max_iter):
    fitness = np.array([energy_cost_function(w) for w in wolves])
    sorted_indices = np.argsort(fitness)
    alpha, beta, delta = wolves[sorted_indices[:3]]

    a = 2 - 2 * (t / max_iter) 
    new_wolves = []
    for i in range(num_wolves):
        X = wolves[i]
        X_new = np.zeros(dim)

        for leader in [alpha, beta, delta]:
            r1 = np.random.rand(dim)
            r2 = np.random.rand(dim)
            A = 2 * a * r1 - a
            C = 2 * r2
            D = np.abs(C * leader - X)
            X_leader = leader - A * D
            X_new += X_leader

        X_new /= 3  # Average influence of alpha, beta, delta
        X_new = np.clip(X_new, lb, ub)  # Keep within bounds
        new_wolves.append(X_new)

    wolves = np.array(new_wolves)

# Final best solution
best_index = np.argmin([energy_cost_function(w) for w in wolves])
best_solution = wolves[best_index]
best_cost = energy_cost_function(best_solution)

print("Best solution:", best_solution)
print("Minimum energy cost:", best_cost)
