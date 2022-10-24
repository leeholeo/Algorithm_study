def kmp(source, target):
    def pi_array(string):
        _pis = [0] * len(string)
        _source_idx = 1
        _target_idx = 0
        while _source_idx < len(string):
            while string[_source_idx] != string[_target_idx] and _target_idx > 0:
                _target_idx = _pis[_target_idx-1]
            if string[_source_idx] == string[_target_idx]:
                _target_idx += 1
            _pis[_source_idx] = _target_idx
            _source_idx += 1
        return _pis

    pis = pi_array(target)
    source_idx = 0
    target_idx = 0
    while source_idx < len(source):
        while source[source_idx] != target[target_idx] and target_idx > 0:
            target_idx = pis[target_idx - 1]
        if source[source_idx] == target[target_idx]:
            target_idx += 1
            if target_idx == len(target):
                return 1
        source_idx += 1
    return 0


P = input()
S = input()
print(kmp(P, S))
