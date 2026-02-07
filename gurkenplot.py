#!python3
from matplotlib import pyplot as plt
import numpy as np
import std


def parse_date(s):
    s = s.replace(".", "-")
    return s
    return np.datetime64(s)


def to_delta_t(timestamp):
    np.timedelta64(timestamp - np.datetime64("2026-01-01"), "d")
    return timestamp

def format_date(epoch_timestamp, _) -> str:
    # return strftime('%Y-%m-%d', localtime(epoch_timestamp))
    return str(epoch_timestamp)


def parse_csv(fname):
    content = std.readfile(fname)
    dates = [parse_date(line.split(";")[0]) for line in content]
    prices = [float(line.split(";")[1]) for line in content]
    return dates, prices

def main():
    dates, prices = parse_csv("./gurken.csv")
    std.default.plt_pretty("Datum", "Gurkenpreis / €")
    plt.scatter(dates, prices)
    plt.gca().xaxis.set_major_formatter(format_date)
    plt.show()
    

if __name__ == "__main__":
    main()
