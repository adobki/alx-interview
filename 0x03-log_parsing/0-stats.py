#!/usr/bin/python3
""" Log parsing challenge """
from random import random, randint
from re import match
from sys import stdin
from time import sleep
from typing import Iterable, Optional


def check_line(log_line: str, status_codes: Iterable[int]) -> Iterable[int]:
    """ Checks a line to ensure it is in the right log format """
    try:
        # Check for valid IP address
        ip = match(r'([0-9]{1,3}\.){3}[0-9]{1,3}', log_line).span()[1]

        # Check valid date sequence follows IP
        date = match(r' - \[.*]', log_line[ip:]).span()[1]

        # Check request info string follows date
        req = match(' ".*"', log_line[ip + date:]).span()[1]
        req_str = log_line[ip + date:][:req].split()
        if len(req_str) != 3:
            raise AttributeError('Invalid request string format!')

        # Check valid status code follows request string
        status = match(' [0-9]{3}', log_line[ip + date + req:-1]).span()[1]
        status_str = int(log_line[ip + date + req:][:status])
        if status_str not in status_codes:
            raise AttributeError('Invalid HTTP status code!')

        # Check valid file size at end of line
        size = match(r' \d*$', log_line[ip + date + req + status:]).span()[1]
        size_str = int(log_line[ip + date + req + status:][:size])

        # Get and return status code and file size
        return status_str, size_str

    # Catch AttributeError raised when a regex match fails on log_line
    except AttributeError:
        pass
    # except AttributeError as err:
    #     print('Invalid line!', err, end='\t')

    return 0, 0


# def log_parser(log_lines: list) -> str:
def log_parser(log_lines: Optional[list] = None) -> None:
    """ Reads stdin line by line and computes various metrics """
    line = ' '
    lines, status_code, file_size, i = 1, 0, 0, 0
    status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    summary = {'codes': {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                         '404': 0, '405': 0, '500': 0},
               'size': 0}

    while line:
        skip, close = False, False
        try:
            # Use list for inputs if one was passed, else use standard input
            if log_lines:
                line = log_lines[i]
                i += 1

                # Pause for 1 or 0 seconds
                sleep(random())

                # Make line invalid at random for testing with list
                if not randint(0, 4):
                    line = f'zz{line}'
                if not randint(0, 4):
                    line = ' '.join(line.split()[:-1])
                if not randint(0, 4):
                    line = ' '.join(line.split('"'))
                if not randint(0, 2):
                    tmp = line.rfind(' ') - 2
                    line = f'{line[:tmp]}9{line[tmp + 1:]}'
            else:
                line = stdin.readline()

            # Check if line is right format and parse needed data
            status_code, file_size = check_line(line, status_codes)
            if not status_code or not file_size:
                skip = True
        # except (KeyboardInterrupt, EOFError) as err:
        #     print(f'You quit! Haha! [{err}]')
        except (KeyboardInterrupt, EOFError):
            close = True
            break
        except IndexError as err:
            # print(f'Shit! [{err}]')
            close = True
            break
        finally:
            # if not close:
            #     print(f'{lines:2d}. {line[:-1]}')
            if not close and not skip and file_size and status_code:
                # Record file size
                summary['size'] += file_size
                # Record status code
                summary['codes'][str(status_code)] += 1
            if lines and not lines % 10 or close:
                # Print current status
                print(f'File size: {summary["size"]}')
                for key in sorted(summary['codes'].keys()):
                    if summary['codes'].get(key):
                        print(f'{key}: {summary["codes"][key]}')
                # Reset codes status
                summary['codes'] = {'200': 0, '301': 0, '400': 0, '401': 0,
                                    '403': 0, '404': 0, '405': 0, '500': 0}
            lines += 1


if __name__ == '__main__':
    """ Tests the code in this module """
    # import datetime
    # logs = []
    # base = '{:d}.{:d}.{:d}.{:d} - [{}] "GET /projects/260 HTTP/1.1" {} {}\n'
    # for i in range(10000):
    #     logs.append(
    #         base.format(randint(1, 255), randint(1, 255),
    #                     randint(1, 255), randint(1, 255),
    #                     datetime.datetime.now(),
    #                     choice(status_codes),
    #                     randint(1, 1024))
    #     )
    # log_parser(logs)
    log_parser()
