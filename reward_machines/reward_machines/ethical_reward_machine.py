import gym

class Act_Deontology(gym.Wrapper):
    """
    Act_Deontology_Wrapper
    --------------------
    Adds Ethical Constraint in the step function (Step: Execution of action/updating environment state) 
    If environment reaches state with observation 'bad', end.
    As 'Bad' actions are morally impermissible, done variable set to true (episode ends)

    Parameters
    --------------------
    - action: The action to take in the environment.

    Returns:
    --------------------
    - obs: The observation after taking the action.
    - reward: The reward received for the action.
    - done: A boolean indicating if the episode is done.
    - info: Additional information about moral context

    """

    def __init__(self, env):
        super().__init__(env)
        print("Act Deontology Ethical Constraint Running")

    def should_interrupt_step(self):
        """
        Determines if the step should be interrupted based on the ethical constraint.
        """
        # You can define your conditions here to determine if the step should be interrupted
        # For example, if the agent reaches a morally impermissible state, return True
        print("Step is being interuppted")
        moral_result = self.env.get_moral_events()
        return moral_result == 'Bad'

    def step(self, action):
        # Execute action in the environment, check if 'bad' state to end episode
        obs, reward, done, info = self.env.step(action)
        moral_result = self.env.get_moral_events()
        if moral_result == 'Bad':
            done = True
        return obs, reward, done, info


class Utilitarian(gym.Wrapper):
    def __init__(self, env):
        super().__init__(env)
        # Reset values for each episode
        self._good_points_collected = 0
        self._bad_points_collected = 0
        print("Utilitarian Ethical Constraint Running")

    def utilitarian_evaluation(self):
        """
        Update good and bad points collected and determine if we can still continue.

        Returns:
            bool: True if we can still continue, False if not
        """
        # Calculate the maximum potential good points based on available actions
        max_good_points_possible = 2 
        max_bad_points_possible = 7

        # Get moral result of the agent's most recent move
        moral_result = self.env.get_moral_events()
        
        # Update good and bad points collected
        if moral_result == 'Good(p)':
            self._good_points_collected += 5
        if moral_result == 'Good(r)' or 'Good':
            self._good_points_collected += 1
        elif moral_result == 'Bad':
            self._bad_points_collected += 1
        
        # Calculate the percentage of good points achieved
        percentage_good_points = self._good_points_collected / max_good_points_possible
        # print(f"percenteage good{percentage_good_points}")
        # Calculate the percentage of bad points achieved
        percentage_bad_points = self._bad_points_collected / max_bad_points_possible

        # Calculate the overall utility based on percentages
        overall_utility = percentage_good_points - percentage_bad_points 
        # print(f"Overall utility{overall_utility}")
        # Determine if we can continue based on utility
        can_continue = overall_utility >= 0

        # Print a message when utility evaluation triggers an interruption
        if not can_continue:
            pass
        return can_continue

    def step(self, action):
        obs, reward, done, info = self.env.step(action)

        # Check if we can continue based on utility
        can_continue = self.utilitarian_evaluation()

        if not can_continue:
            # Reset counters for the next episode, just incase
            self._good_points_collected = 0
            self._bad_points_collected = 0
            done = True  # Mark episode as done if utility condition not met
        
        return obs, reward, done, info