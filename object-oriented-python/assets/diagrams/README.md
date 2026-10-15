# OOP Diagram Integration Notes

Eight original SVGs, with editable author source in `build_diagrams.py`.
All are conceptual models, **not UML relationship diagrams**. All have embedded
accessible `title` and `desc` elements. Render at about 500px wide, preserving aspect ratio.
The examples deliberately say “ILLUSTRATIVE EXAMPLE”: identifiers need not match
concurrently authored editor exercises.

## Recommended placements and alt text

Paths below use the frozen plan's module and lesson directories, relative to the
course root. These are integration recommendations, not claims about headings in
unwritten lessons. Insert after the specified explanation and before the coding task.
Copy each canonical SVG beside its target `lesson.md` and reference only its filename in Markdown. The platform image copier handles lesson-adjacent files, not shared files under `assets/`; a `../../assets/diagrams/` reference will not be published correctly. Keep the canonical originals here for regeneration and verify the local copies byte-for-byte.

| SVG | Planned lesson file | Exact conceptual insertion point | Suggested alt text |
| --- | --- | --- | --- |
| `class-and-instance-state.svg` | `01-classes-and-objects/11-independent-instance-lists/lesson.md` | Immediately after the explanation that `self.pages = []` in `__init__` creates a fresh list for each instance. | One Notebook class supplies shared behavior, while instances a and b own separate pages lists; changing a leaves b unchanged. |
| `bound-method-self.svg` | `02-object-interfaces/01-bound-methods/lesson.md` | Immediately after introducing `__self__` and `__func__`, before the exercise. | A bound method stores its receiving instance and original function: a.deposit(5) calls Account.deposit(a, 5). |
| `reflected-operator-dispatch.svg` | `03-python-protocols/06-reflected-multiplication/lesson.md` | Immediately after explaining `NotImplemented` and `__rmul__`. | For 3 times an unrelated Vector, int multiplication declines with NotImplemented; Python tries Vector.__rmul__, producing a new vector or TypeError if both decline. |
| `cooperative-mro-order.svg` | `04-inheritance/12-cooperative-diamond/lesson.md` | Immediately after the diamond's base declarations and before tracing cooperative `super()` calls. | With B and C inheriting A and D inheriting B then C, the MRO is D, B, C, A, object; super in B continues at C on a D instance. |
| `composed-service-delegation.svg` | `04-inheritance/07-compose-a-service/lesson.md` | Immediately after the explanation of storing an injected helper object, before the implementation task. | CheckoutService stores a gateway and delegates charge to it; real and fake gateways can be supplied without making the service a gateway subclass. |
| `enum-member-and-value.svg` | `07-enums-and-records/02-explicit-enum-values/lesson.md` | Immediately after contrasting the member, its name, and its explicit value. | Plain Enum member Status.PAID becomes the stored string paid through .value, and Status("paid") reconstructs the member; the member is not the string. |
| `descriptor-lookup-precedence.svg` | `08-descriptors/08-non-data-descriptor-priority/lesson.md` | Immediately after contrasting data and non-data descriptor priority, before the shadowing exercise. | Ordinary attribute lookup tries a readable data descriptor, instance dictionary, non-data descriptor, then ordinary class attribute; missing lookup may use __getattr__. |
| `cart-order-invoice-snapshot.svg` | `10-ecommerce-project/07-order-snapshot/lesson.md` | Immediately after explaining why checkout copies cart line values into independent order records; invoice is a preview of its later consumer. | Checkout copies cart line values into an independent order snapshot; invoices use captured order quantities and prices, so later cart or catalog edits do not change the invoice. |

## Verification

Evidence directory:
`/Users/piyush.patel/.hermes/profiles/curriculum-dev/cache/scratch/oop-diagram-review/`

- `contact-sheet.png`: all eight diagrams at 500px width.
- `contact-sheet-top.png`, `contact-sheet-bottom.png`: readable four-diagram sheets, both visually inspected with the vision tool.
- `<filename>.png`: all eight full-size renders; `<filename>.500.png`: all eight lesson-width renders.
- `geometry-report.json`: zero canvas, card, text-overlap, connector-alignment or crossing errors across all eight diagrams; negative fixtures detect invalid labels, misaligned arrows and arrows crossing cards.
- `artifact-manifest.json`: dimensions, nonempty file sizes, and final SVG/PNG SHA-256 hashes.
- `render.cjs`: repeatable Chrome/Playwright browser rendering and geometry checks.
- `verify_examples.py`: all eight conceptual examples pass executable Python assertions.

Full-size SVG width is 600px; heights range from 560px to 800px. All eight parse as XML and contain accessible titles and descriptions. Rendering used installed Chrome because the Playwright-managed headless-shell binary was absent. Initial generation defects were corrected and all evidence regenerated. Final visual inspection found readable labels, consistent styling, no clipping, and clear connectors.

No lesson files were read for alignment or modified: they were not yet present during this parallel task. Writers should preserve the illustrative-example distinction or adapt identifiers only if they regenerate and reverify the affected diagram. No commits were made.
