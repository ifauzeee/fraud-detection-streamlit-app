import os
from datetime import datetime

# --- CONFIGURATION ---
# Generate output file name with timestamp to avoid overwriting
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
OUTPUT_FILE = f"all_project_code_{timestamp}.txt"

# Super complete list of code file extensions
CODE_EXTENSIONS = {
    # Web Frontend
    ".js", ".mjs", ".cjs", ".jsx", ".ts", ".tsx", ".html", ".htm",
    ".css", ".scss", ".sass", ".less", ".vue", ".svelte", ".svg",
    ".coffee", ".lit", ".elm",

    # Backend / Server
    ".py", ".rb", ".php", ".java", ".go", ".rs", ".c", ".cpp",
    ".cs", ".h", ".hpp", ".pl", ".ex", ".exs", ".kt", ".kts", ".scala",
    ".r", ".jl", ".dart", ".swift",

    # Scripting & Shell
    ".sh", ".bash", ".zsh", ".ps1", ".psm1", ".bat", ".cmd", ".lua",
    ".vbs", ".fish",

    # Database / Query
    ".sql", ".graphql", ".gql", ".cypher", ".prisma",

    # Data Science / Notebook
    ".ipynb", ".rmd", ".sas", ".jl", ".mat", ".pickle", ".pkl", ".ndjson",

    # Configuration / Serialization
    ".json", ".xml", ".yml", ".yaml", ".toml", ".ini", ".env",
    ".cfg", ".properties", ".conf", ".ini.sample",

    # Templating
    ".erb", ".ejs", ".hbs", ".pug", ".j2", ".jinja2", ".twig", ".mustache",

    # Documentation / Markup
    ".md", ".rst", ".adoc", ".tex", ".txt", ".org", ".asciidoc",

    # Docker / DevOps / CI
    "Dockerfile", ".dockerfile", ".gitignore", ".gitattributes", ".editorconfig",
    ".travis.yml", ".circleci", ".github/workflows", ".gitlab-ci.yml", ".k8s.yaml",

    # Others
    ".makefile", ".mk", ".gradle", ".pom", ".psd1"
}

# Directories to exclude (important for performance)
EXCLUDE_DIRS = {
    "node_modules", ".git", "dist", "build", "vendor",
    "__pycache__", ".vscode", ".idea", "venv"
}
# --- END CONFIGURATION ---

def main():
    """Main function to search and combine code files with numbering and relative paths."""
    
    root_dir = os.getcwd()  # Root folder
    file_count = 0          # Counter for file numbering

    with open(OUTPUT_FILE, "w", encoding="utf-8", errors="ignore") as outfile:
        print(f"Starting process, output will be saved as: {OUTPUT_FILE}\n")
        
        for dirpath, dirnames, filenames in os.walk(root_dir):
            dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
            
            for filename in filenames:
                if any(filename.endswith(ext) for ext in CODE_EXTENSIONS):
                    file_path = os.path.join(dirpath, filename)
                    # Compute relative path from root
                    relative_path = os.path.relpath(file_path, root_dir)
                    file_count += 1
                    
                    try:
                        # Write header with file number and relative path
                        outfile.write("=" * 80 + "\n")
                        outfile.write(f"FILE {file_count}: {relative_path}\n")
                        outfile.write("=" * 80 + "\n\n")
                        
                        with open(file_path, "r", encoding="utf-8", errors="ignore") as infile:
                            outfile.write(infile.read())
                            outfile.write("\n\n")
                            
                        print(f"[{file_count}] Added: {relative_path}")
                        
                    except Exception as e:
                        print(f"Failed to read file {relative_path}: {e}")

    print(f"\nProcess completed! {file_count} files were combined into {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
