# CoderLAP `v0.4.1-quiz-launch`

Release date: `2026-10-14`

The homepage CoderQuiz card and footer now open the protected
`https://quiz.coderlap.com/` catalogue directly. One central `quiz_url` setting
controls both destinations. The Quiz provides four reviewed DE/HU packages:
100 programming questions and the first 35 Informatik questions.

Since v0.4.0, the DE/HU/EN privacy and imprint pages also describe the Quiz
origin, temporary Basic Auth, and separate local language, topic and practice
storage. The release adds no application accounts or server-side result storage.

Validation covers the active and unpublished template paths, the bilingual
static build, and the authenticated production Quiz: all package paths, DE/HU,
answer explanations, source links and restoration after reload/package switching.
The 390 px browser viewport had no horizontal overflow; this does not replace
a physical iPhone check. The GitHub Release records the final CI/deploy run and
live LAP link verification after promotion to main.

CoderCoaster remains marked as in development. Shared invitation-based login
and further Informatik packages are separate follow-up tasks.
