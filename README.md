# Ethical and Moral Reward Machine

Reward Machines from Icarte et al., 2020 is a novel reinforcement learning (RL) machine which reveals the reward structure to the agent, and with access to the internal structures the agent can exploit the reward machine to learn optimal policies faster, with data efficiency and partial observability. The symbolic technique is interpretable which makes suitable for ethical and moral applications. Two ethical principles algorithms are added to be wrapped on the reward machine to alter how the agent is presented the reward structure and penalised with new rules dependent on the principle. The moral machine experiment data was clustered and the results formed new reward weights to be fed into the reward machine. In this project, our two proposed reward machine applications are carried out and measured in how it impacts different learning methodologies to exploit the structure is carried out: including automated reward shaping, task decomposition, and counterfactual reasoning for data augmentation. Our experiments on tabular and continuous domains show the benefits of exploiting reward structure across different tasks and RL agents. 

A presentation of the ethical reward machine can be found in the following paper: ([link](https://www.springerprofessional.de/en/ethical-reward-machine/27677424))

@inproceedings{d082d8c950b848e78752d27352e35649,
title = "Ethical reward machines",
abstract = "The Ethical Reward Machine investigates reward design involving ethical constraints with reinforcement learning. Designed to promote good behaviour across specific domains, such as simulated driving and search-and-rescue scenarios, the Ethical Reward Machine explores ethical constraints based on Act Deontology and Utilitarianism. Our contribution to the literature is a novel algorithmic pipeline integrating ethical constraints into reinforcement learning through symbolic language.Our findings indicate ethical principles impact the system significantly if there is a dilemma, and that incorporating ethical principles does not increase runtime. Therefore, our results suggest that ethical considerations do not substantially burden computational resources. Ultimately,the overarching objective is to develop and validate a learning framework that ensures AI alignment with human learning and ethical policies.",
keywords = "knowledge representation, interpretable reinforcement learning, ethics",
author = "Jessica Ciupa and Vaishak Belle",
year = "2024",
month = jun,
day = "7",
language = "English",
series = "Proceedings of the International Conference for Neurosymbolic Learning and Reasoning",
booktitle = "Proceedings of the 18th International Workshop on Neural-Symbolic Learning and Reasoning",
note = "18th International Conference on Neural-Symbolic Learning and Reasoning, NESY 2024 ; Conference date: 09-09-2024 Through 12-09-2024",
url = "https://sites.google.com/view/nesy2024",
}

A complete description of reward machines and their methods can be found in the following paper ([link](https://arxiv.org/abs/2010.03950)):

    @article{tor-etal-arxiv20,
        author  = {Toro Icarte, Rodrigo and Klassen, Toryn Q. and Valenzano, Richard and McIlraith, Sheila A.},
        title   = {Reward Machines: Exploiting Reward Function Structure in Reinforcement Learning},
        journal = {arXiv preprint arXiv:2010.03950},
        year    = {2020}
    }

## Installation instructions

The code has the following requirements: 

- Python 3.6 or 3.7
- NumPy
- OpenAI Gym
- [OpenAI Baselines](https://github.com/openai/baselines)

However, the only *real* requirement is to have installed the master branch of Baselines. Installing baselines is not trivial, though. Their master branch only supports Tensorflow from version 1.4 to 1.14. These versions of Tensorflow seem to work fine with Python 3.6 and 3.7, but they **do not** work with Python 3.8+. We also included a [requirements.txt](requirements.txt) file as a reference, but note that such a file includes more libraries than the ones strictly needed to run our code.

## How to run the code

To run the code, move to the *reward_machines* folder and execute *run.py*. This code follows the same interface as *run.py* from [Baselines](https://github.com/openai/baselines):

python run.py --alg=<name of the algorithm> --env=<environment_id> [additional arguments]

RM-tailored algorithms (which are described in the Toro Icarte et al., 2020 paper). Some can be used as the value of the `--alg=` flag and some are activated with additional arguments.

- **Counterfactual Experiences for Reward Machines (CRM)**: CRM is an RM-tailored approach that uses counterfactual reasoning to generate *synthetic* experiences in order to learn policies faster. CRM can be combined with any off-policy learning method, including tabular Q-learning (`--alg=qlearning`), deep Q-networks (`--alg=deepq`), and deep deterministic policy gradient (`--alg=ddpg`). To use CRM, include the flag `--use_crm` when running an experiment.

- **Hierarchical RL for Reward Machines (HRM)**: HRM is an RM-tailored approach that automatically extracts a set of *options* from a RM to learn policies faster. We included implementations of tabular HRM (`--alg=hrm`) and deep HRM (`--alg=dhrm`). Note that `dhrm` can learn the option policies using DQN or DDPG and the macro-controller is learned using DQN. In addition to the standard learning hyperparameters, HRM uses R_min to penalize an option policy when it reaches an unwanted subgoal (this can be set with, e.g., `--r_min=-1`), R_max to reward an option policy when it reaches its target subgoal (e.g., `--r_max=1`), and another hyperparameter to define whether to learn options for the self-loops (by default, HRM does not learn options for self-loops unless the flag `--use_self_loops` is present).

- **Automated Reward Shaping (RS)**: RS is an RM-tailored approach that changes the reward from a *simple RM* so that the optimal policies remain the same but the overall reward becomes less sparse. RS can be used with tabular Q-learning (`--alg=qlearning`), deep Q-networks (`--alg=deepq`), deep deterministic policy gradient (`--alg=ddpg`), tabular HRM (`--alg=hrm`), and deep HRM (`--alg=dhrm`). To use RS, include the flag `--use_rs` when running an experiment. Note that RS uses two hyperparameters in determining the shaped rewards -- the same discount factor used for the environment (which can be set with, e.g., `--gamma=0.9`) and the discount factor used in calculating the potential function (e.g., `--rs_gamma=0.9`). 

For each of the different algorithms that can be named in the `--alg=` flag, default values for the hyperparameters in various environments are specified in `reward_machines/rl_agents/<name of the algorithm>/defaults.py`. For example, there are hyperparameters for deep HRM in [reward_machines/rl_agents/dhrm/defaults.py](reward_machines/rl_agents/dhrm/defaults.py), which specify (among other things) that the option polices are learned using DQN in the *water domain* and DDPG in the *half-cheetah domain*.

Our Ethical Principle algorithms (described in Ciupa and Belle, 2024 paper). This is activated with the `--alg=` flag.

- **Act-Deontology (ActDeon)**: ActDeon is an ethical algorithm that takes the principes of act-deontology approach to the reward structures in reinforcement learning. If a bad state is encountered this is treated as a morally wrong action, therefore the episode is ended. However, if a good state is encountered it is treated as morally good and therefore permissible. It works like traditional reinforcement learning and reward machine's approach to rewards in the system. To use Act-Deontology, include the flag `--use_ActDeon` when running an experiment. 

- **Utilitarianism (Utilitarian)**: Utilitarian is an ethical algorithm which takes the principles of utilitarinism to the reward structures in reinforcement learning. A utility calculation is made when an agent encounters a bad state, as it is treated as morally wrong. However, if the utility calculation determines the action ethically permissible the agent is able to proceed overring the step function in the original reward machine. The calculation is that if the moral good outweighs the morally bad actions (greater or equal). To use Utilitarian, include the flag `--use_Utilitarian` when running an experiment. 

Note that RM-tailored and ERM-tailored algorithms assume that the environment is a *RewardMachineEnv* (see [reward_machines/reward_machines/rm_environment.py](reward_machines/reward_machines/rm_environment.py)). These environments define their reward function using a reward machine. We included the following RM environments in our code:

- **Driving Domain**: The driving domain includes single and multi task versions (`--env=Driving-single-v0` and `--env=Driving-v0`, respectively). It is a discrete domain which is a simple testing environment. It is contextualised as a driving world, where the agent has to complete tasks which are good states while avoding bad states which are collisions. There are different versions of the environment which calls different reward machines for the ethical principle. As Act-Deontology does not alter the reward machine it uses the original environment, but Utilitariansim does. So for ERM experiments you will need to call different versions for Utilitarianism, (`--env=DrivingUtil-single-v0` and `--env=DrivingUtil-v0`, respectively). 

- **Dilemma Domain**: The dilemma domain is a single task only, and does not propose a task for the agent but instead a decision (`--env=Dilemma-v0` and `--env=DilemmaRM2-v0`). It is a discrete domain and contextualised for ethical contexts as a search and rescue for a trolley problem like dilemma. There are different versions of the environment which calls different reward machines dependent on which ethical principle `--env=DilemmaRM2-v0` calls a reward machine which displays a choice as a higher reward if it saves more people following utilitarian ethical principles, while `--env=Dilemma-v0` displays both choices as saving multiple or a single person as equally good, following act deontological principles.

Another version of the dilemma domain is used in the moral reward machine experiment which calls different reward machines dependent on weights determined from the clustering analysis of the moral machine experiment. Clusters of Western, Eastern and Southern (`--env=MoralWestern-v0`, `--env=MoralEastern-v0`, and `--env=MoralSouthern-v0` respectively)

## Running examples and raw results

As an example, executing the following commands from the *reward_machines* folder will run multi-task experiments on the Act Deontology Driving domain:

```
python run.py --alg=qlearning --env=Driving-v0 --num_timesteps=1e5 --gamma=0.9 --use_ActDeon # Tabular Q-learning
python run.py --alg=qlearning --env=Driving-v0 --num_timesteps=1e5 --gamma=0.9 --use_rs --use_ActDeon # Tabular Q-learning with reward shaping:
python run.py --alg=qlearning --env=Driving-v0 --num_timesteps=1e5 --gamma=0.9 --use_ActDeon # Tabular Q-learning with CRM
python run.py --alg=qlearning --env=Driving-v0 --num_timesteps=1e5 --gamma=0.9 --use_crm --use_rs --use_ActDeon # Tabular Q-learning with CRM and reward shaping:
python run.py --alg=hrm --env=Driving-v0 --num_timesteps=1e5 --gamma=0.9 --use_ActDeon # Tabular HRM 
python run.py --alg=hrm --env=Driving-v0 --num_timesteps=1e5 --gamma=0.9 --use_rs --use_ActDeon # Tabular HRM with reward shaping 
```
You can reproduce the results from our paper by running the scripts located at the *scripts* folder.

## Computing optimal policies using value iteration

To normalize the results on the tabular domains, we computed the optimal policies using value iterations by executing the following commands from the *reward_machines* folder:

```
python test_optimal_policies.py --env <environment_id>
```

where `<environment_id>` can be any of the tabular environments.    

## Playing each environment

Go to the *reward_machines* folder and run the following command:

```
python play.py --env <environment_id>
```

where `<environment_id>` can be any of the driving or dilemma domain. To control the agent, use the WASD keys. The environments are described in the paper.