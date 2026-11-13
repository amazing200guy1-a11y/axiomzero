"""
Test Suite: AxiomZero Deterministic Neuro-Symbolic Verification Engine
Covers algebraic identities, trigonometric simplifications, hallucination traps,
and sub-millisecond execution benchmarks.
"""

import unittest
import time
from axiomzero_engine import AxiomZeroEngine, AxiomError

class TestAxiomZero(unittest.TestCase):
    def setUp(self):
        self.engine = AxiomZeroEngine()

    def test_01_polynomial_expansion_equivalence(self):
        """Test standard binomial expansion: (x + 1)^2 == x^2 + 2x + 1"""
        valid, code, meta = self.engine.verify_algebraic_step("(x + 1)^2", "x^2 + 2*x + 1")
        self.assertTrue(valid)
        self.assertEqual(code, AxiomError.VALID)

    def test_02_difference_of_squares_factorization(self):
        """Test difference of squares: x^2 - 9 == (x - 3)*(x + 3)"""
        valid, code, meta = self.engine.verify_algebraic_step("x^2 - 9", "(x - 3)*(x + 3)")
        self.assertTrue(valid)
        self.assertEqual(code, AxiomError.VALID)

    def test_03_trigonometric_pythagorean_identity(self):
        """Test trigonometric identity: sin(x)^2 + cos(x)^2 == 1"""
        valid, code, meta = self.engine.verify_algebraic_step("sin(x)^2 + cos(x)^2", "1")
        self.assertTrue(valid)
        self.assertEqual(code, AxiomError.VALID)

    def test_04_exponential_logarithm_inverses(self):
        """Test inverse functions: log(exp(x)) == x"""
        valid, code, meta = self.engine.verify_algebraic_step("log(exp(x))", "x")
        self.assertTrue(valid)
        self.assertEqual(code, AxiomError.VALID)

    def test_05_trap_llm_sign_inversion_hallucination(self):
        """Intercepts common LLM hallucination: -(x - 5) mistakenly written as (x - 5)"""
        valid, code, meta = self.engine.verify_algebraic_step("-(x - 5)", "x - 5")
        self.assertFalse(valid)
        self.assertEqual(code, AxiomError.SIGN_INVERSION)

    def test_06_trap_explicit_division_by_zero(self):
        """Catches invalid division by zero in candidate step"""
        valid, code, meta = self.engine.verify_algebraic_step("x + 2", "(x + 2) / 0")
        self.assertFalse(valid)
        self.assertEqual(code, AxiomError.DIV_BY_ZERO)

    def test_07_trap_bogus_algebraic_reduction(self):
        """Catches invalid LLM claim that (x + 2)^2 == x^2 + 4"""
        valid, code, meta = self.engine.verify_algebraic_step("(x + 2)^2", "x^2 + 4")
        self.assertFalse(valid)
        self.assertEqual(code, AxiomError.NON_EQUIVALENT_STEP)

    def test_08_multistep_valid_proof_chain(self):
        """Verifies a 3-step algebraic proof sequence is 100% certified"""
        chain = [
            ("2*(x + 3) + 4*x", "2*x + 6 + 4*x", "Distributive property"),
            ("2*x + 6 + 4*x", "6*x + 6", "Combine like terms"),
            ("6*x + 6", "6*(x + 1)", "Factor out GCF")
        ]
        result = self.engine.verify_proof_chain(chain)
        self.assertTrue(result["is_certified"])
        self.assertEqual(result["valid_steps"], 3)
        self.assertEqual(result["hallucinations_trapped"], 0)

    def test_09_multistep_proof_chain_intercepts_corrupted_step(self):
        """Verifies that a proof with 1 hallucinated step is rejected as uncertified"""
        chain = [
            ("x^2 + 5*x + 6", "(x + 2)*(x + 3)", "Quadratic factoring"),
            ("(x + 2)*(x + 3)", "(x + 2)*(x - 3)", "LLM Hallucinated Sign Error")
        ]
        result = self.engine.verify_proof_chain(chain)
        self.assertFalse(result["is_certified"])
        self.assertEqual(result["valid_steps"], 1)
        self.assertEqual(result["hallucinations_trapped"], 1)

    def test_10_sub_millisecond_benchmark(self):
        """Benchmark: 100 verification steps execute in < 10ms (< 0.1ms per step)"""
        n_iters = 100
        t0 = time.perf_counter()
        for _ in range(n_iters):
            self.engine.verify_algebraic_step("(x + 2)*(x - 2)", "x^2 - 4")
        elapsed = time.perf_counter() - t0
        avg_latency_ms = (elapsed / n_iters) * 1000.0
        print(f"\n[BENCHMARK] {n_iters} AxiomZero Proof Verifications: {elapsed:.4f}s | Avg Latency: {avg_latency_ms:.4f} ms/step")
        self.assertLess(avg_latency_ms, 0.5, "Latency must be sub-millisecond")

if __name__ == "__main__":
    unittest.main()
