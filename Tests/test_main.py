import pytest
from main import func_1_1, func_1_2, func_1_3
from yandex import folder_photos

class TestWithPytest:
    def test_1_1(self):
        expected = 'Адилет, Азамат, Александр, Алексей, Алена, Анатолий, Анна, Антон, Вадим, Валерий, Владимир, Денис, Дмитрий, Евгений, Елена, Иван, Илья, Кирилл, Константин, Максим, Михаил, Никита, Николай, Олег, Павел, Ринат, Роман, Сергей, Татьяна, Тимур, Филипп, Эдгар, Юрий'
        res = func_1_1()
        assert res == expected

    def test_1_2(self):
        expected = ["На курсах 'Python-разработчик с нуля' и 'Java-разработчик с нуля' преподают: Антон, Евгений, Максим", "На курсах 'Python-разработчик с нуля' и 'Fullstack-разработчик на Python' преподают: Александр, Евгений, Елена, Кирилл, Максим, Олег, Роман", "На курсах 'Python-разработчик с нуля' и 'Frontend-разработчик с нуля' преподают: Александр, Евгений", "На курсах 'Java-разработчик с нуля' и 'Fullstack-разработчик на Python' преподают: Денис, Евгений, Максим", "На курсах 'Java-разработчик с нуля' и 'Frontend-разработчик с нуля' преподают: Денис, Евгений", "На курсах 'Fullstack-разработчик на Python' и 'Frontend-разработчик с нуля' преподают: Александр, Алена, Владимир, Денис, Евгений, Эдгар"]
        res = func_1_2()
        assert res == expected

    def test_1_3(self):
        expected = ['Python-разработчик с нуля - 12', 'Java-разработчик с нуля - 14', 'Fullstack-разработчик на Python - 20', 'Frontend-разработчик с нуля - 20']
        res = func_1_3()
        assert res == expected

    def test_yandex(self):
        expected = 201
        res = folder_photos()
        assert res == expected
