# # Interface Segregation (ISP):


from abc import ABC, abstractmethod
import time


class Work(ABC):
    @staticmethod
    @abstractmethod
    def work() -> None:
        pass


class Eat(ABC):
    @staticmethod
    @abstractmethod
    def eat() -> None:
        pass


class Worker(Work, Eat):
    @staticmethod
    def work() -> None:
        print("I'm normal worker. I'm working.")

    @staticmethod
    def eat() -> None:
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(Work, Eat):
    @staticmethod
    def work() -> None:
        print("I'm super worker. I work very hard!")

    @staticmethod
    def eat() -> None:
        print("Lunch break....(3 secs)")
        time.sleep(3)


class Robot(Work):
    @staticmethod
    def work() -> None:
        print("I'm a robot. I'm working....")


class Manager(ABC):
    def __init__(self):
        self.worker: [Worker, SuperWorker, Robot, None] = None

    @abstractmethod
    def set_worker(self, worker: object) -> [None, Exception]:
        pass


class WorkManager(Manager):
    def set_worker(self, worker: object) -> [None, Exception]:
        assert isinstance(worker, Work), f"`worker` must be of type {Work}"
        self.worker = worker

    def manage(self) -> None:
        self.worker.work()


class BreakManager(Manager):
    def set_worker(self, worker: object) -> [None, Exception]:
        assert isinstance(worker, Eat), f"`worker` must be of type {Eat}"
        self.worker = worker

    def lunch_break(self) -> None:
        self.worker.eat()


work_manager = WorkManager()
break_manager = BreakManager()
work_manager.set_worker(Worker())
break_manager.set_worker(Worker())
work_manager.manage()
break_manager.lunch_break()

work_manager.set_worker(SuperWorker())
break_manager.set_worker(SuperWorker())
work_manager.manage()
break_manager.lunch_break()

work_manager.set_worker(Robot())
work_manager.manage()
try:
    break_manager.set_worker(Robot())
    break_manager.lunch_break()
except:
    pass

# I'm normal worker. I'm working.
# Lunch break....(5 secs)
# I'm super worker. I work very hard!
# Lunch break....(3 secs)
# I'm a robot. I'm working....
