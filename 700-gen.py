def generate_enemies():
    with open('system.txt', 'w') as f:
        # Generate square enemies (type 0)
        for i in range(300):
            # EnemyP lines for squares
            f.write(f"EnemyP{i} = EnemyP({i}, 0, {i});\n")
        
        # Generate circle enemies (type 1)
        for i in range(300, 700):
            # EnemyP lines for circles
            f.write(f"EnemyP{i} = EnemyP({i}, 1, {i-300});\n")
            
        f.write("\n")
        
        # Generate square enemies (type 0)
        for i in range(300):
            # Enemy lines for squares
            f.write(f"Enemy{i} = Enemy({i}, 0);\n")
        
        # Generate circle enemies (type 1)
        for i in range(300, 700):
            # Enemy lines for circles
            f.write(f"Enemy{i} = Enemy({i}, 1);\n")
            
        f.write("\nsystem  ")
        
        # Write all Enemy names
        enemies = [f"Enemy{i}" for i in range(700)]
        enemy_ps = [f"EnemyP{i}" for i in range(700)]
        
        f.write(", ".join(enemies + enemy_ps) + ",\n")

if __name__ == "__main__":
    generate_enemies()
    print("Enemy definitions written to system.txt")