### Project Plan: Translating GKA to MIDI and Extending music21

#### Overview
This project involves developing a system to translate a custom Carnatic music notation format, GKA, into MIDI and an extended version of Python’s `music21` library. The goal is to create a comprehensive tool that supports bidirectional translation between GKA, MIDI, and extended `music21` objects.

---

#### 1. GKA Notation Structure

**Provided GKA File Example:**
```
[sa]-saa ; -|
[ri] (saa./ (ri.)\ saa./ (ri.)\ sa.)-|
[ga] (ri/ma\) ga<. ((ma\)) ga< (.)-|
[ma] maa ;-|
[pa] paa ;--|
[da] (paa./(da).\ paa. /(da).\pa)-|
[ni] (da/Sa<) (Sa\ ni) Sa\ (ni Sa)-|
[Sa] Saa ;-|

[Sa] ((pa))/Saa ,.(.)-|
[ni] (Sa ni) (Sa>.) \\\ni. ) ((Sa>>).) \(ni.) ((Sa)) -|
[da] ((ni))\\\pa. (((da))) \\\pa<(.) (((da))) \\\(pa<)(.) -|
[pa] paa ;-|
[ma] \\\maa ;-|
[ga] ((ma))ga(.) ((ma>>)) \\\ga(.) ((ma>>)) \\\\(ga)(.)-|
[ri] ((ga))\\\sa<. ((ri)) \\\sa<(.) ((ri)) \\\\\(sa<) -|
[sa] saa;-|
```

**Key Observations:**
1. **Pitch Representation:** The format uses syllables (e.g., `sa`, `ri`, `ga`) to represent pitches.
2. **Gamaka Indications:** Ornamentations such as slides (`\`, `/`), oscillations (`((...))`), and jumps (`<`, `>`) are explicitly noted.
3. **Phrasing and Duration:** Notation includes elements for phrasing (`;`, `-`), pauses (`.`), and other rhythmic indicators.
4. **Hierarchy:** Square brackets (`[...]`) seem to group pitches into hierarchical units.
5. **Complex Constructs:** Nested ornamentations (e.g., `(((da)))`) and combinations of slides and jumps are present.

---

#### 2. GKA Notation Details

**Gamakam Representation:**
- **Slides:** `/` and `\` extend transitions between notes.
- **Oscillations:** `((...))` indicate kampitham or vibrato-like effects.
- **Jumps:** `<` and `>` modify pitch frequency subtly to simulate microtonal shifts.

**Duration and Rhythmic Modifiers:**
- Parentheses `(...)` adjust note duration.
- Brackets `[...]` group multiple notes into phrases.
- Separators `;` and `-` define phrasing boundaries and breaks.

**Pitch Modifiers:**
- `<` and `>` reduce or increase pitch by specific ratios.
- Symbols like `*` indicate alternate gamakam forms.

**Phrasing Examples:**
- Complex phrases maintain overall duration by nesting elements within brackets.
- Variations in gamakams contribute to distinguishing raaga identities.

**Comprehensive Gamakam Support:**
- The tool will support various gamakams, including:
  - **Kampitham (Oscillations):** Indicated by nested parentheses and pitch modifiers.
  - **Nokku (Grace Notes):** Rapid ascent or descent around a target note.
  - **Jaaru (Glides):** Smooth transitions between notes with extended slides.
  - **Janta (Doubled Notes):** Pairing of notes with subtle tonal differences.
  - **Thirupam (Turns):** Intricate note turns and oscillations within a small range.

---

#### 3. Extensions to `music21`

**New Objects to be Added:**
- **Gamaka Object:** To represent slides, oscillations, and other ornamentations.
- **Pitch Modifiers:** Extended note definitions to include microtonal shifts.
- **Duration Adjusters:** Mechanisms to enforce rhythmic consistency across transformations.

**Integration:**
- Define mappings between GKA symbols and `music21` elements.
- Extend `music21` parsing and rendering logic to interpret GKA syntax.

---

#### 4. Translation Workflow

**Input Formats:**
- Text-based GKA files.
- MIDI files.

**Output Formats:**
- Extended `music21` objects.
- Standard MIDI files.

**Translation Steps:**
1. Parse GKA file into structured data.
2. Map GKA symbols to extended `music21` objects.
3. Convert `music21` representation to MIDI, ensuring accurate gamakam rendering.
   - **Mapping Note:** Pitch bends will be used as the primary mechanism to represent gamakams in MIDI. Precise mappings for each gamakam will be defined to ensure fidelity.
4. Support bidirectional translation between GKA, MIDI, and `music21`.

---

#### 5. AI-Assisted Parsing

**Role of AI:**
- Automate extraction of GKA elements from annotated examples.
- Validate mappings against known raaga patterns.

**Tools and Techniques:**
- Use natural language processing (NLP) to interpret comments and guidelines.
- Implement pattern recognition for identifying gamakam structures.

---

#### 6. Testing and Validation

**Test Cases:**
- Basic note translations.
- Complex gamakam phrases.
- Raaga-specific variations.

**Validation Criteria:**
- Accuracy of MIDI playback.
- Consistency with traditional Carnatic music standards.

---

#### 7. Documentation

**User Guide:**
- Examples of input and output formats.
- Explanation of supported gamakams and features.

**Developer Documentation:**
- Code structure and API references.
- Guidelines for extending functionality.

---

#### 8. Limitations and Scope

**Supported Raagas:**
- **Carnatic:** Sankarabharanam.

**Western Notation:**
- Support for **Major Scales** only.

**Placeholders for Further Clarification:**
1. **Gamaka Mapping:**
   - Pitch bends will be the primary method for representing gamakams in MIDI. Precise mappings for each gamakam need to be defined.
   - Should certain gamakams be omitted if they cannot be accurately represented?

2. **Raaga Extensions:**
   - Will additional Carnatic raagas need support in the future?
   - Should the tool be designed with modularity to add raagas incrementally?

3. **Western Notation Compatibility:**
   - Are there specific constraints when converting between GKA and Western Major Scales?
   - Should dynamics and articulations be supported?

4. **AI Role:**
   - What exact tasks will AI handle (e.g., error correction, gamakam interpretation)?
   - Are there fallback mechanisms if AI fails to interpret certain GKA features?

5. **Performance Requirements:**
   - Are there specific performance benchmarks (e.g., real-time conversion, minimal latency)?

---

#### 9. Timeline and Milestones

**Phase 1:** Define GKA parsing logic and extend `music21`.
**Phase 2:** Implement bidirectional translation.
**Phase 3:** Validate with examples and refine mappings.
**Phase 4:** Document and release tool.

---


#### Technical Specifications

**Development Environment:**
- Python version requirements (e.g., Python 3.8+)
- Required dependencies and versions (music21, midiutil, etc.)
- Development OS compatibility requirements
- Recommended IDE/tools

**Performance Requirements:**
- Maximum file size limitations for GKA input
- Processing time expectations (e.g., < 2s for typical file)
- Memory usage constraints
- Real-time processing requirements (if any)


#### Data Structures and Types

**GKA Parser:**
```typescript
// Core types for the parser
interface GKANote {
    pitch: string;           // Basic pitch (sa, ri, ga, etc.)
    duration: number;        // Duration in beats
    gamakams: Gamakam[];    // Array of applied gamakams
    modifiers: Modifier[];   // Pitch/duration modifiers
}

interface Gamakam {
    type: 'slide' | 'oscillation' | 'jump';
    direction: 'up' | 'down';
    intensity: number;       // 0-1 scale
    duration: number;        // Relative to note duration
}

interface Phrase {
    notes: GKANote[];
    metadata: {
        bracket: string;     // Type of grouping
        tempo: number;       // BPM if specified
    }
}
```

3. **Specific MIDI Mapping Details**
```markdown
#### MIDI Implementation Details

**Pitch Mapping:**
- sa = MIDI note 60 (Middle C)
- ri = MIDI note 62
- ga = MIDI note 64
[Complete mapping needed]

**Gamakam to MIDI Controls:**
- Slides: Pitch bend range ±2 semitones
- Oscillations: Modulation wheel (CC1)
- Amplitude variations: Volume (CC7)
[Complete mapping needed]

**MIDI Channel Allocation:**
- Channel 1: Primary melody
- Channel 2: Gamakam effects
[Complete allocation scheme needed]
```

4. **Error Handling**
```markdown
#### Error Handling Specifications

**Parser Errors:**
- Invalid syntax handling
- Missing bracket/parenthesis recovery
- Unknown symbol handling
- Malformed file handling

**MIDI Generation Errors:**
- Out-of-range note handling
- Unsupported gamakam combinations
- Resource exhaustion handling

**Validation Rules:**
- Maximum nesting depth for gamakams
- Valid pitch range constraints
- Duration consistency checks
```

5. **API Design**
```markdown
#### API Specification

**Core Classes:**
```python
class GKAParser:
    def parse_file(self, filepath: str) -> GKAScore
    def parse_string(self, content: str) -> GKAScore
    
class GKAToMIDI:
    def convert(self, gka_score: GKAScore) -> MIDIFile
    
class Music21Extension:
    def from_gka(self, gka_score: GKAScore) -> Stream
    def to_gka(self, stream: Stream) -> GKAScore
```

6. **Test Specifications**
```markdown
#### Testing Requirements

**Unit Test Coverage:**
- Minimum coverage requirement (e.g., 85%)
- Critical paths requiring 100% coverage

**Test Data:**
- Standard test files needed
- Edge case examples
- Performance test datasets

**Validation Suite:**
- Required test scenarios
- Acceptance criteria for each feature
- Performance benchmarks
```

7. **File Format Specifications**
```markdown
#### File Format Details

**GKA File Format:**
- Encoding requirements (UTF-8)
- Line ending handling
- Maximum file size
- Required header format
- Comment syntax and rules

**Output MIDI Format:**
- MIDI file version
- Required meta events
- Time division specifications
- Controller usage restrictions
```

These additions would provide the necessary technical detail for implementation. Would you like me to elaborate on any of these sections or suggest additional areas that need specification?