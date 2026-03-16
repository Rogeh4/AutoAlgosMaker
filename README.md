# AutoAlgosMaker

An automated pipeline designed to solve BSU (Computer Mathematics) algorithm labs using Large Language Models. It parses university lab requirements, generates high-quality Python code, and organizes solutions into a clean directory structure.

## Getting Started

### Installation

Clone the repository and install the required dependencies:

`pip install -r requirements.txt`


#### Configuration

Create a .env file in the root directory and add your credentials:

`OPENAI_API_KEY=your_openrouter_api_key
MODEL_NAME=allenai/molmo-2-8b:free`


#### Usage

Launch the main script and follow the prompts:

`python main.py`


Surname: Used for directory naming (All_Labs_Surname).
Year: Defines the course source (e.g., 2025).
Modes: Enter 'all' to sync everything or specific numbers (e.g., 1 2 5) to target labs.


## Project Structure

`main.py: The entry point and user interface.

src/core.py: Orchestrates the parsing, solving, and saving workflow.

src/parser.py: Scrapes lab data from the university website.

src/llm_client.py: Handles communication with the AI and code extraction.

src/file_manager.py: Manages the local file system and skipping logic.

data/: Your local repository of solved assignments.`
