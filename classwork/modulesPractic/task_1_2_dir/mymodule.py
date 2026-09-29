PI = 3.141592
VERSION = "1.0.0"
_secret = "secret"

def circle_area(r): return PI * r**2
def circle_len(r): return 2 * PI * r
def sphere_volume(r):
    """Возвращает объем сферы радиуса r."""
    return (4/3) * PI * r**3
def _helper(): return PI/2

if __name__ == '__main__':
    print(f"[{VERSION}] Самопроверка mymodule:")
    print(f"    L(r=5) = {circle_len(5)}")
    print(f"    S(r=5) = {circle_area(5)}")
