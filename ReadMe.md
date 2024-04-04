# Abstract

This project is an alternative to [Generative Agents](https://github.com/joonspk-research/generative_agents.git), substituting the GPT model with the Mixtral model from the University of Illinois at Urbana-Champaign. The aim is to conduct simulations with specific persona settings and evaluate the Mixtral model's performance in interactions resembling human-like NPC communication.

## Files Modified

- reverie/backend_server/persona/prompt_template/gpt_structure.py
- reverie/backend_server/persona/prompt_template/run_gpt_prompt.py
- reverie/backend_server/reverie.py
- All files under reverie/backend_server/persona/prompt_template
- reverie.py

For the details of the changes, see the comments within the files.

**New File Added:**
- `run_simulations` easier method to run the simulation with large number of steps
- `environment/frontend_server/storage/base_the_vile_n5` 5 person version of simulation with some evial personality
- `reverie/backend_server/API.py` (Used for accessing the Llama model From university)
> **Note**: If you are the student in the university, asked the acess account and password First and you need enter the account and password into this API file before any simulation beginning

## Simulation Steps

### Step 0
Download all required envirnoment which stored in 'environment/frontend_server/requirements.txt'

### Step 1

Open a terminal and navigate to the frontend_server directory.

```bash
cd environment/frontend_server
```
Then run the server.
```bash
python manage.py runserver
```

### Step 2
In another terminal, navigate to the backend_server directory. 
```bash
cd reverie/backend_server
```
Then run the backend.
```bash
python reverie.py
```
### Step 3
Follow the on-screen instructions for setup.

1. You'll be prompted to `Enter the name of the forked simulation:`
  - Go to `environment/frontend_server/storage` to see package names:
    - `base_the_ville_isabella_maria_klaus`: a smaller simulation with 3 people
    - `base_the_ville_n25`: a larger simulation with 25 people
  - Chooce the enter the package name which you want to simulation
  -  For testing, considering less computation cost, enter:
  ```bash
  base_the_ville_isabella_maria_klaus
  ```

2. Then it would shows `Enter the name of the new simulation:` and you can type any name like:
```bash
test-simulation
```

4. Finally, in `Enter option:`, type `run` followed by a number to specify the simulation duration like:
```bash
 run 10
```

## Final Steps:
You would able to see the `Enter option:` again after one simulation complete:
- To save the results, type `fin`
- To exit without saving, type `exit`
- To run another simulation, type "run" followed by a number.





