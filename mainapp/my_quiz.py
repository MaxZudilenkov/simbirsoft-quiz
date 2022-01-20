from quiz.dto import QuizDTO, QuestionDTO, ChoiceDTO

Myquiz = QuizDTO(
    "1",
    "Тест по программированию",
    [
        QuestionDTO(
            "1-1",
            "Какой из представленных типов данных является изменяемым ...?",

            [
                ChoiceDTO(
                    "1-1-1",
                    "Целые числа",
                    False
                ),
                ChoiceDTO(
                    "1-1-2",
                    "Множества",
                    True,
                ),

                ChoiceDTO(
                    "1-1-3",
                    "Строки",
                    False
                ),
                ChoiceDTO(
                    "1-1-4",
                    "Кортежи",
                    False,
                )
            ],
        ),

        QuestionDTO(
            "1-2",
            "Что может быть ключом в словаре?",
            [
                ChoiceDTO(
                    "1-2-1",
                    "Неизменяемые типы данных",
                    True
                ),
                ChoiceDTO(
                    "1-2-2",
                    "Только строки",
                    False
                ),

                ChoiceDTO(
                    "1-2-3",
                    "Только числа",
                    False
                ),
                ChoiceDTO(
                    "1-2-4",
                    "Изменяемые типы данных",
                    False
                )

            ]
        ),

        QuestionDTO(
            "1-3",
            "Как называется уникальное значение, "
            "используемые в веб-приложениях "
            "для предотвращения атак с подделкой межсайтовых запросов?",

            [
                ChoiceDTO(
                    "1-3-1",
                    "CSRF-token",
                    True
                ),
                ChoiceDTO(
                    "1-3-2",
                    "CMTP-token",
                    False,
                ),

                ChoiceDTO(
                    "1-3-3",
                    "HTTPS",
                    False
                ),
                ChoiceDTO(
                    "1-3-4",
                    "MVP",
                    False,
                )
            ],
        ),

        QuestionDTO(
            "1-4",
            "Какие из представленных методов HTTP существуют ?",

            [
                ChoiceDTO(
                    "1-4-1",
                    "GIVE",
                    False
                ),
                ChoiceDTO(
                    "1-4-2",
                    "SIT",
                    False,
                ),

                ChoiceDTO(
                    "1-4-3",
                    "PUT",
                    True
                ),
                ChoiceDTO(
                    "1-4-4",
                    "TRACE",
                    True,
                )
            ],
        ),
        QuestionDTO(
            "1-5",
            "Какие из представленных уровыней изоляции "
            "транзакций не существуют?",

            [
                ChoiceDTO(
                    "1-5-1",
                    "Read Completed",
                    True
                ),
                ChoiceDTO(
                    "1-5-2",
                    "Read Commited",
                    False,
                ),

                ChoiceDTO(
                    "1-5-3",
                    "Read Relative",
                    True
                ),
                ChoiceDTO(
                    "1-5-4",
                    "Repeatable Read",
                    False,
                )
            ],
        ),

    ],

)
