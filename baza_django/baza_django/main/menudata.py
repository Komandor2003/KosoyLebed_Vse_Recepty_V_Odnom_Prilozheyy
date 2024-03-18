def massiv():
    menuData = [
        {
            "name": "Салат Цезарь",
            "image": "caesar.jpg",
            "description": "Свежий салат с куриным филе, листьями салата айсберг и хрустящими крутонами.",
            "ingredients": [
                ["Куриное филе", 200],
                ["Салат айсберг", 100],
                ["Крутоны", 50]
            ],
            "totalWeight": "350 г",
            "calories": "350 ккал",
            "mealTime": "День",
            "containsMeat": 1,
            "seafood": 0,
            "healthy": 0,
            "drink": 1,
            "difficulty": "Легкий"
        },
        {
            "name": "Паста Карбонара",
            "image": "carbonara.jpg",
            "description": "Итальянская паста с беконом, яйцами и сливками.",
            "ingredients": [
                ["Спагетти", 150],
                ["Бекон", 100],
                ["Яйца", 50],
                ["Сливки", 50]
            ],
            "totalWeight": "350 г",
            "calories": "500 ккал",
            "mealTime": "День",
            "containsMeat": 1,
            "seafood": 0,
            "healthy": 0,
            "drink": 0,
            "difficulty": "Средний"
        },
        {
            "name": "Суп-лапша",
            "image": "soup.jpg",
            "description": "Питательный суп с говядиной, лапшой и свежими овощами.",
            "ingredients": [
                ["Говядина", 200],
                ["Лапша", 150],
                ["Морковь", 50],
                ["Лук", 50]
            ],
            "totalWeight": "450 г",
            "calories": "300 ккал",
            "mealTime": "День",
            "containsMeat": 1,
            "seafood": 0,
            "healthy": 0,
            "drink": 0,
            "difficulty": "Средний"
        },
        {
            "name": "Омлет",
            "image": "omelette.jpg",
            "description": "Нежный омлет с помидорами и сыром.",
            "ingredients": [
                ["Яйца", 100],
                ["Молоко", 50],
                ["Помидоры", 50],
                ["Сыр", 50]
            ],
            "totalWeight": "250 г",
            "calories": "250 ккал",
            "mealTime": "Утро",
            "containsMeat": 0,
            "seafood": 0,
            "healthy": 0,
            "drink": 0,
            "difficulty": "Легкий"
        },
        {
            "name": "Рис с овощами",
            "image": "rice_vegetables.jpg",
            "description": "Паровой рис с морковью, горошком и луком.",
            "ingredients": [
                ["Рис", 200],
                ["Морковь", 100],
                ["Горошек", 50],
                ["Лук", 50]
            ],
            "totalWeight": "450 г",
            "calories": "400 ккал",
            "mealTime": "День",
            "containsMeat": 0,
            "seafood": 0,
            "healthy": 0,
            "drink": 0,
            "difficulty": "Легкий"
        },
        {
            "name": "Куриные крылышки",
            "image": "chicken_wings.jpg",
            "description": "Жареные куриные крылышки с соусом барбекю.",
            "ingredients": [
                ["Куриные крылья", 250],
                ["Соус барбекю", 50]
            ],
            "totalWeight": "300 г",
            "calories": "450 ккал",
            "mealTime": "Вечер",
            "containsMeat": 1,
            "seafood": 0,
            "healthy": 0,
            "drink": 0,
            "difficulty": "Средний"
        },
        {
            "name": "Гречневая каша",
            "image": "buckwheat_porridge.jpg",
            "description": "Ароматная гречневая каша с маслом.",
            "ingredients": [
                ["Гречка", 150],
                ["Вода", 300],
                ["Соль", 5],
                ["Масло", 10]
            ],
            "totalWeight": "465 г",
            "calories": "350 ккал",
            "mealTime": "Утро",
            "containsMeat": 1,
            "seafood": 1,
            "healthy": 1,
            "drink": 1,
            "difficulty": "Легкий"
        },
        {
            "name": "Суп-харчо",
            "image": "harchosoup.jpg",
            "description": "Пикантный суп с говядиной, рисом и специями.",
            "ingredients": [
                ["Говядина", 200],
                ["Рис", 150],
                ["Томатная паста", 50],
                ["Специи", 5]
            ],
            "totalWeight": "400 г",
            "calories": "280 ккал",
            "mealTime": "День",
            "containsMeat": 1,
            "seafood": 0,
            "healthy": 0,
            "drink": 0,
            "difficulty": "Средний"
        },
        {
            "name": "Пицца",
            "image": "pizza.jpg",
            "description": "Аппетитная пицца с ветчиной, сыром и соусом.",
            "ingredients": [
                ["Тесто", 300],
                ["Соус", 100],
                ["Сыр", 150],
                ["Ветчина", 50]
            ],
            "totalWeight": "600 г",
            "calories": "600 ккал",
            "mealTime": "Вечер",
            "containsMeat": 1,
            "seafood": 0,
            "healthy": 0,
            "drink": 1,
            "difficulty": "Сложный"
        },
        {
            "name": "Фруктовый салат",
            "image": "fruitsalad.jpg",
            "description": "Свежий салат с яблоками, бананами, апельсинами и грушами.",
            "ingredients": [
                ["Яблоки", 200],
                ["Бананы", 100],
                ["Апельсины", 100],
                ["Груши", 50]
            ],
            "totalWeight": "450 г",
            "calories": "200 ккал",
            "mealTime": ["Утро", "Вечер"],
            "containsMeat": 0,
            "seafood": 0,
            "healthy": 1,
            "drink": 0,
            "difficulty": "Легкий"
        }
    ]
    return menuData