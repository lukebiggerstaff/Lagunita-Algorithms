import sys

keys = [
    [ 1,.05 ],
    [ 2, .4 ],
    [ 3, .08 ],
    [ 4, .04 ],
    [ 5, .1 ],
    [ 6, .1 ],
    [ 7, .23 ]
]
keys.sort(key=lambda x: x[1],reverse=True)
print(keys)

