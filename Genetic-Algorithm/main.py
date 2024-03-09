import random

# تعداد دروس در هر ترم
terms = {
    'term1': ['course1', 'course1', 'course1'],
    'term2': ['course2', 'course2', 'course2'],
    'term3': ['course3', 'course3', 'course3'],
    'term4': ['course4', 'course4', 'course4'],
    'term5': ['course5', 'course5', 'course5'],
    'term6': ['course6', 'course6', 'course6'],
    'term7': ['course7', 'course7', 'course7'],
    'term8': ['course8', 'course8', 'course8']
}

# تعداد روزها
total_days = 14

# تعداد حداکثر امتحانات در یک روز
max_exams_per_day = 3

# تابع تولید جمعیت اولیه
def initialize_population(population_size, terms):
    return [random.sample(terms.values(), len(terms)) for _ in range(population_size)]

# تابع ارزیابی انطباق (fitness)
def calculate_fitness(schedule):
    # ارزیابی بر اساس تعداد امتحانات تکراری در یک روز و تعداد امتحانات از یک ترم در یک روز
    duplicate_exams_penalty = sum(schedule.count(day) - len(set(day)) for day in schedule)
    same_term_penalty = sum(day.count(term) for day in schedule for term in day) - len(schedule)
    return -duplicate_exams_penalty - same_term_penalty

# تابع چندگانه‌سازی (crossover)
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# تابع جهش
def mutate(individual, mutation_rate):
    mutated_individual = individual.copy()
    for i in range(len(mutated_individual)):
        if random.random() < mutation_rate:
            # جابجایی دو درس در یک روز
            swap_index = random.randint(0, len(mutated_individual[i]) - 1)
            swap_index_2 = random.randint(0, len(mutated_individual[i]) - 1)
            mutated_individual[i][swap_index], mutated_individual[i][swap_index_2] = (
                mutated_individual[i][swap_index_2],
                mutated_individual[i][swap_index],
            )
    return mutated_individual

# تنظیمات الگوریتم ژنتیک
population_size = 50
mutation_rate = 0.1
generations = 100

# ایجاد جمعیت اولیه
population = initialize_population(population_size, terms)

# اجرای الگوریتم ژنتیک
for generation in range(generations):
    # محاسبه ارزش (fitness) هر فرد
    fitness_scores = [calculate_fitness(individual) for individual in population]

    # انتخاب والدین بر اساس ارزش (fitness)
    parents = random.choices(population, weights=fitness_scores, k=2)

    # تولید فرزندان با ترکیب والدین
    offspring1, offspring2 = crossover(parents[0], parents[1])

    # اعمال جهش به فرزندان
    offspring1 = mutate(offspring1, mutation_rate)
    offspring2 = mutate(offspring2, mutation_rate)

    # جایگزینی فرزندان با برخی افراد جمعیت
    population[random.randint(0, population_size - 1)] = offspring1
    population[random.randint(0, population_size - 1)] = offspring2

# یافتن بهترین برنامه‌ریزی در جمعیت
best_schedule = max(population, key=calculate_fitness)

print("بهترین برنامه‌ریزی:")
for i, day in enumerate(best_schedule):
    print(f"روز {i + 1}: {day}")
