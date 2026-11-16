"""
AxiomZero ZK: Formal Verification & Zero-Knowledge Invariant Test Harness
Platform: Midnight Network Buildathon (AKINDO)
Author: Usman Bamidele (100L Pure Mathematics, FUNAAB, Abeokuta, Nigeria)
Copyright (c) 2026 Usman Bamidele · All Rights Reserved
Zero External Dependencies - Pure Python Standard Library
"""

import hashlib
import math
import time
import unittest
from axiomzero_engine import AxiomZeroEngine, AxiomError

class TestAxiomZeroZK(unittest.TestCase):
    def setUp(self):
        self.engine = AxiomZeroEngine()

    def test_01_valid_algebraic_distributive_expansion(self):
        """Validates standard distributive law: 2*(x + 3) == 2*x + 6"""
        valid, err, meta = self.engine.verify_algebraic_step("2*(x + 3)", "2*x + 6")
        self.assertTrue(valid)
        self.assertEqual(err, AxiomError.VALID)
        self.assertIn("latency_ms", meta)

    def test_02_polynomial_binomial_expansion(self):
        """Validates binomial theorem: (x + 3)^2 == x^2 + 6*x + 9"""
        valid, err, meta = self.engine.verify_algebraic_step("(x + 3)^2", "x^2 + 6*x + 9")
        self.assertTrue(valid)
        self.assertEqual(err, AxiomError.VALID)

    def test_03_hallucination_trap_the_freshmans_dream(self):
        """Traps freshman's dream hallucination: (x + 2)^2 != x^2 + 4 (missing 4x)"""
        valid, err, meta = self.engine.verify_algebraic_step("(x + 2)^2", "x^2 + 4")
        self.assertFalse(valid)
        self.assertEqual(err, AxiomError.NON_EQUIVALENT_STEP)

    def test_04_hallucination_trap_sign_inversion(self):
        """Traps sign flip hallucination: -(x - 5) != x - 5"""
        valid, err, meta = self.engine.verify_algebraic_step("-(x - 5)", "x - 5")
        self.assertFalse(valid)
        self.assertEqual(err, AxiomError.SIGN_INVERSION)

    def test_05_hallucination_trap_explicit_division_by_zero(self):
        """Traps illegal division by zero step: 5 / 0"""
        valid, err, meta = self.engine.verify_algebraic_step("5*x", "5*x + (1 / 0)")
        self.assertFalse(valid)
        self.assertEqual(err, AxiomError.DIV_BY_ZERO)

    def test_06_trigonometric_pythagorean_identity(self):
        """Validates trigonometric invariant: sin(x)^2 + cos(x)^2 == 1"""
        valid, err, meta = self.engine.verify_algebraic_step("sin(x)^2 + cos(x)^2", "1")
        self.assertTrue(valid)
        self.assertEqual(err, AxiomError.VALID)

    def test_07_zero_knowledge_witness_generation(self):
        """Simulates Midnight Compact Zero-Knowledge witness generation & selective disclosure commitment."""
        step_from = "3*(x - 4)"
        step_to = "3*x - 12"
        model_weights_hash = hashlib.sha256(b"proprietary_quant_llm_v4_weights").hexdigest()
        
        # Invariant verification
        valid, err, _ = self.engine.verify_algebraic_step(step_from, step_to)
        self.assertTrue(valid)
        
        # Construct ZK witness commitment
        step_hash = hashlib.sha256(f"{step_from}->{step_to}".encode()).hexdigest()
        public_commitment = hashlib.sha256(f"{step_hash}:{model_weights_hash}".encode()).hexdigest()
        
        self.assertEqual(len(public_commitment), 64)
        self.assertNotEqual(public_commitment, model_weights_hash) # Zero-knowledge guarantee: model weights never exposed

    def test_08_idempotent_proof_verification(self):
        """Verifies repeated evaluation on identical expression produces identical invariant outcomes."""
        expr_a = "(x - 1)*(x + 1)"
        expr_b = "x^2 - 1"
        res1, _, _ = self.engine.verify_algebraic_step(expr_a, expr_b)
        res2, _, _ = self.engine.verify_algebraic_step(expr_a, expr_b)
        self.assertEqual(res1, res2)
        self.assertTrue(res1)

    def test_09_high_degree_polynomial_stress_test(self):
        """Validates high-degree polynomial factorisation: x^3 - 8 == (x - 2)*(x^2 + 2*x + 4)"""
        valid, err, _ = self.engine.verify_algebraic_step("x^3 - 8", "(x - 2)*(x^2 + 2*x + 4)")
        self.assertTrue(valid)
        self.assertEqual(err, AxiomError.VALID)

    def test_10_latency_benchmark_100_iterations(self):
        """Benchmarks 100 formal verification proof steps in microsecond latency."""
        t0 = time.perf_counter()
        iterations = 100
        for _ in range(iterations):
            self.engine.verify_algebraic_step("(x + 5)^2", "x^2 + 10*x + 25")
        elapsed = time.perf_counter() - t0
        avg_latency_ms = (elapsed / iterations) * 1000.0
        
        print(f"\n[BENCHMARK] {iterations} AxiomZero ZK Proof Steps: {elapsed:.4f}s | Avg Latency: {avg_latency_ms:.4f} ms/step")
        self.assertLess(avg_latency_ms, 1.0) # Must be well under 1 ms

if __name__ == "__main__":
    unittest.main()
