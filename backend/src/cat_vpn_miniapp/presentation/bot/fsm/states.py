from aiogram.fsm.state import State, StatesGroup


class AddKeyFSM(StatesGroup):
    user = State()
    key = State()
    valid_until = State()
    success = State()
