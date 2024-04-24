from django.core.exceptions import ValidationError
import re


def validate_test(value):
    check = re.fullmatch(r'[a-zA-Z0-9.@+_-]{0,15}', value) #Кириллица, цифры и символы .@+_-
    if not check:
        raise ValidationError(
            "Используйте указанные символы.",
            params={"value": value},
        )