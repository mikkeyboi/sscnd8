clear all
close all

addpath(genpath('D:\Studies\sscnd8\references\bg_model_matlab'))
%% Set initial conditions

%time variables
tmax=1000; %maximum time (ms)
dt=0.01; %timestep (ms)
t=0:dt:tmax;
n=10; %number of neurons in each nucleus (TH, STN, GPe, GPi)

%initial membrane voltages for all cells
v1=-62+randn(n,1)*5;
v2=-62+randn(n,1)*5;
v3=-62+randn(n,1)*5;
v4=-62+randn(n,1)*5;
r=randn(n,1)*2;

%Sensorimotor cortex input to thalamic cells
[Istim, timespike]=createSMC(tmax,dt,14,0.2);
% BGnetwork loads Istim.mat which has all the initial conditions
save('Istim.mat','Istim','timespike','tmax','dt','v1','v2','v3','v4','r','n');

%% Running BGnetwork.m
h=BGnetwork(0,0,0); %healthy
pd = BGnetwork(1,0,0); %PD
dbs=BGnetwork(1,1,130); %PD with DBS

