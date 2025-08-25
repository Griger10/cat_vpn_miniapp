from aiogram.fsm.state import StatesGroup, State


class AddKeyFSM(StatesGroup):
    user = State()
    key = State()
    valid_until = State()
    success = State()
