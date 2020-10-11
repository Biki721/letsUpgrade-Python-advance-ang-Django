#!/usr/bin/env python
# coding: utf-8

# In[20]:


communication = [ "Nick Fury : Tony Stark, Maria Hill, Norman Osborn", 
                  "Hulk : Tony Stark, HawkEye, Rogers",
                  "Rogers : Thor",
                  "Tony Stark: Pepper Potts, Nick Fury", 
                  "Agent 13 : Agent-X, Nick Fury, Hitler", 
                  "Thor: HawkEye, BlackWidow", 
                  "BlackWidow:Hawkeye", 
                  "Maria Hill : Hulk, Rogers, Nick Fury", 
                  "Agent-X : Agent 13, Rogers", 
                  "Norman Osborn: Tony Stark, Thor" ]


# In[21]:


prim_key = "Nick Fury";

abc = dict();
shield = [];
hydra =[];
				  
for line in  communication:
	str = line.split(':');
	keyval = str[0].strip()
	abc[keyval] = str[1];
	
def addShields(key):
	if key not in shield:
		if key in abc.keys():
			shield.append(key)
			agents = abc[key].split(',')
			for agent in agents:
				agent = agent.strip()
				addShields(agent)
	
		
def findHacker(prim):
	addShields(prim)
	for x in abc.keys():
		if x not in shield:
			hydra.append(x)
		
	for hack in hydra:
		print("HYDRA:", hack)
		
findHacker(prim_key)


# In[ ]:




