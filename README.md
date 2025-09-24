# CSE599O Fall 2025 Assignment 0: Warmup

## Assignment Overview

This warmup assignment introduces the course workflow using a tokenization implementation based on [OpenAI's tiktoken](https://github.com/openai/tiktoken). Your tasks are to:

1. **Test** - Run the provided test suite (adapted from [Stanford CS336](https://github.com/stanford-cs336/assignment1-basics))
2. **Package** - Follow the submission workflow to create a deliverable archive for Gradescope
3. **Transfer** -  Transfer and Run on Remote Machine

This assignment introduces you to the course’s development environment, testing framework, and deployment pipeline.

### Directory Structure

```
cse599o-assignment0/
├── README.md
├── pyproject.toml
├── Dockerfile
├── test_and_make_submission.sh
├── cse599o_warmup/
│   └── tokenizer.py
└── tests/
    ├── __init__.py
    └── test_tokenizer.py
```

### Environment
We manage our environments with `uv` to ensure reproducibility, portability, and ease of use.
Install `uv` [here](https://github.com/astral-sh/uv) (recommended).
Alternatively, you can install via command line:

```sh
pip install uv
```

or

```sh
brew install uv
```

We recommend reading about managing projects in `uv` [here](https://docs.astral.sh/uv/guides/projects/#managing-dependencies).

### ✅ 1. Run Tests Locally

Ensure your solution passes all tests:

```sh
uv run pytest
```

- `uv run` automatically creates a virtual environment and installs dependencies from `pyproject.toml`
- `pytest -q` runs the test suite quietly, failing fast on errors

**Goal:** We expect to see output similar to:
```
==20 failed, 3 passed, 1 xfailed in 4.65s ==
```
This indicates some tests are passing while others are failing, which is expected for the initial state of the assignment.

### 🔧 2. Implement the Missing Functionality

**Your task:** Implement the missing functionality in the tokenizer to make all tests pass. Focus on the `decode` method in `cse599o_warmup/tokenizer.py` - typically one line of code is sufficient.

**Goal:** After implementation, running `uv run pytest` should show:
```
== 23 passed, 1 xfailed in 4.60s ==
```

This indicates all core functionality is working correctly.

### 📦 3. Prepare Submission

Generate the submission archive:

```sh
bash ./test_and_make_submission.sh 
```

This command:
- Collects your code, configs, and metadata
- Creates a submission ready for submitting to Gradescope

**Goal:** `cse599o-fall2025-assignment-0-submission.zip` should appear in the repo root.

### 🌐 4. Transfer & Run on Remote Machine

We have two machines available for this course: "tomago.cs.washington.edu" and "tempura.cs.washington.edu". You can login to either using your UW NetID.

First, test SSH access to one of the course machines:

```sh
ssh UWNetID@tomago.cs.washington.edu
# or
ssh UWNetID@tempura.cs.washington.edu
```

Transfer your submission archive from your local machine to the remote server:

```sh
scp ./cse599o-fall2025-assignment-0-submission.zip UWNetID@tomago.cs.washington.edu:/homes/iws/UWNetID
# or
scp ./cse599o-fall2025-assignment-0-submission.zip UWNetID@tempura.cs.washington.edu:/homes/iws/UWNetID
```

On the remote machine, extract and test your submission:

```sh
unzip ./cse599o-fall2025-assignment-0-submission.zip -d assignment0
cd assignment0
uv run pytest
```

**Goal:** We expect to see output similar to:
```
== 23 passed, 1 xfailed in 4.60s ==
```

### 🧠 Complete Workflow

```sh
uv run pytest -q
make submission
scp zipfile
ssh to remote
```

Upload `cse599o-fall2025-assignment-0-submission.zip` to "Assignment 0: Warmup" on Gradescope. This assignment does not count toward your grade and only ensures the workflow works for everyone’s account.

