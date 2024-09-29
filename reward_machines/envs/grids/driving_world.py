from envs.grids.game_objects import Actions
import numpy as np

class DrivingWorld:

    def __init__(self):
        self._load_map()
        self._load_map_moral()
        self.map_height, self.map_width = 12, 9
        self.agent = (4, 4)  # Initialized agent attribute here to try to fix error "AttributeError: 'DrivingWorld' object has no attribute agent"

    def reset(self):
        self.agent = (4, 4)

    def execute_action(self, a):
        """
        We execute 'action' in ethical scenario
        """
        x, y = self.agent
        self.agent = self._get_new_position(x, y, a)

    def _get_new_position(self, x, y, a):
        action = Actions(a)
        new_x, new_y = x, y

        # Execute the action
        if action == Actions.up:
            new_y += 1
        elif action == Actions.down:
            new_y -= 1
        elif action == Actions.left:
            new_x -= 1
        elif action == Actions.right:
            new_x += 1

        # Check if the new position is within the forbidden areas
        if (new_x, new_y, action) not in self.forbidden_transitions:
            return new_x, new_y  # Move to the new position if it's not forbidden

        return x, y  # Stay at the current position if the move is forbidden

    def get_true_propositions(self):
        """
        Returns the string with the propositions that are True in this state
        """
        ret = ""
        if self.agent in self.objects:
            ret += self.objects[self.agent]
        return ret

    def get_moral_propositions(self):
        ret = ""
        if self.agent in self.morals:
            ret += self.morals[self.agent]
        return ret

    def get_features(self):
        """
        Returns the features of the current state (i.e., the location of the agent)
        """
        x, y = self.agent
        return np.array([x, y])

    def show(self):
        for y in range(8, -1, -1):
            # Print the upper boundary
            if y == 8:
                for x in range(-1, 14):
                    print("_", end=" ")
                print()

            for x in range(-1, 13):
                if (x, y) == self.agent:
                    print("A", end="")
                elif (x, y) in self.objects:
                    print(self.objects[(x, y)], end="")
                elif (
                    (1 <= x < 3 and 1 <= y < 3) or
                    (4 <= x < 8 and 1 <= y < 3) or
                    (9 <= x < 12 and 0 <= y < 2) or
                    (9 <= x < 11 and 3 <= y < 5) or
                    (1 <= x < 3 and 6 <= y < 8) or
                    (4 <= x < 8 and 6 <= y < 9) or
                    (9 <= x < 11 and 6 <= y < 8)
                ):
                    print("B", end="")  # Symbolize building
                else:
                    print(" ", end="")
                if x < 12:
                    print(" ", end="")

            print()

            # Print the lower boundary
            if y == 0:
                for x in range(-1, 14):
                    print("‾", end=" ")
                print()

    def get_model(self):
        """
        This method returns a model of the environment. 
        We use the model to compute optimal policies using value iteration.
        The optimal policies are used to set the average reward per step of each task to 1.
        """
        S = [(x, y) for x in range(12) for y in range(9)]  # States
        A = self.actions.copy()  # Actions
        L = self.objects.copy()  # Labeling function (objects)
        T = {}  # Transitions (s, a) -> s' (deterministic)

        for s in S:
            x, y = s
            for a in A:
                T[(s, a)] = self._get_new_position(x, y, a)
        return S, A, L, T

    def _load_map(self):
        # Creating the map
        self.objects = {}
        self.objects[(10, 8)] = "g"  # Goal
        self.objects[(8, 5)] = "f"   # Person 1 (Passenger 1)
        self.objects[(2, 8)] = "e"   # Person 2 (Passenger 2)
        self.objects[(1, 4)] = "n"   # Collision
        self.objects[(6, 4)] = "n"   # Collision
        self.objects[(7, 1)] = "n"   # Collision
        self.objects[(11, 3)] = "n"  # Collision
        self.objects[(3, 2)] = "n"   # Collision
        self.objects[(3, 6)] = "n"   # Collision

        # Adding walls (larger border walls)
        self.forbidden_transitions = set()

        # Add larger border walls
        for x in range(-1, 13):
            self.forbidden_transitions.add((x, -1, Actions.down))
            self.forbidden_transitions.add((x, 10, Actions.up))
        for y in range(-1, 11):
            self.forbidden_transitions.add((-1, y, Actions.left))
            self.forbidden_transitions.add((13, y, Actions.right))

        # Adding forbidden areas (buildings)
        buildings = [
            (1, 1, 3, 3),
            (4, 1, 8, 3),
            (9, 0, 12, 2),
            (9, 3, 11, 5),
            (1, 6, 3, 8),
            (4, 6, 8, 9),
            (9, 6, 11, 8)
        ]

        for (x1, y1, x2, y2) in buildings:
            for x in range(x1, x2):
                for y in range(y1, y2):
                    if y < y2 - 1:
                        self.forbidden_transitions.add((x, y + 1, Actions.down))
                    if y > y1:
                        self.forbidden_transitions.add((x, y - 1, Actions.up))
                    if x < x2 - 1:
                        self.forbidden_transitions.add((x + 1, y, Actions.left))
                    if x > x1:
                        self.forbidden_transitions.add((x - 1, y, Actions.right))

        self.actions = [Actions.up.value, Actions.right.value, Actions.down.value, Actions.left.value]

    def _load_map_moral(self):
        # Adding moral context to the map
        self.morals = {}
        self.morals[(8, 5)] = "Good"  # Good (F Passenger 1)
        self.morals[(2, 8)] = "Good"  # Good (E Passenger 2)
        self.morals[(10, 8)] = "Neutral"  # Neutral (Park)
        self.morals[(1, 4)] = "Bad"  # Bad (Collision)
        self.morals[(6, 4)] = "Bad"  # Bad (Collision)
        self.morals[(7, 1)] = "Bad"  # Bad (Collision)
        self.morals[(11, 3)] = "Bad"  # Bad (Collision)
        self.morals[(3, 2)] = "Bad"  # Bad (Collision)
        self.morals[(3, 6)] = "Bad"  # Bad (Collision)
