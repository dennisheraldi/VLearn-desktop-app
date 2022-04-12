# Welcome to VLearn contributing guide!

Thank you for investing your time in contributing to our project! Any contribution you make will be reflected on this project :sparkles:. 

In this guide you will get an overview of the contribution workflow from opening an issue, creating a PR, reviewing, and merging the PR.

Use the table of contents icon on the top left corner of this document to get to a specific section of this guide quickly.

## New contributor guide

To get an overview of the project, read the [README](README.md). Here are some resources to help you get started with open source contributions:

- [Finding ways to contribute to open source on GitHub](https://docs.github.com/en/get-started/exploring-projects-on-github/finding-ways-to-contribute-to-open-source-on-github)
- [Set up Git](https://docs.github.com/en/get-started/quickstart/set-up-git)
- [GitHub flow](https://docs.github.com/en/get-started/quickstart/github-flow)
- [Collaborating with pull requests](https://docs.github.com/en/github/collaborating-with-pull-requests)


## Getting started

Make sure you created a good quality code with unit testing.

### Make Changes

#### Make changes locally

1. Fork the repository.
- Using GitHub Desktop:
  - [Getting started with GitHub Desktop](https://docs.github.com/en/desktop/installing-and-configuring-github-desktop/getting-started-with-github-desktop) will guide you through setting up Desktop.
  - Once Desktop is set up, you can use it to [fork the repo](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/cloning-and-forking-repositories-from-github-desktop)!

- Using the command line:
  - [Fork the repo](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo#fork-an-example-repository) so that you can make your changes without affecting the original project until you're ready to merge them.

3. Install or update to **python 3.7 or later**. You have to install the package and the appropriate requirement for the project by running:
    ```bash
    pip install -e .
    pip install -r requirements-dev.txt
    ```

4. Create a working branch and start with your changes!

### Commit your update

Commit the changes once you are happy with them.

Once your changes are ready, don't forget to self-review to speed up the review process :zap: .

### Pull Request

When you're finished with the changes, create a pull request, also known as a PR.
- Before requesting a pull request, make sure you **HAVE** passed the pylint, isort and coverage requirements:
    - Run pylint by following command:
        ```bash
        pylint vlearn
        ```
      Make sure it reports a minimum score of 0.9 (90%).
    - Run isort by following command:
        ```bash
        isort tests src
        ```
    - Run coverage by following command:
        ```bash
        coverage run -m unittest discover -s tests
        coverage report --fail-under=80
        ```
      Make sure it reports a minimum total score of 0.8 (80%). Always write a good unit test if you add new features.
- Don't forget to [link PR to issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue) if you are solving one.
- Enable the checkbox to [allow maintainer edits](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/allowing-changes-to-a-pull-request-branch-created-from-a-fork) so the branch can be updated for a merge.
Once you submit your PR, a team member will review your proposal. We may ask questions or request for additional information.
- We may ask for changes to be made before a PR can be merged, either using [suggested changes](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/incorporating-feedback-in-your-pull-request) or pull request comments. You can apply suggested changes directly through the UI. You can make any other changes in your fork, then commit them to your branch.
- As you update your PR and apply changes, mark each conversation as [resolved](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/commenting-on-a-pull-request#resolving-conversations).
- If you run into any merge issues, checkout this [git tutorial](https://lab.github.com/githubtraining/managing-merge-conflicts) to help you resolve merge conflicts and other issues.

### Your PR is merged!

Congratulations :tada::tada: The VLearn team thanks you :sparkles:. 

Once your PR is merged, your contributions will be visible on the repository.
