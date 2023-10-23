#!/usr/bin/python3
"""Log parsing challenge"""
from typing import List, Union, Optional


def validUTF8(data: List[int], verbose: Optional[bool] = False) -> bool:
    """
    param data: A list of integers that represent the binary data to
                be parsed.
    return: True if data is in a valid UTF-8 format, False otherwise
    """
    if not isinstance(data, list) \
            or False in [isinstance(x, int) for x in data]:
        return False

    continuation_bytes = 0
    for num in data:
        # Convert integer to byte/eight least significant bits (256 == 2^8)
        num %= 256

        # Print verbose output
        if verbose:
            left = continuation_bytes
            print(f'{num}[{left}], ' if left else f'{num}, ', end='')

        if num >= 254:
            # Invalid byte -> 254 or 255 > maximum 253 '1111110x' for UTF-8
            return False
        if num < 128:
            # Continuation byte '10xxxxxx' expected but not found '0xxxxxxx'
            if continuation_bytes:
                return False
            # Valid 8-bit/byte character expected/found. Move on to next byte
        elif num < 192:
            # Continuation byte '10xxxxxx' provided but not expected
            if not continuation_bytes:
                return False
            # Continuation byte found, update remainder
            continuation_bytes -= 1
        elif num >= 192:
            # Continuation byte '10xxxxxx' expected but not found '11xxxxxx'
            if continuation_bytes:
                return False
            # Character with multiple bytes found. Get length/number of bytes
            continuation_bytes = len(bin(num)[2:].split('0')[0]) - 1

        # Valid byte. Move to next byte in sequence

    # No invalid bytes found in sequence after parsing all bytes
    return True


if __name__ == '__main__':
    """Tests the code in this module"""
    def print_decimal_binary(dec: Union[int, list]) -> None:
        """Convert one/list of decimal(s) to binary then prints it/them"""
        if not isinstance(dec, (int, list)):
            return
        dec = [dec] if isinstance(dec, int) else dec
        for num in dec:
            num %= 256
            print(f'{num:>8}: {bin(num)[2:]:0>8} <- {bin(num)}')

    data = [65]
    print(validUTF8(data, verbose=True))
    print_decimal_binary(data)

    data = [80, 121, 116, 104, 111, 110, 32, 105,
            115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data, verbose=True))
    print_decimal_binary(data)

    data = [229, 65, 127, 256]
    print(validUTF8(data, verbose=True))
    print('ERROR: Continuation byte "10xxxxxx" expected but not found @65')
    print_decimal_binary(data)
