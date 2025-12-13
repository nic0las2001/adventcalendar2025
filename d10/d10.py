input = open("inputs/d10.txt","r")
import numpy as np

class MachineClass:
    def __init__(self, target, buttons, joltage):
        self.target = target
        self.initial = [0]*len(self.target)
        self.buttons_num = buttons
        self.joltage = joltage

        # convert buttons to 0/1s list 
        self.buttons = [list(self.initial) for _ in self.buttons_num]
        for idx, button in enumerate(self.buttons_num):
            for num in button:
                self.buttons[idx][num] = 1

        self.buttons_vert = np.transpose(np.array(self.buttons)).tolist()

        self.buttons_int = [int("".join(map(str, button))) for button in self.buttons]

machines = []
for line in input:
    if len(line) > 1:
        raw_machine = line[:-1].split(" ")
        machine = []
        target = [0 if c == "." else 1 for c in raw_machine[0][1:len(raw_machine[0])-1]] # light target
        joltage = [int(c) for c in raw_machine[-1][1:len(raw_machine[-1])-1].split(",")] #joltage
        buttons = []
        for button in raw_machine[1:len(raw_machine)-1]:
            buttons.append([int(x) for x in button[1:len(button)-1].split(",")])
        machines.append(MachineClass(target, buttons, joltage))

fewer_presses = []
for machine in machines: 
    keep_running = True
    start_options = [machine.initial]
    pressed = 0
    while keep_running:
        pressed += 1
        outcomes = []
        for option in start_options:
            for button in machine.buttons:
                result = [(x + y) % 2 for x,y in zip(option, button)]
                outcomes.append(list(result))
                if result == machine.target:
                    keep_running = False
                    break
        start_options = outcomes
        if not keep_running:
            fewer_presses.append(pressed)

print("P1:", sum(fewer_presses))

import sympy as sp # attempt 2: try to solve as a system with a free variable 

tot_clicks = 0
for machine in machines: 
    symbols = [sp.symbols("x"+ str(l)) for l in range(len(machine.buttons))]
    equations = []
    # global joltage one: (maybe not needed)
    # jolt_eq = [sum([x*y for x,y in zip(machine.buttons_int, symbols)])]
    # equations += jolt_eq
    # equations[0] -= int("".join(map(str, machine.joltage)))
    # print(equations)
    # print(machine.buttons_vert)
    for button in machine.buttons_vert:
        equations += [sum([x*y for x,y in zip(button,symbols)])]
    equations = [x-y for x,y in zip(equations, machine.joltage)]
    sol = sp.linsolve(equations, symbols)
    
    # check how many variables in solution
    indiv_clicks = list(list(sol)[0])
    clicks = sum(indiv_clicks)
    unknowns = []
    for s in symbols:
        if str(s) in str(clicks):
            unknowns.append(s)
    
    # mild cheating: equations inspection of the solution reveals 3 unknowns max 
    max_jolt = max(machine.joltage)

    if len(unknowns) == 0:
        tot_clicks += clicks
    else:
        #1 unknown
        min_u1 = 1e9
        for n in range(max_jolt):
            for expr in indiv_clicks:
                print(type(expr))
                if len(unknowns) == 1:
                    if type(expr) != sp.core.add.Add:
                        val = expr.evalf()
                    else:
                        val = expr.subs({unknowns[0]: n}).evalf()
                    print(type(val), unknowns)
                
                    if float(val) < 0 or not float(val).is_integer():
                        break
                    elif clicks.subs({unknowns[0]: n}) < min_u1:
                        min_u1 = clicks.subs({unknowns[0]: n})
        print(min_u1)





# same logic with / and % but in reverse? flawed: its not necessarily the remainder of the biggest division
# maybe break down each digit to have a system / solve with a matrix 
# for machine in machines: 
#     keep_running = True
#     start_options = [(machine.joltage, 0)]
#     while keep_running:
#         outcomes = []
#         for option in start_options:
#             for button in machine.buttons:
#                 but_num = int("".join(map(str, button)))
#                 opt_num = int("".join(map(str, option[0])))
#                 result = opt_num % but_num
#                 presses = opt_num // but_num

#                 padded_result = str(result).rjust(len(machine.joltage), "0")
#                 result_seq = [int(n) for n in padded_result]


#                 outcomes.append((result_seq,option[1]+presses))
#                 if result_seq == machine.initial:
#                     keep_running = False
#                     tot_presses = option[1]+presses
#                     break
#         start_options = outcomes
#         if not keep_running:
#             fewer_presses.append(tot_presses)