#maximizar el poder de nuestro ejército
# Import OR-Tools wrapper for linear programming
from ortools.linear_solver import pywraplp
# Create a solver using the GLOP backend
solver = pywraplp.Solver('Maximize army power', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

# Create the variables we want to optimize
swordsmen = solver.IntVar(0, solver.infinity(), 'swordsmen')
bowmen = solver.IntVar(0, solver.infinity(), 'bowmen')
horsemen = solver.IntVar(0, solver.infinity(), 'horsemen')

# Add constraints for each resource
solver.Add(swordsmen*60 + bowmen*80 + horsemen*140 <= 1200) # Food
solver.Add(swordsmen*20 + bowmen*10 <= 800)                 # Wood
solver.Add(bowmen*40 + horsemen*100 <= 600)                 # Gold

# Maximize the objective function
solver.Maximize(swordsmen*70 + bowmen*95 + horsemen*230)

# Solve problem
status = solver.Solve()
# If an optimal solution has been found, print results
if status == pywraplp.Solver.OPTIMAL:  
    print('================= Solution =================')  
    print(f'Solved in {solver.wall_time():.2f} milliseconds in {solver.iterations()} iterations')  
    print()  
    print(f'Optimal power = {solver.Objective().Value()} 💪power')  
    print('Army:')  
    print(f' - 🗡️Swordsmen = {swordsmen.solution_value()}')  
    print(f' - 🏹Bowmen = {bowmen.solution_value()}')  
    print(f' - 🐎Horsemen = {horsemen.solution_value()}')
else:  
    print('The solver could not find an optimal solution.')

