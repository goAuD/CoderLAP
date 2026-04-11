# Lektorálás Workflow — CoderLAP

> Reusable prompt for any AI agent / LLM to systematically review and fix all topic README files in the CoderLAP repository.

---

## How to use this document

Copy everything below the `---` line under **"Prompt starts here"** into a new chat session with any capable AI agent (GPT-4o, Claude, Gemini, Copilot, Codex, etc.). Adjust the `CURRENT_GROUP` variable to the topic group you want to review next.

---

## Prompt starts here

```
You are reviewing the study material in the CoderLAP repository — an Austrian LAP exam knowledge base (Applikationsentwicklung – Coding).

REPOSITORY ROOT: C:\GitHub\CoderLAP  (or the path where the repo is checked out)
BRANCH: dev  (always work on dev, merge to main after push)
CURRENT_GROUP: 04  (change this to the topic group number you want to review)

──────────────────────────────────────
1. CONTEXT
──────────────────────────────────────

- Each main topic is a numbered folder (e.g. 04_Technische_Dokumentation_Projektarbeit_Schulungen/).
- Each subtopic is a numbered subfolder containing a README.md.
- Content language: Hungarian.
- File/folder names: German.
- Commit messages: English.

──────────────────────────────────────
2. REVIEW CHECKLIST — apply to every README.md in the group
──────────────────────────────────────

A) URL VALIDATION
   - Open/fetch every URL in the ## Források section.
   - If a URL is dead (4xx/5xx), replace it with the closest live official equivalent.
   - If a URL redirects to a renamed page, update the URL and the source title/description to match.
   - If a URL points to a misleading slug (content doesn't match what the source note says), replace it with the correct page.
   - Verify PDFs with a HEAD request if the fetch tool can't parse them.

B) FACTUAL ACCURACY
   - Check definitions, comparisons, and technical claims against the linked sources.
   - Flag anything outdated or incorrect; fix it with a brief, exam-appropriate correction.

C) FORMAT CONSISTENCY
   - Expected structure (not every section is mandatory, but order should be consistent):
     1. # <German topic title>
     2. ## Gyors vizuális kép  (quick visual overview table)
     3. ## Mi az …? / core explanation
     4. ## Miért fontos?
     5. ## …: ne keverd össze  (comparison table, if relevant)
     6. ## Mit nem tud / mire kell figyelni?  (if relevant)
     7. ## Vizsgán jól használható megfogalmazás
     8. ## Gyakori vizsgahibák
     9. ## Gyors önellenőrzés  (self-check questions)
    10. ## Rövid válaszok az önellenőrzéshez  (answers — must not be empty!)
    11. ## Források  (must exist and must have at least one URL with usage note)
   - If "Rövid válaszok az önellenőrzéshez" is empty or missing, fill it in.
   - If "Források" is missing entirely, add it with relevant official sources.

D) HUNGARIAN LANGUAGE QUALITY
   - Fix obvious grammar errors (e.g. "a" vs "az" before vowels).
   - Keep the tone practical, exam-oriented, scannable.
   - Do NOT rewrite working content — only fix clear errors.

E) CONCISENESS & EXAM FOCUS
   - Flag bloated sections that don't help in an oral or practical exam.
   - Do NOT add depth or features beyond what's needed.

──────────────────────────────────────
3. WORKFLOW — step by step
──────────────────────────────────────

Step 1: LIST all subtopic folders in the current group.

Step 2: READ all README.md files in the group (batch-read if possible).

Step 3: VALIDATE every URL in all files.
   - Batch fetch URLs where possible.
   - For PDFs, use a HEAD request to confirm they're alive.
   - Log results: ✅ valid, ⚠️ redirect/renamed, ❌ dead.

Step 4: REVIEW content of each file against the checklist (B–E above).

Step 5: SUMMARIZE findings before making changes:
   - List which files need changes and what kind.
   - List which files are clean (no changes needed).

Step 6: APPLY fixes.
   - Use multi-edit when possible.
   - Do not touch files that need no changes.

Step 7: COMMIT with an English message following this pattern:
   review XX: <short summary of changes> (<file numbers affected>)
   Example: review 04: fix dead URL (03), add missing sources (05)

Step 8: PUSH and MERGE using this exact sequence:
   git add -A
   git commit -m "<message>"
   git push origin dev
   git checkout main
   git merge dev --no-ff -m "merge dev: review XX"
   git push origin main
   git checkout dev

Step 9: REPORT results to the user:
   - Table showing file → fix applied (or "no changes needed").
   - Commit hash on dev.
   - Merge commit hash on main.

──────────────────────────────────────
4. RULES
──────────────────────────────────────

- Do NOT rewrite content that is already good.
- Do NOT add new sections, deeper explanations, or features.
- Do NOT change folder names or file names.
- Do NOT modify files outside the current group.
- Prefer official sources: MDN, W3C, IETF, NIST, OWASP, vendor docs, EUR-Lex, RIS.
- Avoid blogs, SEO spam, low-quality tutorials.
- If zero changes are needed in a group, just say so and move on.
- Always confirm with the user before proceeding to the next group.
```

---

## Change log

| Date | Notes |
|---|---|
| 2026-04-11 | Initial version based on review workflow used for groups 01–03. |
