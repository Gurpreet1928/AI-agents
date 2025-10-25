# agent.py
import os, time, json, random
import requests
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class CloudInsightAgent:
    def __init__(self):
        self.memory = []
        self.goal = "Analyze system metrics and suggest optimizations. Reapply optimizations and do analysis again"

    def fetch_metrics(self):
        # generate some values to "FEED" to LLM and get suggestions, these values can be replaced by actual data from system
        metrics = {
            "cpu_usage": random.randint(30, 95),
            "memory_usage": random.randint(40, 90),
            "latency_ms": random.randint(10, 200)
        }
        print(f" Metrics from the system: {metrics}")
        return metrics

    def think(self, metrics):
        # send data to LLM and get suggestions on "ACTION"
        prompt = f"""
        Based on the system metrics: {json.dumps(metrics)},
        suggest optimizations or debugging.
        """
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a cloud optimization agent."},
                {"role": "user", "content": prompt}
            ]
        )
        action = response.choices[0].message.content.strip()
        print(f" Received action from LLM : {action}")
        return action

    def act(self, action):
        # execute the action ( feed it back to the system) 
        result = f" Performed analysis: {action}"
        self.memory.append(result)
        print(f" Action taken: {result}")
        return result

    def run(self, steps=3):
        print(" Starting my Cloud Agent...\n")
        for i in range(steps):
            metrics = self.fetch_metrics()
            action = self.think(metrics)
            self.act(action)
            time.sleep(1)
        print("\n Memory Log:")
        for entry in self.memory:
            print("-", entry)

if __name__ == "__main__":
    agent = CloudInsightAgent()
    agent.run()

