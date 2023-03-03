from project.user import User
from project.library import Library


class Registration:
    def add_user(self, user: User, library: Library) -> [None, str]:   # user == user_object, library == library_object
        if user not in library.user_records:
            library.user_records.append(user)
        else:   # elif user in library.user_records:
            user_id = user.user_id
            return f"User with id = {user_id} already registered in the library!"

    def remove_user(self, user: User, library: Library) -> [None, str]:   # user == user_object, library == library_object
        if user in library.user_records:
            library.user_records.remove(user)
        else:   # elif user not in library.user_records:
            return "We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str, library: Library) -> str:   # library == library_object
        user_objects_list = [user_object for user_object in library.user_records
                             if user_object.user_id == user_id]
        if user_objects_list:   # if len(user_objects_list) > 0:
            user_object = user_objects_list[0]
            if user_object.username == new_username:
                return "Please check again the provided username - it should be different than the username used so far!"
            else:   # elif user_object.username != new_username:
                for username, books_dict in library.rented_books.items():
                    if username == user_object.username:
                        del library.rented_books[username]
                        library.rented_books[new_username] = books_dict
                        break
                    else:   # elif username != user_object.username:
                        continue
                user_object.username = new_username
                return f"Username successfully changed to: {new_username} for user id: {user_id}"
        else:   # elif len(user_objects_list) == 0:
            return f"There is no user with id = {user_id}!"
