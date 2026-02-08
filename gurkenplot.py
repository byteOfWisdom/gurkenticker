#!python3
from matplotlib import pyplot as plt
import matplotlib as mpl
import numpy as np
import std


def parse_date(s):
    s = s.replace(".", "-")
    return np.datetime64(s)


@np.vectorize
def to_delta_t(timestamp):
    dt = timestamp - np.datetime64("1970-01-01")
    return int(dt / np.timedelta64(1, "D"))


@np.vectorize
def format_date(time_days, _) -> str:
    start = np.datetime64("1970-01-01")
    return np.datetime_as_string(start + np.timedelta64(time_days, "D"))


def parse_csv(fname):
    content = std.readfile(fname)
    dates = [parse_date(line.split(";")[0]) for line in content]
    prices = [float(line.split(";")[1]) for line in content]
    return dates, prices


def main():
    dates, prices = parse_csv("./gurken.csv")
    std.default.plt_pretty("Datum", "Gurkenpreis / €")
    days = to_delta_t(dates)
    print(days)
    for d in days:
        print(format_date(d, None))
    plt.scatter(days, prices)
    formatter = mpl.dates.DateFormatter('%d-%m-%Y')
    plt.gca().xaxis.set_major_formatter(formatter)
    # plt.gca().xaxis.set_major_formatter(format_date)
    plt.show()
    

if __name__ == "__main__":
    main()
