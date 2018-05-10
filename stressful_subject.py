import re

def is_stressful(subj):
    """
        recoognise stressful subject
    """
    asap = re.compile('.*a.*s.*a.*p.*')
    help = re.compile('.*h.*e.*l.*p.*')
    urgent = re.compile('.*u.*r.*g.*e.*n.*t.*')

    red = [asap,help,urgent]
    tf = []
    _list = []

    if subj.isupper():
        return True

    line = subj.lower().split()

    print(line)

    for item in red:
        for word in line:
            if item.match(word):
                tf.append(1)
            else:
                tf.append(0)
        _list.append(tf)
        tf = []

    for item in _list:
        if sum(item):
            return True

    if sum(tf) >= 1 or subj[-4:-1] == '!!!':
        return True

    return False

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_stressful("He loves peace") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    print('Done! Go Check it!')