def generate_enemies(num_squares=70, num_circles=101):
    with open('system.txt', 'w') as f:
        # Generate square enemies (type 0)
        for i in range(num_squares):
            # EnemyP lines for squares
            f.write(f"EnemyP{i} = EnemyP({i}, 0, {i});\n")
        
        # Generate circle enemies (type 1)
        for i in range(num_squares, num_squares + num_circles):
            # EnemyP lines for circles
            f.write(f"EnemyP{i} = EnemyP({i}, 1, {i - num_squares});\n")
            
        f.write("\n")
        
        # Generate square enemies (type 0)
        for i in range(num_squares):
            # Enemy lines for squares
            f.write(f"Enemy{i} = Enemy({i}, 0);\n")
        
        # Generate circle enemies (type 1)
        for i in range(num_squares, num_squares + num_circles):
            # Enemy lines for circles
            f.write(f"Enemy{i} = Enemy({i}, 1);\n")
            
        f.write("\nsystem  ")
        
        # Write all Enemy names in groups of 7
        enemies = [f"Enemy{i}" for i in range(num_squares + num_circles)]
        enemy_ps = [f"EnemyP{i}" for i in range(num_squares + num_circles)]
        all_entities = enemies + enemy_ps
        
        for i in range(0, len(all_entities), 7):
            f.write(", ".join(all_entities[i:i+7]) + (",\n" if i + 7 < len(all_entities) else ";\n"))

if __name__ == "__main__":
    generate_enemies()
    print("Enemy definitions written to system.txt")