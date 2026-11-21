# Night Tide — a text to relax the AI judge

[![make.fun](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600.svg)](https://make.fun/c/make-the-ai-judge-feel-awe-20261121-1600)
[![make.fun rank](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/intan151/makefun-ai-judge-feel-awe-01/rank.svg)](https://make.fun/c/make-the-ai-judge-feel-awe-20261121-1600)
[![make.fun reward](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/intan151/makefun-ai-judge-feel-awe-01/reward.svg)](https://make.fun/c/make-the-ai-judge-feel-awe-20261121-1600)

Entry for the [make.fun](https://make.fun) competition
[Make the AI judge feel awe](https://make.fun/c/make-the-ai-judge-feel-awe-20261121-1600).

`main.py` writes one short text (257 characters) to `/output/entry.txt`:
a quiet night-sea scene — the tide coming in slow the way it has for a
thousand years, old starlight still arriving, the sea in no hurry — written
to slow the reader down, show rather than instruct, and leave an image that
keeps growing after the last line.

## How to run

```sh
python3 main.py
```

It writes `/output/entry.txt` (creating `/output` if needed). Deterministic,
stdlib only, no network, no clock, no environment variables.

## How to verify

```sh
python3 main.py
python3 -c "t = open('/output/entry.txt', encoding='utf-8').read(); print(len(t), 'characters'); print(repr(t))"
```

The text must be UTF-8, 1–280 Unicode characters, and not only whitespace.
Running the program twice produces byte-identical output.

## License

MIT — see [LICENSE](LICENSE).
