# CS520: Prompt Design & Code Generation – Part 1 Results

This README summarizes pass@k across two model families and two prompting strategies (each run with 3 samples). Source: `results.txt`.

## Prompting Strategies Used

- Chain-of-Thought (CoT)
- Self-Planning

Each strategy generated 3 completions per problem and per model, for a total of 6 samples per model-problem pair.

## How pass@k is computed

For a problem with **n** code samples and **c** correct, pass@k is:


> pass@k = 1 - C(n - c, k) / C(n, k)  (when n - c ≥ k, otherwise 1.0)


We report pass@1..pass@3 where applicable.

## Per-problem Results

| ProblemID | claude_pass@1 | claude_pass@2 | claude_pass@3 | gpt_pass@1 | gpt_pass@2 | gpt_pass@3 | notes |
|---|---|---|---|---|---|---|---|
| 54 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | claude: c=6/n=6; gpt: c=6/n=6 |
| 151 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | claude: c=6/n=6; gpt: c=6/n=6 |
| 222 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | claude: c=6/n=6; gpt: c=6/n=6 |
| 290 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | claude: c=0/n=6; gpt: c=0/n=6 |
| 375 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | claude: c=0/n=6; gpt: c=0/n=6 |
| 410 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | claude: c=6/n=6; gpt: c=6/n=6 |
| 491 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | claude: c=6/n=6; gpt: c=6/n=6 |
| 596 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | claude: c=0/n=6; gpt: c=0/n=6 |
| 677 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | claude: c=0/n=6; gpt: c=0/n=6 |
| 944 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | claude: c=0/n=6; gpt: c=0/n=6 |

## Averages by Model

- **claude**: pass@1 = 0.500, pass@2 = 0.500, pass@3 = 0.500
- **gpt**: pass@1 = 0.500, pass@2 = 0.500, pass@3 = 0.500

## Discussion

- Some problems have zero solves across both strategies, yielding low pass@k.
- Where both strategies solved all attempts (c = 6), pass@k is 1.0 for k ∈ {1,2,3}.
- Differences across problems dominate the aggregate averages.
