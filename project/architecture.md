# WeddingBazaar – Architecture & Database Design

## System Architecture (High-Level)
- Frontend: React (Vite) in `client/web/` using Redux Toolkit and React Router.
- Backend: FastAPI in `server/` with REST APIs, Pydantic schemas, and JWT-based auth.
- DB: PostgreSQL (managed via SQLAlchemy + Alembic). Admin via pgAdmin.
- Caching/Queues (optional for MVP): Redis + Celery for background tasks (emails, notifications, file processing).
- Storage: Local or S3-compatible object storage for media uploads.
- Payments: Stripe (escrow-like flows modeled at application layer).
- Notifications: Email (FastAPI-Mail) and in-app notifications.

## Services & Components
- API Gateway (FastAPI app): routing, auth, validation, rate limiting (future).
- Auth Service: registration, login, token management, roles & permissions.
- Vendor Service: vendor profiles, services, pricing, availability, portfolios.
- Package Service: generation, iteration tracking, itemized inclusions, budgets.
- Booking & Payment Service: bookings, invoices, payment intents, escrow holds, payouts.
- Event Management Service: sub-events, timelines, tasks, checklists, status updates.
- Guest Management: guest lists, RSVPs, seating, accommodations.
- Messaging: in-app chat between couples and vendors.
- Reviews & Ratings: post-event vendor feedback.

## Environment Variables (Backend)
- `DATABASE_URL=postgresql+psycopg2://user:password@host:port/dbname`
- `SECRET_KEY=...`
- `ACCESS_TOKEN_EXPIRE_MINUTES=60`
- `STRIPE_API_KEY=...`
- `MAIL_USERNAME=...`
- `MAIL_PASSWORD=...`
- `MAIL_FROM=...`
- `REDIS_URL=redis://localhost:6379/0` (optional)

## Database Schema (Initial Draft)

### users
| Column        | Type | Constraints / Notes |
| ---           | ---  | --- |
| id            | UUID | PK |
| email         | text | unique |
| phone         | text | optional unique (configurable) |
| password_hash | text |  |
| first_name    | text |  |
| last_name     | text |  |
| role          | enum | couple, family, vendor, admin |
| is_active     | bool | default true |
| created_at    | timestamptz | default now() |
| updated_at    | timestamptz | default now() |

### couples
| Column        | Type | Constraints / Notes |
| ---           | ---  | --- |
| id            | UUID | PK |
| user_id       | UUID | FK -> users.id, unique |
| budget_min    | numeric |  |
| budget_max    | numeric |  |
| guest_count   | int |  |
| preferred_cities | text[] |  |
| wedding_dates | daterange | or separate table |

### family_members
| Column     | Type | Constraints / Notes |
| ---        | ---  | --- |
| id         | UUID | PK |
| couple_id  | UUID | FK -> couples.id |
| user_id    | UUID | FK -> users.id |
| relation   | text |  |
| permissions| jsonb| role-based permissions |

### vendors
| Column       | Type | Constraints / Notes |
| ---          | ---  | --- |
| id           | UUID | PK |
| user_id      | UUID | FK -> users.id, unique |
| business_name| text |  |
| description  | text |  |
| city         | text |  |
| rating_avg   | numeric |  |
| review_count | int |  |
| verified     | bool | default false |

### vendor_services
| Column      | Type | Constraints / Notes |
| ---         | ---  | --- |
| id          | UUID | PK |
| vendor_id   | UUID | FK -> vendors.id |
| category    | enum | venue, photography, dj, makeup, catering, decor, transport, other |
| title       | text |  |
| base_price  | numeric |  |
| min_price   | numeric |  |
| max_price   | numeric |  |
| pricing_unit| text | per_day, per_event, per_guest |
| metadata    | jsonb|  |

### service_media
| Column            | Type | Constraints / Notes |
| ---               | ---  | --- |
| id                | UUID | PK |
| vendor_service_id | UUID | FK -> vendor_services.id |
| url               | text |  |
| media_type        | text | image, video |
| caption           | text |  |

### packages
| Column         | Type | Constraints / Notes |
| ---            | ---  | --- |
| id             | UUID | PK |
| couple_id      | UUID | FK -> couples.id |
| title          | text |  |
| status         | enum | draft, proposed, iterating, accepted, booked |
| iteration_count| int  | default 0, max 5 (check) |
| estimated_total| numeric |  |
| created_at     | timestamptz | default now() |
| updated_at     | timestamptz | default now() |

### package_items
| Column           | Type | Constraints / Notes |
| ---              | ---  | --- |
| id               | UUID | PK |
| package_id       | UUID | FK -> packages.id |
| vendor_service_id| UUID | FK -> vendor_services.id, nullable until selection |
| category         | enum | same as vendor_services.category |
| description      | text |  |
| estimated_cost   | numeric |  |
| final_cost       | numeric |  |
| status           | enum | suggested, accepted, replaced, removed |

### vendor_shortlists
| Column           | Type | Constraints / Notes |
| ---              | ---  | --- |
| id               | UUID | PK |
| package_item_id  | UUID | FK -> package_items.id |
| vendor_service_id| UUID | FK -> vendor_services.id |
| rank             | int  |  |
| notes            | text |  |

### bookings
| Column       | Type | Constraints / Notes |
| ---          | ---  | --- |
| id           | UUID | PK |
| couple_id    | UUID | FK -> couples.id |
| package_id   | UUID | FK -> packages.id |
| status       | enum | pending, confirmed, in_progress, completed, cancelled |
| event_date   | date |  |
| venue_address| text |  |
| total_amount | numeric |  |

### payments
| Column                 | Type | Constraints / Notes |
| ---                    | ---  | --- |
| id                     | UUID | PK |
| booking_id             | UUID | FK -> bookings.id |
| amount                 | numeric |  |
| currency               | text |  |
| status                 | enum | pending, authorized, captured, refunded, failed |
| method                 | enum | card, upi, netbanking, other |
| escrow_hold            | bool |  |
| stripe_payment_intent_id | text |  |
| created_at             | timestamptz | default now() |
| updated_at             | timestamptz | default now() |

### payment_transactions
| Column          | Type | Constraints / Notes |
| ---             | ---  | --- |
| id              | UUID | PK |
| payment_id      | UUID | FK -> payments.id |
| type            | enum | authorize, capture, refund |
| amount          | numeric |  |
| stripe_charge_id| text |  |
| status          | enum | success, failed |
| created_at      | timestamptz | default now() |

### events
| Column     | Type | Constraints / Notes |
| ---        | ---  | --- |
| id         | UUID | PK |
| booking_id | UUID | FK -> bookings.id |
| name       | text | Mehendi, Sangeet, Wedding, Reception |
| start_at   | timestamptz |  |
| end_at     | timestamptz |  |
| location   | text |  |

### event_tasks
| Column            | Type | Constraints / Notes |
| ---               | ---  | --- |
| id                | UUID | PK |
| event_id          | UUID | FK -> events.id |
| title             | text |  |
| assigned_vendor_id| UUID | FK -> vendors.id, nullable |
| status            | enum | todo, in_progress, done |
| due_at            | timestamptz |  |
| completed_at      | timestamptz |  |

### vendor_status_updates
| Column    | Type | Constraints / Notes |
| ---       | ---  | --- |
| id        | UUID | PK |
| event_id  | UUID | FK -> events.id |
| vendor_id | UUID | FK -> vendors.id |
| message   | text |  |
| status    | enum | en_route, setup_in_progress, setup_complete, service_delivered |
| created_at| timestamptz | default now() |

### guests
| Column     | Type | Constraints / Notes |
| ---        | ---  | --- |
| id         | UUID | PK |
| couple_id  | UUID | FK -> couples.id |
| full_name  | text |  |
| phone      | text |  |
| email      | text |  |
| group      | text | family, friends, colleagues, other |

### rsvps
| Column    | Type | Constraints / Notes |
| ---       | ---  | --- |
| id        | UUID | PK |
| guest_id  | UUID | FK -> guests.id |
| event_id  | UUID | FK -> events.id |
| response  | enum | yes, no, maybe |
| plus_ones | int  |  |
| notes     | text |  |

### seating_tables
| Column   | Type | Constraints / Notes |
| ---      | ---  | --- |
| id       | UUID | PK |
| event_id | UUID | FK -> events.id |
| name     | text |  |
| capacity | int  |  |

### seating_assignments
| Column          | Type | Constraints / Notes |
| ---             | ---  | --- |
| id              | UUID | PK |
| seating_table_id| UUID | FK -> seating_tables.id |
| guest_id        | UUID | FK -> guests.id |

### accommodations
| Column           | Type | Constraints / Notes |
| ---              | ---  | --- |
| id               | UUID | PK |
| guest_id         | UUID | FK -> guests.id |
| hotel_name       | text |  |
| check_in         | date |  |
| check_out        | date |  |
| transport_required | bool |  |

### messages
| Column          | Type | Constraints / Notes |
| ---             | ---  | --- |
| id              | UUID | PK |
| sender_user_id  | UUID | FK -> users.id |
| receiver_user_id| UUID | FK -> users.id |
| package_item_id | UUID | FK -> package_items.id, nullable |
| body            | text |  |
| created_at      | timestamptz | default now() |
| read_at         | timestamptz |  |

### notifications
| Column   | Type | Constraints / Notes |
| ---      | ---  | --- |
| id       | UUID | PK |
| user_id  | UUID | FK -> users.id |
| type     | text |  |
| payload  | jsonb|  |
| is_read  | bool | default false |
| created_at | timestamptz | default now() |

### reviews
| Column    | Type | Constraints / Notes |
| ---       | ---  | --- |
| id        | UUID | PK |
| vendor_id | UUID | FK -> vendors.id |
| couple_id | UUID | FK -> couples.id |
| rating    | int  | 1–5 (check) |
| comment   | text |  |
| created_at| timestamptz | default now() |

### documents
| Column        | Type | Constraints / Notes |
| ---           | ---  | --- |
| id            | UUID | PK |
| owner_user_id | UUID | FK -> users.id |
| url           | text |  |
| doc_type      | text | contract, invoice, media, other |
| metadata      | jsonb|  |
| created_at    | timestamptz | default now() |

## Indices & Constraints (examples)
- Unique: `users.email`, `users.phone` (optional), `vendors.user_id`, `couples.user_id`.
- Indices on foreign keys: `vendor_services.vendor_id`, `package_items.package_id`, `payments.booking_id`, etc.
- Check constraints (business rules): `packages.iteration_count <= 5`, `rating between 1 and 5`.

## ERD (Textual Overview)
- One `user` can be a `couple`, `family_member`, `vendor`, or `admin` (role-based).
- A `couple` has many `packages`; a `package` has many `package_items` and `vendor_shortlists`.
- A `booking` is tied to one accepted `package`; it has many `payments` and `events`.
- `events` have `event_tasks`, `vendor_status_updates`, and guest `rsvps`/`seating`.
- `vendors` offer `vendor_services` with `service_media`; receive `reviews` from couples.
- Messaging and notifications connect users across flows.

## Migration Strategy
- Use Alembic for versioned migrations.
- Seed reference data (service categories) via migration or fixtures.
- Backfill and evolve schema per feature flags and phases.
