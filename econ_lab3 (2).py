#!/usr/bin/env python
# coding: utf-8

# # COMS W1002 Computing in Economics  
# ## Lab 3

# __Problem 1:__ Recall from lecture that the European *put* option is very similar to the European *call* option except that the payout is postive when the stock price $S_T$ is less than $K$. The payout is computed as $C_T = (K - S_T )^+$. Recall also that the formula for computing the price $C_0$ of an option (derivative of the BLM stock prices) that yields a payoff $C_T$ at time $T$ is:
# $$ C_0 = \frac{1}{(1+r)^T}E^*(C_T), $$  
# 
# where $*$ refers to the fact that we must use the value $p^*$ instead of the original (real) $p$ for the up/down probability of the BLM. (The real value of $p$ is not needed for pricing.) Use Monte Carlo simulation to estimate the price $C_0$ of a European put option.
# 
# Here are the parameters to use: $T = 10, r = 0.01, u = 1.02, d= 0.96, S_0 = 50, K = 55$. Recall that 
# $$ p^* = \frac{1+r-d}{u-d} . $$  
# 
# For the Monte Carlo, use $n=10,000$ _iid_ copies of $C_T$ (for averaging).

# In[4]:


import random

T = 10
r = 0.01
u = 1.02
d = 0.96
S0 = 50
K = 55
n = 10000

#p_star = (1+r-d)/(u-d)
#Simulate 1 time step(1day)
#Run 30 day simulation to avg out the randomness (10,000 times)

def single(p, u, d):
    #make a single random proce movement thats one time step
    if random.random()<= p:
        return u
    else:
        return d

def BLM(S0, T, p, u, d):
    #single price path over t time periods, using BLM
    BLMpath = [0 for k in range(T + 1)]
    BLMpath[0] = S0
    Ysamples = [single(p, u, d) for k in range(T)]
    S = S0
    for k in range(1, T + 1):
        S = S * Ysamples[k - 1]
        BLMpath[k] = S
    return BLMpath

def find_CT(T, R, u, d, S0, K):
    #calculate the payoff of a european put at maturity for single path
    p_star = (1 + r - d)/ (u-d)
    BLMpath = BLM(S0, T, p_star, u, d)
    ST = BLMpath[-1]
    CT = max(K - ST, 0)
    return CT

def monte_carlo(T, r, u, d, S0, K, n):
    #run simulation n times and average the payoffs
    total = 0
    for x in range(n):
        total += find_CT(T, r, u, d, S0, K)
    avg_CT = total /n  #discount back to present value using risk free rate
    C0 = avg_CT/(1 + r) ** T
    return C0 
    
    return
print(monte_carlo(T, r, u, d, S0, K, n))


# In[ ]:




