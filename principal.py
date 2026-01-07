import math

def calculate_panels(a, b, x, y):
    """
    Calcula el número máximo de paneles a x b en un techo x x y.
    Considera rotaciones (ambas orientaciones) y usa área total para maximizar.
    """
    # Verificación básica: si no caben en ninguna orientación, retorna 0
    if (a > x and b > x) or (a > y and b > y) or (min(a, b) > min(x, y)) or (max(a, b) > max(x, y)):
        return 0
    
    # Área del techo
    area_techo = x * y
    
    # Área de paneles en ambas orientaciones
    area_panel_1 = a * b
    area_panel_2 = b * a  # Rotación
    
    # Máximo entre las dos orientaciones
    max_1 = math.floor(area_techo / area_panel_1)
    max_2 = math.floor(area_techo / area_panel_2)
    
    return max(max_1, max_2)

if __name__ == "__main__":
    # Ejemplos
    print("Paneles 1x2 en techo 2x4:", calculate_panels(1, 2, 2, 4))  # 4
    print("Paneles 1x2 en techo 3x5:", calculate_panels(1, 2, 3, 5))  # 7
    print("Paneles 2x2 en techo 1x10:", calculate_panels(2, 2, 1, 10))  # 0