# WeddingBazaar – Product Specs

## Vision
Create a one‑stop wedding concierge platform for couples and families to plan, manage, and execute weddings end‑to‑end with less stress, transparent budgeting, and coordinated vendor management.

## Target Users
- Couples planning their wedding
- Families involved in planning and approvals
- Vendors offering wedding services (venues, decorators, photographers, DJs, makeup artists, caterers, etc.)

## Core Objectives
1. End‑to‑end planning from requirements to execution
2. Smart vendor discovery and matching by preferences, location, and budget
3. Package creation and iteration (flexible up to 5 iterations)
4. Transparent budgeting and centralized payment tracking (incl. escrow)
5. Real‑time event‑day updates and notifications

## Key Features (MVP + beyond)
- Couple onboarding with nominal fee (₹5,000)
- Smart package creation from inputs: budget, guests, dates, locations, required services
- Vendor interaction and selection with ratings/reviews
- Centralized booking and payment flow; track estimated vs actual spend
- Guest management (RSVP, seating, accommodation & transport)
- Event timeline and task management per sub‑event (mehendi, sangeet, wedding, reception)
- On‑ground status updates from vendors ("decor ready", "catering delivered", etc.)
- Collaboration portal for families
- Personalization: themes, digital invites, gift registry, media repository
- Optional/premium: destination planning, AI assistant, live vendor tracking, post‑wedding services

## Revenue Model
- Onboarding fee: ₹5,000 per couple
- Vendor commission: 15–25% per booking
- Premium add‑ons: concierge, destination planning, priority recommendations

## Technical & Operational
- Stack: FastAPI backend, React + Redux frontend, PostgreSQL, Redis (optional), Celery (optional)
- Teams: Product, Engineering (FE/BE), Design, QA, DB/Cloud, Planners, Vendor Ops, CS, Finance/Legal, Marketing

## MVP Phased Approach
- Phase 1: Onboarding & inputs, smart package + up to 5 iterations, vendor selection, payment tracking & budgeting
- Phase 2: Guest management (RSVP, seating, accommodations), event/timeline dashboards with reminders, real‑time updates
- Phase 3: AI recommendations, digital invitations & gift registry, destination planning

## User Stories

### Couples
- As a couple, I can sign up and create a profile so that I can start planning my wedding.
- As a couple, I can enter my budget, guest count, dates, and cities so that I receive a tailored package.
- As a couple, I can request up to 5 iterations of my package so that I can fine‑tune it to my needs.
- As a couple, I can shortlist and select vendors for each service so that I can finalize my package.
- As a couple, I can pay vendors via a secure flow so that my payments are tracked and protected (escrow‑like).
- As a couple, I can view estimated vs actual spend so that I remain on budget.
- As a couple, I can manage guests (RSVPs, seating, accommodations) so that logistics are streamlined.
- As a couple, I can view real‑time vendor updates on event days so that I know progress on the ground.
- As a couple, I can collaborate with family members with permissions so that decisions are aligned.

### Family Members
- As a family member, I can be invited to a couple’s planning workspace so that I can participate.
- As a family member, I can comment/approve items based on permissions so that I help decision‑making.

### Vendors
- As a vendor, I can register and create my business profile so that couples can find me.
- As a vendor, I can list services with pricing and media so that my offerings are clear.
- As a vendor, I can respond to couple inquiries and post event status updates so that coordination improves.
- As a vendor, I can receive bookings and payouts so that I can deliver services reliably.

### Admin
- As an admin, I can verify vendors and manage categories so that the platform quality remains high.
- As an admin, I can view platform metrics so that I track adoption and GMV.

## Application Workflows

### 1) Onboarding & Inputs
1. User registers (role = couple). Optional: family invites.
2. Couple enters planning inputs: budget, guests, cities, dates, required services.
3. Pay onboarding fee (₹5,000) to proceed to package generation.

### 2) Smart Package Generation & Iteration
1. System generates initial package with suggested items and vendors.
2. Couple requests changes (up to 5 iterations): replace vendors, tweak inclusions, adjust estimates.
3. Shortlists maintained per item; couple approves final selections per category.

### 3) Vendor Interaction & Selection
1. Couple reviews vendor profiles, ratings, and portfolios.
2. Accept/Reject vendors per package item; request alternatives as needed.
3. Finalize package: status changes to accepted/booked pending payment.

### 4) Booking & Payments
1. Create booking from accepted package; event date(s) and venue captured.
2. Create payment intents (advance/post‑event) with escrow‑like holds.
3. Capture/refund as milestones are met; maintain full transaction history.

### 5) Event Management & Real‑Time Updates
1. Create sub‑events (mehendi, sangeet, wedding, reception) with timelines and tasks.
2. Assign vendors to tasks; vendors post status updates (e.g., setup_complete, service_delivered).
3. Couple views live updates dashboard.

### 6) Guest Management
1. Import/add guests; manage groups.
2. Collect RSVPs per event; manage seating tables and assignments.
3. Coordinate accommodations and transport for out‑of‑town guests.

### 7) Post‑Event
1. Collect reviews for vendors.
2. Manage documents (invoices, contracts, media) and finalize payments.
