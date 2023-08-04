"""
Задание №6. Напишите программу банкомат.
Начальная сумма равна нулю.
Допустимые действия: пополнить, снять, выйти.
Сумма пополнения и снятия кратны 50 у.е.
Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
После каждой третей операции пополнения или снятия начисляются проценты - 3%.
Нельзя снять больше, чем на счёте.
При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной.
Любое действие выводит сумму денег.
"""
from typing import Union

FEE_MIN: int = 30  # minimum amount of fee
FEE_MAX: int = 600  # minimum amount of fee
FEE_PERCENT: float = 1.5  # percentage of the fee
BONUS_PERCENT: int = 3  # bonus percentage
BONUS_CHECK: int = 3  # amount of operations must be multiple of
RICH_TAX: int = 10  # rich tax percentage
RICH_VALUE: int = 5000000  # rich boarder value
VALUE_CHECK: int = 50  # amount of money must be multiple of

MSG_ACCOUNT: str = 'Your account is: {balance}'
MSG_TOP_UP: str = 'Top up value: {top}. Your account is: {balance}'
MSG_WITHDRAW: str = 'Withdrawal value: {withdraw}. Your account is: {balance}'
MSG_ERROR: str = 'Value must be % 50. '
MSG_AMOUNT: str = 'You trying to withdraw more than your account balance: {balance}'
MSG_FEE: str = 'Fee of operation will be: {fee}'
MSG_RICH_TAX: str = 'Your bank account: "{balance}" is greater than {max_value}.'
MSG_RICH_TAX_APPLIED: str = 'Applied rich tax: {tax}. Your balance: {balance}'
MSG_BONUS_APPLIED: str = 'Applied bonus: {bonus}. Your balance: {balance}'
MSG_EXIT: str = 'Exited. Your balance: {balance}'


class Atm:
    def __init__(self):
        self.account = 0
        self.count_of_operations = 0

    def check_balance(self) -> None:
        """
        Check if balance is greater than rich tax boarder value.
        """
        if self.account > RICH_VALUE:
            print(MSG_RICH_TAX.format(balance=self.account, max_value=RICH_VALUE))
            self.apply_rich_tax()

    def apply_rich_tax(self) -> None:
        """
        Apply rich tax before operation.
        """
        self.account -= (tax := self.account * RICH_TAX / 100)
        print(MSG_RICH_TAX_APPLIED.format(tax=tax, balance=self.account))

    def check_value(self, value: Union[int, float]) -> bool:
        """
        Check if value is multiple of VALUE_CHECK.
        :param value: value to check.
        :return: True if number is multiple of VALUE_CHECK, False otherwise.
        :raise: RuntimeError if TypeError catch.
        """
        try:
            return True if not value % VALUE_CHECK else False

        except TypeError as error:
            raise RuntimeError(
                f'Error: "{error}". ' + MSG_ACCOUNT.format(balance=self.account)
            ) from error

    def check_amount(self, amount: Union[int, float]) -> None:
        """
        Check if amount is lower or equal to bank account.
        :param amount: amount of money to withdraw.
        :raise: RuntimeError if amount greater than bank account.
        """
        if amount > self.account:
            raise RuntimeError(MSG_AMOUNT.format(balance=self.account))

    def check_count_of_operations(self) -> None:
        """
        Check if operation is a bonus one.
        """
        if not self.count_of_operations % BONUS_CHECK:
            self.apply_bonus()

    def apply_bonus(self) -> None:
        """
        Applying a bonus to the account.
        """
        self.account += (bonus := self.account * BONUS_PERCENT / 100)
        print(MSG_BONUS_APPLIED.format(bonus=bonus, balance=self.account))

    @staticmethod
    def calculate_withdraw_fee(money: Union[int, float]) -> Union[int, float]:
        """
        Calculate fee of withdraw operation.
        :param money: amount of money to withdraw.
        :return: amount of fee.
        """
        fee = money / 100 * FEE_PERCENT

        if fee < FEE_MIN:
            fee = FEE_MIN

        elif fee > FEE_MAX:
            fee = FEE_MAX

        print(MSG_FEE.format(fee=fee))
        return fee

    def top_up(self, money: Union[int, float]) -> None:
        """
        Top up your bank account.
        :param money: money to top up your account.
        """
        self.check_balance()
        if self.check_value(value=money):
            self.account += money
            self.count_of_operations += 1
            self.check_count_of_operations()
            print(MSG_TOP_UP.format(top=money, balance=self.account))
        else:
            print(MSG_ERROR + MSG_ACCOUNT.format(balance=self.account))

    def withdraw(self, money: float) -> None:
        """
        Withdraw from your bank account.
        :param money: amount of money to withdraw.
        """
        self.check_balance()
        if self.check_value(value=money):
            fee = self.calculate_withdraw_fee(money=money)
            amount = money + fee
            self.check_amount(amount=amount)
            self.account -= amount
            self.count_of_operations += 1
            self.check_count_of_operations()
            print(MSG_WITHDRAW.format(withdraw=amount, balance=self.account))
        else:
            print(MSG_ERROR + MSG_ACCOUNT.format(balance=self.account))

    def exit(self) -> int:
        """
        Exit from the program.
        :return: exit code.
        """
        self.check_balance()
        print(MSG_EXIT.format(balance=self.account))
        return -1


bank_account = Atm()
bank_account.top_up(10000000)
bank_account.exit()
bank_account.withdraw(134)
