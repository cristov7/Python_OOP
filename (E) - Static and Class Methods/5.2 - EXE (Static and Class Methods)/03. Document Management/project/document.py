from typing import List
from project.category import Category
from project.topic import Topic


class Document:
    def __init__(self, document_id: int, category_id: int, topic_id: int, file_name: str):
        self.id = document_id
        self.category_id = category_id
        self.topic_id = topic_id
        self.file_name = file_name
        self.tags: List[str] = []

    @classmethod
    def from_instances(cls, document_id: int, category: Category, topic: Topic, file_name: str):
        category_id = category.id
        topic_id = topic.id
        return cls(document_id, category_id, topic_id, file_name)

    def add_tag(self, tag_content: str) -> None:
        if tag_content not in self.tags:
            self.tags.append(tag_content)

    def remove_tag(self, tag_content: str) -> None:
        if tag_content in self.tags:
            self.tags.remove(tag_content)

    def edit(self, file_name: str) -> None:
        self.file_name = file_name

    def __repr__(self) -> str:
        document_id = self.id
        file_name = self.file_name
        category_id = self.category_id
        topic_id = self.topic_id
        tags = ", ".join(self.tags)
        return f"Document {document_id}: {file_name}; category {category_id}, topic {topic_id}, tags: {tags}"
