import os
import json

class Memory:

    def __init__(self):

        os.makedirs("data", exist_ok=True)

        self.file = "data/user_memory.json"

        if not os.path.exists(self.file):

            with open(self.file, "w") as f:

                json.dump({}, f)

    def load(self):

        with open(self.file, "r") as f:

            return json.load(f)

    def save(self, data):

        with open(self.file, "w") as f:

            json.dump(data, f, indent=4)


memory = Memory()