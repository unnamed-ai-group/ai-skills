# Testing skills

## Define success first

Before testing, write down:

- the task;
- the expected result;
- the important safety and accessibility boundaries;
- the AI product and model being tested;
- the evidence that will count as a pass.

## Use safe, realistic tests

Use realistic tasks, but remove names, private messages, medical information, passwords, client details, and other sensitive information.

Test more than one product or model when a skill claims broad support. Record differences. Do not promise identical results across products.

## Combine automated and human review

Automate checks with objective answers, such as required files, valid frontmatter, required warnings, or expected output fields.

Use human review for judgement calls. Accessibility review should include people with relevant lived experience whenever possible. One person's experience does not represent everyone with the same disability.

## Record evidence

Add this table to the pull request or a linked issue:

| Product and model | Task | Expected result | Actual result | Pass or fail | Reviewer | Notes and corrections |
|---|---|---|---|---|---|---|
| Example | Example task | Expected behaviour | Observed behaviour | Pass | Name or role | Limits or changes |

Keep a correction log for repeated testing. Record the failure, its effect, the change made, and the new result. Do not erase failed results just because a later test passed.
