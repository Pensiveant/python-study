'''
模块示例
'''
_author = 'pensiveant'
__all__ = ['x', 'y','z']

x = 0
y = 0
z = 0


def toJson(p):
    return {
        'x': p['x'],
        'y': p['y'],
        'z': p['z'],
    }
