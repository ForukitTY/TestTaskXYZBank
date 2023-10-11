import csv
import arrow
import datetime


def solve_fibonacci_quiz() -> int:
    def fib(n):
        # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,
        if n in [2, 3]:
            return 1
        return fib(n - 1) + fib(n - 2)

    day: int = datetime.date.today().day
    res: int = fib(day + 1)
    return res


def save_transactions_to_scv(rows, path):
    """
    :param rows: List like [{'Date-Time': 'Oct 9, 2023 3:34:42 PM', 'Amount': '34', 'Transaction Type': 'Debit'},...]
    :param path: директория, куда сохранять результат
    :return: None
    """
    with open(f'{path}/transactions.csv', 'w', newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter=' ')
        for row in rows:
            date_time_from_row: str = row["Date-Time"]

            # преобразую "Oct 9, 2023 3:34:42 AM" в формат "ДД Месяц ГГГГ ЧЧ:ММ:СС"
            date_time = datetime.datetime.strptime(date_time_from_row, '%b %d, %Y %I:%M:%S %p')
            time_ = str(date_time.time())
            date = arrow.get(str(date_time.date()), "YYYY-MM-DD").format("DD MMMM YYYY", locale="ru")
            join_date_time = " ".join([date, time_])

            amount = int(row["Amount"])  # Пополнять и снимать можно только целочисленные значения, поэтому в int
            transaction_type: str = row["Transaction Type"]

            writer.writerow([join_date_time, amount, transaction_type])
