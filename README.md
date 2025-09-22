# CSE599O Fall 2025 Assignment 0: Warmup

## Assignment Overview

This warmup assignment introduces the course workflow using a tokenization implementation based on [OpenAI's tiktoken](https://github.com/openai/tiktoken). Your tasks are to:

1. **Test** - Run the provided test suite (adapted from [Stanford CS336](https://github.com/stanford-cs336/assignment1-basics))
2. **Package** - Follow the submission workflow to create a deliverable archive for Gradescope
3. **Containerize** - Build a Docker image that can execute on remote machines

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

### 🐳 4. Build Docker Image

Build a container image containing your solution:

This typically runs:
```sh
docker build -t hw0-image .
```

- `-t hw0-image` tags the image for easy reference
- The Dockerfile installs dependencies and copies your code

**Goal:** A Docker image named `hw0-image` should appear in `docker images`.

### 🗜 5. Export Image

Export the image as a portable tarball:

This usually runs:
```sh
docker save hw0-image -o hw0-image.tar
```

**Goal:** You now have a portable `hw0-image.tar` file.

### 🌐 6. Transfer & Run on Remote Machine

Copy the tarball to a remote machine:

```sh
scp hw0-image.tar user@remote:/tmp/
```

Then on the remote machine:

```sh
docker load -i /tmp/hw0-image.tar
docker run --rm hw0-image
```

- `docker load` imports the image into the remote Docker store
- `docker run` starts a container and executes your program/tests

**Goal:** We expect to see output similar to:
```
== 23 passed, 1 xfailed in 4.60s ==
```

### 🧠 Complete Workflow

```sh
uv run pytest -q
make submission
make docker-image
make zip-image
scp hw0-image.tar user@remote:/tmp/
ssh user@remote "docker load -i /tmp/hw0-image.tar && docker run --rm hw0-image"
```

Upload `cse599o-fall2025-assignment-0-submission.zip` to "Assignment 0: Warmup" on Gradescope. This assignment does not count toward your grade and only ensures the workflow works for everyone’s account.

