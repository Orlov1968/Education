import unittest
import runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        run_walk = runner.Runner("Slim")
        for i in range(1, 11):
            run_walk.walk()
        self.assertEqual(run_walk.distance, 50)

    def test_run(self):
        run_run = runner.Runner("Grig")
        for j in range(1, 11):
            run_run.run()
        self.assertEqual(run_run.distance, 100)

    def test_challenge(self):
        r_walk = runner.Runner("Slim")
        r_run = runner.Runner("Grig")
        for k in range(1, 11):
            r_walk.walk()
            r_run.run()
        self.assertNotEqual(r_walk.distance, r_run.distance)
