from app.memory.store import LocalMemory

def test_memory_roundtrip(tmp_path):
    store=LocalMemory(str(tmp_path/"memory.json"))
    store.save({"name":"Mika"})
    assert store.load()["name"]=="Mika"
