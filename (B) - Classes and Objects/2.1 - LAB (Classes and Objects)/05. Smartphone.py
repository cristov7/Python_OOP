from typing import List


class Smartphone:
    def __init__(self, memory: int):
        self.memory = memory
        self.apps: List[str] = []
        self.is_on: bool = False

    def power(self) -> None:
        if not self.is_on:   # if self.is_on == False:
            self.is_on = True
        else:   # elif self.is_on == True:
            self.is_on = False

    def install(self, app: str, app_memory: int) -> str:
        if self.is_on:  # if self.is_on == True:
            if self.memory >= app_memory:
                self.apps.append(app)
                self.memory -= app_memory
                return f"Installing {app}"
            else:   # elif self.memory < app_memory:
                return f"Not enough memory to install {app}"
        else:  # elif self.is_on == False:
            return f"Turn on your phone to install {app}"

    def status(self) -> str:
        total_apps_count = len(self.apps)
        memory_left = self.memory
        return f"Total apps: {total_apps_count}. Memory left: {memory_left}"


# smartphone = Smartphone(100)
# print(smartphone.install("Facebook", 60))
# smartphone.power()
# print(smartphone.install("Facebook", 60))
# print(smartphone.install("Messenger", 20))
# print(smartphone.install("Instagram", 40))
# print(smartphone.status())


# from typing import List
# 
# 
# class Smartphone:
#     def __init__(self, memory: int):
#         self.memory = memory
#         self.apps: List[str] = []
#         self.is_on: bool = False
# 
#     def power(self) -> None:
#         if not self.is_on:   # if self.is_on == False:
#             self.is_on = True
#         else:   # elif self.is_on == True:
#             self.is_on = False
# 
#     def install(self, app: str, app_memory: int) -> str:
#         if self.memory >= app_memory and self.is_on:
#             self.apps.append(app)
#             self.memory -= app_memory
#             return f"Installing {app}"
#         elif self.memory >= app_memory and not self.is_on:
#             return f"Turn on your phone to install {app}"
#         else:
#             return f"Not enough memory to install {app}"
# 
#     def status(self) -> str:
#         total_apps_count = len(self.apps)
#         memory_left = self.memory
#         return f"Total apps: {total_apps_count}. Memory left: {memory_left}"
