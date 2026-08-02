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

To end the night, I got back into this after dinner and refactored the section analysis completely. Found that I was attempting to integrate sections into the JSON response twice and had to clean this up before things got out of hand. All is well now.



## Session 007 - Import Intelligence and realizing refactoring is just a part of the whole thing

Date: 2026-07-30

Feels like it can very quickly become a messy codebase and refuse to accept that as acceptable. Spent some time refactoring the import model setup and am now using an import_data model while leaving the imports schema as a strict API contract only. I like the idea of using mappers to translate info from the domain models to the API layer and will represent upcoming function parsing in this way.

Completed today:

- Reworked import logic moving from a central schema to a domain model with mapping to the analysis API.
- Added an intelligence directory with five standard Windows APIs (will expand this library soon).
- Cleaned up some wording and unused imports after the rework.
- Created a import analyzer test suite and added three tests to help ensure stability.

On the upcoming agenda:

- Function discovery (Similar to imports but with some added requirements).
- Studying Capstone as it will be necessary for function discovery.
- String intelligence on the radar.



## Session 008 - Establishing the foundations for function discovery

Date: 2026-07-31

I looked to AI for quite a bit of assistance here. Trying to figure out the math for when Capstone should start translating bytes was truly daunting and I'll admit a bit of defeat here. Not that I'm anti-AI, just that I'm doing my best to make all opportunities learning opportunites. That said, still feel that I'm learning plenty, even given the short duration.

What's now done:

- There's now a FunctionData and InstructionData model.
- Completed the function analysis pipeline.
- Created separate functions in the Function Analyzer to convert RVA to file offsets and extract bytes from each section.

Now what?:

- Now to integrate Capstone given those extracted bytes (the docs make this look super easy, we shall see).
- Tidying things up a bit and deciding if I need a separate sections schema. May remove and refactor after thinking on it a bit.



## Session 009 - Setting up the Capstone disassembler

Date: 2026-08-01

Been a busy day, but wanted to get even just a tiny bit built. Importing Capstone and setting up the disassembler wasn't bad at all.

Completed today:

- Capstone disassembler created and mapped to the function analyzer.
- Created one unit test (will expand this).
- Verified instructions are being returned in the API response.

Up next:

- Define logic to determine when a function ends (right now I'm just feeding Capstone the first 100 bytes).
- Just keep building from here and trying not to get carried away.



## Session 010 - Functions: recursive discovery, call target extraction, size calculation, boundary determination

Date: 2026-08-02

It was incredibly rewarding seeing how a lot of the DSA practice I've been doing outside of this project intertwines with today's work. In the recursive function discovery, I'm using a set to add visited functions and checking each time to see that the function isn't in visited before recursing (is that a word?). Just pretty cool to see small things come together in such a way.

Done for now (maybe I'll do more later):

- Can now find the entry point of the executable.
- Reworked the function analyzer so that the conversion of the relative virtual address (RVA) to offset is more robust.
- Created several private methods in the function analyzer and moved a lot of the logic out of the main analyze method itself.
- Checking to see if the mnemonic == 'call' and creating a calls list based on this.

What's to come:

- There's still a lot to improve as far as function naming, relationships, and just overall accuracy.
- Need to start studying control flow graphs as integrating these will be the next major step.
