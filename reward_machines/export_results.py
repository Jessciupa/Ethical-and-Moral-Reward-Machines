"""
This code exports summary results for all our approaches and runs.
"""
from collections import deque
import numpy as np

def get_precentiles_str(a):
    p25 = "%0.4f"%float(np.percentile(a, 25))
    p50 = "%0.4f"%float(np.percentile(a, 50))
    p75 = "%0.4f"%float(np.percentile(a, 75))
    return [p25, p50, p75]

def export_avg_results_multitask_grid(agent,env,maps,seeds):
    """
    NOTE: 
        - Find a way to summarize the results coming from different seeds
        - This is tricky because the timesteps per trace might be different
    """
    if 'driving' in env:
        num_episodes_avg = 400
        num_total_steps = 1e5
        max_length = 100 
        # These values were computed using python test_optimal_policies.py --env Driving-v0
        optimal_rewards = dict(
            RMEnv =[0.021056896352971022, 0.02223704553392025, 0.030381492031773438, 0.029568570099147824, 0.028591107021728984, 0.01698443909619106, 0.01846431419356979, 0.022195745620423268, 0.023432205498423144, 0.012990580561337057],
            UtilRMEnv =[0.029351862026684234, 0.08145408101872667, 0.03686954558213452, 0.04016888761057505, 0.02377734567512407, 0.016688913949401675, 0.019328533833491517, 0.026399431925736412, 0.014480703440661439, 0.01608448909869953],
            )
    else:
        assert False, "Invalid environment!"

    stats = [[] for _ in range(max_length)]
    for env_map in maps:
        for seed in seeds:
            # Reading the results for driving world, change for different result file needed (refer to scripts to see destination)
            f_path = "../driving_results/%s/%s/%s/%s/0.0.monitor.csv"%(agent,env,env_map,seed)
            results = []
            f = open(f_path)
            for l in f:
                raw = l.strip().split(',')
                if len(raw) != 3 or raw[0]=='r':
                    continue
                r,l,t = float(raw[0]), float(raw[1]), float(raw[2])
                results.append((t,l,r))
            f.close()

            # collecting average stats
            steps = 0
            rewards = deque([], maxlen=num_episodes_avg)
            steps_tic = num_total_steps/max_length
            for i in range(len(results)):
                _,l,r = results[i]
                rew_per_step = (r/l)/optimal_rewards[env_map][i%len(optimal_rewards[env_map])]
                if (steps+l)%steps_tic == 0:
                    steps += l
                    rewards.append(rew_per_step)
                    stats[int((steps+l)//steps_tic)-1].append(sum(rewards)/len(rewards))
                else:
                    if (steps//steps_tic) != (steps+l)//steps_tic:
                        stats[int((steps+l)//steps_tic)-1].append(sum(rewards)/len(rewards))
                    steps += l
                    rewards.append(rew_per_step)
                if (steps+l)//steps_tic == max_length:
                    break

    # Saving the average performance and standard deviation
    f_out = "../driving_results/summary/%s-%s.txt"%(env,agent)
    f = open(f_out, 'w')
    for i in range(max_length):
        if len(stats[i]) == len(seeds) * len(maps):
            #f.write("\t".join([str((i+1)*steps_tic/1000), "%0.4f"%(sum(stats[i])/len(stats[i]))]) + "\n")
            f.write("\t".join([str((i+1)*steps_tic/1000)] + get_precentiles_str(stats[i])) + "\n")
    f.close()

def export_avg_results_single(agent,env,maps,seeds):
    """
    NOTE: 
        - Find a way to summarize the results coming from different seeds
        - This is tricky because the timesteps per trace might be different
    """
    if 'driving' in env:
        num_episodes_avg = 100
        num_total_steps = 1e5
        max_length = 100 
        # These values were computed using python test_optimal_policies.py --env Driving-single-v0
        optimal_rewards = dict(
            RM3Env =[0.021056896352971022, 0.02223704553392025, 0.030381492031773438, 0.029568570099147824, 0.028591107021728984, 0.01698443909619106, 0.01846431419356979, 0.022195745620423268, 0.023432205498423144, 0.012990580561337057],
            UtilRM3Env =[0.029351862026684234, 0.08145408101872667, 0.03686954558213452, 0.04016888761057505, 0.02377734567512407, 0.016688913949401675, 0.019328533833491517, 0.026399431925736412, 0.014480703440661439, 0.01608448909869953],
            )
    if 'dilemma' in env:
        num_episodes_avg = 100
        num_total_steps = 1e5
        max_length = 100 
        # These values were computed using python test_optimal_policies.py --env=Dilemma-v0
        optimal_rewards = dict(
            RMEnv =[0.021056896352971022, 0.02223704553392025, 0.030381492031773438, 0.029568570099147824, 0.028591107021728984, 0.01698443909619106, 0.01846431419356979, 0.022195745620423268, 0.023432205498423144, 0.012990580561337057],
            RM2Env =[0.029351862026684234, 0.08145408101872667, 0.03686954558213452, 0.04016888761057505, 0.02377734567512407, 0.016688913949401675, 0.019328533833491517, 0.026399431925736412, 0.014480703440661439, 0.01608448909869953],
            )
    if 'western' in env:
        num_episodes_avg = 100
        num_total_steps = 1e5
        max_length = 100 
        # These values were computed using python test_optimal_policies.py --env=MoralWestern-v0
        optimal_rewards = dict(M1=0.028119125449375417)
    if 'eastern' in env:
        num_episodes_avg = 100
        num_total_steps = 1e5
        max_length = 100 
        # These values were computed using python test_optimal_policies.py --env=MoralEastern-v0
        optimal_rewards = dict(M1=0.028054378481019833)
    if 'southern' in env:
        num_episodes_avg = 100
        num_total_steps = 1e5
        max_length = 100 
        # These values were computed using python test_optimal_policies.py --env=MoralSouthern-v0
        optimal_rewards = dict(M1=0.028120434377269198)
    else:
        assert False, "Invalid environment!"


    stats = [[] for _ in range(max_length)]
    for env_map in maps:
        for seed in seeds:
            # Reading the MoRM_results
            f_path = "../MoRM_results/%s/%s/%s/%s/0.0.monitor.csv"%(agent,env,env_map,seed)
            results = []
            f = open(f_path)
            for l in f:
                raw = l.strip().split(',')
                if len(raw) != 3 or raw[0]=='r':
                    continue
                r,l,t = float(raw[0]), float(raw[1]), float(raw[2])
                results.append((t,l,r))
            f.close()

            # collecting average stats
            steps = 0
            rewards = deque([], maxlen=num_episodes_avg)
            steps_tic = num_total_steps/max_length
            for i in range(len(results)):
                _,l,r = results[i]
                rew_per_step = (r/l)/optimal_rewards[env_map]
                if (steps+l)%steps_tic == 0:
                    steps += l
                    rewards.append(rew_per_step)
                    stats[int((steps+l)//steps_tic)-1].append(sum(rewards)/len(rewards))
                else:
                    if (steps//steps_tic) != (steps+l)//steps_tic:
                        stats[int((steps+l)//steps_tic)-1].append(sum(rewards)/len(rewards))
                    steps += l
                    rewards.append(rew_per_step)
                if (steps+l)//steps_tic == max_length:
                    break

    # Saving the average performance and standard deviation
    f_out = "../MoRM_results/summary/%s-%s.txt"%(env,agent)
    f = open(f_out, 'w')
    for i in range(max_length):
        if len(stats[i]) == len(seeds) * len(maps):
            #f.write("\t".join([str((i+1)*steps_tic/1000), "%0.4f"%(sum(stats[i])/len(stats[i]))]) + "\n")
            f.write("\t".join([str((i+1)*steps_tic/1000)] + get_precentiles_str(stats[i])) + "\n")
    f.close()

if __name__ == '__main__':

    algs = ['ql', 'crm', 'hrm', 'hrm-rs', 'ql-rs','crm-rs']

    # Driving world (multitask)
    for alg in algs:
        print(alg,'driving')
        export_avg_results_multitask_grid(alg,'driving',['M1'],list(range(60)))

    # Driving world (single task)
    for alg in algs:
        print(alg,'driving-single')
        export_avg_results_single(alg,'driving-single',['M1'],list(range(60)))

    # Dilemma world (decision)
    for alg in algs:
        print(alg,'dilemma')
        export_avg_results_single(alg,'dilemma',['M1'],list(range(60)))

    # Moral Machine World (Decision in Cultural Dilemma Context)
    for alg in algs:
        print(alg,'western-dilemma')
        export_avg_results_single(alg, 'western', ['M1'], list(range(60)))

    for alg in algs:
        print(alg,'eastern-dilemma')
        export_avg_results_single(alg, 'eastern', ['M1'], list(range(60)))

    for alg in algs:
        print(alg,'southern-dilemma')
        export_avg_results_single(alg, 'southern', ['M1'], list(range(60)))    
        