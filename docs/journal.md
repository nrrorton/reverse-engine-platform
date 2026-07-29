# Engineering Journal

## Session 001 - Project Foundation

Date: 2026-07-24

Worked with AI to establish the initial direction for this project.

We discussed some major decisions as listed below.

- I want to build a tool rather than just another web app.
- I want to build further fundamentals in OOP and will do so incorporating Java into this.
- Using Python for the analysis engine makes sense. I have no desire to rewrite complex libraries at this time.
- I want to keep AI as an explanation layer.
- As odd as this one may seem, as much help as I receive from AI during the build, I will hand type every last character in an attempt to understand everything fully.

Architectural direction:

- Keeping this local and modular.
- I want strict separation between presentation and analysis.

Next steps:

- Begin studying executable formats. (I'll be finding docs, and knowing myself, going excruciatingly slow)
- Developing the domain model within this.


## Session 003 - Begin scaffolding API message layer

Date: 2026-07-26

I've been reading through more of the FastAPI and Microsoft PE documentation. It's a lot, but if I want to be good at something, I know it takes sincere time and dedication.

Completed today:

- FastAPI analysis service initialized.
- Health endpoint created (generic content for now).
- Analysis endpoint created.
- Pydantic analysis contract defined (6 classes currently; ExecutableInfo, Sections, Import, Function, ExtractedString, AnalysisResponse).
- Service created to separate logic from the analyzer itself. 
- Mock analyzer implemented with filler test data.

What's up next:

- Replacing the mock analyzer with a real PE analyzer (begin studying LIEF).


## Session 006 - Making sense of extracted strings

Date: 2026-07-29

Obviously the order in which you pass arguments to a function that expects them in a certain order is important...Just to remember that I'm still incredibly junior.

It was decided yesterday (I know, I'm missing sessions in this journal (a couple now even..)) to build a format independent string extraction engine after finding that LIEF doesn't support dedicated general purpose string extraction.

Completed over the pass three days:

- ASCII string extraction.
- File offset tracking.
- The integration of mappers to remove this logic from the analyzers. 
- AnalysisService is now just an orchestrator.
- Created unit tests to test and verify string extraction works as intended (also just to learn more about Pytest).

For the future me:

- Will work on string classification after understanding all this a bit more.
- I want to make this more section aware, also.