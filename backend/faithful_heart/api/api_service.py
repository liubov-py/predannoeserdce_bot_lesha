from datetime import datetime

from openpyxl import Workbook

from faithful_heart import constants
from faithful_heart.settings import MEDIA_ROOT


def export_users_excel(users):
    """
    Создание файла excel с данными пользователей.
    """
    date_now = datetime.now()
    date_now_formatted = date_now.strftime(constants.DATETIME_FORMAT)
    workbook = Workbook()
    sheet = workbook.active
    sheet.column_dimensions["A"].width = 10
    sheet.column_dimensions["B"].width = 15
    sheet.column_dimensions["C"].width = 18
    sheet.column_dimensions["D"].width = 18
    sheet.column_dimensions["E"].width = 18
    sheet.column_dimensions["F"].width = 18
    headers = [
        "Name",
        "Surname",
        "Phone Number",
        "Username",
        "Chat_id",
        "Email",
    ]
    sheet.append(headers)
    for user in users:
        sheet.append(
            [
                user.name,
                user.surname,
                user.phone_number,
                user.username,
                user.chat_id,
                user.email,
            ]
        )
    workbook.save(f"{MEDIA_ROOT}/Пользователи_{date_now_formatted}.xlsx")

