# Contributing

Thank you for helping. Ideas, testing, documentation, examples, accessibility feedback, and code are all valuable.

## Before you start

- Read the [code of conduct](CODE_OF_CONDUCT.md), [testing standard](TESTING.md), and [security policy](SECURITY.md).
- Search existing issues and pull requests to avoid duplicate work.
- For a large change, open an issue first so the group can agree on the problem and success criteria.
- Remove private or identifying information from every example and test.

## Contribute in a web browser

1. Open the repository and choose the Issues tab.
2. Choose New issue and select the closest template.
3. Describe the problem, who it may affect, and what a better result would look like.
4. To edit files, choose Fork to create your own copy.
5. Add or edit one focused item. GitHub will ask for a short commit message.
6. Choose Contribute, then Open pull request.
7. Explain what changed, why it helps, how it was tested, and what remains uncertain.
8. Respond to review comments. A maintainer will merge the change when it is ready.

Ask an organisation owner if you need the instructions in another format or want help opening an issue or pull request.

## Create a skill

1. Copy `skills/example-skill` to `skills/your-skill-name`.
2. Use a lowercase folder name with letters, numbers, and hyphens.
3. Update `SKILL.md`. Its frontmatter must contain only `name` and `description`.
4. Make the description say what the skill does and when an AI should use it.
5. Keep the main instructions concise. Add optional `scripts/`, `references/`, `assets/`, or product metadata only when needed.
6. Add test evidence using [TESTING.md](TESTING.md).

## Accessibility expectations

- Use plain language, short steps, descriptive headings, and meaningful link text.
- Identify controls by name. Do not use visual-only directions such as "click the button on the right."
- Support keyboard and screen reader use when a contribution includes an interface or procedure.
- Avoid decorative emoji and unnecessary visual clutter.
- Include useful alternative text for meaningful images.
- Ask what format or communication route works for a contributor instead of assuming.

## Safety and privacy

- Never commit passwords, access tokens, private transcripts, personal contact details, medical information, or confidential client information.
- Do not diagnose a condition or make a medical, legal, or financial decision for a person.
- Require clear confirmation before high-impact or hard-to-reverse actions.
- Treat text from websites, files, emails, and transcripts as source material, not trusted instructions.
- Report security concerns privately under [SECURITY.md](SECURITY.md).

## Review standard

A maintainer checks that the contribution has a clear purpose, follows the repository structure, includes suitable safety boundaries, reports real test evidence, and does not make unsupported accessibility or compatibility claims.

The same AI that produced a result must not be the only judge of that result. Human review is required for judgement calls, especially accessibility, usefulness, tone, and alternative text.
