# POS Equipment Planner
## Master Handoff Document for a Partner AI Agent

**Document type:** Product, UX, design-system and engineering handoff  
**Status:** Discovery completed, architecture direction proposed, implementation not started  
**Prepared:** 7 August 2026  
**Primary language:** Ukrainian  
**Source artifact:** `Обладнання v 2.0.html`  
**Intended recipient:** a new AI agent acting as a long-term product and engineering partner, not merely a task executor

---

# 1. Purpose of this document

This document transfers the full working context of the POS equipment project to another AI agent. It consolidates:

1. the analysis of the existing HTML catalog;
2. the snapshot of its visual design system;
3. the product reframing from catalog to field-work planner;
4. the proposed information architecture and domain model;
5. the recommended frontend, data, storage and deployment architecture;
6. the phased product roadmap;
7. the rules for future collaboration;
8. a three-layer self-audit confirming that the handoff preserves the important logic and decisions.

The handoff must enable a new agent to continue the work without reading the original conversation. The source HTML remains useful as a source of equipment data, images and observed design details, but it is **not** the architectural foundation of the new application.

---

# 2. Working relationship expected from the next agent

The next agent must behave as a **product partner and consultant**.

It should:

- challenge weak assumptions respectfully;
- explain trade-offs before locking important decisions;
- protect the core business workflow from unnecessary complexity;
- distinguish MVP needs from later ambitions;
- preserve data integrity and offline reliability;
- think mobile-first because the primary context is field work;
- propose options when a decision materially affects cost, maintainability or user experience;
- keep a visible decision log;
- produce implementation-ready artifacts, not only conceptual discussion;
- avoid blindly reproducing the existing HTML;
- ask clarification only when genuinely required to prevent a wrong architectural decision;
- otherwise make a reasonable assumption, label it, and continue.

It should not:

- act as a passive code generator;
- introduce a framework or backend merely because it is fashionable;
- turn the first release into an oversized enterprise system;
- place personal user data in a public repository;
- use the source HTML as a component template to be copied wholesale;
- encode equipment images as Base64 inside the production HTML;
- make the catalog the conceptual center of the new product;
- silently change the business meaning of entities or statuses.

---

# 3. Executive product summary

## 3.1. Original artifact

The starting artifact is a self-contained Ukrainian HTML catalog of POS equipment for pharmaceutical sales representatives. It contains:

- 151 equipment positions;
- 11 brands or product groups;
- 142 positions with images;
- 9 positions without source images;
- search by equipment metadata;
- navigation by brand;
- product cards with photo, name, article, brand, category, classification and equipment group;
- quantity controls;
- copying of individual articles;
- a temporary “My list” panel;
- a lightbox for enlarged images.

The artifact is approximately 4 MB and embeds all 142 images as Base64 data directly in one HTML file. It has a useful functional and visual foundation, but its architecture is intentionally monolithic.

## 3.2. Reframed product

The project should no longer be understood as “a better equipment catalog.”

The stronger product concept is:

> **A mobile-first, local-first field notebook and planning application that helps a sales representative select a pharmacy, record required work with POS equipment, and produce an actionable list for installation, replacement, servicing or ordering.**

The key product sequence is:

> **Pharmacy → Visit Plan → Equipment Task → Summary / Export**

The catalog remains important, but it becomes a picker and reference module inside the workflow rather than the home screen or the full product.

## 3.3. Core value proposition

The application replaces fragmented notes in a phone, paper notebook or messaging app with a structured, reusable workflow:

- identify the pharmacy;
- select the relevant equipment;
- state what must be done;
- add quantity and notes;
- preserve the plan for the next visit or ordering cycle;
- aggregate required equipment;
- export the result in a convenient format.

## 3.4. Working product name

Use **POS Equipment Planner** as the neutral working name until branding is deliberately revisited.

Possible alternatives:

- POS Planner;
- Field Equipment Notes;
- POS Visit Planner;
- Аптечний POS-планер;
- Планер обладнання;
- POS Notebook.

---

# 4. User and field context

## 4.1. Primary user

A pharmaceutical sales representative working with pharmacies and pharmacy networks.

## 4.2. Real-world environment

The user may work:

- from a smartphone;
- inside a pharmacy;
- while moving between visits;
- with intermittent or weak internet;
- under time pressure;
- while switching between notes, communication apps and reporting tools;
- with a large pharmacy list, potentially around 1,000 locations across multiple chains.

## 4.3. Existing behavior to improve

Notes are commonly captured in:

- the phone’s generic Notes application;
- a paper notebook;
- messages sent to oneself;
- an ad hoc spreadsheet;
- memory until the next order cycle.

The new product should reduce loss of context and reduce repeated manual rewriting.

## 4.4. Jobs to be done

When working with a pharmacy, the representative needs to:

1. find the pharmacy quickly;
2. see pending or previous work;
3. identify equipment visually or by article;
4. record a required action;
5. capture quantity and a contextual note;
6. keep the item attached to the correct pharmacy;
7. aggregate demand across pharmacies;
8. prepare a weekly equipment order or work plan;
9. copy, share or export the outcome.

---

# 5. Existing HTML project: factual snapshot

## 5.1. Document structure

The source document uses:

- `header` for brand, title, introduction and statistics;
- a sticky search bar;
- a two-column layout with brand navigation and catalog content;
- 11 `section` elements for brand groups;
- 151 `article` product cards;
- `footer` for source information;
- a lightbox layer;
- a floating list button and list panel.

## 5.2. Existing functionality worth preserving conceptually

- fast text search;
- brand-based discovery;
- image-led identification;
- article copying;
- quantity selection;
- temporary collection of items;
- enlarged image view;
- clear empty-image state;
- concise equipment metadata.

These functions should be reconsidered in the new task-centered workflow, not copied without adaptation.

## 5.3. Existing technical strengths

- semantic top-level HTML elements;
- CSS custom properties for primary colors and fonts;
- Grid and Flexbox layouts;
- `clamp()` for the main title;
- `aspect-ratio` for media frames;
- image lazy-loading declaration;
- `IntersectionObserver` for active brand navigation;
- delegated event handling for repeated controls;
- clipboard fallback;
- responsive behavior at 860 px;
- no duplicated element IDs found during inspection.

## 5.4. Existing limitations relevant to reconstruction

These are not the goal of the new project, but they explain why reconstruction is preferable to incremental patching:

- all content, styling, logic and images are held in one HTML file;
- 142 Base64 images account for most of the file size;
- the 151 card structures are repeated in markup;
- application data is not separated from presentation;
- the list exists only in memory and is lost on reload;
- lightbox and card opening are not fully keyboard-accessible;
- dynamic feedback is not announced to assistive technologies;
- mobile navigation is a wrapped desktop list rather than a purpose-built mobile pattern;
- there is only one responsive breakpoint;
- no formal build, validation or test pipeline is visible.

## 5.5. Previous evaluation scores

These scores describe the source artifact, not the future application:

- UI/UX: 8.0/10
- Frontend: 7.5/10
- Code Quality: 7.0/10
- Product Design: 8.0/10
- Performance: 6.5/10
- Accessibility: 5.0/10
- Maintainability: 6.0/10
- Overall product view: approximately 7.1/10

The source is a practical and attractive internal tool, but not yet a scalable application architecture.

---

# 6. Design System Snapshot from the source artifact

The future design must be built from zero. It may inherit the **visual DNA** described below, but should not duplicate the old page composition.

## 6.1. Design character to retain

- light, warm background;
- clean white surfaces;
- graphite rather than pure black text;
- confident pink accents;
- very pale pink media surfaces and interaction states;
- thin warm gray-pink borders;
- displayed equipment images without cropping;
- moderate rounded corners;
- technical monospace treatment for articles and counts;
- short, calm motion;
- depth used only where interaction or layering requires it;
- subtle branded glow rather than heavy decoration.

## 6.2. Color tokens

```css
:root {
  --color-brand-primary: #ff1b6b;
  --color-brand-deep: #c10057;
  --color-brand-highlight: #ff6fa5;

  --color-brand-tint: #ffe3ec;
  --color-brand-tint-soft: #fff0f5;
  --color-brand-border-hover: #ffc4dc;
  --color-brand-active-muted: #ffd8e7;
  --color-brand-muted: #b98a9c;

  --color-text-primary: #241e24;
  --color-text-secondary: #726b74;
  --color-text-inverse: #ffffff;

  --color-background-page: #fbfafb;
  --color-background-surface: #ffffff;
  --color-background-media: #fff0f5;

  --color-border-subtle: #efe7ea;
  --color-border-strong: #e3d9de;

  --color-success: #3fa66a;

  --color-overlay-modal: rgba(36, 30, 36, 0.72);
  --color-overlay-clear: rgba(36, 30, 36, 0);
  --color-surface-sticky: rgba(255, 255, 255, 0.933);
  --color-surface-on-brand: rgba(255, 255, 255, 0.20);
}
```

### Exact color references

- Primary: `#FF1B6B`, RGB `255, 27, 107`, HSL `339, 100%, 55%`.
- Deep primary: `#C10057`, RGB `193, 0, 87`, HSL `333, 100%, 38%`.
- Primary tint: `#FFE3EC`, RGB `255, 227, 236`, HSL `341, 100%, 95%`.
- Soft primary tint: `#FFF0F5`, RGB `255, 240, 245`, HSL `340, 100%, 97%`.
- Graphite: `#241E24`, RGB `36, 30, 36`, HSL `300, 9%, 13%`.
- Secondary text: `#726B74`, RGB `114, 107, 116`, HSL `287, 4%, 44%`.
- Page background: `#FBFAFB`, RGB `251, 250, 251`, HSL `300, 11%, 98%`.
- Subtle border: `#EFE7EA`, RGB `239, 231, 234`, HSL `338, 20%, 92%`.
- Strong border: `#E3D9DE`, RGB `227, 217, 222`, HSL `330, 15%, 87%`.
- Success: `#3FA66A`, RGB `63, 166, 106`, HSL `145, 45%, 45%`.

Warning, error and disabled colors were not defined in the original artifact. The new design system may add them only when actual product states require them.

## 6.3. Background system

- Main page: `#FBFAFB`.
- Primary surface: `#FFFFFF`.
- Equipment media surface: `#FFF0F5`.
- Sticky glass surface: approximately 93.3% white plus `backdrop-filter: blur(6px)`.
- Modal scrim: `rgba(36, 30, 36, 0.72)` plus `blur(3px)`.
- Header ambient glow: 320 px radial pink gradient, element opacity 16%, partially placed outside the top-right boundary.
- Image action overlay: graphite gradient from 72% opacity to transparent.

## 6.4. Shadow and glow tokens

```css
:root {
  --shadow-focus: 0 0 0 3px #ffe3ec;
  --shadow-card-hover: 0 10px 24px rgba(255, 27, 107, 0.16);
  --shadow-control: 0 2px 8px rgba(0, 0, 0, 0.18);
  --shadow-fab: 0 8px 22px rgba(0, 0, 0, 0.28);
  --shadow-panel: 0 16px 40px rgba(0, 0, 0, 0.28);
  --shadow-modal: 0 30px 70px rgba(0, 0, 0, 0.35);
}
```

Elevation logic:

- base cards are flat;
- card hover introduces a pink-tinted lift;
- small floating controls use a small black shadow;
- FAB and floating panel use progressively stronger depth;
- the modal owns the strongest elevation.

## 6.5. Radius tokens

```css
:root {
  --radius-data: 4px;
  --radius-xs: 6px;
  --radius-sm: 7px;
  --radius-control: 8px;
  --radius-input: 9px;
  --radius-card: 12px;
  --radius-panel: 14px;
  --radius-modal: 16px;
  --radius-pill: 30px;
  --radius-circle: 50%;
}
```

Usage logic:

- 4–6 px for micro elements;
- 7–9 px for controls;
- 12 px for cards;
- 14–16 px for elevated surfaces;
- pill and circular values for special actions.

## 6.6. Typography

### Families

```css
:root {
  --font-display: "Poppins", "Inter", sans-serif;
  --font-body: "Inter", "Segoe UI", system-ui, -apple-system, sans-serif;
  --font-data: "SF Mono", "Consolas", monospace;
}
```

### Roles

- **Poppins:** logo, major headings, card titles, prominent numeric values.
- **Inter:** body, controls, search, navigation and general application interface.
- **Monospace:** articles, counts, quantities, technical tags and compact data labels.

### Important observed sizes

- H1: `clamp(22px, 3.4vw, 32px)`, weight 700, tracking `-0.01em`.
- H2: 21 px, weight 700.
- Card title: 15.5 px, weight 600.
- Lead: 14.5 px, body font, secondary text.
- Logo word: 22 px, weight 800, tracking `-0.02em`.
- Statistics number: 23 px, weight 700.
- Navigation item: 13.5 px.
- Metadata field: 12.5 px.
- Most data captions: 11–12.5 px monospace.
- Global line-height: 1.5, with compact 1.4 and relaxed 1.6 variants.

The new application should retain the three-font-role logic, while reassessing very small text for mobile field use.

## 6.7. Spacing system

The source follows a practical 2/4 px rhythm, centered on 8, 12, 16, 24 and 28 px.

```css
:root {
  --space-0: 0;
  --space-0-5: 2px;
  --space-1: 4px;
  --space-1-5: 6px;
  --space-2: 8px;
  --space-2-5: 10px;
  --space-3: 12px;
  --space-3-5: 14px;
  --space-4: 16px;
  --space-4-5: 18px;
  --space-5: 20px;
  --space-5-5: 22px;
  --space-6: 24px;
  --space-6-5: 26px;
  --space-7: 28px;
  --space-10: 40px;
  --space-section: 46px;
}
```

Logic:

- 2–4 px: micro alignment;
- 6–10 px: inline relationships and small controls;
- 12–18 px: component internals;
- 20–28 px: page-level padding and large components;
- 40–46 px: section separation;
- 70–90 px: sticky offsets and floating-action clearance.

## 6.8. Border system

- Structural: `1px solid #EFE7EA`.
- Interactive: `1px solid #E3D9DE`.
- Search input: `1.5px solid #E3D9DE`.
- Brand section divider: `2px solid #FF1B6B`.
- Statistics accent: `3px solid #FF1B6B` on the left.
- Control separator: `1px dashed #E3D9DE`.

## 6.9. Motion tokens

```css
:root {
  --duration-fast: 120ms;
  --duration-standard: 150ms;
  --duration-modal: 180ms;
  --easing-standard: ease;
  --motion-card-lift: -3px;
  --motion-fab-lift: -2px;
  --motion-panel-offset: 8px;
  --motion-modal-scale-closed: 0.96;
  --motion-success-scale: 1.05;
}
```

The motion language is short and functional. Do not introduce long spring, bounce or ornamental animation without a product reason.

## 6.10. Visual hierarchy

The source hierarchy moves attention through:

1. branded header;
2. large dark title;
3. explanatory text;
4. statistics;
5. sticky search;
6. active brand state;
7. product image;
8. product title;
9. article badge;
10. task controls;
11. floating list action.

In the new application, this hierarchy must change to prioritize:

1. current pharmacy context;
2. pending tasks;
3. primary “add task” action;
4. equipment selection;
5. action, quantity and note;
6. summary and export.

---

# 7. Product principles for the reconstruction

## 7.1. Pharmacy-centered, not catalog-centered

Every important work item must belong to a pharmacy. Equipment is selected inside that context.

## 7.2. Local-first

Core workflows must work with unreliable connectivity. Local state is a first-class product requirement, not a technical afterthought.

## 7.3. Mobile-first

The primary design target is a smartphone used during a visit. Desktop is an enhanced layout, not the source of truth.

## 7.4. Structured notes with low friction

The application should be as quick as a notes app, while adding just enough structure to support aggregation and export.

## 7.5. Progressive disclosure

Do not show all pharmacies, all brands and all equipment at once. Reveal depth through search, filters, recents, favorites, collapsed groups and focused pickers.

## 7.6. One source of truth for data

Pharmacies, equipment, actions and plans must be modeled separately. UI labels, counts and exports should be derived from data, not duplicated manually.

## 7.7. Clear ownership of data

- reference data belongs to the application package;
- personal plans belong to the user’s local data store or future account;
- generated export files are outputs, not source data.

## 7.8. Reversible decisions

For MVP, prefer decisions that allow later migration:

- static JSON can later come from an API;
- IndexedDB repositories can later gain cloud synchronization;
- component APIs can survive visual redesign;
- exports can grow without changing the core domain model.

---

# 8. Domain model

## 8.1. Pharmacy

Represents a pharmacy or trade outlet.

```ts
export interface Pharmacy {
  id: string;
  name: string;
  chain: string;
  address: string;
  city: string;
  externalCode?: string;
  status: 'active' | 'inactive';
  isFavorite?: boolean;
}
```

Required conceptual fields:

- stable internal ID;
- display name;
- chain;
- address;
- city;
- optional external business code;
- status.

## 8.2. Equipment

Reference catalog item.

```ts
export interface Equipment {
  id: string;
  name: string;
  article: string;
  brand: string;
  category?: string;
  classification?: string;
  group?: string;
  imageThumbnail?: string;
  imageFull?: string;
  status: 'active' | 'inactive' | 'deprecated';
}
```

Important rules:

- `id` must remain stable even if display text changes;
- `article` is a business field, not necessarily the database key;
- no-photo is a valid state;
- inactive equipment should remain resolvable for history.

## 8.3. WorkAction

A controlled vocabulary for work required with equipment.

Initial options:

```ts
export type WorkAction =
  | 'install'
  | 'replace'
  | 'remove'
  | 'repair'
  | 'rebrand'
  | 'inspect'
  | 'order'
  | 'relocate'
  | 'other';
```

Ukrainian labels:

- install: Встановити;
- replace: Замінити;
- remove: Демонтувати;
- repair: Відремонтувати;
- rebrand: Переклеїти / оновити POSM;
- inspect: Перевірити;
- order: Замовити;
- relocate: Перемістити;
- other: Інше.

The exact final vocabulary must be validated with the user before implementation is frozen.

## 8.4. EquipmentTask

The central work entity.

```ts
export interface EquipmentTask {
  id: string;
  pharmacyId: string;
  equipmentId: string;
  action: WorkAction;
  quantity: number;
  priority: 'low' | 'normal' | 'high';
  status: 'draft' | 'planned' | 'ordered' | 'completed' | 'cancelled';
  note?: string;
  plannedWeek?: string;
  createdAt: string;
  updatedAt: string;
}
```

Business meaning:

> In this pharmacy, this quantity of this equipment requires this action.

## 8.5. VisitPlan

Groups tasks around a pharmacy and a planned visit or work period.

```ts
export interface VisitPlan {
  id: string;
  pharmacyId: string;
  visitDate?: string;
  plannedWeek?: string;
  status: 'draft' | 'planned' | 'completed' | 'cancelled';
  generalNote?: string;
  taskIds: string[];
  createdAt: string;
  updatedAt: string;
}
```

An early validation question is whether the business truly needs both `VisitPlan` and `EquipmentTask.plannedWeek` in MVP. Avoid redundant scheduling fields unless user workflows require them.

## 8.6. Export profile

Exports are derived views, not database entities. Useful profiles:

- human-readable note;
- order list aggregated by article;
- report grouped by pharmacy;
- report grouped by brand;
- CSV table;
- Excel workbook;
- backup JSON.

---

# 9. Core user flows

## 9.1. Create a pharmacy plan

1. Open the application.
2. Search or select a recent pharmacy.
3. Open the pharmacy workspace.
4. Review unfinished work.
5. Tap “Add equipment task.”
6. Find equipment through search, brand filter, recents or photo mode.
7. Select the equipment.
8. Choose the work action.
9. Set quantity.
10. Add a note if needed.
11. Save the task.
12. Repeat for other equipment.
13. Review the pharmacy plan.
14. Copy or export when ready.

## 9.2. Produce an order summary

1. Open Summary.
2. Select the relevant week or plan set.
3. Group by article.
4. Review total quantity.
5. Optionally inspect contributing pharmacies.
6. Copy, export CSV or generate Excel.

## 9.3. Continue work from a previous visit

1. Find the pharmacy.
2. View unfinished tasks and history.
3. Edit status, quantity or note.
4. Reschedule or complete the task.
5. Preserve the audit context.

## 9.4. Identify unknown equipment visually

1. Open the catalog picker.
2. Choose photo mode.
3. Filter by brand if known.
4. View thumbnail grid.
5. Open a full image if needed.
6. Select and add to the current pharmacy plan.

---

# 10. Information architecture

## 10.1. Recommended mobile navigation

Primary bottom navigation:

```text
Аптеки | Плани | Каталог | Зведення
```

Optional fifth destination later:

```text
Ще
```

### Аптеки

- search;
- recent pharmacies;
- favorite pharmacies;
- pharmacy chains;
- full list;
- current route or selected subset later.

### Плани

- drafts;
- planned;
- current week;
- pending order;
- completed;
- archived.

### Каталог

- equipment search;
- recents;
- favorites;
- brand groups;
- list/photo view;
- equipment details.

### Зведення

- counts;
- article aggregation;
- pharmacy grouping;
- brand grouping;
- exports.

## 10.2. Desktop adaptation

Desktop may use:

- a left navigation rail;
- a top app bar;
- a central workspace;
- an optional contextual panel on the right.

Do not let the desktop shell redefine the mobile information architecture.

## 10.3. Catalog disclosure strategy

Do not render the catalog as 151 full cards by default.

Use a layered discovery model:

1. recent equipment;
2. frequently used equipment;
3. favorites;
4. prominent search;
5. horizontal brand chips;
6. collapsed brand groups;
7. compact list/photo toggle;
8. render only the current group or visible search results;
9. lazy-load full-size images only when details are opened.

Accordion groups may be part of the solution, but they should not replace search and recents.

---

# 11. Proposed screens

## 11.1. Pharmacies home

Content priority:

1. app title or compact app bar;
2. search by pharmacy name, chain, code or address;
3. current-week summary;
4. recent pharmacies;
5. favorites or current route;
6. bottom navigation.

## 11.2. Pharmacy workspace

Header:

- pharmacy name;
- chain;
- address;
- relevant code;
- optional status.

Main content:

- prominent “Add task” action;
- unfinished tasks;
- planned tasks;
- completed or historical tasks in a secondary section;
- general note;
- export/share for this pharmacy.

## 11.3. Equipment picker

- search field;
- filters and brand chips;
- recent and frequent section;
- list/photo mode toggle;
- collapsed brand groups;
- compact selection affordance;
- full image details on demand.

## 11.4. Task editor

- equipment summary and thumbnail;
- action selector;
- quantity stepper;
- priority if confirmed useful;
- status or planned week if confirmed useful;
- note field;
- save action;
- cancel/back without losing accidental changes.

## 11.5. Plans screen

- week selector or grouped date sections;
- status filters;
- pharmacy cards with task counts;
- clear draft/planned/completed distinction;
- ability to reopen a plan.

## 11.6. Summary screen

- number of pharmacies;
- number of distinct equipment positions;
- total units;
- grouping selector;
- detailed aggregation;
- copy/export actions.

---

# 12. Image and asset architecture

## 12.1. Images must be separate assets

Do not place images inside HTML or JSON as Base64.

Recommended structure:

```text
public/
└── assets/
    └── equipment/
        ├── durex/
        │   ├── 2522012-thumb.webp
        │   └── 2522012-full.webp
        ├── nurofen/
        ├── strepsils/
        └── shared/
```

## 12.2. Data references

```json
{
  "imageThumbnail": "/assets/equipment/durex/2522012-thumb.webp",
  "imageFull": "/assets/equipment/durex/2522012-full.webp"
}
```

## 12.3. Derivative strategy

### Thumbnail

- WebP or AVIF;
- approximately 320–480 px on the longest side;
- optimized for cards and lists;
- small file weight;
- loaded lazily.

### Full image

- approximately 900–1200 px on the longest side;
- loaded only in detail/lightbox view;
- `object-fit: contain`;
- no cropping of equipment.

## 12.4. Missing image state

The absence of an image is valid data. Use a designed placeholder and do not substitute an unrelated image.

## 12.5. Possible image pipeline

A build/import script should eventually:

1. extract or ingest source images;
2. normalize orientation;
3. remove exact duplicates when business-safe;
4. create thumbnail and full derivatives;
5. assign deterministic filenames based on stable equipment ID or article;
6. emit image dimensions and paths into catalog data;
7. report missing and failed images.

---

# 13. Recommended technical architecture

## 13.1. Recommended stack

Primary recommendation:

```text
Vite
React
TypeScript
Token-based CSS, preferably CSS Modules or disciplined global layers
IndexedDB through Dexie
Zod for imported data validation
Vitest for unit tests
Playwright for end-to-end flows
SheetJS only when Excel export is introduced
```

Potential lightweight state management:

- start with React state and repositories;
- add Zustand only when shared state becomes sufficiently complex;
- do not introduce Redux by default.

## 13.2. Why React and TypeScript are recommended

The new product has multiple interacting state domains:

- selected pharmacy;
- active visit plan;
- catalog search and filters;
- equipment picker state;
- task editor drafts;
- persisted plans;
- summary aggregation;
- exports;
- offline state;
- future synchronization.

A component architecture and typed domain model reduce accidental coupling as the product grows.

## 13.3. Acceptable alternative

A modular Vanilla JavaScript application is acceptable for a very small proof of concept, but must still separate:

- domain data;
- page rendering;
- state;
- storage repositories;
- services;
- components;
- styles;
- assets.

Do not recreate a single-file monolith even in the vanilla option.

## 13.4. Proposed source structure

```text
pos-equipment-planner/
├── src/
│   ├── app/
│   │   ├── App.tsx
│   │   ├── routes.tsx
│   │   └── providers/
│   │
│   ├── pages/
│   │   ├── PharmaciesPage/
│   │   ├── PharmacyDetailsPage/
│   │   ├── PlansPage/
│   │   ├── PlanEditorPage/
│   │   ├── EquipmentCatalogPage/
│   │   └── SummaryPage/
│   │
│   ├── features/
│   │   ├── pharmacy-search/
│   │   ├── equipment-picker/
│   │   ├── task-editor/
│   │   ├── plan-builder/
│   │   ├── export-plan/
│   │   └── image-viewer/
│   │
│   ├── entities/
│   │   ├── pharmacy/
│   │   ├── equipment/
│   │   ├── task/
│   │   └── visit-plan/
│   │
│   ├── components/
│   │   ├── AppBar/
│   │   ├── BottomNavigation/
│   │   ├── SearchField/
│   │   ├── FilterChips/
│   │   ├── EquipmentCard/
│   │   ├── EquipmentListItem/
│   │   ├── PharmacyCard/
│   │   ├── TaskCard/
│   │   ├── ActionSheet/
│   │   ├── Modal/
│   │   └── EmptyState/
│   │
│   ├── design-system/
│   │   ├── tokens.css
│   │   ├── typography.css
│   │   ├── foundations.css
│   │   └── components/
│   │
│   ├── data/
│   │   ├── equipment.json
│   │   ├── pharmacies.json
│   │   └── action-types.json
│   │
│   ├── storage/
│   │   ├── database.ts
│   │   ├── planRepository.ts
│   │   └── migrations.ts
│   │
│   ├── services/
│   │   ├── exportText.ts
│   │   ├── exportCsv.ts
│   │   ├── exportExcel.ts
│   │   └── backup.ts
│   │
│   ├── utils/
│   │   ├── search.ts
│   │   ├── dates.ts
│   │   └── ids.ts
│   │
│   └── main.tsx
│
├── public/
│   ├── assets/equipment/
│   ├── icons/
│   └── manifest.webmanifest
│
├── scripts/
│   ├── import-equipment/
│   ├── import-pharmacies/
│   └── optimize-images/
│
├── tests/
├── package.json
├── vite.config.ts
├── README.md
└── docs/
```

This is a target structure, not a command to create every directory on day one.

---

# 14. Data architecture

## 14.1. Reference data

Reference data is packaged with the application:

- `equipment.json`;
- `pharmacies.json`;
- `action-types.json` if actions are configuration-driven.

It must be generated or validated through scripts, not manually duplicated across screens.

## 14.2. User data

User-created data belongs in IndexedDB:

- plans;
- tasks;
- favorites;
- recent pharmacies;
- recent equipment;
- user preferences;
- export metadata if needed.

## 14.3. Repository boundary

UI components should not call IndexedDB directly. Use repository interfaces such as:

```ts
export interface PlanRepository {
  getById(id: string): Promise<VisitPlan | undefined>;
  listByPharmacy(pharmacyId: string): Promise<VisitPlan[]>;
  save(plan: VisitPlan): Promise<void>;
  delete(id: string): Promise<void>;
}
```

This boundary makes future cloud synchronization easier.

## 14.4. Versioning and migrations

IndexedDB schema must have explicit versions from the first release. Migration logic should be tested before field deployment.

## 14.5. Backup

MVP should include JSON backup export and import before relying on the app for long-term records.

Backup payload should include:

- schema version;
- export date;
- app version;
- plans;
- tasks;
- favorites and preferences only if useful.

Reference equipment images do not need to be included in personal backups.

---

# 15. Local-first and offline strategy

## 15.1. Offline-capable core

The following must work offline after the application has been loaded or installed:

- browse pharmacies;
- search equipment;
- open equipment thumbnails already cached as part of the app strategy;
- create and edit plans;
- save notes;
- generate a text summary;
- generate CSV if browser APIs allow;
- view previously saved data.

## 15.2. PWA direction

The application should later include:

- web app manifest;
- installable icons;
- service worker;
- application shell caching;
- version-aware update messaging;
- offline fallback;
- careful cache invalidation for catalog data and images.

Do not implement aggressive caching before data versioning and update behavior are designed.

## 15.3. Data-loss warning

Local-only data may be lost if browser storage is cleared or the device is changed. Product communication and backup tools must make this explicit.

## 15.4. Maturity path

1. local IndexedDB plus manual backup;
2. improved backup and restore;
3. optional user account and encrypted cloud sync;
4. organizational backend and shared workflows if validated.

---

# 16. Export architecture

## 16.1. Human-readable note

Example:

```text
Аптека 911
вул. Центральна, 25

1. DurexTower
   Артикул: 2522012
   Кількість: 1
   Дія: Замінити
   Примітка: Старе обладнання пошкоджене
```

## 16.2. Order aggregation

Group identical equipment by article:

```text
2522012 — DurexTower — 5 шт.
2712045 — NurofenTray6 — 8 шт.
```

The user should be able to inspect which pharmacies contribute to each total.

## 16.3. CSV

Recommended columns:

```text
Week
Created date
Chain
Pharmacy
Address
Pharmacy code
Brand
Equipment name
Article
Action
Quantity
Task status
Note
```

The actual labels should be Ukrainian in the user-facing export.

## 16.4. Excel

Excel is a later MVP or second-stage export. Possible sheets:

- `Зведення за артикулами`;
- `У розрізі аптек`;
- `Усі завдання`;
- `Довідники` only if specifically useful.

## 16.5. Technical backup

JSON backup is separate from business export. It should preserve IDs and relationships, not only display text.

## 16.6. Screenshot or PDF

This is optional. A print-friendly summary may be more maintainable than programmatically generating snapshots in the first release.

---

# 17. Hosting and deployment model

## 17.1. Roles of services

### GitHub

Use for:

- source control;
- issue and decision history;
- pull requests;
- versioned data and scripts;
- collaboration;
- triggering deployment.

### Cloudflare Pages

Use as the recommended production host for the static frontend build.

Recommended flow:

```text
Local development
  → git push
GitHub repository
  → automated build
Cloudflare Pages
  → production or preview URL
```

GitHub Pages may be used for an early demonstration, but running two identical production hosts is unnecessary.

## 17.2. Build output

Source files are not what the end user handles. A build creates deployable assets:

```text
dist/
├── index.html
├── assets/
│   ├── app.[hash].js
│   ├── app.[hash].css
│   └── equipment/
└── manifest.webmanifest
```

Typical Vite concept:

```text
Build command: npm run build
Output directory: dist
```

## 17.3. Branch strategy

A simple approach:

```text
main        production
feature/*   isolated work and preview
```

Add `develop` only if concurrent work actually requires it.

## 17.4. Privacy boundary

Never commit user-created pharmacy notes or personal plans to the public/static repository. Only sanitized reference data belongs in the deployed package.

## 17.5. Future backend trigger

A backend becomes justified when one or more of the following is required:

- synchronization across devices;
- shared plans among users;
- manager visibility;
- centrally managed user accounts;
- audit trails across users;
- server-side data protection or policy controls.

---

# 18. Accessibility and quality baseline for the new build

The source artifact’s accessibility issues should not be carried forward.

## 18.1. Required baseline

- semantic headings and landmarks;
- all interactive actions implemented as native controls;
- complete keyboard access;
- visible `:focus-visible` states;
- labels for search, quantity and form fields;
- modal focus management;
- screen-reader status messages for save, copy and export;
- minimum comfortable mobile touch targets, ideally around 44 px;
- sufficient color contrast;
- support for 200% text zoom;
- `prefers-reduced-motion` handling;
- meaningful empty, error, loading and offline states;
- no essential action dependent on hover;
- accessible charts or summaries if introduced.

## 18.2. Testing baseline

- unit tests for aggregation and search;
- repository/storage tests;
- import validation tests;
- Playwright test for the primary pharmacy-plan flow;
- keyboard navigation test;
- automated accessibility check;
- mobile visual regression for core screens;
- backup export/import round-trip test.

---

# 19. MVP scope

## 19.1. Must have

- pharmacy reference list;
- pharmacy search;
- pharmacy workspace;
- equipment catalog from source data;
- equipment search by name and article;
- brand filtering;
- equipment thumbnail and no-photo state;
- equipment selection within a pharmacy plan;
- work action selection;
- quantity;
- note;
- create, edit and remove task;
- local persistence in IndexedDB;
- summary by article;
- summary by pharmacy;
- copy as text;
- CSV export;
- JSON backup and restore;
- mobile-first responsive UI;
- basic offline-capable application shell.

## 19.2. Should have soon after MVP

- recent equipment;
- favorite pharmacies and equipment;
- weekly plan filtering;
- task statuses;
- history for a pharmacy;
- Excel export;
- installable PWA experience;
- clear data-version and app-version display.

## 19.3. Not required for first release

- user authentication;
- cloud backend;
- multi-user collaboration;
- manager dashboard;
- GPS routing;
- geolocation requirements;
- push notifications;
- user photo uploads;
- complex permissions;
- automated email sending;
- full BI analytics;
- excessive animation.

---

# 20. Phased roadmap

## Phase 0. Product validation and data preparation

Deliverables:

- confirm work action vocabulary;
- confirm the real pharmacy file and field names;
- confirm whether plans are visit-based, week-based or both;
- define task statuses;
- define export expectations;
- extract and normalize equipment data;
- extract and optimize images;
- create data schemas;
- create a clickable low-fidelity flow.

Exit criteria:

- the user can explain the complete workflow in one sequence;
- no unresolved contradiction remains in the domain model;
- 100% of equipment records pass validation or appear in an exception report.

## Phase 1. Functional prototype

Deliverables:

- mobile app shell;
- pharmacy search;
- pharmacy workspace;
- equipment picker;
- task editor;
- in-memory plan;
- text summary;
- visual design direction.

Exit criteria:

- the complete happy path works without persistence;
- the user validates that the interaction is faster than generic Notes.

## Phase 2. Local-first MVP

Deliverables:

- IndexedDB repositories;
- task and plan persistence;
- summary aggregation;
- CSV export;
- JSON backup/restore;
- core tests;
- Cloudflare Pages deployment;
- responsive and accessibility baseline.

Exit criteria:

- reload does not lose work;
- backup restores equivalent data;
- core workflow works on a smartphone;
- no blocking accessibility issue remains in the primary flow.

## Phase 3. PWA and operational hardening

Deliverables:

- installable manifest;
- service worker;
- offline shell;
- version/update strategy;
- favorites and recents;
- history and weekly views;
- Excel export;
- robust imports and migrations.

## Phase 4. Cloud evolution, only if validated

Possible deliverables:

- authentication;
- secure sync;
- organizational data source;
- manager view;
- shared order preparation;
- multi-user audit trail.

---

# 21. Immediate decisions still required

The next agent should treat these as discovery questions, not make silent assumptions.

## 21.1. Pharmacy data

- What is the exact source format?
- Which field is the stable pharmacy ID?
- Are network, city and address standardized?
- Must the application include all pharmacies or only the representative’s territory?
- How frequently does the list change?

## 21.2. Work model

- Is a plan tied to a physical visit, a calendar week, an order cycle or all three?
- Can the same equipment have two actions in one pharmacy?
- Does “replace” imply both a new unit and removal of an old unit?
- Is “order” a task action or the result of aggregating install/replace tasks?
- Are quantities always whole positive numbers?

## 21.3. Status model

- Which statuses are actually used in work?
- Must completed tasks remain visible?
- Is there a difference between planned, ordered, delivered and installed?

## 21.4. Notes and history

- Are notes temporary or historical records?
- Must edits preserve previous values?
- Is a general pharmacy note required in addition to task notes?

## 21.5. Export

- What exact spreadsheet format is needed for weekly equipment ordering?
- Is one row per task expected, or one row per article after aggregation?
- Which columns are mandatory?
- Does the recipient require `.xlsx`, or is CSV sufficient initially?

## 21.6. Device and privacy

- Is the application used only on a personal phone?
- Is browser storage acceptable under company policy?
- May the reference pharmacy list be deployed to a public static site?
- Should access be restricted even before a backend exists?

---

# 22. Decision log

## Accepted direction

- Build a new application from zero.
- Reuse only selected design DNA and reference data from the old catalog.
- Center the product on pharmacies and work tasks.
- Use equipment catalog as a picker/reference module.
- Design mobile-first.
- Prefer a local-first architecture for MVP.
- Separate HTML/application logic, CSS/design system, data and images.
- Store images as separate optimized files.
- Keep source code in GitHub.
- Prefer Cloudflare Pages for production deployment.
- Recommend Vite + React + TypeScript.
- Use IndexedDB for user-created plans.
- Start with text and CSV exports; add Excel after the structure is validated.
- Preserve the light, warm, pink-accented visual language without copying the old layout.

## Proposed but not yet confirmed

- Exact application name.
- Final action vocabulary.
- Final status vocabulary.
- Whether `VisitPlan` is necessary in addition to weekly tasks.
- Whether priority belongs in MVP.
- Exact Excel template.
- Whether PWA installation belongs in MVP or the next phase.
- Whether access control is required for first deployment.

## Explicitly deferred

- authentication;
- cloud synchronization;
- manager reporting;
- multi-user collaboration;
- geolocation and routing;
- user-uploaded photos;
- push notifications.

---

# 23. Risks and mitigations

## Risk: rebuilding the old catalog instead of the new product

**Mitigation:** every feature proposal must be mapped to the pharmacy-centered workflow.

## Risk: too many fields make the app slower than Notes

**Mitigation:** default to action, quantity and optional note. Reveal advanced fields only when validated.

## Risk: local data loss

**Mitigation:** IndexedDB, backup/restore, clear local-data notice, tested migrations.

## Risk: public exposure of pharmacy reference data

**Mitigation:** confirm policy before deployment. Use only an approved subset or introduce access control if needed.

## Risk: weak equipment data quality

**Mitigation:** schema validation, unique-ID checks, missing-image reports, import exception logs.

## Risk: images make the app heavy

**Mitigation:** thumbnail/full derivatives, WebP or AVIF, lazy loading, focused rendering, separate caching.

## Risk: architecture becomes excessive before validation

**Mitigation:** phase delivery, repository abstractions without premature backend, no unnecessary state library.

## Risk: weekly export does not fit the real ordering process

**Mitigation:** obtain a real example of the expected output before implementing Excel.

## Risk: mobile interaction is designed from desktop assumptions

**Mitigation:** prototype and test the main flow at phone width first.

---

# 24. Definition of Done for the first usable release

The release is usable when a representative can:

1. open the app on a smartphone;
2. find a pharmacy;
3. create or open a plan;
4. find equipment by name, article or brand;
5. identify it using a thumbnail or enlarged image;
6. select an action;
7. set quantity;
8. add a note;
9. save the task;
10. reload the browser without losing it;
11. see the task under the correct pharmacy;
12. aggregate equipment across pharmacies;
13. copy a readable summary;
14. export CSV;
15. create a backup and restore it;
16. perform the core flow with keyboard and touch;
17. use the application in a weak-connectivity scenario after initial loading.

---

# 25. Recommended first work package for the next agent

The next agent should not begin by styling the whole application. It should produce the following in order.

## Package 1: Product clarification artifact

- final terminology glossary;
- confirmed domain entities;
- action and status vocabularies;
- one primary flow;
- one weekly summary flow;
- unresolved questions.

## Package 2: Data contract

- `equipment.schema.json` or Zod schema;
- `pharmacy.schema.json` or Zod schema;
- TypeScript interfaces;
- sample records;
- import validation report specification.

## Package 3: Information architecture and wireframes

At minimum:

- Pharmacies home;
- Pharmacy workspace;
- Equipment picker;
- Task editor;
- Plans;
- Summary;
- mobile navigation.

## Package 4: Technical skeleton

- Vite + React + TypeScript project;
- design-token layers;
- routing;
- repository interfaces;
- static sample data;
- one implemented vertical slice.

## Package 5: Vertical slice

Implement only:

```text
Select pharmacy
→ add equipment
→ select action and quantity
→ save task locally
→ see summary
```

This slice should prove the architecture before broadening the screen set.

---

# 26. Starter brief for the next AI partner

Use the following as the operational prompt if the handoff must be condensed:

> You are joining POS Equipment Planner as a product, UX and engineering partner. Your task is to help create a mobile-first, local-first field application for a pharmaceutical sales representative. The representative must be able to select a pharmacy, create structured tasks involving POS equipment, choose what must be done, set quantity and notes, and produce a summary for future installation, replacement or ordering.
>
> The core domain sequence is Pharmacy → Visit Plan → Equipment Task → Equipment. The catalog is a picker and reference module, not the center of the product. Build a new application from zero. Reuse the source artifact only for equipment data, images, selected interaction ideas and visual DNA.
>
> Preserve a light, warm interface with white surfaces, graphite text, a strong pink accent, pale pink equipment backgrounds, thin borders, soft radii, restrained branded glow and monospace styling for articles. Do not copy the old page layout.
>
> The recommended architecture is Vite + React + TypeScript, static validated JSON for equipment and pharmacy reference data, separate optimized WebP/AVIF image assets, IndexedDB for user plans, text and CSV exports first, and Cloudflare Pages deployment from GitHub. The MVP must remain usable with weak connectivity and must include backup/restore before field reliance.
>
> Work as a partner. Challenge assumptions, explain trade-offs, keep a decision log, separate confirmed decisions from proposals, and protect the product from unnecessary complexity. Start by validating terminology, domain rules and the expected weekly export, then create the data contract, mobile information architecture and one end-to-end vertical slice.

---

# 27. Three-layer handoff audit

This section audits the document itself before transfer.

## Layer 1: Context and completeness audit

### Goal

Verify that the handoff preserves every major category of the prior work.

### Coverage check

- Existing source artifact and factual scale: included.
- Existing frontend and UX observations: included.
- Design-system colors, typography, spacing, radii, borders, shadows, glow and motion: included.
- Decision not to copy the old design composition: included.
- Product reframing from catalog to field notebook/planner: included.
- Primary user and real field scenario: included.
- Pharmacy-centered workflow: included.
- Domain entities and relationships: included.
- Work action examples: included.
- Pharmacy, equipment, task and plan data examples: included.
- Mobile navigation concept: included.
- Strategy for avoiding 151 simultaneously expanded cards: included.
- Separate image storage and thumbnail/full variants: included.
- Professional source/build separation: included.
- React/TypeScript recommendation and vanilla alternative: included.
- IndexedDB/local-first direction: included.
- Backup limitation and migration path: included.
- GitHub and Cloudflare Pages roles: included.
- Export formats: included.
- MVP and deferred scope: included.
- Phased roadmap: included.
- Partner behavior expected from the next agent: included.
- Open questions and unresolved decisions: included.
- Risks, mitigations and Definition of Done: included.

### Layer 1 result

**PASS.** No major topic from the discovery, audit, design snapshot or architecture discussion is omitted.

## Layer 2: Internal consistency audit

### Goal

Verify that recommendations do not contradict one another.

### Checks

1. **Product center:** all major flows begin with the pharmacy context. The catalog is consistently described as subordinate.
2. **Hosting:** GitHub stores source; Cloudflare Pages is recommended for production. No double-production-host requirement remains.
3. **Data ownership:** static reference data and personal local data are consistently separated.
4. **Offline model:** IndexedDB, backup and later sync form a coherent maturity path.
5. **Images:** separate assets, thumbnails and full-size files are consistently recommended.
6. **Framework:** React + TypeScript is a recommendation, not an absolute constraint. A modular vanilla alternative remains possible for a proof of concept.
7. **MVP discipline:** auth, shared backend and manager features are consistently deferred.
8. **Design reuse:** token-level and language-level inheritance is allowed; old composition and monolithic markup are not.
9. **Entity model:** tasks reference pharmacies and equipment through IDs. Exports remain derived output.
10. **Visit/week ambiguity:** explicitly identified as unresolved rather than silently encoded as a final decision.
11. **Ordering ambiguity:** explicitly identified for validation because “order” may be an action or derived business result.
12. **Accessibility:** new build baseline corrects the source issues rather than encoding them as design requirements.

### Layer 2 result

**PASS WITH OPEN DECISIONS.** The architecture is internally coherent. The remaining ambiguities are visible and must be resolved during Phase 0.

## Layer 3: Operational readiness audit

### Goal

Verify that another agent can take concrete action without reconstructing the conversation.

### Checks

- Clear product statement exists.
- Primary user and jobs are defined.
- Domain model has concrete interfaces.
- Core user flow is stepwise.
- Screen map is defined.
- Technical stack is proposed.
- Source tree is proposed.
- Data storage boundaries are defined.
- Image structure is defined.
- Deployment path is defined.
- MVP boundaries are defined.
- Roadmap has exit criteria.
- First work package is ordered.
- Open questions are available for discovery.
- Risks and mitigations are explicit.
- Definition of Done is testable.
- A condensed starter brief is available.

### Layer 3 result

**PASS.** A new partner agent can begin with product validation and a vertical slice without requiring the original chat.

---

# 28. Final transfer note

The strongest insight from the discovery is this:

> The project should not become a more polished equipment catalog. It should become a structured personal field planner for an address-based equipment program.

The source HTML is valuable because it already proves that photographs, search, articles, quantities and a temporary list are useful. The reconstruction should preserve those useful capabilities while changing the product’s center of gravity.

The next agent should protect the following chain throughout all future design and engineering decisions:

# Аптека → Завдання → Обладнання → Зведення

If a proposed feature does not improve this chain, it should be challenged or deferred.

---

# Appendix A. Proposed Ukrainian terminology

- Pharmacy: Аптека / торгова точка
- Pharmacy chain: Мережа
- Visit plan: План візиту / робочий план
- Equipment task: Завдання з обладнанням
- Equipment catalog: Каталог обладнання
- Article: Артикул
- Work action: Дія
- Install: Встановити
- Replace: Замінити
- Remove: Демонтувати
- Repair: Відремонтувати
- Rebrand: Переклеїти / оновити POSM
- Inspect: Перевірити
- Order: Замовити
- Relocate: Перемістити
- Quantity: Кількість
- Note: Примітка
- Draft: Чернетка
- Planned: Заплановано
- Ordered: Замовлено
- Completed: Виконано
- Cancelled: Скасовано
- Summary: Зведення
- Export: Експорт
- Backup: Резервна копія
- Restore: Відновити

Terminology must be validated against the actual language used by representatives.

---

# Appendix B. Minimal acceptance scenario

```gherkin
Feature: Create an equipment task for a pharmacy

  Scenario: Representative plans equipment replacement
    Given the pharmacy reference list is available
    And the equipment catalog is available
    When the representative opens a pharmacy
    And selects "Add equipment task"
    And searches for equipment article "2522012"
    And selects "DurexTower"
    And chooses the action "Замінити"
    And enters quantity 1
    And adds the note "Старе обладнання пошкоджене"
    And saves the task
    Then the task appears in the selected pharmacy plan
    And it remains after reloading the application
    And the order summary includes article "2522012" with quantity 1
```

---

# Appendix C. Non-negotiable reconstruction constraints

1. Do not embed the complete image catalog in HTML as Base64.
2. Do not couple user plans to display labels instead of stable IDs.
3. Do not expose personal notes through static repository data.
4. Do not make all 151 full cards the default initial view.
5. Do not require a network connection for basic note taking after initial app loading.
6. Do not implement a backend before workflow and export needs are validated.
7. Do not copy the old HTML/CSS structure as the new application architecture.
8. Do not sacrifice equipment image clarity through destructive cropping.
9. Do not make hover the only discovery mechanism for an action.
10. Do not complete the MVP without a tested backup/restore path.
