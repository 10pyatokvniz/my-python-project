from app import add

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    
    # Новый тест
    #assert add(-3, -5) == -8  # Новый тест для суммы отрицательных чисел
