#!/bin/bash
cd reward_machines
for i in `seq 0 59`; 
do

	# Act Deontology Multi-task
	python run.py --alg=qlearning --env=Driving-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../driving_results/ql/driving/ActDeon/M1/$i --use_ActDeon
	python run.py --alg=qlearning --env=Driving-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../driving_results/ql-rs/driving/ActDeon/M1/$i --use_rs --use_ActDeon
	python run.py --alg=qlearning --env=Driving-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../driving_results/crm/driving/ActDeon/M1/$i --use_crm --use_ActDeon
	python run.py --alg=qlearning --env=Driving-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../driving_results/crm-rs/driving/ActDeon/M1/$i --use_crm --use_rs --use_ActDeon
	python run.py --alg=hrm --env=Driving-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../driving_results/hrm/driving/ActDeon/M1/$i --use_ActDeon
	python run.py --alg=hrm --env=Driving-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../driving_results/hrm-rs/driving/ActDeon/M1/$i --use_rs --use_ActDeon 

	# Utilitarian Multi-task , Specific DrivingUTIL DFA (allows for mistakes) with Utilitarian Wrapper
	python run.py --alg=qlearning --env=DrivingUtil-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../driving_results/ql/driving/Utilitarian/M1/$i --use_Utilitarian 
	python run.py --alg=qlearning --env=DrivingUtil-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../driving_results/ql-rs/driving/Utilitarian/M1/$i --use_rs --use_Utilitarian 
	python run.py --alg=qlearning --env=DrivingUtil-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../driving_results/crm/driving/Utilitarian/M1/$i --use_crm --use_Utilitarian 
	python run.py --alg=qlearning --env=DrivingUtil-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../driving_results/crm-rs/driving/Utilitarian/M1/$i --use_crm --use_rs --use_Utilitarian 
	python run.py --alg=hrm --env=DrivingUtil-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../driving_results/hrm/driving/Utilitarian/M1/$i --use_Utilitarian 
	python run.py --alg=hrm --env=DrivingUtil-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../driving_results/hrm-rs/driving/Utilitarian/M1/$i --use_rs --use_Utilitarian 

done