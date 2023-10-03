#!/usr/bin/python3
""" Lockboxes challenge """

# Global variable for recursive function
boxes_unlocked = []


def unlocker(boxes: list, box: int = 0, i: int = 0):
    """ Goes through the boxes and unlocks them recursively """
    # Unlock current box
    boxes_unlocked[box] = True

    # Check if array indexes are valid before proceeding
    if box >= len(boxes) or i >= len(boxes[box]) or False not in boxes_unlocked:
        return

    # Check for key and unlock next box if box has key and key's box is locked
    key = int(boxes[box][i]) if isinstance(boxes[box][i], (int, str, bytes)) else 0
    if key and key < len(boxes) and not boxes_unlocked[key]:
        unlocker(boxes, key)

    # Move to next key in box if available
    i += 1
    if i < len(boxes[box]):
        unlocker(boxes, box, i)


def canUnlockAll(boxes):
    """ Returns True if all contained boxes can be opened, False otherwise """
    if len(boxes) == 1:
        return True

    # Update boxes locked state in global variable boxes_unlocked
    boxes_unlocked.clear()
    for item in [False] * len(boxes):
        boxes_unlocked.append(item)

    # Unlock boxes with available keys
    unlocker(boxes)

    # return True if all boxes were unlocked, else False
    return False if False in boxes_unlocked else True


if __name__ == '__main__':
    boxes = [[1]]
    print(canUnlockAll(boxes))

    boxes = ['[1]']
    print(canUnlockAll(boxes))

    boxes = [[1], ['2']]
    print(canUnlockAll(boxes))

    boxes = [[2], ['2']]
    print(canUnlockAll(boxes))

    boxes = [[12, 1, 2], ['1'], []]
    print(canUnlockAll(boxes))

    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, None, [False]], [2], [{0: 9}, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))
