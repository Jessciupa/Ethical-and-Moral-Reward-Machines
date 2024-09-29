#!/bin/bash
cd reward_machines
for i in `seq 0 59`; 
do
	# Moral Western
	python run.py --alg=qlearning --env=MoralWestern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/ql/western/M1/$i 
	python run.py --alg=qlearning --env=MoralWestern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/ql-rs/western/M1/$i --use_rs 
	python run.py --alg=qlearning --env=MoralWestern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/crm/western/M1/$i --use_crm 
	python run.py --alg=qlearning --env=MoralWestern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/crm-rs/western/M1/$i --use_crm --use_rs 
	python run.py --alg=hrm --env=MoralWestern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/hrm/western/M1/$i 
	python run.py --alg=hrm --env=MoralWestern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/hrm-rs/western/M1/$i --use_rs 

	# Moral Southern
	python run.py --alg=qlearning --env=MoralSouthern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/ql/southern/M1/$i 
	python run.py --alg=qlearning --env=MoralSouthern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/ql-rs/southern/M1/$i --use_rs 
	python run.py --alg=qlearning --env=MoralSouthern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/crm/southern/M1/$i --use_crm 
	python run.py --alg=qlearning --env=MoralSouthern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/crm-rs/southern/M1/$i --use_crm --use_rs 
	python run.py --alg=hrm --env=MoralSouthern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/hrm/southern/M1/$i 
	python run.py --alg=hrm --env=MoralSouthern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/hrm-rs/southern/M1/$i --use_rs

	# Moral Southern
	python run.py --alg=qlearning --env=MoralEastern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/ql/eastern/M1/$i 
	python run.py --alg=qlearning --env=MoralEastern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/ql-rs/eastern/M1/$i --use_rs 
	python run.py --alg=qlearning --env=MoralEastern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/crm/eastern/M1/$i --use_crm 
	python run.py --alg=qlearning --env=MoralEastern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/crm-rs/eastern/M1/$i --use_crm --use_rs 
	python run.py --alg=hrm --env=MoralEastern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/hrm/eastern/M1/$i 
	python run.py --alg=hrm --env=MoralEastern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/hrm-rs/eastern/M1/$i --use_rs
done