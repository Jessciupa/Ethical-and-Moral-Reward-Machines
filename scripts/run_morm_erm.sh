#!/bin/bash
cd reward_machines
for i in `seq 0 59`; 
do
	# Moral Western
	python run.py --alg=qlearning --env=MoralWestern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/ql/western/actdeon/M1/$i --use_ActDeon
	python run.py --alg=qlearning --env=MoralWestern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/ql-rs/western/actdeon/M1/$i --use_rs --use_ActDeon
	python run.py --alg=qlearning --env=MoralWestern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/crm/western/actdeon/M1/$i --use_crm --use_ActDeon
	python run.py --alg=qlearning --env=MoralWestern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/crm-rs/western/actdeon/M1/$i --use_crm --use_rs --use_ActDeon
	python run.py --alg=hrm --env=MoralWestern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/hrm/western/actdeon/M1/$i --use_ActDeon
	python run.py --alg=hrm --env=MoralWestern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/hrm-rs/western/actdeon/M1/$i --use_rs --use_ActDeon

	# Moral Southern
	python run.py --alg=qlearning --env=MoralSouthern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/ql/southern/actdeon/M1/$i --use_ActDeon
	python run.py --alg=qlearning --env=MoralSouthern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/ql-rs/southern/actdeon/M1/$i --use_rs --use_ActDeon
	python run.py --alg=qlearning --env=MoralSouthern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/crm/southern/actdeon/M1/$i --use_crm --use_ActDeon
	python run.py --alg=qlearning --env=MoralSouthern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/crm-rs/southern/actdeon/M1/$i --use_crm --use_rs --use_ActDeon
	python run.py --alg=hrm --env=MoralSouthern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/hrm/southern/actdeon/M1/$i --use_ActDeon
	python run.py --alg=hrm --env=MoralSouthern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/hrm-rs/southern/actdeon/M1/$i --use_rs --use_ActDeon

	# Moral Eastern
	python run.py --alg=qlearning --env=MoralEastern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/ql/eastern/actdeon/M1/$i --use_ActDeon
	python run.py --alg=qlearning --env=MoralEastern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/ql-rs/eastern/actdeon/M1/$i --use_rs --use_ActDeon
	python run.py --alg=qlearning --env=MoralEastern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/crm/eastern/actdeon/M1/$i --use_crm --use_ActDeon
	python run.py --alg=qlearning --env=MoralEastern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/crm-rs/eastern/actdeon/M1/$i --use_crm --use_rs --use_ActDeon
	python run.py --alg=hrm --env=MoralEastern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/hrm/eastern/actdeon/M1/$i --use_ActDeon
	python run.py --alg=hrm --env=MoralEastern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/hrm-rs/eastern/actdeon/M1/$i --use_rs --use_ActDeon

	## utilitarian 

	# Moral Western
	python run.py --alg=qlearning --env=MoralWestern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/ql/western/utilitarian/M1/$i --use_Utilitarian
	python run.py --alg=qlearning --env=MoralWestern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/ql-rs/western/utilitarian/M1/$i --use_rs --use_Utilitarian
	python run.py --alg=qlearning --env=MoralWestern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/crm/western/utilitarian/M1/$i --use_crm --use_Utilitarian
	python run.py --alg=qlearning --env=MoralWestern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/crm-rs/western/utilitarian/M1/$i --use_crm --use_rs --use_Utilitarian
	python run.py --alg=hrm --env=MoralWestern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/hrm/western/utilitarian/M1/$i --use_Utilitarian
	python run.py --alg=hrm --env=MoralWestern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/hrm-rs/western/utilitarian/M1/$i --use_rs --use_Utilitarian

	# Moral Southern
	python run.py --alg=qlearning --env=MoralSouthern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/ql/southern/utilitarian/M1/$i --use_Utilitarian
	python run.py --alg=qlearning --env=MoralSouthern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/ql-rs/southern/utilitarian/M1/$i --use_rs --use_Utilitarian
	python run.py --alg=qlearning --env=MoralSouthern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/crm/southern/utilitarian/M1/$i --use_crm --use_Utilitarian
	python run.py --alg=qlearning --env=MoralSouthern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/crm-rs/southern/utilitarian/M1/$i --use_crm --use_rs --use_Utilitarian
	python run.py --alg=hrm --env=MoralSouthern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/hrm/southern/utilitarian/M1/$i --use_Utilitarian
	python run.py --alg=hrm --env=MoralSouthern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/hrm-rs/southern/utilitarian/M1/$i --use_rs --use_Utilitarian

	# Moral Southern
	python run.py --alg=qlearning --env=MoralEastern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/ql/eastern/utilitarian/M1/$i --use_Utilitarian
	python run.py --alg=qlearning --env=MoralEastern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/ql-rs/eastern/utilitarian/M1/$i --use_rs --use_Utilitarian
	python run.py --alg=qlearning --env=MoralEastern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/crm/eastern/utilitarian/M1/$i --use_crm --use_Utilitarian
	python run.py --alg=qlearning --env=MoralEastern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/crm-rs/eastern/utilitarian/M1/$i --use_crm --use_rs --use_Utilitarian
	python run.py --alg=hrm --env=MoralEastern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/hrm/eastern/utilitarian/M1/$i --use_Utilitarian
	python run.py --alg=hrm --env=MoralEastern-v0 --num_timesteps=1e5 --gamma=0.9 --log_path=../MoRM_results/hrm-rs/eastern/utilitarian/M1/$i --use_rs --use_Utilitarian
done