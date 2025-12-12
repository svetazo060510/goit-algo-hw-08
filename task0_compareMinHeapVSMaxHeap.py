import heapq
from typing import List, Tuple

def min_cost_to_connect_cables(cable_lengths: List[int]) -> Tuple[int, List[Tuple[int, int, int]]]:
    """
    Знаходить мінімальну загальну вартість об'єднання всіх кабелів.
    Використовує жадібний алгоритм з Min Heap: завжди об'єднує два найменші кабелі.
    
    :param cable_lengths: Список довжин кабелів.
    :return: Кортеж (мінімальна_загальна_вартість, історія_об'єднань).
    """
    
    # Створюємо копію, оскільки heapq.heapify працює
    heap = list(cable_lengths)
    heapq.heapify(heap)
    
    total_cost = 0
    history = [] 
    
    while len(heap) > 1:
        
        # 1. Витягуємо два найменші кабелі (Min Heap)
        cable1 = heapq.heappop(heap)
        cable2 = heapq.heappop(heap)
        
        # 2. Обчислюємо витрати об'єднання
        current_cost = cable1 + cable2
        total_cost += current_cost
        
        # 3. Зберігаємо історію об'єднання
        history.append((cable1, cable2, current_cost))
        
        # 4. Повертаємо новий об'єднаний кабель назад у купу
        heapq.heappush(heap, current_cost)
        
    return total_cost, history

def max_cost_to_connect_cables(cable_lengths: List[int]) -> Tuple[int, List[Tuple[int, int, int]]]:
    """
    Знаходить МАКСИМАЛЬНУ загальну вартість об'єднання всіх кабелів (Анти-Жадібний, Max Heap).
    
    Використовує Max Heap (імітуємо за допомогою від'ємних значень), 
    щоб завжди об'єднувати два найбільші кабелі.
    
    :param cable_lengths: Список довжин кабелів.
    :return: Кортеж (максимальна_загальна_вартість, історія_об'єднань).
    """
    # Імітуємо Max Heap, зберігаючи від'ємні значення: 
    # найменше від'ємне число в корені відповідає найбільшому додатному.
    max_heap = [-length for length in cable_lengths]
    heapq.heapify(max_heap)
    
    total_cost = 0
    history = []
    
    while len(max_heap) > 1:
        
        # 1. Витягуємо два найбільші кабелі (вилучаємо найменші від'ємні)
        cable1 = -heapq.heappop(max_heap)
        cable2 = -heapq.heappop(max_heap)
        
        # 2. Обчислюємо витрати об'єднання
        current_cost = cable1 + cable2
        total_cost += current_cost
        
        # 3. Зберігаємо історію об'єднання
        history.append((cable1, cable2, current_cost))
        
        # 4. Повертаємо новий об'єднаний кабель назад у купу, 
        # зберігаючи його як від'ємне число.
        heapq.heappush(max_heap, -current_cost)
        
    return total_cost, history

# --- Тестування та Порівняння ---
if __name__ == "__main__":
    
    # Тестові дані
    cables_1 = [4, 3, 2, 6]
    cables_2 = [1, 2, 3, 4, 5, 7, 8, 9]
    
    print("--- Порівняння Витрат: Min Heap (Оптимально) vs Max Heap (Найгірше) ---")
    print("-------------------------------------------------------------------")

    # --- ТЕСТ 1 ---
    print(f"\n[Тест 1] Кабелі: {cables_1}")
    
    # MIN HEAP (Оптимально)
    cost_min_1, history_min_1 = min_cost_to_connect_cables(cables_1)
    print(f"  Min Heap: Загальна вартість = {cost_min_1}")
    print("  Історія (Min Heap):")
    for c1, c2, new_length in history_min_1:
        print(f"    Об'єднання {c1} та {c2} -> {new_length}") 
        
    # MAX HEAP (Анти-Оптимально)
    cost_max_1, history_max_1 = max_cost_to_connect_cables(cables_1)
    print(f"  Max Heap: Загальна вартість = {cost_max_1}")
    print("  Історія (Max Heap):")
    for c1, c2, new_length in history_max_1:
        print(f"    Об'єднання {c1} та {c2} -> {new_length}")
    print(f"  Різниця у вартості: {cost_max_1 - cost_min_1}")
    

    # --- ТЕСТ 2 ---
    print(f"\n[Тест 2] Початкові кабелі: {cables_2}")

    # MIN HEAP (Оптимально)
    cost_min_2, history_min_2 = min_cost_to_connect_cables(cables_2)
    print(f"  Min Heap: Загальна вартість = {cost_min_2}")
    print("  Історія (Min Heap):")
    for c1, c2, new_length in history_min_2:
        print(f"    Об'єднання {c1} та {c2} -> {new_length}") 
        
    # MAX HEAP (Анти-Оптимально)
    cost_max_2, history_max_2 = max_cost_to_connect_cables(cables_2)
    print(f"  Max Heap: Загальна вартість = {cost_max_2}")
    print("  Історія (Max Heap):") 
    for c1, c2, new_length in history_max_2:
        print(f"    Об'єднання {c1} та {c2} -> {new_length}")
    print(f"  Різниця у вартості: {cost_max_2 - cost_min_2}")