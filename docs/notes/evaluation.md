# Evaluation notes

Full worked examples: [Code-generation evaluation terms by example](https://claude.ai/artifact/NonKj3vpN6LBTiWAVXPbrV). ClassEval code vs paper: [ClassEval decoding settings: code vs. paper](https://claude.ai/artifact/6vcDCYRmzQPq8x1s95kzd6).

## Generation

- **Token:** a chunk of text; the model writes one at a time, scoring every possible next token and picking one.
- **Greedy:** always pick the top token. Same output every run (only approximately for API models).
- **Temperature:** reshapes the probabilities before a random pick. 0 = greedy; 0.2 (ClassEval) is nearly greedy; higher flattens.
- **Nucleus (top-p):** keep the most likely tokens whose probabilities sum to p, drop the rest. With top_p = 1.0 nothing is dropped, which is what ClassEval's code effectively does.

## Metrics

- **pass@k:** a task counts as solved if at least one of k attempts passes all tests.
- **n:** samples generated per task (5 in ClassEval). pass@k for k < n uses the unbiased estimator (Eq. 1), the average over every possible choice of k of the n; for pass@1 it reduces to c ÷ n. For k = n it is the plain "did any pass?" count.
- **Class-level vs method-level:** the whole class passes all tests vs each method passes its own tests.
- **DEP(F) / DEP(M):** share of the reference solution's field uses / method calls that the generated code also has.

## ClassEval generation strategies

- **Holistic:** whole class in one prompt.
- **Incremental:** one method per call; the prompt contains the bodies already generated (own code visible).
- **Compositional:** one method per call; the prompt contains only the other methods' signatures and docstrings (spec only).

## TGen (Mathews & Nagappan)

Reports "% solved" rather than pass@k: one deterministic run per problem (temperature 0, seed 1106), with up to 5 dependent remediation rounds. Dependent retries are part of the method, not independent samples.
