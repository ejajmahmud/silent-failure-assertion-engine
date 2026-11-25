"""Tests for Silent Failure Assertion Engine."""
import unittest
from silent_failure_assertion_engine.core import SilentFailureDetector


class TestSilentFailureDetector(unittest.TestCase):
    def setUp(self):
        self.det = SilentFailureDetector()

    def test_catches_test_weakening_and_noop(self):
        r1 = self.det.evaluate(["tests/test_a.py"], deleted_assertions=2, ran_tests=True, patch_lines=4)
        self.assertFalse(r1["passed"])
        self.assertIn("weakened_or_deleted_assertions", r1["silent_failures"])

        r2 = self.det.evaluate([], patch_lines=0)
        self.assertIn("noop_empty_patch", r2["silent_failures"])

    def test_valid_run_passes(self):
        r = self.det.evaluate(["src/a.py"], deleted_assertions=0, ran_tests=True, patch_lines=10, required_files=["src/a.py"])
        self.assertTrue(r["passed"])
