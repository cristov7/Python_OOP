class Topic:
    def __init__(self, topic_id: int, topic: str, storage_folder: str):
        self.id = topic_id
        self.topic = topic
        self.storage_folder = storage_folder

    def edit(self, new_topic: str, new_storage_folder: str) -> None:
        self.topic = new_topic
        self.storage_folder = new_storage_folder

    def __repr__(self) -> str:
        topic_id = self.id
        topic = self.topic
        storage_folder = self.storage_folder
        return f"Topic {topic_id}: {topic} in {storage_folder}"
