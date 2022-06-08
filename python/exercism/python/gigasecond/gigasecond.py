from datetime import timedelta, datetime


def add(moment):
    days, seconds = divmod(1e9, 3600*24)
    hours, seconds = divmod(seconds, 3600)

    return moment + timedelta(days=days, hours=hours, seconds=seconds)