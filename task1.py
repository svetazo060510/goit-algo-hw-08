import heapq
from typing import List, Tuple

def min_cost_to_connect_cables(cable_lengths: List[int]) -> Tuple[int, List[Tuple[int, int, int]]]:
    """
    Знаходить мінімальну загальну вартість об'єднання всіх кабелів.
    Використовує жадібний алгоритм з Min Heap: завжди об'єднує два найменші кабелі.
    
    :param cable_lengths: Список довжин кабелів.
    :return: Кортеж (мінімальна_загальна_вартість, історія_об'єднань).
    """
    
    # Використовуємо вбудований в Python модуль heapq, який реалізує Min Heap.
    # heapq.heapify перетворює список на Min Heap.
    heapq.heapify(cable_lengths)
    
    total_cost = 0
    # Зберігаємо історію операцій для пояснення
    history = [] 
    
    # Продовжуємо, доки в купі не залишиться лише один кабель (кінцевий результат)
    while len(cable_lengths) > 1:
        
        # 1. Витягуємо два найменші кабелі
        # heapq.heappop видаляє та повертає найменший елемент.
        cable1 = heapq.heappop(cable_lengths)
        cable2 = heapq.heappop(cable_lengths)
        
        # 2. Обчислюємо витрати об'єднання
        current_cost = cable1 + cable2
        
        # 3. Оновлюємо загальну вартість
        total_cost += current_cost
        
        # 4. Зберігаємо історію об'єднання: (кабель1, кабель2, нова_довжина)
        history.append((cable1, cable2, current_cost))
        
        # 5. Повертаємо новий об'єднаний кабель назад у купу
        heapq.heappush(cable_lengths, current_cost)
        
    return total_cost, history

# --- Тестування ---
if __name__ == "__main__":
    
    cables_1 = [4, 3, 2, 6]
    cost_1, history_1 = min_cost_to_connect_cables(cables_1)
    
    print(f"--- Тест 1: Кабелі {cables_1} ---")
    print(f"Мінімальна загальна вартість: {cost_1}")
    print("\nІсторія об'єднань (C1 + C2 = Новий Кабель):")
    for c1, c2, new_length in history_1:
        print(f"  Об'єднання {c1} та {c2}. Вартість: {new_length}. Нова купа: {new_length}")
    
    cables_2 = [1, 2, 3, 4, 5]
    cost_2, history_2 = min_cost_to_connect_cables(cables_2)
    
    print(f"\n--- Тест 2: Кабелі {cables_2} ---")
    print(f"Мінімальна загальна вартість: {cost_2}")
    print("\nІсторія об'єднань:")
    for c1, c2, new_length in history_2:
        print(f"  Об'єднання {c1} та {c2}. Вартість: {new_length}. Нова купа: {new_length}")
