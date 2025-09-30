# WeddingBazaar – API Specifications (Draft)

Base URL: `/api/v1`
Auth: Bearer JWT (unless noted `public`)
Content-Type: application/json (multipart/form-data for uploads)

## Conventions
- Pagination: `?page=1&size=20`
- Sorting: `?sort=created_at:desc`
- Filtering: explicit query params per resource
- IDs are UUID strings

---

## Auth
- POST `/auth/register` – Register user (role: couple, vendor, family)
- POST `/auth/login` – Obtain JWT tokens
- POST `/auth/refresh` – Refresh access token
- POST `/auth/logout` – Invalidate refresh token (optional)
- POST `/auth/forgot-password` – Send reset email/OTP
- POST `/auth/reset-password` – Reset with token

## Users
- GET `/users/me` – Get profile of current user
- PATCH `/users/me` – Update profile details
- GET `/users/:id` – Admin only: fetch user by id
- GET `/users` – Admin only: list/search users

## Couples & Family
- POST `/couples` – Create couple profile (post-onboarding)
- GET `/couples/me` – Get own couple profile
- PATCH `/couples/me` – Update couple preferences (budget, guests, cities, dates)
- POST `/couples/family` – Add family member (user_id or invite)
- GET `/couples/family` – List family members
- PATCH `/couples/family/:id` – Update permissions/role
- DELETE `/couples/family/:id` – Remove family member

## Vendors
- POST `/vendors` – Create/claim vendor profile
- GET `/vendors/me` – Get own vendor profile
- PATCH `/vendors/me` – Update business info
- GET `/vendors/:id` – Public vendor details
- GET `/vendors` – Search vendors `?city=&category=&min_price=&max_price=`

## Vendor Services
- POST `/vendor-services` – Create a service (vendor auth)
- GET `/vendor-services/:id` – Public service details
- PATCH `/vendor-services/:id` – Update service (owner)
- DELETE `/vendor-services/:id` – Delete service (owner)
- GET `/vendor-services` – Search/browse services `?vendor_id=&category=&q=`
- POST `/vendor-services/:id/media` – Upload media (multipart)
- DELETE `/vendor-services/:id/media/:media_id` – Remove media

## Packages
- POST `/packages` – Generate initial package (from couple inputs)
- GET `/packages` – List own packages
- GET `/packages/:id` – Get package details
- PATCH `/packages/:id` – Update title/status
- POST `/packages/:id/iterate` – Request an iteration (<= 5)

### Package Items & Shortlists
- POST `/packages/:id/items` – Add item (category, desc, est cost)
- PATCH `/package-items/:item_id` – Update item details/selection
- DELETE `/package-items/:item_id` – Remove item
- GET `/package-items/:item_id/shortlists` – List shortlisted vendors for item
- POST `/package-items/:item_id/shortlists` – Add shortlisted vendor
- PATCH `/vendor-shortlists/:id` – Update rank/notes
- DELETE `/vendor-shortlists/:id` – Remove shortlisted vendor

## Vendor Interaction & Selection
- POST `/package-items/:item_id/select-vendor` – Accept vendor for item
- POST `/package-items/:item_id/reject-vendor` – Reject and request alternative

## Booking & Payments
- POST `/bookings` – Create booking from accepted package
- GET `/bookings` – List own bookings
- GET `/bookings/:id` – Booking details
- PATCH `/bookings/:id` – Update status, event date, venue address

### Payment Flows
- POST `/bookings/:id/payments/intent` – Create payment intent (amount, method)
- POST `/payments/:id/capture` – Capture authorized payment
- POST `/payments/:id/refund` – Refund captured payment
- GET `/bookings/:id/payments` – List payments for a booking
- GET `/payments/:id` – Payment details

## Budget Tracking
- GET `/packages/:id/budget` – Estimated vs actual spend
- GET `/bookings/:id/budget` – Actual spend by vendor/category

## Events & Timelines
- POST `/bookings/:id/events` – Create event (Mehendi, Sangeet, etc.)
- GET `/bookings/:id/events` – List events
- GET `/events/:id` – Event details
- PATCH `/events/:id` – Update event timing/location
- DELETE `/events/:id` – Remove event

### Event Tasks
- POST `/events/:id/tasks` – Create task (title, due, assigned_vendor_id?)
- GET `/events/:id/tasks` – List tasks
- PATCH `/event-tasks/:id` – Update status/assignee/due
- DELETE `/event-tasks/:id` – Delete task

### Real-Time Vendor Updates
- POST `/events/:id/vendor-updates` – Vendor posts status update
- GET `/events/:id/vendor-updates` – List updates

## Guests & RSVPs
- POST `/guests` – Add guest to couple list
- GET `/guests` – List guests (filters: group, search)
- PATCH `/guests/:id` – Update guest details
- DELETE `/guests/:id` – Remove guest
- POST `/rsvps` – Upsert RSVP (guest_id, event_id, response, plus_ones, notes)
- GET `/events/:id/rsvps` – List RSVPs for event

### Seating
- POST `/events/:id/seating-tables` – Create table (name, capacity)
- GET `/events/:id/seating-tables` – List tables
- POST `/seating-tables/:id/assign` – Assign guest to table
- DELETE `/seating-assignments/:id` – Unassign guest

### Accommodations
- POST `/accommodations` – Create accommodation for guest
- GET `/accommodations` – List accommodations (by guest/event)
- PATCH `/accommodations/:id` – Update
- DELETE `/accommodations/:id` – Remove

## Messaging
- POST `/messages` – Send message (to user, optionally link to package_item)
- GET `/messages/threads` – List conversation threads
- GET `/messages/thread/:user_id` – Fetch messages with a user
- POST `/messages/:id/read` – Mark as read

## Notifications
- GET `/notifications` – List current user's notifications
- POST `/notifications/:id/read` – Mark read

## Reviews
- POST `/vendors/:id/reviews` – Add review (rating, comment)
- GET `/vendors/:id/reviews` – List vendor reviews

## Documents & Media
- POST `/documents` – Upload document/media (multipart) with metadata
- GET `/documents` – List current user's documents
- GET `/documents/:id` – Get document metadata
- DELETE `/documents/:id` – Delete document

## Admin (restricted)
- GET `/admin/metrics` – Platform metrics (users, vendors, bookings, GMV)
- POST `/admin/vendors/:id/verify` – Verify vendor
- POST `/admin/categories` – Seed/maintain service categories

---

## Example Schemas (Pydantic outlines)

```json
// POST /auth/register
{
  "email": "user@example.com",
  "password": "secret",
  "role": "couple",
  "first_name": "Aman",
  "last_name": "K"
}
```

```json
// POST /packages (generate)
{
  "budget_min": 800000,
  "budget_max": 1200000,
  "guest_count": 400,
  "cities": ["Jaipur"],
  "dates": ["2026-02-12", "2026-02-13"],
  "services": ["venue", "photography", "dj", "makeup", "catering", "decor"]
}
```

```json
// POST /bookings/:id/payments/intent
{
  "amount": 250000,
  "currency": "INR",
  "method": "card",
  "escrow_hold": true
}
```

---

## Security & Roles
- Public endpoints: vendor search, vendor-service details
- Auth required: most create/update/delete actions
- Role guards:
  - Couples: manage packages, bookings, guests, events
  - Vendors: manage vendor profile/services, post event updates
  - Family: limited read/write via couple permissions
  - Admin: platform-wide moderation and reporting

## Rate Limits (future)
- 60 req/min per token by default; stricter on sensitive endpoints

## Webhooks (future)
- `/webhooks/stripe` – payment events
- `/webhooks/storage` – media processing events
