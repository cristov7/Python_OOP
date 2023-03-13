class Category:
    def __init__(self, category_id: int, name: str):
        self.id = category_id
        self.name = name

    def edit(self, new_name: str) -> None:
        self.name = new_name

    def __repr__(self) -> str:
        category_id = self.id
        name = self.name
        return f"Category {category_id}: {name}"
