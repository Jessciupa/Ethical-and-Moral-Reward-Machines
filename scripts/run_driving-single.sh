#!/bin/bash
cd reward_machines
for i in `seq 0 59`; 
do

	# Act Deontology Single task
	python run.py --alg=qlearning --env=Driving-single-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../driving_results/ql/driving-single/ActDeon/M1/$i --use_ActDeon
	python run.py --alg=qlearning --env=Driving-single-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../driving_results/ql-rs/driving-single/ActDeon/M1/$i --use_rs --use_ActDeon 
	python run.py --alg=qlearning --env=Driving-single-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../driving_results/crm/driving-single/ActDeon/M1/$i --use_crm --use_ActDeon
	python run.py --alg=qlearning --env=Driving-single-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../driving_results/crm-rs/driving-single/ActDeon/M1/$i --use_crm --use_rs --use_ActDeon 
	python run.py --alg=hrm --env=Driving-single-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../driving_results/hrm/driving-single/ActDeon/M1/$i --use_ActDeon
	python run.py --alg=hrm --env=Driving-single-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../driving_results/hrm-rs/driving-single/ActDeon/M1/$i --use_rs --use_ActDeon

	# Utilitarian Single task
	python run.py --alg=qlearning --env=DrivingUtil-single-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../driving_results/ql/driving-single/Utilitarian/M1/$i --use_Utilitarian 
	python run.py --alg=qlearning --env=DrivingUtil-single-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../driving_results/ql-rs/driving-single/Utilitarian/M1/$i --use_rs --use_Utilitarian 
	python run.py --alg=qlearning --env=DrivingUtil-single-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../driving_results/crm/driving-single/Utilitarian/M1/$i --use_crm --use_Utilitarian 
	python run.py --alg=qlearning --env=DrivingUtil-single-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../driving_results/crm-rs/driving-single/Utilitarian/M1/$i --use_crm --use_rs --use_Utilitarian 
	python run.py --alg=hrm --env=DrivingUtil-single-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../driving_results/hrm/driving-single/Utilitarian/M1/$i --use_Utilitarian 
	python run.py --alg=hrm --env=DrivingUtil-single-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../driving_results/hrm-rs/driving-single/Utilitarian/M1/$i --use_rs --use_Utilitarian 

done