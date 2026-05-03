import os

DEFAULT_GH_TOKEN = os.environ.get("GITHUB_TOKEN", None)
DEFAULT_DEVICES = "0"
DEFAULT_CLONE_DIR = "data/repos"
SEMANTIC_CODE_SEARCH_DB_PATH = "/tmp/semantic_code_search_hyperagent/"
ZOEKT_CODE_SEARCH_INDEX_PATH = "/tmp/zoekt_code_search_hyperagent/"
DEFAULT_PATCHES_DIR = "/tmp/hyperagent/patches"
DEFAULT_WORKDIR_CLI = "/tmp/hyperagent/"
DEFAULT_PLANNER_TYPE = "static"
DEFAULT_VLLM_PORT = 5200
DEFAULT_LANGUAGE = "python"
DEFAULT_VERBOSE_LEVEL = 1
DEFAULT_TRAJECTORIES_PATH = "data/agent_trajectories/nav"
DO_NOT_SUMMARIZED_KEYS = ["python", "code_snippet"]

DEFAULT_LLM_CONFIGS = {
    "name": "openai",
    "nav": [{
        "model": "gpt-4o-mini",
        "api_key": os.environ.get("OPENAI_API_KEY"),
        "stop": ["\nObservation:"],
        "api_type": "openai",
    }],
    "edit": [{
        "model": "gpt-4o-mini",
        "api_key": os.environ.get("OPENAI_API_KEY"),
        "stop": ["\nObservation:"],
        "api_type": "openai",
    }],
    "exec": [{
        "model": "gpt-4o-mini",
        "api_key": os.environ.get("OPENAI_API_KEY"),
        "stop": ["\nObservation:"],
        "api_type": "openai",
    }],
    "plan": [{
        "model": "gpt-4o-mini",
        "api_key": os.environ.get("OPENAI_API_KEY"),
        "api_type": "openai",
    }],
    "type": "patch"
}

DEFAULT_IMAGE_NAME = "python:3-slim"
D4J_FOLDER = "data/defects4j"