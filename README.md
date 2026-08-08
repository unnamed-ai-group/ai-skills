# Unnamed AI Group skills

We are building reusable instructions that help AI work better with people with disabilities. We call each set of instructions a skill.

You can contribute ideas, lived experience, research, testing, examples, documentation, or code. You do not need to be a programmer.

## Working principles

- Keep people in control of what a skill does and what it can access.
- Build a useful shared base, then allow each person to adapt it.
- Use an open format and test every product or model named as supported.
- Treat lived experience as evidence. Do not assume everyone with the same disability has the same needs.
- Share what is known, what is untested, and what can go wrong.

This repository is experimental. A published skill is not automatically safe, accessible, or suitable for every person.

## Start contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md). The easiest route works entirely in a web browser:

1. Open an issue to describe an idea, problem, or test result.
2. Fork the repository if you want to edit files.
3. Make one focused change.
4. Open a pull request and explain how you tested it.

Regular contributors may ask an organisation owner for a membership invitation. Membership is not required for a one-time contribution.

## Skill structure

Each skill has its own folder under `skills/` and one required file:

```text
skills/
  skill-name/
    SKILL.md
    agents/       optional product metadata
    scripts/      optional automation
    references/   optional detailed guidance
    assets/       optional templates or resources
```

Start with [skills/example-skill](skills/example-skill). Keep the shared core portable. Put product-specific metadata in an appropriate optional folder and record exactly where the skill was tested.

## Project rules

- [Contribution guide](CONTRIBUTING.md)
- [Testing standard](TESTING.md)
- [Governance](GOVERNANCE.md)
- [Code of conduct](CODE_OF_CONDUCT.md)
- [Security reporting](SECURITY.md)

Project decisions belong in GitHub issues and pull requests. Email or chat may support discussion, but copy the final decision back to GitHub.

## Licence

Unless a file says otherwise, contributions are available under the repository's Apache License 2.0.
