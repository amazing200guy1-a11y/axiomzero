/**
 * AxiomZero: Deterministic Neuro-Symbolic Mathematical Proof Verifier
 * High-speed C99 formal verification core.
 * Copyright (c) 2026 Usman Bamidele. MIT License.
 */

#ifndef AXIOM_CORE_H
#define AXIOM_CORE_H

#include <stdint.h>
#include <stdbool.h>

#ifdef __cplusplus
extern "C" {
#endif

#define AXIOM_MAX_STEPS 64
#define AXIOM_MAX_EXPR_LEN 256
#define AXIOM_NUM_EVAL_POINTS 5

typedef enum {
    AXIOM_STATUS_VALID = 0,
    AXIOM_ERR_DIV_BY_ZERO = 1,
    AXIOM_ERR_DOMAIN_VIOLATION = 2,
    AXIOM_ERR_NON_EQUIVALENT_STEP = 3,
    AXIOM_ERR_INVALID_SYNTAX = 4,
    AXIOM_ERR_CIRCULAR_LOGIC = 5
} AxiomErrorCode;

typedef struct {
    char original_expr[AXIOM_MAX_EXPR_LEN];
    char transformed_expr[AXIOM_MAX_EXPR_LEN];
    char justification[128];
    bool is_verified;
    AxiomErrorCode error_code;
    double latency_microseconds;
} AxiomProofStep;

typedef struct {
    AxiomProofStep steps[AXIOM_MAX_STEPS];
    uint32_t step_count;
    uint32_t verified_count;
    uint32_t hallucination_count;
    double total_latency_us;
    bool is_proof_certified;
} AxiomProofSession;

/* Core Verification API */
void axiom_init_session(AxiomProofSession *session);
AxiomErrorCode axiom_verify_step(AxiomProofSession *session,
                                 const char *step_prev,
                                 const char *step_next,
                                 const char *justification);
bool axiom_check_algebraic_equivalence(const char *expr_a, const char *expr_b);
bool axiom_check_domain_safety(const char *expr, double test_val);

#ifdef __cplusplus
}
#endif

#endif /* AXIOM_CORE_H */
