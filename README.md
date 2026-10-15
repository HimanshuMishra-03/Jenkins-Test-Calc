# Jenkins Calculator CI Practical

This project contains a small calculator module and pytest tests. Jenkins installs
the test dependency and runs the tests whenever it detects a change in the
configured source-control repository.

## Run tests locally

From this folder, install the dependency and run the test suite:

```text
python -m pip install -r requirements.txt
python -m pytest -v
```

## Configure Jenkins

1. Put this folder in a Git repository and push it to your source-control server.
2. In Jenkins, create a **Pipeline** job and select **Pipeline script from SCM**.
3. Select Git, enter the repository URL and credentials if needed, and set the
   script path to `JenkinsPractical-9/Jenkinsfile` if this folder is inside a
   larger repository. Use `Jenkinsfile` if this folder is the repository root.
4. Save the job and select **Build Now** for the first run.

The Jenkinsfile polls the repository every two minutes. Push your code changes
to the configured repository; Jenkins will detect them, run the tests, and
display the JUnit test report in the build. The pipeline runs only
`test_calculator.py`, so unrelated tests in a larger repository are not
collected. The Jenkins agent must have Python and pip installed.
