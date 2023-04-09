from project.tennis_player import TennisPlayer
import unittest


class TennisPlayerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tennis_player = TennisPlayer("Alex", 25, 10.0)
        self.tennis_player_2 = TennisPlayer("Bobby", 35, 50.0)

    def test___init___successfully(self):
        assert self.tennis_player.name == "Alex"
        assert isinstance(self.tennis_player.name, str)
        assert self.tennis_player.age == 25
        assert isinstance(self.tennis_player.age, int)
        assert self.tennis_player.points == 10.0
        assert isinstance(self.tennis_player.points, float)
        assert self.tennis_player.wins == []
        assert isinstance(self.tennis_player.wins, list)

    def test_name_successfully(self):
        assert self.tennis_player.name == "Alex"
        self.tennis_player.name = "Bobby"
        assert self.tennis_player.name == "Bobby"
        assert isinstance(self.tennis_player.name, str)

    def test_name_and_raise_value_error(self):
        assert self.tennis_player.name == "Alex"
        with self.assertRaises(ValueError) as content:
            self.tennis_player.name = "BB"
        assert str(content.exception) == "Name should be more than 2 symbols!"
        assert self.tennis_player.name == "Alex"
        assert isinstance(self.tennis_player.name, str)

    def test_age_successfully(self):
        assert self.tennis_player.age == 25
        self.tennis_player.age = 100
        assert self.tennis_player.age == 100
        assert isinstance(self.tennis_player.age, int)

    def test_age_and_raise_value_error(self):
        assert self.tennis_player.age == 25
        with self.assertRaises(ValueError) as content:
            self.tennis_player.age = 17
        assert str(content.exception) == "Players must be at least 18 years of age!"
        assert self.tennis_player.age == 25
        assert isinstance(self.tennis_player.age, int)

    def test_add_new_win_and_return_none_successfully(self):
        assert self.tennis_player.wins == []
        self.tennis_player.add_new_win("Tournament 1")
        assert self.tennis_player.wins == ["Tournament 1"]
        assert isinstance(self.tennis_player.wins, list)

    def test_add_new_win_and_tournament_name_has_been_already_added_to_the_list_of_wins_successfully(self):
        assert self.tennis_player.wins == []
        self.tennis_player.add_new_win("Tournament 1")
        assert self.tennis_player.wins == ["Tournament 1"]
        assert self.tennis_player.add_new_win("Tournament 1") == "Tournament 1 has been already added to the list of wins!"
        assert self.tennis_player.wins == ["Tournament 1"]
        assert isinstance(self.tennis_player.add_new_win("Tournament 1"), str)

    def test___lt___return_self_points___lt___other_points_successfully(self):
        assert self.tennis_player.points == 10.0
        assert self.tennis_player_2.points == 50.0
        self.assertEqual(self.tennis_player < self.tennis_player_2, "Bobby is a top seeded player and he/she is better than Alex")
        assert self.tennis_player < self.tennis_player_2

    def test___lt___return_self_points___ge___other_points_successfully(self):
        assert self.tennis_player.points == 10.0
        self.tennis_player.points = 50.0
        assert self.tennis_player.points == 50.0
        assert self.tennis_player_2.points == 50.0
        self.assertEqual(self.tennis_player < self.tennis_player_2, "Alex is a better player than Bobby")
        self.tennis_player.points = 100.0
        assert self.tennis_player.points == 100.0
        self.assertEqual(self.tennis_player < self.tennis_player_2, "Alex is a better player than Bobby")

    def test___str___successfully(self):
        assert self.tennis_player.wins == []
        assert self.tennis_player.__str__() == f"Tennis Player: Alex\n"\
                                               f"Age: 25\n" \
                                               f"Points: 10.0\n" \
                                               f"Tournaments won: "
        assert str(self.tennis_player) == f"Tennis Player: Alex\n"\
                                          f"Age: 25\n" \
                                          f"Points: 10.0\n" \
                                          f"Tournaments won: "
        self.tennis_player.add_new_win("Tournament 1")
        assert self.tennis_player.wins == ["Tournament 1"]
        assert self.tennis_player.__str__() == f"Tennis Player: Alex\n"\
                                               f"Age: 25\n" \
                                               f"Points: 10.0\n" \
                                               f"Tournaments won: Tournament 1"
        assert str(self.tennis_player) == f"Tennis Player: Alex\n" \
                                          f"Age: 25\n" \
                                          f"Points: 10.0\n" \
                                          f"Tournaments won: Tournament 1"
        self.tennis_player.add_new_win("Tournament 2")
        assert self.tennis_player.wins == ["Tournament 1", "Tournament 2"]
        assert self.tennis_player.__str__() == f"Tennis Player: Alex\n"\
                                               f"Age: 25\n" \
                                               f"Points: 10.0\n" \
                                               f"Tournaments won: Tournament 1, Tournament 2"
        assert str(self.tennis_player) == f"Tennis Player: Alex\n"\
                                          f"Age: 25\n" \
                                          f"Points: 10.0\n" \
                                          f"Tournaments won: Tournament 1, Tournament 2"
        assert isinstance(self.tennis_player.__str__(), str)
        assert isinstance(str(self.tennis_player), str)


if __name__ == '__main__':
    unittest.main()
