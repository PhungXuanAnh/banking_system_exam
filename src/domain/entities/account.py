from pydantic import BaseModel, ConfigDict


class Account(BaseModel):
    id: int = None
    account_number: str = None
    customer_id: int
    balance: float = 0
    model_config = ConfigDict(from_attributes=True)

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        self.balance -= amount

    def get_balance(self):
        return self.balance
