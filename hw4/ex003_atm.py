"""
Возьмите задачу о банкомате из семинара 2.
Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список.
"""
from typing import Union

FEE_MIN = 30  # minimum amount of fee
FEE_MAX = 600  # minimum amount of fee
FEE_PERCENT = 1.5  # percentage of the fee
BONUS_PERCENT = 3  # bonus percentage
BONUS_CHECK = 3  # amount of operations must be multiple of
RICH_TAX = 10  # rich tax percentage
RICH_VALUE = 5000000  # rich boarder value
VALUE_CHECK = 50  # amount of money must be multiple of

MSG_ACCOUNT = 'Your account is: {balance}'
MSG_TOP_UP = 'Top up value: {top}. Your account is: {balance}'
MSG_WITHDRAW = 'Withdrawal value: {withdraw}. Your account is: {balance}'
MSG_ERROR = 'Value must be % 50. '
MSG_AMOUNT = 'You trying to withdraw more than your account balance: {balance}'
MSG_FEE = 'Fee of operation will be: {fee}'
MSG_RICH_TAX = 'Your bank account: "{balance}" is greater than {max_value}.'
MSG_RICH_TAX_APPLIED = 'Applied rich tax: {tax}. Your balance: {balance}'
MSG_BONUS_APPLIED = 'Applied bonus: {bonus}. Your balance: {balance}'
MSG_EXIT = 'Exited. Your balance: {balance}'


class Atm:
    """ Class for ATM. """

    def __init__(self):
        self.account = 0
        self.count_of_operations = 0
        self.operations: list[str] = []

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
            return not value % VALUE_CHECK

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
            self.operations.append(MSG_TOP_UP.format(top=money, balance=self.account))
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
            self.operations.append(MSG_WITHDRAW.format(withdraw=amount, balance=self.account))
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
print(bank_account.operations)
