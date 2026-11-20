# Open Loadout: library map

Status: DRAFT for Anthony to review. Nothing here is built yet. Every name, section, and count can still change.

This is the full list of what the kit will contain: every section, every skill, every agent, and every team, by name with a one-line note. It exists so we can agree on the whole shape before writing hundreds of files.

## How to read this map

- **Section:** one area of work or life, such as Writing or Money. One section equals one loadout, and lives in one folder under `loadouts/`.
- **Skill:** a how-to guide the AI reads when it does one type of task. Shown as `skill-name`: what it handles.
- **Agent:** a specialist worker that does one step of the work, using the skills. Each agent lists what it handles and what it does not handle, so two agents never do the same job.
- **Team:** a set of agents in a fixed order for a bigger job. Shown as Agent > Agent > Agent.

## Rules that apply to everything

1. **A skill must earn its place.** It only stays if it changes the result in a before-and-after test. A skill covers what the AI gets wrong by default: the steps, the questions to ask, the format, and the common mistakes.
2. **Core sections hold the craft. Other sections hold the situations.** Sections 1 to 5 teach how to write, research, read, think, and plan. Sections 6 to 21 cover real-life situations and point back to the core skills instead of repeating them.
3. **Simple tasks never trigger a team.** A short email needs one skill, not five agents. Teams are for work with distinct steps.
4. **Every team ends the same way.** After the agents listed, the shared Reviewer checks the work and the shared Explainer puts the result in plain words. These two are not repeated in each team line below.
5. **No section has more than 10 agents.**
6. **The AI sees only the section list up front.** Skills are opened one at a time when needed, so a big library does not slow anything down.

## Shared agents (used by every section)

| Agent | Handles | Does not handle |
|---|---|---|
| Reviewer | Checks finished work with fresh eyes against what was asked | Doing the work or rewriting it |
| Explainer | Turns the result into plain words: what happened, what it means, what to do next | Changing the work itself |

## Totals

| Thing | Count |
|---|---|
| Sections | 21 |
| Subsections | 106 |
| Skills | 326 |
| Agents | 98, plus the 2 shared agents |
| Teams | 49 |

## Section list

| # | Area | Section | Folder |
|---|---|---|---|
| 1 | Core | Writing and editing | `loadouts/writing/` |
| 2 | Core | Research and fact checking | `loadouts/research/` |
| 3 | Core | Reading and summarizing | `loadouts/reading/` |
| 4 | Core | Thinking and decisions | `loadouts/thinking/` |
| 5 | Core | Planning and projects | `loadouts/planning/` |
| 6 | Work | Email and work communication | `loadouts/work-communication/` |
| 7 | Work | Presentations and reports | `loadouts/presentations-reports/` |
| 8 | Work | Data and spreadsheets | `loadouts/data/` |
| 9 | Work | Marketing and social content | `loadouts/marketing/` |
| 10 | Work | Sales and customer service | `loadouts/sales-service/` |
| 11 | Work | Running a small business | `loadouts/small-business/` |
| 12 | Work | Career | `loadouts/career/` |
| 13 | Learning | Learning and study | `loadouts/learning/` |
| 14 | Life | Money and personal finance | `loadouts/money/` |
| 15 | Life | Health and wellbeing | `loadouts/health/` |
| 16 | Life | Home and life admin | `loadouts/home-life/` |
| 17 | Life | Relationships and personal messages | `loadouts/relationships/` |
| 18 | Making things | Design and visuals | `loadouts/design/` |
| 19 | Making things | Creative projects | `loadouts/creative/` |
| 20 | Making things | Building and automating | `loadouts/building/` |
| 21 | Making things | Tech help | `loadouts/tech-help/` |

---

# Core

## 1. Writing and editing

Folder: `loadouts/writing/`. The craft of putting anything into words. This is the first section we build, so it has the most detail. Each skill also notes the default mistake it fixes.

### Skills

**Before writing**
- `writing-brief`: works out the reader, the purpose, and the single main point before drafting. Fixes: starting to write with no clear point.
- `outline`: turns a goal or messy notes into an order of points. Fixes: drafts that wander.
- `notes-to-draft`: turns bullet notes, a voice memo, or a brain dump into a first draft. Fixes: the AI adding ideas that were never in the notes.

**Drafting**
- `short-piece`: anything under about 200 words. Point first, one ask. Fixes: long warm-ups and padding.
- `long-piece`: documents with several parts. Headings, flow, and a summary up top. Fixes: walls of text with the key point buried.
- `how-to-and-instructions`: explains how to do something, step by step. Fixes: skipped steps and assumed knowledge.
- `persuade`: makes a case or a request so the reader says yes. Fixes: listing features instead of what the reader cares about.
- `tell-a-story`: narrative for bios, about pages, and personal pieces. Fixes: flat lists of events with no thread.

**Voice and tone**
- `match-my-voice`: learns the user's style from samples and writes like them. Fixes: everything sounding like the same AI.
- `tone-shift`: makes a piece warmer, firmer, more formal, or more casual without changing the meaning. Fixes: tone changes that also change the message.
- `reading-level`: fits the text to the reader: simpler, more expert, or easier for non-native readers. Fixes: one level for everyone.
- `sound-human`: removes the tell-tale AI style: filler, cliches, too much hedging, lists of three. Fixes: writing people spot as AI.

**Editing**
- `tighten`: cuts length without losing meaning, and hits a word count. Fixes: cuts that remove the important part.
- `clarity-edit`: fixes confusing sentences, jargon, and buried points. Fixes: polishing words while the meaning stays unclear.
- `structure-edit`: reorders and regroups a draft that rambles. Fixes: line edits on a draft that needs a new order.
- `proofread`: fixes spelling, grammar, punctuation, and consistency, and changes nothing else. Fixes: the AI rewriting when asked only to proofread.
- `feedback-on-draft`: gives useful notes on someone's draft without rewriting it. Fixes: vague praise and taking over the author's work.

**Special cases**
- `written-to-be-spoken`: text that will be read aloud. Fixes: sentences that look fine but are hard to say.
- `rewrite-for-format`: turns one piece into another, such as an email into a post or a report into a summary. Fixes: copying the old shape into the new format.
- `translate-and-localize`: translates and adapts for the reader's country and culture. Fixes: word-for-word translation.

### Agents

| Agent | Handles | Does not handle |
|---|---|---|
| Outliner | Turning the brief into an order of points | Writing full sentences |
| Drafter | Writing the first full version from the outline | Editing its own draft |
| Voice Matcher | Adjusting a draft to the user's voice, tone, and reading level | Changing content or structure |
| Editor | Tightening, clarifying, and reordering a draft | Adding new content |
| Proofreader | Catching surface errors at the very end | Rephrasing or restructuring |

### Teams

- **Long document:** Outliner > Drafter > Editor > Proofreader. For anything with several parts.
- **Polish my draft:** Editor > Proofreader. For text the user already wrote.
- **In my voice:** Drafter > Voice Matcher. For pieces that must sound like the user.

Short pieces use a single skill and no team.

## 2. Research and fact checking

Folder: `loadouts/research/`. Finding things out and knowing how far to trust them.

### Skills

**Asking the right question**
- `research-question`: turns a vague curiosity into a clear question, a scope, and a search plan.

**Finding**
- `quick-lookup`: a fast answer with a source, for simple facts.
- `deep-search`: many searches across many sources for a broad topic.
- `find-the-original`: tracks a claim, quote, or number back to where it first came from.
- `people-and-company-lookup`: background on a person, business, or organization from public information.

**Judging sources**
- `source-check`: how trustworthy a source is and why, including slant and hidden sales pitches.
- `fact-check`: tests whether one specific claim is true.
- `conflicting-sources`: what to do when good sources disagree.

**Making sense**
- `side-by-side`: lays out findings on several things in one comparison table.
- `pull-it-together`: combines findings into what is known, what is unknown, and what is disputed.
- `numbers-in-context`: checks what a statistic really means and what it leaves out.

**Reporting**
- `research-brief`: the short answer first, then evidence, sources, and how sure we are.
- `cite-sources`: lists sources properly, with links, in the style needed.
- `keep-watch`: tracks a topic over time and reports what changed.

### Agents

| Agent | Handles | Does not handle |
|---|---|---|
| Search Planner | Breaking the question into what to look up and where | Doing the searches |
| Searcher | Finding and collecting sources | Judging whether they are right |
| Source Checker | Judging sources and testing claims | Looking into new topics |
| Synthesizer | Combining checked findings into an answer | Adding any claim without a source |

### Teams

- **Deep research:** Search Planner > Searcher > Source Checker > Synthesizer.
- **Fact check:** Searcher > Source Checker.

## 3. Reading and summarizing

Folder: `loadouts/reading/`. Understanding things other people wrote.

### Skills

**Summaries**
- `quick-summary`: the main points of any text in a few lines.
- `summary-for-someone`: a summary shaped for one reader or one decision.

**Long and hard documents**
- `long-document`: works through a document too long to take in at once without dropping parts.
- `contract-and-terms`: a plain-language read of contracts, leases, and terms, with what to watch for.
- `official-letter`: letters from government, banks, insurers, and schools: what it says, what to do, and by when.
- `technical-or-academic`: papers, manuals, and specs in plain words.

**Conversations and recordings**
- `meeting-notes`: turns a transcript or rough notes into decisions, actions, and owners.
- `thread-catch-up`: turns a long email or chat thread into where things stand and what is needed from you.
- `audio-video-notes`: turns the transcript of a video, podcast, or lecture into notes.

**Pulling things out**
- `find-in-document`: answers a question from a document and shows the exact place it says so.
- `pull-out-details`: extracts dates, names, amounts, and tasks into a list or table.
- `compare-documents`: shows what changed or differs between two versions or two documents.
- `many-documents`: reads a pile of documents and summarizes across them.

**After reading**
- `questions-to-ask`: what the document leaves out and what to ask the sender.

### Agents

| Agent | Handles | Does not handle |
|---|---|---|
| Reader | Reading the whole thing and mapping what is where | Judging or summarizing |
| Extractor | Pulling out facts, dates, amounts, and obligations | Interpreting them |
| Summarizer | Writing the summary for the intended reader | Adding anything that is not in the text |
| Risk Spotter | Flagging catches, deadlines, and missing pieces | Giving legal advice |

### Teams

- **Long document:** Reader > Extractor > Summarizer.
- **Before you sign:** Reader > Extractor > Risk Spotter > Summarizer.

## 4. Thinking and decisions

Folder: `loadouts/thinking/`. Coming up with ideas, solving problems, and choosing.

### Skills

**Ideas**
- `brainstorm`: many ideas fast, before judging any of them.
- `name-it`: names for products, projects, businesses, and pets.

**Understanding a problem**
- `define-the-problem`: finds the real problem before anyone tries to solve it.
- `root-cause`: works out why something keeps happening.
- `break-it-down`: splits a big problem into small parts.

**Deciding**
- `weigh-options`: pros, cons, what matters most, and a recommendation.
- `big-life-decision`: a job, a move, school, or a large purchase, with a values and regret check.
- `risk-check`: what could go wrong and how to guard against it.

**Testing your thinking**
- `poke-holes`: the strongest case against an idea or plan.
- `second-opinion`: an honest review of reasoning the user has already done.
- `check-my-assumptions`: what must be true for this to work.

**Talking it through**
- `think-out-loud`: a thinking partner that asks questions instead of handing over answers.
- `negotiation-prep`: your goals, their side, and your replies, before any negotiation.

### Agents

| Agent | Handles | Does not handle |
|---|---|---|
| Idea Generator | Producing many options | Judging them |
| Problem Framer | Defining the real problem and what matters most | Proposing solutions |
| Option Analyst | Weighing options against what matters | Making the choice for the user |
| Challenger | Arguing the other side and finding weak points | Coming up with new options |

### Teams

- **Make a decision:** Problem Framer > Option Analyst > Challenger.
- **Idea session:** Idea Generator > Challenger > Option Analyst.

## 5. Planning and projects

Folder: `loadouts/planning/`. Turning goals into plans and keeping them on track.

### Skills

**Goals**
- `goal-setting`: turns a fuzzy wish into a clear goal and a way to tell it is done.
- `priorities`: what to do first when everything feels urgent.

**Plans**
- `step-by-step-plan`: a goal turned into ordered steps with time estimates.
- `project-plan`: bigger work with stages, dates, people, and what depends on what.
- `timeline-and-deadline`: works back from a deadline to today.
- `checklist`: a reusable checklist for a task that repeats.

**Time**
- `daily-plan`: a realistic plan for one day.
- `weekly-plan`: a plan for the week and a review at the end of it.
- `routine-and-habit`: builds a routine that sticks.

**Keeping on track**
- `progress-check`: where things stand against the plan and what to change.
- `unstuck`: what to do when a project stalls or keeps getting put off.
- `task-list-cleanup`: turns a messy to-do list into a sorted, doable one.

**Working with others**
- `who-does-what`: splits work and owners across people.
- `handover`: passes work to someone else so nothing is lost.

### Agents

| Agent | Handles | Does not handle |
|---|---|---|
| Scoper | Deciding what is in, what is out, and what done looks like | Listing the steps |
| Planner | Turning the scope into ordered steps with time estimates | Fitting them to a calendar |
| Scheduler | Fitting the plan around real dates and limits | Changing the goal |
| Tracker | Comparing progress to the plan and adjusting it | Starting new plans |

### Teams

- **Plan a project:** Scoper > Planner > Scheduler.
- **Weekly reset:** Tracker > Scheduler.

---

# Work

## 6. Email and work communication

Folder: `loadouts/work-communication/`. The messages and meetings that fill a working day.

### Skills

**Email**
- `work-email`: a clear work email with one ask.
- `email-reply`: answers every part of an email, briefly.
- `follow-up`: chases a reply without nagging.
- `introduction-and-ask`: introduces yourself or two other people and asks for something.
- `inbox-triage`: sorts a pile of emails into reply, do, wait, and ignore.

**Chat and updates**
- `chat-message`: short messages for tools like Slack and Teams.
- `status-update`: progress, what is blocked, and what is next.

**Meetings**
- `meeting-agenda`: the purpose, the items, and the time for each.
- `meeting-prep`: your goal, your questions, and what you will say.
- `meeting-follow-up`: the recap message with decisions and owners.

**Hard conversations at work**
- `give-feedback`: feedback that is clear and kind.
- `say-no`: declines or pushes back without damage.
- `bad-news`: delivers delays, mistakes, and cuts.
- `raise-a-concern`: disagrees with a boss or a decision in a way that gets heard.

**Writing upward**
- `write-for-leaders`: a brief for a busy senior reader, with the ask at the top.

### Agents

| Agent | Handles | Does not handle |
|---|---|---|
| Context Reader | Reading the thread and the situation to find what is being asked and by whom | Writing the reply |
| Message Drafter | Writing the message | Sending it |
| Tone Checker | Checking how the message will land with this reader | Changing the ask |
| Inbox Sorter | Sorting and ranking a pile of messages | Replying to them |

### Teams

- **Hard message:** Context Reader > Message Drafter > Tone Checker.
- **Inbox clear-out:** Inbox Sorter > Message Drafter.

## 7. Presentations and reports

Folder: `loadouts/presentations-reports/`. Slides, reports, and documents made to inform or win people over.

### Skills

**Slides**
- `deck-outline`: the story and slide order before any design.
- `slide-writing`: one point per slide, with a headline that says the point.
- `speaker-notes`: what to say on each slide.
- `deck-cleanup`: fixes an existing deck: cut, reorder, simplify.
- `pitch-deck`: a deck to win money, a client, or approval.

**Reports**
- `report-structure`: summary first, then findings, then the recommendation.
- `one-pager`: the whole case on one page.
- `executive-summary`: the short summary at the top of a long document.
- `proposal`: proposes work or an idea: the problem, the plan, the cost, the ask.
- `recurring-report`: a weekly or monthly report that is quick to fill in.

**Layout**
- `table-and-layout`: makes tables and pages easy to scan.

**Delivering**
- `talk-prep`: rehearsal, timing, the opening, and the close.
- `q-and-a-prep`: likely questions and good answers.

### Agents

| Agent | Handles | Does not handle |
|---|---|---|
| Storyliner | Deciding the message and the order | Writing slides or pages |
| Slide and Page Builder | Writing each slide or page | Changing the storyline |
| Visual Advisor | Deciding which points need a chart, table, or picture, and the layout | Producing the numbers |
| Rehearsal Coach | Preparing the speaker for delivery and questions | Changing the content |

### Teams

- **Build a deck:** Storyliner > Slide and Page Builder > Visual Advisor > Rehearsal Coach.
- **Write a report:** Storyliner > Slide and Page Builder > Visual Advisor.

## 8. Data and spreadsheets

Folder: `loadouts/data/`. Numbers, spreadsheets, and what they mean.

### Skills

**Spreadsheets**
- `formula-help`: writes and explains formulas for Excel and Google Sheets.
- `spreadsheet-build`: sets up a new sheet for a purpose.
- `spreadsheet-fix`: finds why a sheet is broken or giving wrong answers.
- `pivot-and-summary`: summarizes rows by group.

**Cleaning**
- `clean-data`: fixes messy data: duplicates, formats, and blanks.
- `combine-data`: joins lists or files together.
- `data-check`: a sanity check before trusting the numbers.

**Analysis**
- `explore-data`: a first look: what is here and what stands out.
- `answer-from-data`: answers one specific question with the data.
- `trends-and-comparisons`: change over time and differences between groups.
- `simple-forecast`: a sensible estimate with a range, not a single number.
- `survey-results`: analyzes survey or feedback answers, including written comments.

**Showing**
- `make-a-chart`: the right chart for the point, made clearly.
- `dashboard-plan`: a simple tracker for the few numbers that matter.
- `data-story`: explains what the numbers mean and what to do about it.

**Understanding numbers**
- `stats-in-plain-words`: averages, percentages, and margins of error explained simply.

### Agents

| Agent | Handles | Does not handle |
|---|---|---|
| Formula Builder | Writing and fixing formulas and sheet structure | Interpreting results |
| Data Cleaner | Preparing and checking the data | Analyzing it |
| Analyst | Running the numbers to answer the question | Cleaning or presenting |
| Chart Maker | Turning results into clear visuals | Changing the numbers |
| Number Checker | Rechecking the calculations independently | Doing new analysis |

### Teams

- **Analyze my data:** Data Cleaner > Analyst > Number Checker > Chart Maker.
- **Build a spreadsheet:** Formula Builder > Number Checker.

## 9. Marketing and social content

Folder: `loadouts/marketing/`. Getting the word out about a business, a product, or yourself.

### Skills

**Foundations**
- `audience-profile`: who you are talking to and what they care about.
- `message-and-positioning`: what you offer, why it matters, and how you differ.
- `brand-voice`: how the brand sounds, with examples of do and do not.
- `marketing-plan`: a simple plan: goal, channels, budget, and calendar.

**Social media**
- `social-post`: posts that fit each platform.
- `content-calendar`: a month of post ideas with themes.
- `short-video-script`: hooks and scripts for short promotional videos.
- `repurpose-content`: turns one piece into many formats.
- `comments-and-community`: replies to comments and messages, including negative ones.

**Written marketing**
- `website-copy`: home, about, and product pages.
- `blog-post`: a helpful article that also gets found in search.
- `newsletter`: an email newsletter people open.
- `ad-copy`: short ads with several versions to test.
- `product-description`: listings for shops and marketplaces.

**Getting found and measuring**
- `search-basics`: what people search for and how to show up for it.
- `results-review`: reads the marketing numbers and decides what to change.

### Agents

| Agent | Handles | Does not handle |
|---|---|---|
| Audience Profiler | Working out who the audience is and what they care about | Writing content |
| Strategist | The plan, the message, and the channels | Writing the content itself |
| Content Creator | Writing posts, pages, emails, and ads | Setting the strategy |
| Channel Adapter | Reshaping content for each platform's rules and lengths | Coming up with new ideas |
| Results Analyst | Reading the numbers and recommending changes | Writing content |

### Teams

- **Campaign:** Audience Profiler > Strategist > Content Creator > Channel Adapter.
- **Month of content:** Strategist > Content Creator > Channel Adapter.
- **What is working:** Results Analyst > Strategist.

## 10. Sales and customer service

Folder: `loadouts/sales-service/`. Winning customers and keeping them happy.

### Skills

**Finding customers**
- `ideal-customer`: who to sell to and who to skip.
- `prospect-research`: what to learn about a lead before making contact.
- `outreach-message`: a first message that gets a reply.
- `outreach-follow-up`: what to send after no reply, and when to stop.

**Selling**
- `discovery-questions`: questions that uncover what a buyer really needs.
- `sales-call-prep`: getting ready for a sales call.
- `objection-handling`: replies to "too expensive" and "not right now."
- `quote-and-proposal`: a quote or proposal that wins the work.
- `pricing-conversation`: discounts, negotiation, and holding your price.

**After the sale**
- `customer-onboarding`: welcomes and sets up a new customer.
- `check-in-and-renewal`: keeps customers and grows the relationship.
- `ask-for-review-or-referral`: asks happy customers to spread the word.

**Customer service**
- `support-reply`: clear, kind answers to customer questions.
- `angry-customer`: complaints, refunds, and calming things down.
- `help-article`: answers customers can find and use themselves.
- `saved-replies`: reusable answers for the questions that keep coming.

### Agents

| Agent | Handles | Does not handle |
|---|---|---|
| Prospect Researcher | Finding out who the lead is and what matters to them | Writing messages |
| Outreach Writer | First messages and follow-ups | Research or deal strategy |
| Deal Coach | Call prep, objections, proposals, and next steps | Cold outreach |
| Support Responder | Answering customers | Setting company policy |
| Knowledge Builder | Turning repeated questions into saved replies and help articles | Answering live customers |

### Teams

- **Win a customer:** Prospect Researcher > Outreach Writer > Deal Coach.
- **Build a help center:** Support Responder > Knowledge Builder.

## 11. Running a small business

Folder: `loadouts/small-business/`. The behind-the-scenes work of a small business or side job.

### Skills

**Starting**
- `business-idea-check`: tests an idea before money is spent on it.
- `simple-business-plan`: a plan that fits on one page.
- `pricing`: sets prices that cover costs and make sense to customers.
- `startup-checklist`: the steps to get going, and when to ask a professional.

**Money**
- `invoices-and-getting-paid`: invoices, payment terms, and chasing late payers.
- `bookkeeping-basics`: tracks income and costs in sensible categories.
- `cash-flow`: whether there will be enough cash, month by month.
- `business-numbers`: profit, margin, and break-even in plain words.

**Operations**
- `process-and-how-to`: writes down how a job is done so anyone can do it.
- `supplier-and-vendor`: chooses, compares, and deals with suppliers.
- `policies`: refund, booking, and cancellation policies.

**People**
- `job-post-and-hiring`: the job ad, screening, and interview questions.
- `new-hire-setup`: a first-week plan and training.
- `staff-management`: schedules, feedback, and hard staff conversations.

**Legal and admin**
- `simple-agreements`: plain first drafts of simple agreements, with a clear note to have a professional check them.
- `rules-and-compliance`: which rules likely apply and what to ask an accountant or lawyer.

### Agents

| Agent | Handles | Does not handle |
|---|---|---|
| Business Planner | Ideas, plans, and pricing | Bookkeeping |
| Money Minder | Invoices, books, and cash flow | Tax or legal advice |
| Operations Organizer | Processes, suppliers, and policies | Money or hiring |
| People Helper | Hiring, onboarding, and managing staff | Legal contracts |
| Paperwork Drafter | First drafts of agreements and forms, with flags for what needs a professional | Final legal or tax decisions |

### Teams

- **Start a business:** Business Planner > Money Minder > Paperwork Drafter.
- **Hire someone:** People Helper > Paperwork Drafter.
- **Monthly check-up:** Money Minder > Business Planner.

## 12. Career

Folder: `loadouts/career/`. Finding work, getting hired, and moving up.

### Skills

**Direction**
- `career-direction`: what to aim for, given your strengths and interests.
- `career-change`: a plan to move into a new field.

**Applying**
- `resume`: builds or improves a resume.
- `resume-tailoring`: fits a resume to one job posting.
- `cover-letter`: a cover letter that adds to the resume instead of repeating it.
- `linkedin-profile`: a profile that gets found and read.
- `job-search-plan`: where to look, a tracker, and a weekly routine.

**Networking**
- `networking-message`: reaches out to people for advice or a referral.

**Interviews**
- `interview-prep`: likely questions and strong answers from your own experience.
- `mock-interview`: practice with feedback.
- `interview-stories`: turns your experience into clear examples.

**Offers and growth**
- `offer-evaluation`: compares offers on more than pay.
- `salary-negotiation`: what to ask for and how to say it.
- `raise-and-promotion`: builds the case for a raise or promotion.
- `performance-review`: the self-review and goals.
- `first-90-days`: starts a new job strong.

### Agents

| Agent | Handles | Does not handle |
|---|---|---|
| Career Guide | Direction and the overall plan | Writing documents |
| Job Matcher | Reading postings and finding the fit and the gaps | Writing from scratch |
| Resume Builder | The resume, cover letter, and profile | Inventing experience the user does not have |
| Interview Coach | Preparation and practice | Documents |
| Negotiation Coach | Offers, pay, and raises | Job search |

### Teams

- **Apply for a job:** Job Matcher > Resume Builder > Interview Coach.
- **Career change:** Career Guide > Job Matcher > Resume Builder.

---

# Learning

## 13. Learning and study

Folder: `loadouts/learning/`. Understanding new things, for students, parents, teachers, and the curious.

### Skills

**Understanding**
- `explain-it`: explains anything at the right level for this person.
- `worked-example`: walks through a solved problem one step at a time.
- `homework-help`: guides the student to the answer without just handing it over.

**Practice**
- `quiz-me`: practice questions with feedback.
- `flashcards`: cards for facts that need memorizing.
- `teach-it-back`: the learner explains, and the AI finds the gaps.

**Planning study**
- `study-plan`: a schedule that works back from a test date.
- `learn-a-new-skill`: a path from beginner to capable.
- `exam-prep`: strategy, past papers, and weak spots.
- `course-notes`: turns a lecture or reading into study notes.

**School writing**
- `essay-help`: planning, argument, and feedback, without writing the essay for the student.

**Languages**
- `language-practice`: conversation practice with gentle corrections.

**Parents and teachers**
- `help-my-child-learn`: supports a child's learning at their level.
- `lesson-plan`: a lesson with goals and activities.
- `make-a-worksheet-or-quiz`: practice materials with an answer key.
- `grading-and-feedback`: feedback on student work against a clear set of standards.

### Agents

| Agent | Handles | Does not handle |
|---|---|---|
| Tutor | Explaining and guiding | Handing over answers to graded work |
| Quiz Master | Making and marking practice questions | Teaching new material |
| Study Planner | Plans and schedules | Teaching |
| Writing Coach | Feedback on a student's writing | Writing it for them |
| Lesson Designer | Materials for teachers and parents | Tutoring a student directly |

### Teams

- **Exam prep:** Study Planner > Tutor > Quiz Master.
- **Learn a topic:** Tutor > Quiz Master.
- **Class materials:** Lesson Designer > Quiz Master.

---

# Life

## 14. Money and personal finance

Folder: `loadouts/money/`. Everyday money. This section explains and organizes. It does not pick investments or give tax advice, and it says so plainly.

### Skills

**Everyday money**
- `budget`: a budget that fits real life.
- `spending-review`: shows where the money goes, from your statements.
- `bills-and-subscriptions`: finds what to cut and what to negotiate.
- `read-a-statement`: bank statements, card statements, pay slips, and bills in plain words.

**Debt and credit**
- `debt-payoff-plan`: which debt to pay first and how long it will take.
- `credit-basics`: how credit scores work and how to improve one.
- `loan-compare`: the true cost of loans, cards, and mortgages side by side.

**Saving and big purchases**
- `savings-goal`: a target, a timeline, and a monthly amount.
- `big-purchase`: whether you can afford a car, a home, or another big buy.

**Investing and retirement**
- `investing-basics`: plain explanations of how investing works. No picks.
- `retirement-basics`: account types and how much to put away, explained.

**Taxes and insurance**
- `tax-basics`: what likely applies to you and what to gather. Not tax advice.
- `insurance-compare`: understands and compares policies.

**Life events and safety**
- `money-for-life-events`: a baby, a marriage, a divorce, a move, or a lost job.
- `scam-check`: whether an offer or request for money is a scam.

### Agents

| Agent | Handles | Does not handle |
|---|---|---|
| Money Organizer | Gathering and sorting income, spending, and debts | Giving advice |
| Budget Planner | The budget, the payoff plan, and savings targets | Choosing financial products |
| Product Comparer | Comparing loans, accounts, and insurance on true cost | Recommending investments |
| Paperwork Helper | Statements, forms, and tax documents | Tax advice |
| Scam and Risk Checker | Scams, risky offers, and when to see a professional | Planning or budgeting |

### Teams

- **Money check-up:** Money Organizer > Budget Planner.
- **Big purchase:** Money Organizer > Product Comparer > Budget Planner.
- **Tax time:** Money Organizer > Paperwork Helper.

## 15. Health and wellbeing

Folder: `loadouts/health/`. Understanding health information and building healthy routines. This section never diagnoses, never changes medicine doses, and always says when to get real care.

### Skills

**Understanding health information**
- `understand-a-result`: explains what a doctor said or what a test shows, in plain words.
- `medication-questions`: what a medicine is for and what to ask the pharmacist.
- `symptom-guide`: sorts a symptom into urgent, soon, or self-care. Never a diagnosis.
- `health-claim-check`: whether a health claim is backed by evidence.

**Appointments**
- `appointment-prep`: a symptom timeline and the questions to ask.
- `after-visit-summary`: turns visit notes into what to do next.

**Fitness**
- `workout-plan`: a plan that fits your goal, time, and equipment.
- `start-exercising`: a gentle start for beginners.

**Food**
- `eating-plan`: a way of eating that fits your goals.
- `special-diet`: eating with allergies or a condition, following your doctor's guidance.

**Sleep, stress, and mind**
- `sleep-better`: habits and fixes for better sleep.
- `stress-and-overwhelm`: practical steps when it is all too much.
- `journaling-and-reflection`: prompts for thinking things through.
- `hard-day-support`: listening and coping steps, and pointing to real help when it is needed.

**Caring and costs**
- `caregiver-help`: organizes care for a parent, child, or partner, and looks after the carer.
- `medical-bills-and-insurance`: understands coverage, bills, and how to appeal.

### Agents

| Agent | Handles | Does not handle |
|---|---|---|
| Medical Translator | Explaining results, diagnoses, and medicines in plain words | Diagnosing or advising treatment |
| Visit Prepper | Getting ready for an appointment and following up after | Medical explanations |
| Fitness Coach | Exercise plans | Food or medical questions |
| Nutrition Guide | Eating plans | Treating medical conditions |
| Wellbeing Companion | Stress, sleep, and reflection | Therapy or crisis care |
| Safety Screener | Checking every health answer for urgent signs and limits | Giving advice itself |

### Teams

- **Doctor visit:** Visit Prepper > Medical Translator > Safety Screener.
- **Get healthier:** Fitness Coach > Nutrition Guide > Safety Screener.

## 16. Home and life admin

Folder: `loadouts/home-life/`. The paperwork and planning of everyday life.

### Skills

**Paperwork**
- `fill-a-form`: help with forms and applications.
- `formal-letter`: letters to landlords, companies, and agencies.
- `complaint-and-refund`: gets a problem with a company fixed.
- `dispute-and-appeal`: fights a bill, a fine, or a denied claim.
- `cancel-and-switch`: cancels a service or moves to a new provider.

**Home**
- `home-maintenance`: an upkeep schedule and help when something breaks.
- `diy-project`: the plan, the steps, and the safety notes.
- `hire-a-pro`: finding one, comparing quotes, and what to ask.
- `moving`: the checklist and timeline for a move.
- `renting-and-housing`: lease questions, landlord issues, and house hunting.
- `car-care`: maintenance, repair quotes, and buying or selling a car.

**Food**
- `meal-planning`: a week of meals and the grocery list.
- `recipe-help`: adapts, swaps ingredients, and scales recipes.

**Shopping**
- `buying-guide`: compares products for your needs and budget.

**Travel**
- `trip-plan`: the itinerary, bookings to compare, and what to pack.

**Family and events**
- `event-planning`: parties, weddings, and gatherings.
- `parenting-help`: ideas and approaches that fit the child's age.
- `gift-ideas`: gifts that fit the person and the budget.

### Agents

| Agent | Handles | Does not handle |
|---|---|---|
| Paperwork Handler | Forms, letters, complaints, and disputes | Legal advice |
| Home Advisor | Maintenance, repairs, hiring help, moving, and cars | Paperwork |
| Shopping Scout | Comparing products and prices | Buying anything |
| Trip Planner | Itineraries and travel preparation | Booking or paying |
| Meal Planner | Meal plans, recipes, and grocery lists | Medical diets |
| Event and Family Organizer | Events, gifts, and family logistics | Travel or shopping comparisons |

### Teams

- **Plan a trip:** Trip Planner > Shopping Scout.
- **Plan an event:** Event and Family Organizer > Shopping Scout > Meal Planner.
- **Move house:** Home Advisor > Paperwork Handler.

## 17. Relationships and personal messages

Folder: `loadouts/relationships/`. The words that matter most: to family, friends, and partners. This section helps people say what they mean. It is not therapy.

### Skills

**Everyday personal messages**
- `personal-message`: texts and notes to friends and family that sound like you.
- `reply-help`: what to say back to a tricky message.

**Big moments**
- `toast-and-speech`: weddings, birthdays, and retirements.
- `card-message`: birthday, thank-you, and congratulations messages.
- `condolence`: what to say when someone is grieving.
- `eulogy-and-tribute`: honoring someone who has died.
- `vows-and-love-letter`: wedding vows and letters to a partner.

**Hard conversations**
- `difficult-conversation-prep`: what to say and how to say it.
- `apology`: an apology that actually repairs things.
- `set-a-boundary`: says what you need, clearly and kindly.
- `conflict-cool-down`: sees both sides and brings the temperature down.

**Dating**
- `dating-profile`: a profile that sounds like the real you.
- `dating-messages`: openers and replies.

**Understanding people**
- `read-the-situation`: several possible readings of a message or behavior, not one guess.
- `family-matters`: tricky family situations with in-laws, teenagers, or aging parents.

### Agents

| Agent | Handles | Does not handle |
|---|---|---|
| Situation Reader | Understanding who is involved, the history, and what the user wants | Taking sides |
| Message Writer | Drafting the message in the user's own voice | Deciding what the user should want |
| Occasion Writer | Speeches, cards, and tributes | Everyday messages |
| Conversation Coach | Preparing and practicing for a hard talk | Therapy |

### Teams

- **Hard conversation:** Situation Reader > Conversation Coach > Message Writer.
- **Big moment:** Situation Reader > Occasion Writer.

---

# Making things

## 18. Design and visuals

Folder: `loadouts/design/`. Making things look good, with or without design skills.

### Skills

**Images with AI**
- `image-prompt`: describes a picture so an image tool makes what you meant.
- `image-edit-request`: changes an existing image.
- `consistent-style`: keeps one look across many images.

**Brand look**
- `brand-basics`: colors, fonts, and a logo direction.
- `logo-brief`: what a logo should say, ready for a tool or a designer.

**Layouts**
- `flyer-and-poster`: one clear message that can be read from a distance.
- `social-graphic`: graphics sized and styled for each platform.
- `document-layout`: clean pages for resumes, reports, and handouts.
- `slide-design`: the look of slides, once the content is set.
- `invitation-and-card`: invitations and greeting cards.
- `infographic`: turns information into one picture.

**Web and screens**
- `web-page-layout`: the sections of a page and what goes where.
- `color-and-font-pick`: colors and fonts that work together.

**Feedback**
- `design-feedback`: what works, what does not, and what to fix first.
- `accessibility-check`: readable for everyone: contrast, text size, and image descriptions.

### Agents

| Agent | Handles | Does not handle |
|---|---|---|
| Art Director | Deciding the look and the direction | Making the design |
| Image Prompter | Writing and refining prompts for image tools | Layout |
| Layout Designer | Arranging words and pictures on a page or screen | Creating the images |
| Design Critic | Reviewing for clarity and accessibility | Redesigning |

### Teams

- **Make a graphic:** Art Director > Layout Designer > Design Critic.
- **Brand kit:** Art Director > Image Prompter > Layout Designer.

## 19. Creative projects

Folder: `loadouts/creative/`. Stories, scripts, songs, and hobbies. The creator's voice always comes first.

### Skills

**Stories**
- `story-idea`: premises and what-ifs.
- `plot-and-outline`: the shape of a story from start to end.
- `character-builder`: people with wants, flaws, and a voice.
- `world-building`: settings with rules that hold together.
- `scene-and-dialogue`: scenes that move and speech that sounds real.
- `story-feedback`: notes on a draft that keep the writer's voice.

**Poems, songs, and humor**
- `poem`: poems in any form.
- `song-lyrics`: lyrics with a hook, verses, and rhythm.
- `jokes-and-humor`: jokes, funny captions, and light roasts.

**Scripts and shows**
- `video-script`: scripts for longer videos.
- `podcast-plan-and-script`: the show idea, episode plans, and scripts.

**Games and play**
- `tabletop-game-helper`: campaigns, characters, and puzzles.
- `kids-stories-and-activities`: bedtime stories and games for children.

**Bigger projects**
- `hobby-project-plan`: crafts, gardening, woodworking, music practice, and more.
- `memoir-and-family-history`: turns memories into a written record.
- `book-project`: plans and finishes a long manuscript, with self-publishing basics.

### Agents

| Agent | Handles | Does not handle |
|---|---|---|
| Idea Sparker | Premises and options | Drafting |
| Story Architect | Plot, characters, and world | Writing the prose |
| Creative Writer | Writing scenes, verses, and scripts in the creator's style | Changing the plan |
| Script Producer | Planning and formatting videos, podcasts, and shows | Fiction prose |
| Creative Editor | Notes that protect the creator's voice | Rewriting the piece |

### Teams

- **Write a story:** Idea Sparker > Story Architect > Creative Writer > Creative Editor.
- **Make a video or podcast:** Idea Sparker > Script Producer > Creative Editor.

## 20. Building and automating

Folder: `loadouts/building/`. Simple websites, small apps, and automations for people who are not programmers. This section will not beat kits made only for coding, and it does not try to.

### Skills

**Planning**
- `idea-to-plan`: turns an idea into a plain-language plan: what it does, who it is for, and the first version.
- `pick-the-tools`: chooses between no-code tools, simple builders, and real code.

**Websites**
- `simple-website`: a personal or small business site.
- `online-store-setup`: a shop that takes orders and payments.
- `website-fix-and-update`: changes and repairs to a site you already have.
- `domain-and-hosting`: web addresses, hosting, and going live, in plain words.

**Apps and scripts**
- `small-app`: a simple working app or tool.
- `script-for-a-task`: a small program for one job, such as renaming files.
- `explain-this-code`: what a piece of code does, in plain words.
- `fix-an-error`: what an error means and how to fix it.
- `add-a-feature`: changes an existing project without breaking it.

**Automation**
- `automate-a-task`: connects apps so repeating work happens on its own.
- `ai-assistant-setup`: sets up a custom AI helper with saved instructions.

**Safe and working**
- `test-it`: checks it works before you rely on it.
- `save-and-back-up`: keeps a history so you can always go back.
- `launch-checklist`: security, private data, and the last checks before going live.

### Agents

| Agent | Handles | Does not handle |
|---|---|---|
| Product Planner | Turning the idea into a plan and small steps | Building |
| Builder | Writing the code or setting up the tool | Testing its own work |
| Tester | Checking it works and trying to break it | Fixing what it finds |
| Fixer | Finding the cause of an error and fixing it | Adding new features |
| Launch Checker | Security, backups, and go-live checks | Building |

### Teams

- **Build something new:** Product Planner > Builder > Tester > Fixer > Tester > Launch Checker.
- **Fix something broken:** Fixer > Tester.
- **Automate a task:** Product Planner > Builder > Tester.

## 21. Tech help

Folder: `loadouts/tech-help/`. Help with phones, computers, apps, and staying safe online.

### Skills

**Fixing problems**
- `troubleshoot-device`: a phone, computer, or tablet problem, one step at a time.
- `wifi-and-internet`: slow or broken internet.
- `error-message-help`: what an error message means and what to do.
- `slow-or-full-device`: speeds up a device and frees up space.

**How do I**
- `how-to-in-an-app`: exact steps inside common apps.
- `new-device-setup`: sets up a new device and moves everything from the old one.
- `learn-a-tool`: gets you going with a new app fast.

**Safety and privacy**
- `account-security`: passwords and two-step login.
- `is-this-safe`: suspicious links, messages, and downloads.
- `hacked-or-locked-out`: what to do right now and how to recover.
- `privacy-settings`: who can see what, and how to change it.
- `backup-and-recovery`: backs up what matters and gets lost things back.

**Choosing tech**
- `what-to-buy`: the right device for your needs and budget.
- `which-app-or-service`: picks an app, service, or plan.

**Helping others**
- `help-a-relative`: instructions simple enough for a family member who is not technical.
- `smart-home-setup`: smart speakers, lights, cameras, and making them work together.

### Agents

| Agent | Handles | Does not handle |
|---|---|---|
| Troubleshooter | Finding the cause, one change at a time | Writing long guides |
| Step-by-Step Guide | Exact instructions for the user's device and app | Diagnosing the problem |
| Security Helper | Accounts, privacy, suspicious messages, and recovery | Buying advice |
| Tech Advisor | What to buy or which app to use | Fixing problems |

### Teams

- **Fix it:** Troubleshooter > Step-by-Step Guide.
- **Lock it down:** Security Helper > Step-by-Step Guide.

---

## What is not decided yet

- The exact file format for a skill, an agent, a team, and the roadmap that routes between them.
- How pinpoint references from one skill to another are written.
- How the kit is installed in each tool.
- Which sections ship in the first public version.
