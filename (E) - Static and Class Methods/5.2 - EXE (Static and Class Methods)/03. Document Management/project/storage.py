from typing import List
from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories: List[Category] = []   # [category_objects]
        self.topics: List[Topic] = []          # [topic_objects]
        self.documents: List[Document] = []    # [document_objects]

    def add_category(self, category: Category) -> None:   # category == category_object
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic) -> None:   # topic == topic_object
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document) -> None:   # document == document_object
        if document not in self.documents:
            self.documents.append(document)

    @staticmethod
    def search_object(object_id: int, objects_list: list) -> [object, None]:
        current_objects_list = [current_object for current_object in objects_list
                                if current_object.id == object_id]
        if current_objects_list:
            current_object = current_objects_list[0]
            return current_object

    def edit_category(self, category_id: int, new_name: str) -> None:
        category_object = self.search_object(category_id, self.categories)
        if category_object:
            category_object.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str) -> None:
        topic_object = self.search_object(topic_id, self.topics)
        if topic_object:
            topic_object.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str) -> None:
        document_object = self.search_object(document_id, self.documents)
        if document_object:
            document_object.edit(new_file_name)

    def delete_category(self, category_id: int) -> None:
        category_object = self.search_object(category_id, self.categories)
        if category_object:
            self.categories.remove(category_object)

    def delete_topic(self, topic_id: int) -> None:
        topic_object = self.search_object(topic_id, self.topics)
        if topic_object:
            self.topics.remove(topic_object)

    def delete_document(self, document_id: int) -> None:
        document_object = self.search_object(document_id, self.documents)
        if document_object:
            self.documents.remove(document_object)

    def get_document(self, document_id: int) -> str:
        document_object = self.search_object(document_id, self.documents)
        if document_object:
            return document_object.__repr__()   # document_object.__repr__() == str(document_object)

    def __repr__(self) -> str:
        documents = "\n".join([document_object.__repr__()   # document_object.__repr__() == str(document_object)
                               for document_object in self.documents])
        return f"{documents}"
