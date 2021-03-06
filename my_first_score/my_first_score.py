from iconservice import *

TAG = 'FirstScore'


class FirstScore(IconScoreBase):

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)

    def on_install(self) -> None:
        super().on_install()

    def on_update(self) -> None:
        super().on_update()
    
    @external(readonly=True)
    def hello(self) -> str:
        Logger.debug(f'Hello, world!', TAG)
        return f"hello, {self.msg.sender}. My name is {self.name()}"

    @external
    @payable
    def receive_funds(self) -> None:
        Logger.debug(f"{self.msg.value} received from {self.msg.sender}", TAG)

    @external(readonly=True)
    def name(self) -> str:
        return 'Swopnil Parajuli'

