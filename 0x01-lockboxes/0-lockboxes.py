#!/usr/bin/python3
""" Lockboxes challenge """


def canUnlockAll(boxes):
    """ Returns True if all contained boxes can be opened, False otherwise """
    if not isinstance(boxes, list):
        return False
    for box in boxes:
        if not isinstance(box, list):
            return False
    if len(boxes) == 1:
        return True

    # Set boxes locked state
    boxes_unlocked = [False] * len(boxes)

    # Unlock boxes with available keys
    box, keys = 0, [0]
    while box < len(keys):
        # Unlock current box
        boxes_unlocked[keys[box]] = True

        # Check if all boxes already unlocked
        if False not in boxes_unlocked:
            break

        for key in boxes[keys[box]]:
            # Check key and unlock its box if key is valid
            key = int(key) if isinstance(key, (int, str, bytes)) else 0
            if key and key < len(boxes) and key not in keys:
                boxes_unlocked[key] = True
                keys.append(key)
        box += 1

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

    boxes = [[1, 4, None, [False]], [2], [{0: 9}, 4, 1], [3], [],
             [4, 1], [5, 6]]
    print(canUnlockAll(boxes))
