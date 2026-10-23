# Tutor LMS reference study

Studied: **Workademy**, **Pathwise** and **Wellthrive**, the three official Tutor LMS demo themes, on 23 October 2026. Captures (full-page screenshots, page text, headings, links) are in `workademy/`, `pathwise/` and `wellthrive/` next to this file; `index.tsv` in each lists what was captured. `plugin-templates.txt` lists the 281 template files in the Tutor LMS plugin itself (v4.1.1), which is what a theme overrides.

Lesson and quiz pages are behind a login on all three demos, so the learning screens below come from the plugin's own `learning-area/` templates.

---

## 1. What each demo is

| Demo | Model | Closest to Elena? | Notes |
|---|---|---|---|
| **Wellthrive** | One coach selling her own courses and services | **Yes.** Same "one person, own method" story | Short nav (Home, Courses, Services, Articles, About). Course page is the cleanest of the three. |
| **Pathwise** | Course marketplace, many mentors and categories | No, but has the fullest page set | Mega-menu of categories, cart, sign up, instructors archive, FAQ, careers. |
| **Workademy** | Corporate training (teams, B2B) | No | Pricing/membership page, blog, instructors, "Contact sales". |

---

## 2. Page inventory

✓ = the demo has it. **Elena** column = whether the Atelier needs it.

| Page | URL pattern | Workademy | Pathwise | Wellthrive | Tutor template | Elena |
|---|---|---|---|---|---|---|
| Home | `/` | ✓ | ✓ | ✓ | theme page | ✓ (v7 one-pager) |
| Course archive (all courses) | `/courses` | ✓ | ✓ | ✓ | `archive-course.php`, `course-filter/*`, `loop/*` | ✓ |
| Course category archive | `/course-category/{slug}/` | ✓ | ✓ | – | same as archive | Optional (by medium: Pencil, Ink, Watercolour, Oil, Acrylic) |
| **Single course** | `/courses/{slug}/` | ✓ | ✓ | ✓ | `single-course.php`, `single/course/*` | ✓ **design next** |
| **Lesson (learning area)** | `/courses/{slug}/lessons/{slug}/` | login | login | login | `single-lesson.php`, `learning-area/*` | ✓ **design next** |
| Quiz | `/courses/{slug}/quizzes/{slug}/` | login | login | login | `single-quiz.php`, `learning-area/quiz/*` | ✓ |
| Assignment | `/courses/{slug}/assignments/{slug}/` | – | – | – | `single-assignment.php` (Pro) | ✓ for the final critique piece |
| Lesson preview (free) | same as lesson | – | – | – | `single-preview-lesson.php` | ✓ the "free lesson" |
| Instructors archive | `/instructors/` | ✓ | ✓ | – | `instructor/*` | No (one teacher). Guest teachers could live on About. |
| Instructor profile | `/profile/{user}` | ✓ | ✓ | – | `public-profile.php` | No (About covers it) |
| Pricing / membership | `/membership` | ✓ | – | – | Tutor subscriptions (Pro) | Optional: "All-access" plan if Elena sells one |
| About | `/about/` | ✓ | ✓ | ✓ | theme page | ✓ (longer version of v7 section 02) |
| Contact | `/contact/` | ✓ | ✓ | ✓ | theme page | ✓ |
| FAQ | `/faq/` | ✓ | ✓ | – | theme page | ✓ (v7 has 4 questions; full page later) |
| Blog / articles | `/blogs/`, `/articles/` | ✓ | ✓ | ✓ | theme `index.php` / `single.php` | ✓ "Studio notes" (the newsletter already promises them) |
| Services | `/service/{slug}/` | – | – | ✓ | custom post type | ✓ Portfolio review, Live class (v7 CTA cards) |
| Login | `/login` | ✓ | ✓ | ✓ | `login.php`, `login-form.php` | ✓ |
| Registration | `/registration`, `/signup` | ✓ | ✓ | – | `dashboard/registration.php` | ✓ |
| Cart | `/cart` | – | ✓ | – | `ecommerce/cart.php` | ✓ |
| Checkout + success/failure | `/checkout` | – | – | – | `ecommerce/checkout.php`, `order-placement-*.php` | ✓ |
| Student dashboard | `/dashboard/` | – | – | – | `dashboard/*` (85 files) | ✓ restyle, don't redesign |
| Privacy, Terms | `/privacy-policy/`, `/terms-conditions/` | ✓ | – | ✓ | theme page | ✓ |
| Testimonials | `/testimonials/` | ✓ | – | – | theme page | Optional ("See the full wall") |

**Recommended page set for the Atelier (14 + dashboard):** Home · Courses · Single course · Lesson / learning area · Quiz · Assignment (final critique) · Free lesson preview · About · Studio notes (blog list + article) · Services (portfolio review, live class) · FAQ · Contact · Login / Register · Cart / Checkout · Dashboard (restyled plugin templates).

---

## 3. Course content structure (the Tutor LMS model)

```
Course
 ├─ meta: title, slug, category, tags, level, duration, price / sale price,
 │        featured image, intro video, certificate (yes/no), instructor(s)
 ├─ text: overview · what you'll learn · requirements · target audience ·
 │        material includes · (theme-specific) what's included
 └─ Topics (ordered)                      ← "Topic 1: …", "1 – The Journaling Mindset"
      └─ Items (ordered, mixed)
           ├─ Lesson       video / text / downloads; can be a free preview
           ├─ Quiz         true-false, single/multiple choice, matching,
           │                fill-in-the-blank, ordering, image answering, open-ended
           └─ Assignment   (Pro) upload + instructor grading
```

What each demo shows from this model on the course page:

| Field | Workademy | Pathwise | Wellthrive | Tutor template |
|---|---|---|---|---|
| Rating + review count | ✓ | ✓ | ✓ (above title) | `loop/rating.php`, `single/course/reviews.php` |
| Enrolled count | ✓ | ✓ | ✓ | `course-entry-box.php` |
| Level, duration, lesson count | ✓ | – | ✓ | `course-entry-box.php` |
| Certificate yes/no | ✓ | – | – | entry box |
| Price, sale price, Add to cart | ✓ | ✓ | ✓ ("Onetime payment") | `add-to-cart-tutor.php` |
| Overview | ✓ | – | ✓ | `course-content.php` |
| What you'll learn | ✓ | ✓ | ✓ | `course-benefits.php` |
| Requirements | ✓ | – | – | `course-requirements.php` |
| Material includes | ✓ | – | – | `material-includes.php` |
| What's included (custom list) | – | – | ✓ | theme field |
| Curriculum: topics as accordions | ✓ | ✓ | ✓ | `course-topics.php` |
| Per-topic totals (time · lessons · quizzes) | – | ✓ (lessons, quiz) | ✓ (time, lessons, quiz) | theme |
| Syllabus totals (lessons · quizzes · tasks · resources) | ✓ | – | – | theme |
| Instructor card(s) | ✓ | ✓ | – | `instructors.php` |
| Reviews: average, 5-bar histogram, cards | ✓ | ✓ | ✓ | `reviews.php`, `reviews-loop.php` |
| Related courses | ✓ | ✓ | ✓ | theme |
| Closing CTA | ✓ | – | ✓ ("free discovery call") | theme |

**Lesson naming (Wellthrive):** items are prefixed by type, so the curriculum reads like a programme: *Lesson:*, *Practice:*, *Reflection:*, *Bonus:*, *Audio:*. Topics carry a total time and counts (e.g. "1 hr 27 min · 4 Lessons · 0 Quiz"). This fits Elena's Look · Sketch · Paint method well.

**Single course page order, best of the three (Wellthrive order, Workademy fields):**
1. Breadcrumb · rating · title · enrolled count
2. Hero image or intro video beside an **entry box**: level, duration, lessons, certificate, price / sale, Add to cart (Continue learning when enrolled)
3. What's included (the downloads and extras)
4. Overview + What you'll learn (two columns)
5. Requirements / materials list (pencils, paper; links to the downloadable materials PDF)
6. **Curriculum**: topic accordions with per-topic time and counts; free-preview lessons marked
7. Instructor (Elena, one card)
8. Reviews: average + histogram + cards
9. More courses (3 cards)
10. Closing CTA (free lesson or portfolio review)

---

## 4. Learning area (lesson, quiz, assignment)

From `templates/learning-area/` in the plugin:

| Part | Template | Content |
|---|---|---|
| Header | `components/header.php` | Course title, progress, close / back to course |
| Sidebar | `components/sidebar.php`, `sidebar-nav-item.php` | Topics with their lessons, quizzes and assignments; done / current / locked states |
| Lesson body | `lesson/content.php` | Video (YouTube, Vimeo, self-hosted, Bunny) or text |
| Lesson tabs | `lesson/overview.php`, `exercise-files.php`, `comments.php` | Overview · Exercise files (reference sheets) · Comments |
| Lesson footer | `lesson/footer.php` | Previous / Mark as complete / Next |
| Subpages | `subpages/qna.php`, `announcements.php`, `reviews.php`, `course-info.php` | Q&A · Announcements · Reviews · Course info |
| Quiz | `quiz/content.php`, `attempt.php`, `progress-bar.php`, `question.php`, `questions/*`, `modals/result.php` | Start screen, timer/progress, one question at a time, result modal, attempt history |

For the Atelier the key screen is the lesson: a large video, Elena's reference sheet as an exercise file, and a "Submit your drawing" step that feeds the private critique.

---

## 5. Example: Elena's course in this structure

**Course 01 · Foundations of Drawing** (Pencil · Beginner · 6 topics · 24 items: 21 lessons, 2 quizzes, 1 assignment · 6h 10m · $79 · certificate)

In Tutor LMS, Practice, Reflection and Bonus items are all lessons with a prefixed title. The poster card on the site says "24 lessons"; it should read 21 (or count items) once the real curriculum is set.

| Topic | Items |
|---|---|
| 1 – Learning to look · 58 min | Lesson: How artists see (free preview) · Lesson: Shapes, values and edges · Practice: Blind contour, 10 minutes · Quiz: Spot the edges |
| 2 – Line and gesture · 1 hr 02 min | Lesson: Holding the pencil · Lesson: Gesture before detail · Practice: Thirty 30-second gestures · Reflection: What your lines say |
| 3 – Measuring and proportion · 1 hr 05 min | Lesson: Sight-size and the pencil ruler · Lesson: Negative space · Practice: Drawing a chair · Quiz: Proportion check |
| 4 – Light and value · 1 hr 10 min | Lesson: Three values, not seven · Lesson: Cast shadows · Practice: An egg on white paper · Bonus: Value scale sheet (PDF) |
| 5 – Texture and edges · 58 min | Lesson: Lost and found edges · Lesson: Paper, graphite and blending · Practice: A crumpled bag · Reflection: Your favourite edge |
| 6 – The final piece · 57 min | Lesson: Choosing your subject · Lesson: Building the drawing in layers · Practice: Your final drawing · **Assignment: Submit for Elena's critique** |

Course text fields: *What's included* (24 video lessons, 6 reference sheets, materials list, 1 private video critique, certificate) · *What you'll learn* (5 bullets) · *Requirements* (an HB and a 4B pencil, a kneaded eraser, A4 cartridge paper) · *Target audience* (complete beginners).

---

## 6. Next design steps

1. **Single course page** in the v7 system (white page, cream surfaces, flat cards, poster card language), using section 3's order.
2. **Learning area / lesson screen** (restyled plugin layout: sidebar curriculum, video, tabs, prev/next).
3. **Courses archive** (poster cards + medium filter + level filter).
4. Then About, Studio notes, Services, Contact, Login/Register, Cart/Checkout, and dashboard restyle.
