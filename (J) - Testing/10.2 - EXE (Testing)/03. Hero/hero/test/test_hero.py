import unittest
from project.hero import Hero


class HeroTests(unittest.TestCase):
    def setUp(self) -> None:
        self.hero = Hero("Batman", 1, 100.00, 10.00)
        self.enemy_hero = Hero("Joker", 1, 100.00, 10.00)

    def test___init___successfully(self):
        hero_username = self.hero.username
        expected_hero_username = "Batman"
        self.assertEqual(hero_username, expected_hero_username)
        hero_level = self.hero.level
        expected_hero_level = 1
        self.assertEqual(hero_level, expected_hero_level)
        hero_health = self.hero.health
        expected_hero_health = 100.00
        self.assertEqual(hero_health, expected_hero_health)
        hero_damage = self.hero.damage
        expected_hero_damage = 10.00
        self.assertEqual(hero_damage, expected_hero_damage)

    def test_battle_and_raise_exception(self):
        with self.assertRaises(Exception) as content:
            self.hero.battle(self.hero)
        result = str(content.exception)
        expected_result = "You cannot fight yourself"
        self.assertEqual(result, expected_result)

    def test_battle_and_raise_value_error_because_of_hero_health(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as content:
            self.hero.battle(self.enemy_hero)
        result = str(content.exception)
        expected_result = "Your health is lower than or equal to 0. You need to rest"
        self.assertEqual(result, expected_result)

    def test_battle_and_raise_value_error_because_of_enemy_hero_health(self):
        self.enemy_hero.health = 0
        with self.assertRaises(ValueError) as content:
            self.hero.battle(self.enemy_hero)
        result = str(content.exception)
        expected_result = "You cannot fight Joker. He needs to rest"
        self.assertEqual(result, expected_result)

    def test_battle_and_return_draw_successfully(self):
        self.hero.level = 10
        self.enemy_hero.level = 10
        result = self.hero.battle(self.enemy_hero)
        expected_result = "Draw"
        self.assertEqual(result, expected_result)
        hero_health = self.hero.health
        expected_hero_health = 0
        self.assertEqual(hero_health, expected_hero_health)
        enemy_hero_health = self.enemy_hero.health
        expected_enemy_hero_health = 0
        self.assertEqual(enemy_hero_health, expected_enemy_hero_health)

    def test_battle_and_return_you_win_successfully(self):
        self.hero.level = 10
        result = self.hero.battle(self.enemy_hero)
        expected_result = "You win"
        self.assertEqual(result, expected_result)
        hero_level = self.hero.level
        expected_hero_level = 11
        self.assertEqual(hero_level, expected_hero_level)
        hero_health = self.hero.health
        expected_hero_health = 95.00
        self.assertEqual(hero_health, expected_hero_health)
        hero_damage = self.hero.damage
        expected_hero_damage = 15.00
        self.assertEqual(hero_damage, expected_hero_damage)
        enemy_hero_health = self.enemy_hero.health
        expected_enemy_hero_health = 0
        self.assertEqual(enemy_hero_health, expected_enemy_hero_health)

    def test_battle_and_return_you_lose_successfully(self):
        self.enemy_hero.level = 10
        result = self.hero.battle(self.enemy_hero)
        expected_result = "You lose"
        self.assertEqual(result, expected_result)
        enemy_hero_level = self.enemy_hero.level
        expected_enemy_hero_level = 11
        self.assertEqual(enemy_hero_level, expected_enemy_hero_level)
        enemy_hero_health = self.enemy_hero.health
        expected_enemy_hero_health = 95.00
        self.assertEqual(enemy_hero_health, expected_enemy_hero_health)
        enemy_hero_damage = self.enemy_hero.damage
        expected_enemy_hero_damage = 15.00
        self.assertEqual(enemy_hero_damage, expected_enemy_hero_damage)
        hero_health = self.hero.health
        expected_hero_health = 0
        self.assertEqual(hero_health, expected_hero_health)

    def test_battle_return_you_lose_but_still_alive_successfully(self):
        self.enemy_hero.level = 5
        result = self.hero.battle(self.enemy_hero)
        expected_result = "You lose"
        self.assertEqual(result, expected_result)
        enemy_hero_level = self.enemy_hero.level
        expected_enemy_hero_level = 6
        self.assertEqual(enemy_hero_level, expected_enemy_hero_level)
        enemy_hero_health = self.enemy_hero.health
        expected_enemy_hero_health = 95.00
        self.assertEqual(enemy_hero_health, expected_enemy_hero_health)
        enemy_hero_damage = self.enemy_hero.damage
        expected_enemy_hero_damage = 15.00
        self.assertEqual(enemy_hero_damage, expected_enemy_hero_damage)
        hero_health = self.hero.health
        expected_hero_health = 50
        self.assertEqual(hero_health, expected_hero_health)

    def test___str___successfully(self):
        hero_result = self.hero.__str__()
        expected_hero_result = "Hero Batman: 1 lvl\nHealth: 100.0\nDamage: 10.0\n"
        self.assertEqual(hero_result, expected_hero_result)


if __name__ == '__main__':
    unittest.main()
