import gym, random
from gym import spaces
import numpy as np
from reward_machines.rm_environment import RewardMachineEnv
from envs.grids.dilemma_world import DilemmaWorld
from envs.grids.driving_world import DrivingWorld
from envs.grids.mm_world import MoralMachineWorld
from envs.grids.value_iteration import value_iteration

class GridEnv(gym.Env):
    def __init__(self, env):
        self.env = env
        N,M      = self.env.map_height, self.env.map_width
        self.action_space = spaces.Discrete(4) # up, right, down, left
        self.observation_space = spaces.Box(low=0, high=max([N,M]), shape=(2,), dtype=np.uint8)

    def get_events(self):
        return self.env.get_true_propositions()
    
    def get_moral_events(self):
        return self.env.get_moral_propositions()

    def step(self, action):
        self.env.execute_action(action)
        obs = self.env.get_features()
        reward = 0 # all the reward comes from the RM
        done = False
        info = {}
        return obs, reward, done, info

    def reset(self):
        self.env.reset()
        return self.env.get_features()

    def show(self):
        self.env.show()

    def get_model(self):
        return self.env.get_model()

class GridRMEnv(RewardMachineEnv):
    def __init__(self, env, rm_files):
        super().__init__(env, rm_files)

    def render(self, mode='human'):
        if mode == 'human':
            # commands
            str_to_action = {"w":0,"d":1,"s":2,"a":3}

            # play the game!
            done = True
            while True:
                if done:
                    print("New episode --------------------------------")
                    obs = self.reset()
                    print("Current task:", self.rm_files[self.current_rm_id])
                    self.env.show()
                    print("Features:", obs)
                    print("RM state:", self.current_u_id)
                    print("Events:", self.env.get_events())

                print("\nAction? (WASD keys or q to quit) ", end="")
                a = input()
                print()
                if a == 'q':
                    break
                # Executing action
                if a in str_to_action:
                    obs, rew, done, _ = self.step(str_to_action[a])
                    self.env.show()
                    print("Features:", obs)
                    print("Reward:", rew)
                    print("RM state:", self.current_u_id)
                    print("Events:", self.env.get_events())
                else:
                    print("Forbidden action")
        else:
            raise NotImplementedError

    def test_optimal_policies(self, num_episodes, epsilon, gamma):
        """
        This code computes optimal policies for each reward machine and evaluates them using epsilon-greedy exploration

        PARAMS
        ----------
        num_episodes(int): Number of evaluation episodes
        epsilon(float):    Epsilon constant for exploring the environment
        gamma(float):      Discount factor

        RETURNS
        ----------
        List with the optimal average-reward-per-step per reward machine
        """
        S,A,L,T = self.env.get_model()
        print("\nComputing optimal policies... ", end='', flush=True)
        optimal_policies = [value_iteration(S,A,L,T,rm,gamma) for rm in self.reward_machines]
        print("Done!")
        optimal_ARPS = [[] for _ in range(len(optimal_policies))]
        print("\nEvaluating optimal policies.")
        for ep in range(num_episodes):
            if ep % 100 == 0 and ep > 0:
                print("%d/%d"%(ep,num_episodes))
            self.reset()
            s = tuple(self.obs)
            u = self.current_u_id
            rm_id = self.current_rm_id
            rewards = []
            done = False
            while not done:
                a = random.choice(A) if random.random() < epsilon else optimal_policies[rm_id][(s,u)]
                _, r, done, _ = self.step(a)
                rewards.append(r)
                s = tuple(self.obs)
                u = self.current_u_id
            optimal_ARPS[rm_id].append(sum(rewards)/len(rewards))
        print("Done!\n")

        return [sum(arps)/len(arps) for arps in optimal_ARPS]

# Driving Domain, RMEnv: all 4 tasks / RM3Env: 1 task with original DFAs (Act Deontology)
class DrivingRMEnv(GridRMEnv):
    def __init__(self):
        rm_files = ["./envs/grids/reward_machines/driving/t%d.txt"%i for i in range(1,5)]
        env = DrivingWorld()
        super().__init__(GridEnv(env),rm_files)
    
class DrivingRM3Env(GridRMEnv):
    def __init__(self):
        rm_files = ["./envs/grids/reward_machines/driving/t3.txt"]
        env = DrivingWorld()
        super().__init__(GridEnv(env),rm_files)

# Driving Domain, RMEnv: all 4 tasks / RM3Env: 1 task with original DFAs (Utilitarian)
class DrivingUtilRMEnv(GridRMEnv):
    def __init__(self):
        rm_files = ["./envs/grids/reward_machines/driving_util/t%d.txt"%i for i in range(1,5)]
        env = DrivingWorld()
        super().__init__(GridEnv(env),rm_files)

class DrivingUtilRM3Env(GridRMEnv):
    def __init__(self):
        rm_files = ["./envs/grids/reward_machines/driving_util/t3.txt"]
        env = DrivingWorld()
        super().__init__(GridEnv(env),rm_files)

# Dilemma Domain, RMEnv: all four tasks available for Act Deontology
class DilemmaRMEnv(GridRMEnv):
    def __init__(self):
        rm_files = ["./envs/grids/reward_machines/dilemma/t%d.txt"%i for i in range(1,4)]
        env = DilemmaWorld()
        super().__init__(GridEnv(env),rm_files)

# Dilemma Domain, RM2Env: Only T2 viable with Utilitarianism
class DilemmaRM2Env(GridRMEnv):
    def __init__(self):
        rm_files = [
            "./envs/grids/reward_machines/dilemma/t2.txt",
            "./envs/grids/reward_machines/dilemma/t3.txt"
        ]
        env = DilemmaWorld()
        super().__init__(GridEnv(env),rm_files)

# ----------------------------------------- MORAL MACHINE WESTERN (AGE PREFERENCE)
class MoralWestern(GridRMEnv):
    def __init__(self):
        rm_files = ["./envs/grids/reward_machines/mm_western/t%d.txt"%i for i in range(1,4)]
        env = MoralMachineWorld()
        super().__init__(GridEnv(env),rm_files)

# ----------------------------------------- MORAL MACHINE SOUTHERN (AGE PREFERENCE)
class MoralSouthern(GridRMEnv):
    def __init__(self):
        rm_files = ["./envs/grids/reward_machines/mm_southern/t%d.txt"%i for i in range(1,4)]
        env = MoralMachineWorld()
        super().__init__(GridEnv(env),rm_files)

# ----------------------------------------- MORAL MACHINE EASTERN (AGE PREFERENCE)
class MoralEastern(GridRMEnv):
    def __init__(self):
        rm_files = ["./envs/grids/reward_machines/mm_eastern/t%d.txt"%i for i in range(1,4)]
        env = MoralMachineWorld()
        super().__init__(GridEnv(env),rm_files)