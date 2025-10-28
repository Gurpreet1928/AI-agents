python3 --version : python3.9.6
python3 -m venv venv

pip3 install -r requirements.txt   ( pip3 for mac)

#generate PAI keys
Go to https://platform.openai.com
Sign in (or create a free account).
In the top-right corner, click your profile picture → View API keys
Click Create new secret key
Copy the generated key (looks like sk-abc123...)
( pay for the plan if needed, if you receive error like insufficient quota)

touch .env
**# add OPENAI_API_KEY=... in .env**

python3 agent.py
