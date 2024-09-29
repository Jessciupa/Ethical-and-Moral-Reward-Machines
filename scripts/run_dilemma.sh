#!/bin/bash
cd reward_machines
for i in `seq 0 59`; 
do

	# Dilemma RM1 Env calls on ActDeon Reward Machine DFA with ActDeon Wrapper with ALL Learning Methodologies
	python run.py --alg=qlearning --env=Dilemma-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../dilemma_results/ql/dilemma/ActDeon/M1/$i --use_ActDeon
	python run.py --alg=qlearning --env=Dilemma-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../dilemma_results/ql-rs/dilemma/ActDeon/M1/$i --use_rs --use_ActDeon
	python run.py --alg=qlearning --env=Dilemma-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../dilemma_results/crm/dilemma/ActDeon/M1/$i --use_crm --use_ActDeon
	python run.py --alg=qlearning --env=Dilemma-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../dilemma_results/crm-rs/dilemma/ActDeon/M1/$i --use_crm --use_rs --use_ActDeon
	python run.py --alg=hrm --env=Dilemma-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../dilemma_results/hrm/dilemma/ActDeon/M1/$i --use_ActDeon 
	python run.py --alg=hrm --env=Dilemma-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../dilemma_results/hrm-rs/dilemma/ActDeon/M1/$i --use_rs --use_ActDeon

	# Dilemma RM2 Env calls on Utilitarian Reward Machine DFA with Utilitarian Wrapper with ALL Learning Methodologies
	python run.py --alg=qlearning --env=DilemmaRM2-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../dilemma_results/ql/dilemma/Utilitarian/M1/$i --use_Utilitarian
	python run.py --alg=qlearning --env=DilemmaRM2-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../dilemma_results/ql-rs/dilemma/Utilitarian/M1/$i --use_rs --use_Utilitarian
	python run.py --alg=qlearning --env=DilemmaRM2-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../dilemma_results/crm/dilemma/Utilitarian/M1/$i --use_crm --use_Utilitarian
	python run.py --alg=qlearning --env=DilemmaRM2-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../dilemma_results/crm-rs/dilemma/Utilitarian/M1/$i --use_crm --use_rs --use_Utilitarian
	python run.py --alg=hrm --env=DilemmaRM2-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../dilemma_results/hrm/dilemma/Utilitarian/M1/$i --use_Utilitarian 
	python run.py --alg=hrm --env=DilemmaRM2-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../dilemma_results/hrm-rs/dilemma/Utilitarian/M1/$i --use_rs --use_Utilitarian

done