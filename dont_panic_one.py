import sys
import math

# Don't Panic - Episode 1
# https://www.codingame.com/ide/puzzle/don't-panic-episode-1

# nb_floors: number of floors
# width: width of the area
# nb_rounds: maximum number of rounds
# exit_floor: floor on which the exit is found
# exit_pos: position of the exit on its floor
# nb_total_clones: number of generated clones
# nb_additional_elevators: ignore (always zero)
# nb_elevators: number of elevators
nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in input().split()]
elevators = []
leading_clone = 0
clones = []

for i in range(nb_elevators):
    # elevator_floor: floor on which this elevator is found
    # elevator_pos: position of the elevator on its floor
    elevator_floor, elevator_pos = [int(j) for j in input().split()]
    elevators.append([elevator_floor, elevator_pos])
    

print("nb_floors:", nb_floors, "width:", width, "nb_rounds:", nb_rounds, "exit_floor:", exit_floor, file=sys.stderr) 
print("exit_pos:", exit_pos, "nb_total_clones:", nb_total_clones, file=sys.stderr) 
print("nb_additional_elevators:", nb_additional_elevators, "nb_elevators:", nb_elevators, file=sys.stderr)
print("elevators:", elevators, file=sys.stderr)

# game loop
while True:
    # clone_floor: floor of the leading clone
    # clone_pos: position of the leading clone on its floor
    # direction: direction of the leading clone: LEFT or RIGHT
    clone_floor, clone_pos, direction = input().split()
    clone_floor = int(clone_floor)
    clone_pos = int(clone_pos)
    decision = "WAIT"
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    # action: WAIT or BLOCK
    print("clone floor:", clone_floor, "clone pos:", clone_pos, "direction:", direction, file=sys.stderr)
    if int(clone_floor) is int(exit_floor):
        if (int(clone_pos) > int(exit_pos) and direction == "RIGHT") or (int(clone_pos) < int(exit_pos) and direction == "LEFT"):
            decision = "BLOCK"
            
    for e in elevators:
        if e[0] == clone_floor:
            if (clone_pos > e[1] and direction == "RIGHT") or (clone_pos < e[1] and direction == "LEFT"):
                elevators.remove(e)
                decision = "BLOCK"
            
    
    print(decision)