import os
from mem0 import Memory

os.environ["OPENAI_API_KEY"] = ""
os.environ["OPENAI_BASE_URL"] = "https://api.openai.com/v1"

config = {
    "llm": {
        "provider": "openai",
        "config": {
            "model": "gpt-4o-mini",
            "temperature": 0.2,
            "max_tokens": 1500,
        }
    },
    "history_db_path": "history.db"
}

m = Memory.from_config(config)

result = m.add("I am working on improving my tennis skills. Suggest some online courses.", user_id="alice", metadata={"category": "hobbies"})

# Created memory --> 'Improving her tennis skills.' and 'Looking for online suggestions.'
# print(result)

# 检索所有记忆
all_memories = m.get_all()

# print(all_memories)

memory_id = all_memories[0]["id"]
# 检索特定记忆
specific_memory = m.get(memory_id)


related_memories = m.search(query="What are Alice's hobbies?", user_id="alice")


result = m.update(memory_id=memory_id, data="Likes to play tennis on weekends")

history = m.history(memory_id=memory_id)

# print(history)

m.delete(memory_id=memory_id)  
m.delete_all(user_id="alice")  
m.reset()