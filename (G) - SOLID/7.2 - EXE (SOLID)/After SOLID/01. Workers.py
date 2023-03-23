# # Dependency Inversion (DIP):


from abc import ABC, abstractmethod


class BaseWorker(ABC):
    @staticmethod
    @abstractmethod
    def work() -> None:
        pass


class Worker(BaseWorker):
    @staticmethod
    def work() -> None:
        print("I'm working!!")


class SuperWorker(BaseWorker):
    @staticmethod
    def work() -> None:
        print("I work very hard!!!")


class Manager:
    def __init__(self):
        self.worker: [Worker, SuperWorker, None] = None

    def set_worker(self, worker: object) -> [None, Exception]:
        assert isinstance(worker, BaseWorker), f'`worker` must be of type {BaseWorker}'
        self.worker = worker

    def manage(self) -> None:
        if self.worker is not None:
            self.worker.work()


worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()

super_worker = SuperWorker()
try:
    manager.set_worker(super_worker)
    manager.manage()
except AssertionError:
    print("manager fails to support super_worker....")

# I'm working!!
# I work very hard!!!
